"""
1.4.18 *asarvanāmasthāne … yaci bham* — *bha* saṃjñā on *aṅga*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def _anga_pullinga() -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("S"), mk("a"), mk("S"), mk("i"), mk("n")],
        tags={"prātipadika", "anga", "pulliṅga"},
        meta={"upadesha_slp1": "SaSin"},
    )


def _sup_Sas_first_S() -> Term:
    return Term(
        kind="pratyaya",
        varnas=[mk("S"), mk("a"), mk("s")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Sas"},
    )


def test_metadata():
    r = SUTRA_REGISTRY["1.4.18"]
    assert r.sutra_id == "1.4.18"
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.17" in r.anuvritti_from


def test_bha_pullinga_Sas_sashin():
    """Puṃ: *śas* is not *sarvanāmasthāna*; onset *ś* → *yaci* → *bha*."""
    s0 = State(terms=[_anga_pullinga(), _sup_Sas_first_S()])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" in s1.terms[0].tags
    assert 0 in s1.samjna_registry["1.4.18_bha_anga_indices"]


def test_no_bha_napumsaka_Sas():
    anga = _anga_pullinga()
    anga.tags.discard("pulliṅga")
    anga.tags.add("napuṃsaka")
    s0 = State(terms=[anga, _sup_Sas_first_S()])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" not in s1.terms[0].tags
    assert s1.samjna_registry.get("1.4.18_bha_anga_indices") in (None, frozenset())


def test_no_bha_sarvanamasthana_tag():
    pr = _sup_Sas_first_S()
    pr.tags.add("sarvanamasthana")
    s0 = State(terms=[_anga_pullinga(), pr])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" not in s1.terms[0].tags


def test_no_bha_Si_upadesha_even_if_yaci_onset():
    anga = _anga_pullinga()
    pr = Term(
        kind="pratyaya",
        varnas=[mk("S"), mk("i")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Si"},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" not in s1.terms[0].tags


def test_no_bha_su_upadesha_not_yaci_onset():
    """Nom. sg. *su~* surface begins with *s* — not *ac* / *yaṭ*-type here."""
    anga = Term(
        kind="prakriti",
        varnas=[mk("r"), mk("A"), mk("m"), mk("a")],
        tags={"prātipadika", "anga", "pulliṅga"},
        meta={"upadesha_slp1": "rAma"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=[mk("s"), mk("u")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "s~"},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" not in s1.terms[0].tags


def test_bha_y_onset_non_sarva_upadesha():
    anga = _anga_pullinga()
    pr = Term(
        kind="pratyaya",
        varnas=[mk("y"), mk("a")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "yat_test"},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" in s1.terms[0].tags


def test_bha_ac_onset_Bis_not_sarvanamasthana():
    anga = _anga_pullinga()
    pr = Term(
        kind="pratyaya",
        varnas=[mk("B"), mk("i"), mk("s")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Bis"},
    )
    s0 = State(terms=[anga, pr])
    # *Bis* is not in the puṃ/stri sarvanāmasthāna five; onset is *B* — not *yaci*.
    s1 = apply_rule("1.4.18", s0)
    assert "bha" not in s1.terms[0].tags


def test_bha_vowel_onset_non_sarvanamasthana_upadesha():
    """Synthetic *sup* with vowel-initial surface and non-listed upadeśa."""
    anga = _anga_pullinga()
    pr = Term(
        kind="pratyaya",
        varnas=[mk("a"), mk("n")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "aR_test"},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("1.4.18", s0)
    assert "bha" in s1.terms[0].tags


def test_siti_pada_1_4_16_blocks_bha_yus():
    """*ūrṇā* + *yus*: **1.4.16** *pada* blocks **1.4.18** *bha*."""
    anga = Term(
        kind="prakriti",
        varnas=[mk("U"), mk("r"), mk("R"), mk("A")],
        tags={"prātipadika", "anga", "pulliṅga"},
        meta={"upadesha_slp1": "UrRA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=[mk("y"), mk("u"), mk("s")],
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "yus"},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("1.4.17", s0)
    s2 = apply_rule("1.4.16", s1)
    s3 = apply_rule("1.4.18", s2)
    assert "pada_1_4_16" in s3.terms[0].tags
    assert "bha" not in s3.terms[0].tags


def test_bha_badhas_pada_1_4_17_Sas_order():
    """**1.4.17** *pada* on stem, then **1.4.18** *bha* removes ``pada_1_4_17``."""
    s0 = State(terms=[_anga_pullinga(), _sup_Sas_first_S()])
    s1 = apply_rule("1.4.17", s0)
    assert "pada_1_4_17" in s1.terms[0].tags
    s2 = apply_rule("1.4.16", s1)
    assert "pada_1_4_16" not in s2.terms[0].tags
    s3 = apply_rule("1.4.18", s2)
    assert "bha" in s3.terms[0].tags
    assert "pada_1_4_17" not in s3.terms[0].tags
