"""
शम्भु — उकारान्त पुंलिङ्ग — 24-cell paradigm tests.

Covers:
  • derive_SamBu_pulliṅga(v, vac) matches gold reference for all 24 cells.
  • derive_ukarant_pullinga works for other u-stems (भानु, गुरु).
  • stem_slp1_looks_ukarant_pullinga guard logic.
  • Key sūtra trace assertions for the two corrected cells:
      2-3 (शम्भून्)  — 6.1.103 u-arm, NOT 6.4.146 guṇa.
      (Other cells verified via gold JSON.)
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest
import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.SamBu_subanta import (
    SAMBHU_PUM_24_CELLS,
    derive_SamBu_pulliṅga,
    derive_ukarant_pullinga,
    iter_SamBu_paradigm,
    sambhu_cell_key,
    stem_slp1_looks_ukarant_pullinga,
)
from pipelines.subanta import derive


def _gold_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "data"
        / "reference"
        / "subanta_gold"
        / "SamBu_pullinga.json"
    )


def _gold_cells() -> dict:
    with _gold_path().open(encoding="utf-8") as f:
        return json.load(f)["cells"]


# ── gold-corpus check ────────────────────────────────────────────────────────

def test_24_cells_match_gold():
    cells = _gold_cells()
    for v, vac in SAMBHU_PUM_24_CELLS:
        st = derive_SamBu_pulliṅga(v, vac)
        key = sambhu_cell_key(v, vac)
        dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
        assert dev == cells[key]["form_dev"], f"cell {key}: got {dev!r}"


def test_derive_SamBu_same_as_derive():
    for v, vac in SAMBHU_PUM_24_CELLS:
        s1 = derive_SamBu_pulliṅga(v, vac)
        s2 = derive("SamBu", v, vac, "pulliṅga")
        assert s1.flat_slp1() == s2.flat_slp1(), f"mismatch at {v}-{vac}"


# ── iter helper ──────────────────────────────────────────────────────────────

def test_iter_paradigm_length_and_keys():
    t = iter_SamBu_paradigm()
    assert len(t) == 24
    assert {k for k, _ in t} == {f"{v}-{vac}" for v in range(1, 9) for vac in range(1, 4)}


# ── sūtra-trace assertions for the critical cells ───────────────────────────

def _fired(st, sutra_id: str) -> bool:
    return any(
        e.get("sutra_id") == sutra_id and e.get("status", "").startswith("APPLIED")
        for e in st.trace
    )


def test_2_3_uses_6_1_103_not_6_4_146_guna():
    """शम्भु + शस् → शम्भून् via pūrva-savarṇa dīrgha (6.1.103 u-arm), NOT bhasya guṇa."""
    st = derive_SamBu_pulliṅga(2, 3)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भून्", f"got {dev!r}"
    # 6.1.103 must fire
    assert _fired(st, "6.1.103"), "6.1.103 did not fire for 2-3"
    # 6.4.146 must NOT have changed u→o (stem would have ended in 'o' before 6.1.103)
    guna_fired_wrongly = any(
        e.get("sutra_id") == "6.4.146"
        and e.get("status", "").startswith("APPLIED")
        and "→" in str(e.get("form_after", ""))
        and "o" in str(e.get("form_after", "")).lower()
        and "SamBo" in str(e.get("form_after", ""))
        for e in st.trace
    )
    assert not guna_fired_wrongly, "6.4.146 wrongly applied guṇa (u→o) before śas"


def test_1_1_nom_sg_trace():
    """शम्भु + सुँ → शम्भुः via 8.2.66 + 8.3.15."""
    st = derive_SamBu_pulliṅga(1, 1)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भुः"
    assert _fired(st, "8.2.66")
    assert _fired(st, "8.3.15")


def test_1_3_nom_pl_trace():
    """शम्भु + जस् → शम्भवः via 7.3.109 (गुण) + 6.1.78 (एचोऽयवायावः)."""
    st = derive_SamBu_pulliṅga(1, 3)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भवः"
    assert _fired(st, "7.3.109")
    assert _fired(st, "6.1.78")


def test_4_1_dat_sg_trace():
    """शम्भु + ङे → शम्भवे via 7.3.111 (घेर्ङिति गुण) + 6.1.78."""
    st = derive_SamBu_pulliṅga(4, 1)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भवे"
    assert _fired(st, "7.3.111")
    assert _fired(st, "6.1.78")


def test_6_2_gen_du_trace():
    """शम्भु + ओस् → शम्भ्वोः via 6.1.77 (इको यणचि)."""
    st = derive_SamBu_pulliṅga(6, 2)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भ्वोः"
    assert _fired(st, "6.1.77")


def test_6_3_gen_pl_trace():
    """शम्भु + आम् → शम्भूनाम् via 7.1.54 (नुट्) + 6.4.3 (नामी दीर्घ)."""
    st = derive_SamBu_pulliṅga(6, 3)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भूनाम्"
    assert _fired(st, "7.1.54")
    assert _fired(st, "6.4.3")


def test_7_1_loc_sg_trace():
    """शम्भु + ङि → शम्भौ via 7.3.119 + 6.1.88 (वृद्धि)."""
    st = derive_SamBu_pulliṅga(7, 1)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भौ"
    assert _fired(st, "6.1.88")


def test_8_1_voc_sg_trace():
    """शम्भु + सु (सम्बुद्धि) → शम्भो via 7.3.108 (ह्रस्वस्य गुणः) + 6.1.69."""
    st = derive_SamBu_pulliṅga(8, 1)
    dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
    assert dev == "शम्भो"
    assert _fired(st, "7.3.108")
    assert _fired(st, "6.1.69")


# ── derive_ukarant_pullinga helper ───────────────────────────────────────────

def test_ukarant_helper_SamBu_matches():
    for v, vac in SAMBHU_PUM_24_CELLS:
        s1 = derive_ukarant_pullinga("SamBu", v, vac)
        s2 = derive_SamBu_pulliṅga(v, vac)
        assert s1.flat_slp1() == s2.flat_slp1(), f"mismatch at {v}-{vac}"


def test_ukarant_helper_BAnu():
    """भानु (BAnu) shares the same u-stem spine."""
    cells_dev = {
        "1-1": "भानुः", "1-2": "भानू", "1-3": "भानवः",
        "2-1": "भानुम्", "2-2": "भानू", "2-3": "भानून्",
        "6-3": "भानूनाम्", "7-1": "भानौ", "8-1": "भानो",
    }
    for key, expected in cells_dev.items():
        v, vac = map(int, key.split("-"))
        st = derive_ukarant_pullinga("BAnu", v, vac)
        dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
        assert dev == expected, f"BAnu {key}: got {dev!r}, want {expected!r}"


def test_ukarant_helper_guru():
    """गुरु (guru) — same ghī-saṃjñaka u-stem paradigm."""
    cells_dev = {
        "1-1": "गुरुः", "1-2": "गुरू", "1-3": "गुरवः",
        "2-3": "गुरून्", "4-1": "गुरवे", "6-3": "गुरूणाम्",
        "7-1": "गुरौ", "8-1": "गुरो",
    }
    for key, expected in cells_dev.items():
        v, vac = map(int, key.split("-"))
        st = derive_ukarant_pullinga("guru", v, vac)
        dev = slp1_to_devanagari(st.terms[0].varnas) if st.terms else ""
        assert dev == expected, f"guru {key}: got {dev!r}, want {expected!r}"


def test_ukarant_helper_rejects_non_u_stem():
    with pytest.raises(ValueError, match="उकारान्त"):
        derive_ukarant_pullinga("hari", 1, 1)
    with pytest.raises(ValueError, match="उकारान्त"):
        derive_ukarant_pullinga("rAma", 1, 1)


# ── stem shape guard ─────────────────────────────────────────────────────────

def test_stem_ukarant_positive():
    assert stem_slp1_looks_ukarant_pullinga("SamBu")
    assert stem_slp1_looks_ukarant_pullinga("guru")
    assert stem_slp1_looks_ukarant_pullinga("  BAnu  ")


def test_stem_ukarant_negative():
    assert not stem_slp1_looks_ukarant_pullinga("")
    assert not stem_slp1_looks_ukarant_pullinga("hari")
    assert not stem_slp1_looks_ukarant_pullinga("rAma")
    assert not stem_slp1_looks_ukarant_pullinga("SamBuH")
