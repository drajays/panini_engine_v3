"""
1.1.100 *Kāśikā* न मात्रा समासे — *paribhāṣā* (scheduling id; not Pāṇini *1.1.14* pāṭha).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_100 as s1100


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.100"]
    assert r.sutra_id == "1.1.100"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "mAtrA" in r.text_slp1
    assert "samAse" in r.text_slp1


def test_gate_set_and_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    assert s1100.GATE_KEY not in s0.paribhasha_gates
    s1 = apply_rule("1.1.100", s0)
    assert s1100.mAtrA_samAse_kaSika_paribhasha_set(s1)
    assert s1.paribhasha_gates[s1100.GATE_KEY].get("active") is True
    s2 = apply_rule("1.1.100", s1)
    assert s2.paribhasha_gates == s1.paribhasha_gates


def test_helper_false_initially():
    s = State(terms=[Term(kind="prakriti", varnas=[mk("k")])])
    assert not s1100.mAtrA_samAse_kaSika_paribhasha_set(s)
