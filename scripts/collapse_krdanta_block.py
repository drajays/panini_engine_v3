#!/usr/bin/env python3
"""
scripts/collapse_krdanta_block.py

SAFE MANUAL COLLAPSE AID (krdanta-focused)
=========================================
This script does **not** auto-edit pipeline code. It supports the manual
collapse protocol:

1) Identify the largest duplicate scheduling block that involves `pipelines/krdanta.py`
2) Print exact file/line ranges and the source lines to replace
3) Create a timestamped backup of `pipelines/krdanta.py`

Run from repo root:

    python scripts/collapse_krdanta_block.py
"""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(".").resolve()
KRDANTA = ROOT / "pipelines" / "krdanta.py"
BACKUP_DIR = ROOT / ".collapse_backups"


def main() -> int:
    if not KRDANTA.is_file():
        raise SystemExit(f"missing: {KRDANTA}")

    # Show current state
    lines = KRDANTA.read_text(encoding="utf-8").splitlines()
    print("Current krdanta.py line count:", len(lines))

    # Backup
    BACKUP_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bk = BACKUP_DIR / f"{ts}_krdanta.py.bak"
    shutil.copy2(KRDANTA, bk)
    print(f"Backed up to: {bk}")

    # Find the largest duplicate group involving krdanta
    import sys

    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from audit.scheduling_block_auditor import SchedulingBlockAuditor

    a = SchedulingBlockAuditor(project_root=str(ROOT))
    a.scan()
    dups = a.find_duplicates()

    krdanta_groups = sorted(
        [g for g in dups if any("pipelines/krdanta.py" == o.file for o in g.occurrences)],
        key=lambda g: -g.length,
    )

    if not krdanta_groups:
        print("No krdanta duplicates found — already clean!")
        return 0

    g = krdanta_groups[0]
    print()
    print(f"Target block : {g.fingerprint}")
    print(f"Length       : {g.length}")
    print(f"Sequence     : {' -> '.join(g.sids)}")
    print()

    for o in g.occurrences:
        if o.file != "pipelines/krdanta.py":
            continue
        print(f"Location     : {o.file}:{o.func}  L{o.start_line}-{o.end_line}")
        print("=== BLOCK TO REPLACE ===")
        for i in range(o.start_line - 1, o.end_line):
            if 0 <= i < len(lines):
                print(f"  {i+1:4d}: {lines[i]}")
        print("========================")
        print()

    print("Next steps (manual, safest):")
    print("- Map this block to an existing helper in `core/canonical_pipelines.py` (or extract one).")
    print("- Replace each occurrence with a single canonical call.")
    print("- Run: `pytest tests/ -q`")
    print("- Run: `python audit/scheduling_block_auditor.py .` and then ratchet:")
    print("        `python audit/ratchet_collapse.py --ratchet-to-current`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

