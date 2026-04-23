"""
1.1.7 हलोऽनन्तराः संयोगः — *saṃyoga* = contiguous *hal*; registry bootstrap.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term, Varna
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_7 as s117


def _v(*chars: str) -> list:
    return [Varna(slp1=c, dev="", tags=set()) for c in chars]


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.7"]
    assert r.sutra_id == "1.1.7"
    assert r.sutra_type is SutraType.SAMJNA
    assert "halo" in r.text_slp1.lower() or "hal" in r.text_slp1


def test_hal_letter_vs_ac():
    assert s117.is_hal_letter("k")
    assert s117.is_hal_letter("A") is False
    assert s117.is_hal_letter("a") is False


def test_has_samyoga_consecutive_hals():
    assert s117.has_samyoga_consecutive_hals(_v("k", "t"))
    assert s117.has_samyoga_consecutive_hals(_v("h", "r"))
    # hal–vowel–hal: only non-adjacent hals, not 1.1.7 *saṃyoga* span
    assert not s117.has_samyoga_consecutive_hals(_v("k", "a", "t"))


def test_samjna_bootstrap_idempotent():
    t = Term(kind="prakriti", varnas=[mk("r"), mk("A"), mk("m"), mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.7", s0)
    assert s1.samjna_registry.get("samyoga") == s117.SAMYOGA_REGISTER_VALUE
    s2 = apply_rule("1.1.7", s1)
    assert s2.samjna_registry.get("samyoga") == s1.samjna_registry.get("samyoga")


def test_samyoga_samjna_is_registered_helper():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s = State(terms=[t], samjna_registry={"samyoga": s117.SAMYOGA_REGISTER_VALUE})
    assert s117.samyoga_samjna_is_registered(s)
