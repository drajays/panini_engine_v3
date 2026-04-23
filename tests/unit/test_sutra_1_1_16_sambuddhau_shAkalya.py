"""1.1.16 सम्बुद्धौ शाकल्यस्य… — *saṃjñā* (ashtadhyayi *i* 11016)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_16 as s1116


def test_metadata():
    r = SUTRA_REGISTRY["1.1.16"]
    assert r.sutra_id == "1.1.16"
    assert r.sutra_type is SutraType.SAMJNA
    assert r.text_slp1 == s1116.TEXT_SLP1
    assert "शाकल्य" in r.text_dev


def test_samjna_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.16", s0)
    assert s1116.sambuddhau_shakalya_samjna_is_registered(s1)
    assert s1116.sambuddhau_shakalya_gate_is_set(s1)
    s2 = apply_rule("1.1.16", s1)
    assert s2.samjna_registry.get(s1116.SAMJNA_KEY) == s1.samjna_registry.get(s1116.SAMJNA_KEY)
