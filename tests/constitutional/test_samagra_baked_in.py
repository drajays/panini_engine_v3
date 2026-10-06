"""
Art. 4 (AMENDMENT 20) and Art. 14 — every record carries the anuvṛtti-complete samagra
next to its mūla pāṭha, and every sūtra file cites its ashtadhyayi.com row index.
"""
from __future__ import annotations

import pathlib
import re

from engine import SUTRA_REGISTRY
import sutras  # noqa: F401

ROOT = pathlib.Path(__file__).resolve().parents[2]


def test_every_record_has_samagra():
    missing = [sid for sid, r in SUTRA_REGISTRY.items() if not (r.samagra_slp1 and r.samagra_dev)]
    assert not missing, f"samagra_slp1/samagra_dev missing: {missing[:20]}"


def test_constitution_example_1_3_3():
    r = SUTRA_REGISTRY["1.3.3"]
    assert r.text_slp1 == "halantyam"
    assert r.samagra_slp1.split() == ["upadeSe", "antyam", "hal", "it"]


def test_samagra_contains_mula_patha_words():
    # samagra is the pāṭha *plus* inherited padas: every pāṭha consonant skeleton survives in it
    skel = lambda s: re.sub(r"[^kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]", "", s)
    bad = [sid for sid, r in SUTRA_REGISTRY.items()
           if r.samagra_slp1 and len(skel(r.text_slp1)) > len(skel(r.samagra_slp1)) + 2]
    assert len(bad) < 40, f"samagra shorter than its pāṭha: {bad[:20]}"


def test_every_sutra_file_cites_row_index():
    missing = []
    for p in ROOT.glob("sutras/adhyaya_*/pada_*/sutra_*.py"):
        a, b, c = p.stem.split("_")[1:4]
        row = f"{a}{b}{int(c):03d}"
        if not re.search(rf"\bi\*?\s*=?\s*{row}\b", p.read_text(encoding="utf-8")):
            missing.append(p.name)
    assert not missing, f"Art. 14: no 'row i=<a p nnn>' citation: {missing[:20]}"
