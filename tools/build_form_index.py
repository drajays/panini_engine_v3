"""
tools/build_form_index.py — generate the form index (CONSTITUTION Art. 17).

Derives every cell this engine can reach over the lexicon it has, and stores
the surface, the lemma, the features and the **cell key** that re-derives it.
A refusal is recorded as a gap (Art. 18), never swallowed.

    python3 -m tools.build_form_index                 # full build
    python3 -m tools.build_form_index --dhatus 40     # a slice, for a trial
    python3 -m tools.build_form_index --verify 200    # re-derive a sample
    python3 -m tools.build_form_index --stats

Verification is the property that keeps the index honest: a stored form the
engine can no longer derive is a build failure, not a stale row.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from engine.form_index import DB_PATH, connect, stats  # noqa: E402

LAKARAS = ("laT", "laG", "liT", "lRT", "loT")
LINGAS = {"pulliṅga": "pum", "strīliṅga": "stri", "napuṃsaka": "napumsaka"}


def stem_lexicon() -> list[tuple[str, str]]:
    """(stem, liṅga) from every stem list the repo actually carries."""
    from pipelines.patha_pipeline import PATHA_LEXICON

    seen: dict[tuple[str, str], None] = {}
    for entry in PATHA_LEXICON:
        seen[(entry.stem_slp1, entry.linga)] = None

    linga_file = _ROOT / "data" / "inputs" / "linga_anushasana.json"
    if linga_file.exists():
        data = json.loads(linga_file.read_text(encoding="utf-8"))
        for linga in LINGAS:
            for stem in data.get(linga, []):
                seen[(stem, linga)] = None

    sarvadi_file = _ROOT / "data" / "inputs" / "sarvadi_slp1.json"
    if sarvadi_file.exists():
        for stem in json.loads(sarvadi_file.read_text(encoding="utf-8")).get("sarvadi", []):
            seen[(stem, "pulliṅga")] = None
    return sorted(seen)


def dhatu_lexicon(limit: int | None) -> list[dict[str, Any]]:
    from pipelines.dhatupatha import _envelope, _payload

    entries = _envelope(_payload())["entries"]
    return entries[:limit] if limit else entries


def subanta_cells(stems: list[tuple[str, str]]) -> Iterator[dict[str, Any]]:
    for stem, linga in stems:
        for vibhakti in range(1, 9):
            for vacana in range(1, 4):
                yield {
                    "kind": "subanta", "lemma": stem,
                    "features": {"linga": linga, "vibhakti": vibhakti, "vacana": vacana},
                    "cell_key": f"subanta:{stem}:{LINGAS[linga]}:{vibhakti}:{vacana}",
                }


def tinanta_cells(dhatus: list[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    for entry in dhatus:
        upadesha = entry.get("upadesha_slp1")
        if not upadesha:
            continue
        # Two roots can share an upadeśa (homonyms in different gaṇas), so the
        # pāṭha id disambiguates: without it the later row silently replaces
        # the earlier and a lemma disappears from the index.
        pid = entry.get("dhatupatha_id") or entry.get("id") or upadesha
        for lakara in LAKARAS:
            for purusha in range(1, 4):
                for vacana in range(1, 4):
                    yield {
                        "kind": "tinanta", "lemma": upadesha,
                        "features": {"lakara": lakara, "prayoga": "kartari",
                                     "purusha": purusha, "vacana": vacana},
                        "cell_key": f"tinanta:{upadesha}@{pid}:{lakara}:{purusha}:{vacana}",
                    }


def derive_cell(cell: dict[str, Any]) -> Any:
    from pipelines.subanta import derive as sub_derive
    from pipelines.tinanta import derive as tin_derive

    f = cell["features"]
    if cell["kind"] == "subanta":
        return sub_derive(cell["lemma"], f["vibhakti"], f["vacana"], linga=f["linga"])
    return tin_derive(cell["lemma"], f["lakara"], f["prayoga"], f["purusha"], f["vacana"])


def build(dhatu_limit: int | None, stem_limit: int | None,
          path: Path | None = None) -> dict[str, Any]:
    import sutras  # noqa: F401

    stems = stem_lexicon()[:stem_limit] if stem_limit else stem_lexicon()
    dhatus = dhatu_lexicon(dhatu_limit)
    cells = [*subanta_cells(stems), *tinanta_cells(dhatus)]

    target = path or DB_PATH
    target.unlink(missing_ok=True)
    conn = connect(target, write=True)   # closed explicitly below
    started = time.time()
    written = refused = 0
    with conn:
        for cell in cells:
            try:
                state = derive_cell(cell)
                conn.execute(
                    "INSERT OR REPLACE INTO forms "
                    "(surface_slp1, surface_dev, kind, lemma, features, cell_key, branch) "
                    "VALUES (?,?,?,?,?,?,0)",
                    (state.flat_slp1(), state.flat_dev(), cell["kind"], cell["lemma"],
                     json.dumps(cell["features"], ensure_ascii=False), cell["cell_key"]),
                )
                written += 1
            except Exception as ex:
                conn.execute(
                    "INSERT OR REPLACE INTO gaps (cell_key, kind, lemma, reason) VALUES (?,?,?,?)",
                    (cell["cell_key"], cell["kind"], cell["lemma"],
                     f"{type(ex).__name__}: {ex}"[:300]),
                )
                refused += 1
        conn.execute("ANALYZE")
        conn.executemany(
            "INSERT OR REPLACE INTO meta (key, value) VALUES (?,?)",
            [
                ("generated_at", datetime.now(timezone.utc).isoformat(timespec="seconds")),
                ("stems", str(len(stems))),
                ("dhatus", str(len(dhatus))),
                ("cells", str(len(cells))),
                ("seconds", f"{time.time() - started:.1f}"),
            ],
        )
    conn.close()
    return {"cells": len(cells), "written": written, "refused": refused,
            "seconds": round(time.time() - started, 1), "path": str(target)}


def write_manifest(path: Path | None = None) -> Path:
    """The committed fingerprint of an uncommitted 10 MB artifact.

    The database itself is a build product and is not in version control — it
    is rewritten wholesale by every build. What is committed is this manifest:
    the counts, and a deterministic sample of surface → lemma pairs that a
    rebuild must reproduce.
    """
    from engine.form_index import sample as index_sample

    summary = stats(path)
    fingerprint = [
        {"surface": row["surface_slp1"], "lemma": row["lemma"], "cell": row["cell_key"]}
        for row in index_sample(50, path)
    ]
    manifest = _ROOT / "data" / "index" / "manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(
        json.dumps({**summary, "fingerprint": fingerprint}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return manifest


def verify(n: int) -> int:
    """Re-derive a sample; a mismatch is a build failure (Art. 17)."""
    import sutras  # noqa: F401
    from engine.form_index import sample

    rows = sample(n)
    bad = []
    for row in rows:
        cell = {"kind": row["kind"], "lemma": row["lemma"], "features": row["features"]}
        try:
            surface = derive_cell(cell).flat_slp1()
        except Exception as ex:
            bad.append((row["cell_key"], row["surface_slp1"], f"{type(ex).__name__}"))
            continue
        if surface != row["surface_slp1"]:
            bad.append((row["cell_key"], row["surface_slp1"], surface))
    print(f"  verified {len(rows) - len(bad)}/{len(rows)} rows re-derive exactly")
    for key, stored, now in bad[:10]:
        print(f"    ✗ {key}: stored {stored}, engine now gives {now}")
    return 1 if bad else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the generated-forms index.")
    ap.add_argument("--dhatus", type=int, default=None, help="limit dhātus (trial builds)")
    ap.add_argument("--stems", type=int, default=None, help="limit stems")
    ap.add_argument("--verify", type=int, metavar="N", default=None)
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args(argv)

    if args.stats:
        print(json.dumps(stats(), ensure_ascii=False, indent=2))
        return 0
    if args.verify is not None:
        return verify(args.verify)

    result = build(args.dhatus, args.stems)
    manifest = write_manifest()
    print(f"\n  form index — {DB_PATH.relative_to(_ROOT)}")
    print(f"  cells    : {result['cells']}")
    print(f"  written  : {result['written']}")
    print(f"  refused  : {result['refused']}   (recorded as gaps)")
    print(f"  seconds  : {result['seconds']}")
    print(json.dumps(stats(), ensure_ascii=False, indent=2))
    print(f"  manifest : {manifest.relative_to(_ROOT)}  (committed; the .db is not)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
