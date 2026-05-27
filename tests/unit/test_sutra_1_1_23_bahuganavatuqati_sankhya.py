"""
1.1.23 *bahuganavatuḍati saṅkhyā* — *saṅkhyā* *saṃjñā* for *bahu* / *gaṇa* / *vatu* / *ḍati* (ashtadhyayi *i* 11023).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_23 as s1123

_S_11023: str = "बहुगणवतुडति संख्या"


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.23"]
    assert r.sutra_id == "1.1.23"
    assert r.sutra_type is SutraType.SAMJNA
    assert "bahu" in r.text_slp1
    assert r.anuvritti_from == ()


def test_pATha():
    assert s1123._TEXT_DEV == _S_11023
    assert s1123.SUTRA.padaccheda_dev == "बहु-गण-वतु-डति / संख्या"


def test_sankhya_set():
    # Audit P1a: 1.1.23 fires only when a prātipadika in the saṅkhyā set is
    # on the tape. The test must therefore present such a stem (e.g. "bahu").
    t = Term(
        kind="prakriti",
        varnas=[mk("a")],
        tags={"prātipadika"},
        meta={"upadesha_slp1": "bahu"},
    )
    s0 = State(terms=[t], samjna_registry={})
    s1 = apply_rule("1.1.23", s0)
    assert s1123.sankhya_samjna_1_1_23_is_registered(s1)
    for stem in ("bahu", "gaNa", "vatu", "qati", "tAvat", "kati"):
        assert s1123.pratipadika_slp1_in_sankhya_samjna(s1, stem)
    assert not s1123.pratipadika_slp1_in_sankhya_samjna(s1, "rAma")
    s2 = apply_rule("1.1.23", s1)
    assert s2.samjna_registry.get(s1123.SANKHYA_KEY) is s1.samjna_registry.get(s1123.SANKHYA_KEY)


def test_no_stamp_when_no_sankhya_pratipadika():
    """Audit P1a (CONSTITUTION Art. 14): registry-stamp is suppressed for a
    derivation that has no saṅkhyā-eligible stem (e.g. राम)."""
    t = Term(
        kind="prakriti",
        varnas=[mk("a")],
        tags={"prātipadika"},
        meta={"upadesha_slp1": "rAma"},
    )
    s0 = State(terms=[t], samjna_registry={})
    s1 = apply_rule("1.1.23", s0)
    assert not s1123.sankhya_samjna_1_1_23_is_registered(s1)
