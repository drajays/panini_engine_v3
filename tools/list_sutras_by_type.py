"""
tools/list_sutras_by_type.py
──────────────────────────────

Dumps SUTRA_REGISTRY grouped by SutraType.  Useful for quick audits
of which SutraTypes are under-populated.

Usage:
    python -m tools.list_sutras_by_type
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib     import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, SutraType


def main():
    buckets = defaultdict(list)
    for sid, rec in SUTRA_REGISTRY.items():
        buckets[rec.sutra_type].append((sid, rec))

    for t in SutraType:
        entries = buckets.get(t, [])
        entries.sort(key=lambda p: tuple(int(x) for x in p[0].split(".")))
        print(f"\n── {t.name}  ({len(entries)} sūtra{'s' if len(entries)!=1 else ''}) ──")
        for sid, rec in entries:
            print(f"  {sid:<10}  {rec.text_dev}")

    total = len(SUTRA_REGISTRY)
    print(f"\nTotal: {total} sūtra{'s' if total != 1 else ''} in registry.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
