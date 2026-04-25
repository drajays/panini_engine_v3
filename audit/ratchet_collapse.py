"""
audit/ratchet_collapse.py — safe duplicate *ratchet* utilities.

This repository collapses duplicate **scheduling** blocks incrementally by
rewiring pipelines to call canonical wrappers in ``core.canonical_pipelines``.

This script is intentionally conservative:
  - It NEVER edits pipeline code automatically (no brittle line surgery).
  - It can (a) show current duplicate counts, (b) lower the constitutional
    baseline after intentional collapses, and (c) write a progress log.

If you want an automated collapsER, implement it as *pattern-based*
refactors per-file (like we did for ``pipelines/subanta_trc.py``), not by
blind line ranges.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(".").resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audit.scheduling_block_auditor import SchedulingBlockAuditor  # noqa: E402

GATE_FILE = ROOT / "tests" / "constitutional" / "test_no_new_duplicates.py"
RATCHET_LOG = ROOT / "docs" / "ratchet_log.md"


def _read_gate_baseline() -> int:
    txt = GATE_FILE.read_text(encoding="utf-8")
    m = re.search(r"MAX_DUPLICATE_GROUPS\s*=\s*(\d+)", txt)
    if not m:
        raise RuntimeError(f"MAX_DUPLICATE_GROUPS not found in {GATE_FILE}")
    return int(m.group(1))


def _write_gate_baseline(new_value: int) -> None:
    txt = GATE_FILE.read_text(encoding="utf-8")
    out = re.sub(
        r"MAX_DUPLICATE_GROUPS\s*=\s*\d+",
        f"MAX_DUPLICATE_GROUPS = {new_value}",
        txt,
    )
    if out == txt:
        raise RuntimeError(f"failed to update MAX_DUPLICATE_GROUPS in {GATE_FILE}")
    GATE_FILE.write_text(out, encoding="utf-8")


def _audit() -> tuple[int, list]:
    a = SchedulingBlockAuditor(project_root=ROOT)
    a.scan()
    dups = a.find_duplicates()
    return len(dups), dups


def _append_log(*, baseline_before: int, baseline_after: int, current: int) -> None:
    RATCHET_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = (
        f"## {ts}\n\n"
        f"- **baseline_before**: {baseline_before}\n"
        f"- **baseline_after**: {baseline_after}\n"
        f"- **current_duplicates**: {current}\n"
        f"- **delta**: {baseline_before - baseline_after}\n\n"
    )
    if not RATCHET_LOG.exists():
        RATCHET_LOG.write_text("# Ratchet log\n\n" + entry, encoding="utf-8")
    else:
        RATCHET_LOG.write_text(RATCHET_LOG.read_text(encoding="utf-8") + entry, encoding="utf-8")


def cmd_status() -> int:
    baseline = _read_gate_baseline()
    n, dups = _audit()
    print("═" * 60)
    print("RATCHET STATUS")
    print("═" * 60)
    print(f"gate baseline        : {baseline}")
    print(f"current duplicates   : {n}")
    print(f"slack (baseline-n)   : {baseline - n}")
    print("")
    print("Progress tracker (target trajectory):")
    print("  START   : 112")
    print("  After   5: 107   (python audit/ratchet_collapse.py --run 5)")
    print("  After  10: 102")
    print("  After  20:  92")
    print("  After  50:  62")
    print("  After  80:  32")
    print("  After 100:  12")
    print("  After 112:   0")
    print("")
    if dups:
        print("Top 5 groups (longest first):")
        for g in dups[:5]:
            seq = " → ".join(g.sids[:4]) + (" …" if len(g.sids) > 4 else "")
            files = len({o.file for o in g.occurrences})
            print(f"- {g.fingerprint}  len={g.length}  files={files}  {seq}")
    else:
        print("CLEAN: zero duplicates.")
    print("═" * 60)
    return 0


def cmd_next(*, n: int = 1) -> int:
    """
    Print the next N biggest duplicate groups (largest first).

    This is intentionally *non-destructive*: collapsing is done by targeted,
    pattern-based refactors (one file at a time) with full tests, not by this
    script automatically rewriting source.
    """
    baseline = _read_gate_baseline()
    count, dups = _audit()
    if not dups:
        print("CLEAN: zero duplicates.")
        return 0

    print(f"gate baseline      : {baseline}")
    print(f"current duplicates : {count}")
    print("")
    take = max(1, int(n))
    print(f"Next {min(take, len(dups))} group(s) to collapse (largest first):")
    for i, g in enumerate(dups[:take], 1):
        seq = " → ".join(g.sids[:6]) + (" …" if len(g.sids) > 6 else "")
        files = sorted({o.file for o in g.occurrences})
        print(f"\n[{i}] {g.fingerprint}  len={g.length}  files={len(files)}")
        print(f"    {seq}")
        for o in g.occurrences[:10]:
            print(f"    - {o.file}:{o.func} ({o.start_line}–{o.end_line})")
        if len(g.occurrences) > 10:
            print(f"    … (+{len(g.occurrences)-10} more)")

    print("\nSuggested workflow:")
    print("- refactor one pipeline to call an existing canonical wrapper in `core/canonical_pipelines.py`")
    print("- run: `pytest tests/ -q`")
    print("- re-run: `python audit/scheduling_block_auditor.py .` (expect duplicates to drop)")
    print("- then: `python audit/ratchet_collapse.py --ratchet-to-current` to lower the ceiling")
    return 0


def cmd_ratchet_to_current(*, allow_increase: bool) -> int:
    baseline_before = _read_gate_baseline()
    current, _dups = _audit()
    if not allow_increase and current > baseline_before:
        print(
            f"Refusing to raise baseline: current={current} > baseline={baseline_before}. "
            "Fix duplicates or run with --allow-increase."
        )
        return 2
    _write_gate_baseline(current)
    _append_log(baseline_before=baseline_before, baseline_after=current, current=current)
    print(f"updated MAX_DUPLICATE_GROUPS: {baseline_before} → {current}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Ratchet duplicate scheduling baseline safely.")
    p.add_argument("--status", action="store_true", help="Show current baseline and duplicate count.")
    p.add_argument("--next", action="store_true", help="Show the next biggest duplicate group to collapse.")
    p.add_argument("--run", type=int, default=0, metavar="N", help="Show the next N biggest groups.")
    p.add_argument(
        "--ratchet-to-current",
        action="store_true",
        help="Set MAX_DUPLICATE_GROUPS to current duplicates count (after intentional collapses).",
    )
    p.add_argument(
        "--allow-increase",
        action="store_true",
        help="Allow raising baseline (not recommended).",
    )
    args = p.parse_args(argv)

    if args.status:
        return cmd_status()
    if args.next:
        return cmd_next(n=1)
    if args.run:
        return cmd_next(n=args.run)
    if args.ratchet_to_current:
        return cmd_ratchet_to_current(allow_increase=args.allow_increase)
    return cmd_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

