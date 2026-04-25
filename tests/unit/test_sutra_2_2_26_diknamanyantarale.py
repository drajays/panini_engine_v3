from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule


def _with_samasa_adhikara(s: State) -> State:
    return apply_rule("2.1.3", s)
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_metadata():
    r = SUTRA_REGISTRY["2.2.26"]
    assert r.sutra_id == "2.2.26"
    assert r.sutra_type is SutraType.VIDHI


def test_merges_dakziRa_pUrva():
    t1 = Term(kind="prakriti", varnas=[mk("d")], tags={"prātipadika"}, meta={"dik_name": "dakziRa"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrva"})
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))

    s1 = apply_rule("2.2.26", s0)
    assert len(s1.terms) == 1
    assert s1.terms[0].meta.get("upadesha_slp1") == "dakziRapUrva"
    assert {"diksamasa", "bahuvrihi", "hrasva_final", "upasarjana"}.issubset(s1.terms[0].tags)
    assert s1.meta.get("diksamasa_compound") is True
    assert s1.meta.get("bahuvrihi_formed") is True
    assert s1.meta.get("vartika_puMvat_applied") is False
    assert s1.meta.get("1_2_48_hrasva_applied") is True


def test_merges_uttrA_pUrvA_aliases():
    t1 = Term(kind="prakriti", varnas=[mk("u")], tags={"prātipadika"}, meta={"dik_name": "uttrA"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrvA"})
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert s1.flat_slp1() == "uttarapUrva"
    assert {"bahuvrihi", "diksamasa", "hrasva_final", "upasarjana"}.issubset(s1.terms[0].tags)
    assert s1.meta.get("diksamasa_compound") is True
    assert s1.meta.get("bahuvrihi_formed") is True
    assert s1.meta.get("vartika_puMvat_applied") is True
    assert s1.meta.get("1_2_48_hrasva_applied") is True


def test_dik_name_normalizes_spaced_uttrA_Ns():
    t1 = Term(
        kind="prakriti",
        varnas=[mk("u")],
        tags={"prātipadika"},
        meta={"dik_name": "uttrA Ns"},
    )
    t2 = Term(
        kind="prakriti",
        varnas=[mk("p")],
        tags={"prātipadika"},
        meta={"dik_name": "pUrvA Ns"},
    )
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert s1.flat_slp1() == "uttarapUrva"


def test_no_merge_without_samasa_adhikara():
    t1 = Term(kind="prakriti", varnas=[mk("d")], tags={"prātipadika"}, meta={"dik_name": "dakziRa"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrva"})
    s0 = State(terms=[t1, t2], meta={"diksamasa_compound": True})
    s1 = apply_rule("2.2.26", s0)
    assert len(s1.terms) == 2


def test_yaugika_meta_blocks_merge():
    t1 = Term(
        kind="prakriti",
        varnas=[mk("d")],
        tags={"prātipadika"},
        meta={"dik_name": "dakziRa", "dik_yaugika": True},
    )
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrva"})
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert len(s1.terms) == 2


def test_asymmetric_diknama_tag_blocks_merge():
    t1 = Term(
        kind="prakriti",
        varnas=[mk("d")],
        tags={"prātipadika", "diknama"},
        meta={"dik_name": "dakziRa"},
    )
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrva"})
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert len(s1.terms) == 2


def test_vartika_puMvat_meta_true_for_strI_type_dik_names():
    t1 = Term(kind="prakriti", varnas=[mk("u")], tags={"prātipadika"}, meta={"dik_name": "uttrA"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrvA"})
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert s1.terms[0].meta.get("vartika_sarvanAma_puMvat_vrtti") is True


def test_vartika_puMvat_meta_false_for_hrasva_a_only_dik_names():
    t1 = Term(kind="prakriti", varnas=[mk("d")], tags={"prātipadika"}, meta={"dik_name": "dakziRa"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrva"})
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert s1.terms[0].meta.get("vartika_sarvanAma_puMvat_vrtti") is False


def test_both_diknama_tags_merge():
    t1 = Term(
        kind="prakriti",
        varnas=[mk("d")],
        tags={"prātipadika", "diknama"},
        meta={"dik_name": "dakziRa"},
    )
    t2 = Term(
        kind="prakriti",
        varnas=[mk("p")],
        tags={"prātipadika", "diknama"},
        meta={"dik_name": "pUrva"},
    )
    s0 = _with_samasa_adhikara(State(terms=[t1, t2], meta={"diksamasa_compound": True}))
    s1 = apply_rule("2.2.26", s0)
    assert len(s1.terms) == 1
    assert s1.terms[0].meta.get("upadesha_slp1") == "dakziRapUrva"


def test_cond_false_without_meta_flag():
    t1 = Term(kind="prakriti", varnas=[mk("d")], tags={"prātipadika"}, meta={"dik_name": "dakziRa"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={"dik_name": "pUrva"})
    s0 = State(terms=[t1, t2], meta={})

    s1 = apply_rule("2.2.26", s0)
    assert len(s1.terms) == 2
