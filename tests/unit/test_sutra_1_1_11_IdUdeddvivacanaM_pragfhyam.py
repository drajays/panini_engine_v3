"""
1.1.11 ईदूदेद्द्विवचनं प्रगृह्यम् — *pragṛhya* vowel set (dual context in *vidhi*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_11 as s1111


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.11"]
    assert r.sutra_id == "1.1.11"
    assert r.sutra_type is SutraType.SAMJNA
    assert "I" in r.text_slp1 or "dU" in r.text_slp1


def test_vowel_membership():
    # ईत् · ऊत् · एत् — exactly three, no more.
    for slp1 in ("I", "U", "e"):
        assert s1111.is_pragrahya_slp1_vowel(slp1)
    # ऐ, ओ, औ are NOT named by this sūtra: *rāmau* is not pragṛhya, hence
    # *rāmau + imau → rāmāv imau* (6.1.78).  Final *o* of a nipāta is 1.1.15.
    for slp1 in ("E", "o", "O", "a", "A"):
        assert not s1111.is_pragrahya_slp1_vowel(slp1)


def test_samjna_bootstrap_idempotent():
    # Audit P1b: 1.1.11 fires only when some Term has a pragṛhya-eligible
    # vowel anta (ī, ū, e). Use a stem ending in ī (g + I).
    t = Term(kind="prakriti", varnas=[mk("g"), mk("I")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.11", s0)
    assert s1.samjna_registry.get("pragrahya") == s1111.PRAGHYA_VOWEL_SLP1
    s2 = apply_rule("1.1.11", s1)
    assert s2.samjna_registry.get("pragrahya") == s1.samjna_registry.get("pragrahya")


def test_no_stamp_when_no_pragriya_eligible_anta():
    """Audit P1b: a derivation with no pragṛhya-eligible vowel anta (e.g.
    रामाणाम् stem 'rAma') should NOT stamp the registry."""
    t = Term(kind="prakriti", varnas=[mk("a")])  # final 'a' is hrasva, not pragṛhya
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.11", s0)
    assert not s1111.pragrahya_samjna_is_registered(s1)


def test_pragrahya_samjna_is_registered():
    s = State(terms=[], samjna_registry={"pragrahya": s1111.PRAGHYA_VOWEL_SLP1})
    assert s1111.pragrahya_samjna_is_registered(s)


def test_act_tags_pragrahya_on_a_dvivacana_pada():
    """प्रगृह्य belongs to the finished dual *pada* (1.4.14)."""
    t = Term(
        kind="pada",
        varnas=[mk("g"), mk("I")],
        tags={"prātipadika", "anga", "pada"},
    )
    s0 = State(terms=[t], meta={"vibhakti_vacana": "1-2", "linga": "pulliṅga"})
    s1 = apply_rule("1.1.11", s0)
    assert s1111.PRAGHYA_TERM_TAG in s1.terms[0].tags


def test_act_does_not_tag_a_stem_still_awaiting_its_sup():
    """*nadī* is not pragṛhya before its औ arrives — else 6.1.77 is blocked
    and the dual comes out *nadīau* instead of नद्यौ."""
    t = Term(
        kind="prakriti",
        varnas=[mk("n"), mk("a"), mk("d"), mk("I")],
        tags={"prātipadika", "anga"},
    )
    s0 = State(terms=[t], meta={"vibhakti_vacana": "1-2", "linga": "strīliṅga"})
    s1 = apply_rule("1.1.11", s0)
    assert s1111.PRAGHYA_TERM_TAG not in s1.terms[0].tags
