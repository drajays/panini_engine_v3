"""Regression: राधा (ā-stem strī) 24 cells vs ``data/reference/subanta_gold/rADA_strilinga.json``."""
from __future__ import annotations

import pytest

from engine.sig import extract_applied_path
from phonology.joiner import slp1_to_devanagari
from pipelines.subanta import derive

_ALL_CELLS = [f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)]


def _contains_contiguous_subsequence(path: list[str], sequence: list[str]) -> bool:
    if not sequence:
        return True
    width = len(sequence)
    return any(path[i : i + width] == sequence for i in range(0, len(path) - width + 1))


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_rADA_strI_cell_matches_gold(rADA_strI_gold, cell):
    v, vv = cell.split("-")
    state = derive("rADA", int(v), int(vv), linga="strīliṅga")
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = rADA_strI_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"


def test_derive_akarant_strilinga_wrapper_matches_gold_cell():
    from pipelines.subanta import derive_akarant_strilinga

    st = derive_akarant_strilinga("rADA", 8, 1)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "राधे"


def test_derive_akarant_strilinga_rejects_non_A_final():
    from pipelines.subanta import derive_akarant_strilinga

    with pytest.raises(ValueError, match="दीर्घ"):
        derive_akarant_strilinga("rAma", 1, 1)


def test_rADA_strI_trace_smoke_prathamA_eka_includes_6_1_68():
    """Glass-box anchor: apṛkta *su*-lopa on long-ā strī stem (cf. plan / clips)."""
    st = derive("rADA", 1, 1, linga="strīliṅga")
    path = extract_applied_path(st.trace)
    assert "6.1.68" in path


def test_rADA_strI_trace_smoke_sambuddhi_eka_7_3_106_then_6_1_69():
    st = derive("rADA", 8, 1, linga="strīliṅga")
    path = extract_applied_path(st.trace)
    assert _contains_contiguous_subsequence(path, ["7.3.106", "6.1.69"])


def test_rADA_strI_trace_smoke_sambuddhi_dvi_6_1_87():
    """Engine path uses **6.1.87** (Ā + dual ``O``) for surface राधे; clip may cite 7.1.18 + 1.1.55."""
    st = derive("rADA", 8, 2, linga="strīliṅga")
    path = extract_applied_path(st.trace)
    assert "6.1.87" in path


def test_rADA_strI_trace_smoke_sambuddhi_bahu_jas_tripadi():
    st = derive("rADA", 8, 3, linga="strīliṅga")
    path = extract_applied_path(st.trace)
    assert _contains_contiguous_subsequence(path, ["6.1.101", "1.4.110", "8.2.66", "8.3.15"])
