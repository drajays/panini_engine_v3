"""1.1.15 ओत् — *pragṅhya* *saṃjñā* (ashtadhyayi *i* 11015)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_15 as s1115


def test_metadata():
    r = SUTRA_REGISTRY["1.1.15"]
    assert r.sutra_id == "1.1.15"
    assert r.sutra_type is SutraType.SAMJNA
    assert r.text_slp1 == "ot"
    assert r.text_dev == "ओत्"
    assert r.anuvritti_from == ("1.1.11", "1.1.14")


def test_samjna_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.15", s0)
    assert s1115.ot_praghy_samjna_is_registered(s1)
    assert s1115.ot_gate_is_set(s1)
    s2 = apply_rule("1.1.15", s1)
    assert s2.samjna_registry.get(s1115.OT_KEY) == s1.samjna_registry.get(s1115.OT_KEY)
