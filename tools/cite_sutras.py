"""
tools/cite_sutras.py — write Article 14 citations from the local corpus.
───────────────────────────────────────────────────────────────────────

Article 16 counts a sūtra as implemented only when it is invoked, moves the
state, is **cited**, and is tested. `make coverage` reports the sūtras that
already do real work and lack only the citation — 296 of them on 2026-09-15.

This tool closes that condition **from data, never from memory** (Art. 14's
own rule): every line it writes comes out of ``sutra_ref_out/<id>.json``, the
vendored ashtadhyayi + Kāśikā reference record for that sūtra. Where the record
has no Kāśikā udāharaṇa, the tool says so and writes nothing — a missing source
is a gap to report (Art. 18), never a sentence to invent.

It never touches ``cond`` or ``act``. No rule logic changes.

    python3 -m tools.cite_sutras --prakarana sandhi              # dry run
    python3 -m tools.cite_sutras --prakarana sandhi --apply
    python3 -m tools.cite_sutras --ids 6.1.88,6.1.101 --apply
    python3 -m tools.cite_sutras --worklist --limit 25 --apply
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

REF_DIR = _ROOT / "sutra_ref_out"
SUTRAS_DIR = _ROOT / "sutras"
TESTS_DIR = _ROOT / "tests"

MARKER = "Citation (CONSTITUTION Art. 14)"

# Art. 3: these strings may not appear anywhere under sutras/ — a reference
# record that carries one is a source we cannot quote here, so we report it.
FORBIDDEN = (
    "sk_kashika", "siddhanta_kaumudi", "Siddhanta-Kaumudi", "Siddhānta-Kaumudī",
    "prakarana_order", "prakarana_index", "kashika_priority",
)


def row_index(sutra_id: str) -> int:
    """ashtadhyayi.com row index: 6.4.3 → 64003 (Art. 14, source #1)."""
    a, p, n = sutra_id.split(".")
    return int(f"{a}{p}{int(n):03d}")


def ref_record(sutra_id: str) -> dict[str, Any] | None:
    path = REF_DIR / (sutra_id.replace(".", "_") + ".json")
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def sutra_file(sutra_id: str) -> Path | None:
    hits = list(SUTRAS_DIR.rglob("sutra_" + sutra_id.replace(".", "_") + ".py"))
    return hits[0] if len(hits) == 1 else None


def _test_files(sutra_id: str, limit: int = 3) -> list[str]:
    """Tests that name this sūtra — Art. 14 cross-validation option (b)."""
    hits: list[str] = []
    for path in sorted(TESTS_DIR.rglob("*.py")):
        try:
            if sutra_id in path.read_text(encoding="utf-8"):
                hits.append(path.relative_to(_ROOT).as_posix())
        except OSError:
            continue
        if len(hits) >= limit:
            break
    return hits


def build_citation(sutra_id: str) -> tuple[str | None, list[str]]:
    """Return (citation block, gaps). The block is None when Art. 14 cannot be met."""
    gaps: list[str] = []
    rec = ref_record(sutra_id)
    if rec is None:
        return None, [f"{sutra_id}: no sutra_ref_out record"]

    text = rec.get("text") or {}
    dev = (text.get("dev") or "").strip()
    padaccheda = ((text.get("padaccheda") or {}).get("dev") or "").strip()
    inheritance = rec.get("inheritance") or {}
    anuvrtti = (inheritance.get("anuvrtti_pada") or "").strip()
    adhikara = (inheritance.get("adhikara") or "").strip()

    kashika = [
        text for source, text in map(_example, rec.get("examples") or [])
        if source.lower().startswith("kashika") and text
    ][:3]
    if not kashika:
        gaps.append(f"{sutra_id}: reference record carries no Kāśikā udāharaṇa")
    if not dev:
        gaps.append(f"{sutra_id}: reference record carries no sūtra text")
    if gaps:
        return None, gaps

    tests = _test_files(sutra_id)
    if not tests:
        gaps.append(f"{sutra_id}: no test names this sūtra (Art. 14 cross-validation)")
        return None, gaps

    gloss_sa = ((rec.get("gloss") or {}).get("sa") or "").strip()

    lines = [
        MARKER,
        f"  Source #1 — ashtadhyayi.com row i = {row_index(sutra_id)} · {dev}",
    ]
    if padaccheda:
        lines.append(f"              padaccheda: {padaccheda}")
    if anuvrtti:
        lines.append(f"              anuvṛtti:   {anuvrtti}")
    if adhikara:
        lines.append(f"              adhikāra:   {adhikara}")
    lines.append(f"  Source #2 — Kāśikā {sutra_id} udāharaṇa:")
    lines.extend(f"                {k}" for k in kashika)
    if gloss_sa:
        lines.append(f"  Gloss (sa) — {gloss_sa}")
    lines.append("  Cross-check — surface pinned by: " + ", ".join(tests))
    lines.append(
        f"  Reference record: sutra_ref_out/{sutra_id.replace('.', '_')}.json"
    )
    block = "\n".join(lines)
    leaked = [f for f in FORBIDDEN if f in block]
    if leaked:
        # Art. 3 keeps Kaumudī-flavoured sources out of the engine tree; a record
        # whose examples name one cannot be quoted here.
        return None, [f"{sutra_id}: reference text names {leaked[0]!r} (Art. 3)"]
    return block, []


def _example(entry: Any) -> tuple[str, str]:
    """(source, example text) for a reference record's example, whatever its shape.

    Records are not uniform: some carry flat fields, some a ``raw`` string that
    is a Python dict repr. Never return the repr itself — a citation quotes the
    udāharaṇa, not the record's plumbing.
    """
    if isinstance(entry, str):
        entry = _maybe_dict(entry)
    if not isinstance(entry, dict):
        return "", ""
    source = str(entry.get("source") or "")

    def clean(value: Any) -> str:
        """A usable udāharaṇa, or "" — never a record fragment."""
        if not isinstance(value, str):
            return ""
        v = value.strip()
        return "" if (not v or "{'" in v or '{"' in v or v.endswith("'")) else v

    # Some records store the whole entry as a dict repr in `raw`, and leave
    # fragments of it in the other fields — parse `raw` first when it is one.
    raw = entry.get("raw")
    inner = _maybe_dict(raw) if isinstance(raw, str) and raw.strip().startswith("{") else None
    if isinstance(inner, dict):
        return (source or str(inner.get("source") or ""),
                clean(inner.get("example_dev")) or clean(inner.get("output_dev")))
    for key in ("example_dev", "output_dev", "alt_dev", "raw"):
        text = clean(entry.get(key))
        if text:
            return source, text
    return source, ""


def _maybe_dict(text: str) -> Any:
    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError):
        return text


