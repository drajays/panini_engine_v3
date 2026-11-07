"""engine/samkhya.py — the laukika saṅkhyā words the Kāśikā names, as a lexical fact (data/inputs/samkhya_patha.json, tools/intake_patha.py).

1.1.23 names bahu, gaṇa, vatu, ḍati; the primitive numerals are laukika. The Kāśikā on 1.1.24 / 7.1.21 names the six ṣaṭ-saṃjñaka ones
(ṣaṣ, pañcan, saptan, aṣṭan, navan, daśan); only those are entered, the rest stay source-needed."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_PATH = Path(__file__).resolve().parent.parent / "data" / "inputs" / "samkhya_patha.json"


@lru_cache(maxsize=1)
def laukika() -> frozenset[str]:
    """The numeral stems (SLP1, upadeśa form) the data file lists."""
    return frozenset(e["slp1"] for e in json.loads(_PATH.read_text(encoding="utf-8"))["laukika_numerals"]["entries"])
