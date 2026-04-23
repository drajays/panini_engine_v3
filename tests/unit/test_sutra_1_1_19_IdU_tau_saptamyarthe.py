"""
1.1.19 *IdU tau ca saptamyarthe* — *pragṅhya* *saptamī*-*artha* extension (after **1.1.11**).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_19 as s1119
from sutras.adhyaya_1.pada_1 import sutra_1_1_11 as s1111

# Ashtadhyayi i=11019 *s* (must match ``_TEXT_DEV`` in ``sutra_1_1_19``).
_S_11019: str = (
    "\u0908\u0926\u0942\u0924\u094c \u091a \u0938\u092a\u094d\u0924\u092e\u094d\u092f\u0930\u094d\u0925\u0947"
)


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.19"]
    assert r.sutra_id == "1.1.19"
    assert r.sutra_type is SutraType.SAMJNA
    assert "IdU" in r.text_slp1
    assert r.anuvritti_from == ("1.1.11",)


def test_pATha_bytes_match_ashtadhyayi_s():
    assert s1119._TEXT_DEV == _S_11019


def test_samjna_bootstrap():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t], samjna_registry={"pragrahya": s1111.PRAGHYA_VOWEL_SLP1})
    s1 = apply_rule("1.1.19", s0)
    assert s1119.eeUu_tau_saptamIartha_samjna_is_registered(s1)
    s2 = apply_rule("1.1.19", s1)
    assert s1.samjna_registry.get(s1119.PRAGHYA_SAPTAMI_EE_UU_KEY) is True
    assert s2.samjna_registry.get(s1119.PRAGHYA_SAPTAMI_EE_UU_KEY) is True


def test_requires_1_1_11_bootstrap():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t], samjna_registry={})
    s1 = apply_rule("1.1.19", s0)
    assert not s1119.eeUu_tau_saptamIartha_samjna_is_registered(s1)
    s2 = apply_rule("1.1.11", s0)
    s3 = apply_rule("1.1.19", s2)
    assert s1119.eeUu_tau_saptamIartha_samjna_is_registered(s3)
