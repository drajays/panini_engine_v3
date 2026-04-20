"""
phonology/maheshvara.py — Māheśvara-sūtras as data.
─────────────────────────────────────────────────────

Reads data/inputs/maheshvara_sutras.json at import time.
The file is the SINGLE source of truth for the Śiva-sūtras.

Format (data/inputs/maheshvara_sutras.json):
[
  { "index": 1,  "phonemes": ["a","i","u"],           "it": "N" },
  { "index": 2,  "phonemes": ["f","x"],               "it": "k" },
  ...
]

The `it` letter is NOT mixed into `phonemes`; it is the group-closer.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing  import List, Tuple

_DATA = Path(__file__).parent.parent / "data" / "inputs" / "maheshvara_sutras.json"


def _load():
    with _DATA.open(encoding="utf-8") as f:
        return json.load(f)


MAHESHVARA_SUTRAS = _load()


def ordered_phoneme_sequence() -> List[str]:
    """
    Return the full left-to-right phoneme+it sequence:
      [a, i, u, N, f, x, k, e, o, ng, E, O, c, h, y, v, r, w, l, n, m, ...]
    Used by pratyāhāra derivation.
    """
    seq: List[str] = []
    for s in MAHESHVARA_SUTRAS:
        seq.extend(s["phonemes"])
        seq.append(s["it"])
    return seq


def phoneme_it_pairs() -> List[Tuple[str, str]]:
    """(phoneme, its_group_it) pairs — used by savarṇa tests."""
    out = []
    for s in MAHESHVARA_SUTRAS:
        for p in s["phonemes"]:
            out.append((p, s["it"]))
    return out
