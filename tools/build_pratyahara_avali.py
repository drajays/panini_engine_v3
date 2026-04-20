"""
tools/build_pratyahara_avali.py
─────────────────────────────────

Emit every derivable pratyāhāra from the Māheśvara-sūtras: for each
phoneme `start` in the sequence and each downstream `it` marker, the
set built by phonology.pratyahara.build_pratyahara(start, end_it).

Usage:
    python -m tools.build_pratyahara_avali
    python -m tools.build_pratyahara_avali --json > avali.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from phonology.maheshvara import MAHESHVARA_SUTRAS, ordered_phoneme_sequence
from phonology.pratyahara import build_pratyahara


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--json", action="store_true",
                   help="Emit as JSON mapping 'startIT' -> sorted list.")
    args = p.parse_args(argv)

    seq = ordered_phoneme_sequence()
    it_letters = {s["it"] for s in MAHESHVARA_SUTRAS}

    out = {}
    for i, start in enumerate(seq):
        if start in it_letters:
            continue
        for j in range(i + 1, len(seq)):
            end_it = seq[j]
            if end_it not in it_letters:
                continue
            try:
                members = build_pratyahara(start, end_it)
            except ValueError:
                continue
            key = f"{start}{end_it}"
            out[key] = sorted(members)

    if args.json:
        json.dump(out, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
        print()
    else:
        for k in sorted(out):
            members = " ".join(out[k])
            print(f"{k:<6}  ({len(out[k]):2d})  {members}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
