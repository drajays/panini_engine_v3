"""1.1.17 उञः — paribhāṣā (ashtadhyayi i=11017)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_17 as s1117


def test_metadata():
    r = SUTRA_REGISTRY["1.1.17"]
    assert r.sutra_id == "1.1.17"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert r.text_slp1 == "uYaH"
    assert r.text_dev == "उञः"


def test_gate_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.17", s0)
    assert s1117.uYaH_gate_is_set(s1)
    s2 = apply_rule("1.1.17", s1)
    assert s2.paribhasha_gates == s1.paribhasha_gates