_DOCSTRING_RE = re.compile(r'^(\s*)("""|\'\'\')(.*?)(\2)', re.DOTALL)


def insert_citation(source: str, citation: str) -> str | None:
    """Append the citation to the module docstring. None when already cited."""
    if MARKER in source:
        return None
    m = _DOCSTRING_RE.match(source)
    if not m:
        return None
    indent, quote, body, _ = m.groups()
    body = body.rstrip() + "\n\n" + citation + "\n"
    return source[: m.start()] + f"{indent}{quote}{body}{quote}" + source[m.end():]


def worklist_ids() -> list[str]:
    import sutras  # noqa: F401 — fills SUTRA_REGISTRY
    from engine import SUTRA_REGISTRY
    from engine.coverage import honest_coverage

    return list(honest_coverage(SUTRA_REGISTRY)["moving_but_uncited"])


def by_prakarana(name: str, ids: Iterable[str]) -> list[str]:
    out = []
    for sid in ids:
        rec = ref_record(sid)
        if rec and ((rec.get("classification") or {}).get("prakarana") == name):
            out.append(sid)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Write Art. 14 citations from sutra_ref_out/.")
    ap.add_argument("--ids", help="comma-separated sūtra ids")
    ap.add_argument("--prakarana", help="batch by prakaraṇa, e.g. sandhi / tripadi / samjna")
    ap.add_argument("--worklist", action="store_true",
                    help="take ids from `make coverage`'s moving-but-uncited list")
    ap.add_argument("--limit", type=int, default=30, help="batch size cap (default 30)")
    ap.add_argument("--apply", action="store_true", help="write the files (default: dry run)")
    args = ap.parse_args(argv)

    if args.ids:
        ids = [s.strip() for s in args.ids.split(",") if s.strip()]
    else:
        ids = worklist_ids()
        if args.prakarana:
            ids = by_prakarana(args.prakarana, ids)
    ids = ids[: args.limit]
    if not ids:
        print("nothing to do")
        return 0

    written, skipped, gaps = 0, 0, []
    for sid in ids:
        path = sutra_file(sid)
        if path is None:
            gaps.append(f"{sid}: no unique sūtra file")
            continue
        citation, sid_gaps = build_citation(sid)
        if citation is None:
            gaps.extend(sid_gaps)
            continue
        source = path.read_text(encoding="utf-8")
        updated = insert_citation(source, citation)
        if updated is None:
            skipped += 1
            continue
        if args.apply:
            path.write_text(updated, encoding="utf-8")
        written += 1
        print(f"{'wrote ' if args.apply else 'would '}{sid:>9}  {path.relative_to(_ROOT)}")

    print(f"\n{written} cited, {skipped} already cited, {len(gaps)} gaps"
          + ("" if args.apply else "   (dry run — pass --apply)"))
    for g in gaps:
        print(f"  gap: {g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
