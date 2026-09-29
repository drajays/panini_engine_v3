"""
tools/samsaadhanii_coverage.py — how much of the Gītā's tiṅanta does the engine derive?
────────────────────────────────────────────────────────────────────────────────────────

Reads ``data/reference/samsaadhanii/gita_tinanta.jsonl`` (built by
``tools.fetch_samsaadhanii_ereaders``), runs ``pipelines.tinanta.derive`` on
every resolved cell and compares the surface with the attested word.

    python3 -m tools.samsaadhanii_coverage                   # summary
    python3 -m tools.samsaadhanii_coverage --show mismatch   # list failing cells
    python3 -m tools.samsaadhanii_coverage --write-baseline  # re-lock the ratchet

Outcomes per cell: ``match``, ``mismatch`` (engine derives another form),
``error`` (engine raises), ``unresolved`` (tag could not be mapped to inputs).
A mismatch is a *lead*, not a verdict — Saṃsādhanī is a Tier-4 oracle and the
Gītā has ārṣa forms; triage against Kāśikā before changing a sūtra.
"""
from __future__ import annotations

import argparse
import collections
import json
from dataclasses import dataclass
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = _ROOT / "data" / "reference" / "samsaadhanii" / "gita_tinanta.jsonl"
BASELINE = _ROOT / "tests" / "regression" / "samsaadhanii_gita_tinanta_baseline.json"


@dataclass
class Result:
    key: str
    word: str
    word_slp1: str
    refs: list[str]
    row: dict
    outcome: str = "unresolved"
    produced: str = ""
    detail: str = ""

    @property
    def cell_id(self) -> str:
        return f"{self.key}={self.word_slp1}"


def load_cells(path: Path = SNAPSHOT) -> list[Result]:
    """Unique (cell, attested word) pairs, each with the verses it occurs in."""
    cells: dict[str, Result] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        cid = f"{r['key']}={r['word_slp1']}"
        if cid not in cells:
            cells[cid] = Result(r["key"], r["word"], r["word_slp1"], [], r,
                                detail=r["unresolved"] or "")
        cells[cid].refs.append(r["ref"])
    return list(cells.values())


def derive_cell(row: dict):
    from pipelines.tinanta import derive
    from tools.samsaadhanii_tags import TinantaCell

    fields = TinantaCell.__dataclass_fields__
    cell = TinantaCell(**{k: row[k] for k in fields if k in row})
    return derive(cell.dhatu_id, cell.lakara, cell.prayoga, cell.purusha, cell.vacana,
                  **cell.derive_kwargs())


def run(cells: list[Result]) -> list[Result]:
    import sutras  # noqa: F401

    for c in cells:
        if c.row["unresolved"]:
            continue
        try:
            produced = derive_cell(c.row).flat_slp1()
        except Exception as e:  # noqa: BLE001 — every failure is a coverage datum
            c.outcome, c.detail = "error", f"{type(e).__name__}: {e}"[:160]
            continue
        c.produced = produced
        c.outcome = "match" if produced == c.word_slp1 else "mismatch"
    return cells


def summarize(cells: list[Result]) -> str:
    occ = lambda cs: sum(len(c.refs) for c in cs)  # noqa: E731
    by = collections.defaultdict(list)
    for c in cells:
        by[c.outcome].append(c)
    lines = [f"cells {len(cells)}  (occurrences {occ(cells)})"]
    for o in ("match", "mismatch", "error", "unresolved"):
        lines.append(f"  {o:<10} {len(by[o]):>4} cells  {occ(by[o]):>5} occurrences")

    grid = collections.defaultdict(collections.Counter)
    for c in cells:
        if c.outcome != "unresolved":
            grid[(c.row["prayoga"], c.row["lakara"])][c.outcome] += 1
    lines.append("\nprayoga × lakāra        match / total")
    for (p, l), cnt in sorted(grid.items(), key=lambda kv: -sum(kv[1].values())):
        lines.append(f"  {p:<8} {l:<8} {cnt['match']:>4} / {sum(cnt.values())}")

    fail = collections.Counter()
    for c in by["mismatch"] + by["error"]:
        fail[c.row["dhatu_upadesha_slp1"]] += len(c.refs)
    lines.append("\nmost frequent failing dhātus (occurrences)")
    lines += [f"  {d:<10} {n}" for d, n in fail.most_common(15)]
    return "\n".join(lines)


def write_baseline(cells: list[Result], path: Path = BASELINE) -> None:
    passing = sorted(c.cell_id for c in cells if c.outcome == "match")
    path.write_text(json.dumps({
        "_doc": "Gītā tiṅanta cells the engine derives exactly as Saṃsādhanī attests. "
                "Regenerate with `python3 -m tools.samsaadhanii_coverage --write-baseline`; "
                "only ever grow this list.",
        "passing": passing,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def load_baseline(path: Path = BASELINE) -> list[str]:
    return json.loads(path.read_text(encoding="utf-8"))["passing"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", choices=("match", "mismatch", "error", "unresolved"))
    ap.add_argument("--write-baseline", action="store_true")
    a = ap.parse_args(argv)

    cells = run(load_cells())
    print(summarize(cells))
    if a.show:
        print(f"\n{a.show}:")
        for c in sorted((c for c in cells if c.outcome == a.show), key=lambda c: -len(c.refs)):
            got = f" → {c.produced}" if c.produced else ""
            print(f"  {c.word_slp1:<16}{got:<20} {c.key}  [{', '.join(c.refs[:3])}] {c.detail}")
    if a.write_baseline:
        write_baseline(cells)
        print(f"\nbaseline: {BASELINE.relative_to(_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
