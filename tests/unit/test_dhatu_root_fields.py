"""
AMENDMENT 20 §7 — the two derived root fields of the dhātupāṭha mean exactly what they say.
Regenerate with ``python3 scripts/fill_dhatu_it_lopa.py``.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def entries():
    return json.loads((ROOT / "data/inputs/dhatupatha_upadesha.json").read_text(encoding="utf-8"))["entries"]


def test_raw_field_is_the_engine_it_lopa_residue(entries):
    from scripts.fill_dhatu_it_lopa import it_lopa_residue

    bad = [(e["id"], e["upadesha_slp1"], e["raw_dhatu_after_it_lopa_slp1"], it_lopa_residue(e["id"]))
           for e in entries if e["raw_dhatu_after_it_lopa_slp1"] != it_lopa_residue(e["id"])]
    assert not bad, f"{len(bad)} drifted (run scripts/fill_dhatu_it_lopa.py): {bad[:10]}"


def test_citation_field_is_the_mula_dhatu(entries):
    from phonology.tokenizer import devanagari_to_slp1_flat

    bad = [e["id"] for e in entries
           if e["citation_dhatu_dev"] != e["mula_dhatu_dev"]
           or e["citation_dhatu_slp1"] != devanagari_to_slp1_flat(e["mula_dhatu_dev"])]
    assert not bad, bad[:10]


@pytest.mark.parametrize("eid,raw,citation", [
    ("BvAdi_01_0056", "Rad", "nad"),      # णदँ: 1.3.7 is pratyaya-only — ṇ stays; 6.1.65 gives the citation nad
    ("curAdi_10_0002", "cit", "cint"),    # चितिँ: idit — num (7.1.58) is in the citation, not in the it-lopa residue
    ("BvAdi_01_0434", "trap", "trap"),    # त्रपूँष्: 1.3.3 removes the final ष्
    ("BvAdi_01_1143", "dfS", "dfS"),      # दृशिँर्: irit (1.3.2 vārttika)
])
def test_examples(entries, eid, raw, citation):
    e = next(x for x in entries if x["id"] == eid)
    assert (e["raw_dhatu_after_it_lopa_slp1"], e["citation_dhatu_slp1"]) == (raw, citation)


def test_lookup_accepts_citation_root():
    from pipelines.dhatupatha import resolve_dhatu_identifier

    assert resolve_dhatu_identifier("cint")["upadesha_slp1"] == "citi~"   # citation only (raw is 'cit')
    assert resolve_dhatu_identifier("pac")["upadesha_slp1"] == "qupaca~z"  # डुपचँष्, not पचिँ
