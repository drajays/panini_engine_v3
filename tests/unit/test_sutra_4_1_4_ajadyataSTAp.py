from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from phonology.ajadi_tap_4_1_4 import is_hrasva_akaranta_tapara, is_ajadi_stem, tap_4_1_4_applies


def _stem(slp1: str, *, strI: bool = True, extra_tags: set | None = None) -> Term:
    tags = {"prātipadika", "anga"}
    if strI:
        tags.add("strīliṅga")
    if extra_tags:
        tags |= extra_tags
    varnas = [mk(c) for c in slp1]
    return Term(
        kind="prakriti",
        varnas=varnas,
        tags=tags,
        meta={"upadesha_slp1": slp1},
    )


def test_metadata():
    r = SUTRA_REGISTRY["4.1.4"]
    assert r.sutra_id == "4.1.4"
    assert r.sutra_type is SutraType.VIDHI


def test_phonology_tapara_excludes_dirgha_a():
    assert is_hrasva_akaranta_tapara("kIlAlapA") is False
    assert is_hrasva_akaranta_tapara("Kawva") is True


def test_phonology_ajadi_membership():
    assert is_ajadi_stem("aja") is True
    assert is_ajadi_stem("xyz") is False


def test_tap_eligibility_union():
    assert tap_4_1_4_applies("Kawva", "Kawva") is True
    assert tap_4_1_4_applies("aja", "aja") is True
    assert tap_4_1_4_applies("kIlAlapA", "kIlAlapA") is False


def test_4_1_1_sets_strI_pratipadika_registry_when_strIliṅga():
    st = _stem("Kawva")
    s0 = State(terms=[st])
    s0 = apply_rule("4.1.1", s0)
    assert s0.samjna_registry.get("4.1.1_strI_pratipadika") is True


def test_inserts_wAp_residue_after_strI_adhikara():
    st = _stem("Kawva")
    s0 = State(terms=[st])
    s0 = apply_rule("4.1.1", s0)
    s0 = apply_rule("4.1.3", s0)
    s1 = apply_rule("4.1.4", s0)
    assert any("stri_wAp" in t.tags for t in s1.terms)
    assert len(s1.terms) == 2
    assert s1.terms[1].meta.get("upadesha_slp1") == "wAp"
    assert "TAp_anta" not in s1.terms[0].tags


def test_adds_TAp_anta_when_stem_has_upasarjana():
    st = _stem("uttarapUrva", extra_tags={"upasarjana", "bahuvrihi", "diksamasa"})
    s0 = State(terms=[st])
    s0 = apply_rule("4.1.1", s0)
    s0 = apply_rule("4.1.3", s0)
    s1 = apply_rule("4.1.4", s0)
    assert "TAp_anta" in s1.terms[0].tags
    assert "strīliṅga" in s1.terms[0].tags


def test_skips_tyadadi():
    st = _stem("tad", extra_tags={"tyadadi"})
    s0 = State(terms=[st])
    s0 = apply_rule("4.1.1", s0)
    s0 = apply_rule("4.1.3", s0)
    s1 = apply_rule("4.1.4", s0)
    assert len(s1.terms) == 1


def test_skips_Iiyas_bahuvrIhi_pratishedha():
    st = _stem("bahuSreyasI", extra_tags={"Iyas_bahuvrIhi_pratishedha"})
    s0 = State(terms=[st])
    s0 = apply_rule("4.1.1", s0)
    s0 = apply_rule("4.1.3", s0)
    s1 = apply_rule("4.1.4", s0)
    assert len(s1.terms) == 1


def test_subanta_strI_Kawva_prathamA_applies_4_1_4_in_trace():
    from pipelines.subanta import derive

    s = derive("Kawva", 1, 1, linga="strīliṅga")
    assert any(step.get("sutra_id") == "4.1.4" for step in s.trace)
    assert "Kawv" in s.flat_slp1()
