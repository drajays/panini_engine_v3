"""7.1.2 आयनेयीनीयियः फढखछघाम् प्रत्ययादीनाम् — Ph-Ḍh-Kh-Ch-Gh openers → Āyan-…"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _state_anga_plus_pratyaya(
    stem_slp1: str,
    pratyaya_slp1: str,
    *,
    pratyaya_tags: set[str],
) -> State:
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(stem_slp1),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": stem_slp1},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(pratyaya_slp1),
        tags=set(pratyaya_tags),
        meta={"upadesha_slp1": pratyaya_slp1},
    )
    return State(terms=[stem, pr])


def test_registry() -> None:
    r = SUTRA_REGISTRY["7.1.2"]
    assert r.sutra_id == "7.1.2"
    assert "pratyayAdInAm" in r.text_slp1
    assert "6.4.1" in r.anuvritti_from


def test_Pak_to_Ayana_taddhita() -> None:
    s0 = _state_anga_plus_pratyaya("naqa", "Pak", pratyaya_tags={"taddhita"})
    s1 = apply_rule("7.1.2", s0)
    pr = s1.terms[-1]
    assert pr.meta.get("upadesha_slp1") == "Ayana"
    assert "".join(v.slp1 for v in pr.varnas) == "Ayana"


def test_Qak_to_eya() -> None:
    s0 = _state_anga_plus_pratyaya("vinatA", "Qak", pratyaya_tags={"taddhita"})
    s1 = apply_rule("7.1.2", s0)
    pr = s1.terms[-1]
    assert pr.meta.get("upadesha_slp1") == "eya"
    assert "".join(v.slp1 for v in pr.varnas) == "eya"


def test_K_to_Ina() -> None:
    s0 = _state_anga_plus_pratyaya("kula", "K", pratyaya_tags={"taddhita"})
    s1 = apply_rule("7.1.2", s0)
    pr = s1.terms[-1]
    assert pr.meta.get("upadesha_slp1") == "Ina"
    assert "".join(v.slp1 for v in pr.varnas) == "Ina"


def test_CaH_to_Iya() -> None:
    s0 = _state_anga_plus_pratyaya("SAlA", "CaH", pratyaya_tags={"taddhita"})
    s1 = apply_rule("7.1.2", s0)
    pr = s1.terms[-1]
    assert pr.meta.get("upadesha_slp1") == "Iya"


def test_G_to_iya() -> None:
    s0 = _state_anga_plus_pratyaya("kzatra", "G", pratyaya_tags={"taddhita"})
    s1 = apply_rule("7.1.2", s0)
    pr = s1.terms[-1]
    assert pr.meta.get("upadesha_slp1") == "iya"
    assert "".join(v.slp1 for v in pr.varnas) == "iya"


def test_skipped_when_krt() -> None:
    s0 = _state_anga_plus_pratyaya("kula", "K", pratyaya_tags={"taddhita", "krt"})
    s1 = apply_rule("7.1.2", s0)
    assert s1.terms[-1].meta.get("upadesha_slp1") == "K"


def test_skipped_when_sup() -> None:
    s0 = _state_anga_plus_pratyaya("rAma", "Pak", pratyaya_tags={"taddhita", "sup"})
    s1 = apply_rule("7.1.2", s0)
    assert "".join(v.slp1 for v in s1.terms[-1].varnas) == "Pak"


def test_idempotent_flag() -> None:
    s0 = _state_anga_plus_pratyaya("naqa", "Pak", pratyaya_tags={"taddhita"})
    s1 = apply_rule("7.1.2", s0)
    s2 = apply_rule("7.1.2", s1)
    assert "".join(v.slp1 for v in s2.terms[-1].varnas) == "Ayana"
