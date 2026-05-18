"""Regression: अन्य (sarvanāma, a-stem masculine) 24 cells vs ``anya_pullinga.json``."""
from __future__ import annotations

import pytest

from engine.sig import extract_applied_path
from phonology.joiner import slp1_to_devanagari
from pipelines.subanta import derive, derive_anya_pullinga

_ALL_CELLS = [f"{v}-{vv}" for v in range(1, 9) for vv in range(1, 4)]


def _contains_contiguous_subsequence(path: list[str], sequence: list[str]) -> bool:
    if not sequence:
        return True
    width = len(sequence)
    return any(path[i : i + width] == sequence for i in range(0, len(path) - width + 1))


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_anya_cell_matches_gold(anya_gold, cell):
    v, vv = cell.split("-")
    state = derive("anya", int(v), int(vv), linga="pulliṅga")
    produced = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    gold = anya_gold["cells"][cell]["form_dev"]
    assert produced == gold, f"cell {cell}: produced {produced!r}, gold {gold!r}"


@pytest.mark.parametrize("cell", _ALL_CELLS)
def test_anya_cell_slp1_matches_gold(anya_gold, cell):
    v, vv = cell.split("-")
    state = derive("anya", int(v), int(vv), linga="pulliṅga")
    produced = "".join(v.slp1 for v in state.terms[0].varnas) if state.terms else ""
    gold_slp = anya_gold["cells"][cell]["form_slp1"]
    assert produced == gold_slp, f"cell {cell}: produced {produced!r}, gold {gold_slp!r}"


def test_derive_anya_pullinga_wrapper_matches_derive():
    st1 = derive_anya_pullinga(1, 1)
    st2 = derive("anya", 1, 1, linga="pulliṅga")
    d1 = slp1_to_devanagari(st1.terms[0].varnas) if st1.terms else ""
    d2 = slp1_to_devanagari(st2.terms[0].varnas) if st2.terms else ""
    assert d1 == d2 == "अन्यः"


def test_anya_trace_smoke_prathamA_eka_r_visarga():
    st = derive("anya", 1, 1, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert _contains_contiguous_subsequence(path, ["8.2.66", "8.3.15"])


def test_anya_trace_smoke_prathamA_bahu_jas_shI_guNa():
    st = derive("anya", 1, 3, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "7.1.17" in path and "6.1.87" in path


def test_anya_trace_smoke_dvitIyA_eka_pUrvArUpa():
    st = derive("anya", 2, 1, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "6.1.107" in path


def test_anya_trace_smoke_tritIyA_bahu_bhis_ais():
    st = derive("anya", 3, 3, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "7.1.9" in path and "6.1.88" in path


def test_anya_trace_smoke_caturthI_eka_smE():
    st = derive("anya", 4, 1, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "7.1.14" in path


def test_anya_trace_smoke_pancamI_eka_smAt():
    st = derive("anya", 5, 1, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "7.1.15" in path


def test_anya_trace_smoke_saptamI_bahu_sup_shaTva():
    st = derive("anya", 7, 3, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "8.3.59" in path


def test_anya_trace_smoke_sambuddhi_eka_hal_lopa():
    st = derive("anya", 8, 1, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "6.1.69" in path


def test_anya_trace_smoke_saptamI_dvi_ayAdeza_r_visarga():
    st = derive("anya", 7, 2, linga="pulliṅga")
    path = extract_applied_path(st.trace)
    assert "6.1.78" in path
    assert _contains_contiguous_subsequence(path, ["8.2.66", "8.3.15"])
