"""1.1.62 प्रत्ययलोपे प्रत्ययलक्षणम् — *pratyaya-lakṣaṇa* paribhāṣā (gate)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State

from sutras.adhyaya_1.pada_1.pratyayalakshanam_1_1_62 import (
    PRATYAYALAKSHANAM_GATE,
    pratyayalakshanam_paribhasha_is_active,
)


def test_registry() -> None:
    r = SUTRA_REGISTRY["1.1.62"]
    assert r.sutra_type.name == "PARIBHASHA"
    assert r.sutra_id == "1.1.62"
    assert r.text_slp1 == "pratyayalope pratyayalakzaNam"
    assert r.text_dev == "प्रत्ययलोपे प्रत्ययलक्षणम्"
    assert "सप्तमी" in r.padaccheda_dev
    assert r.anuvritti_from == ()


def test_paribhasha_gate_idempotent() -> None:
    s0 = State(terms=[])
    s1 = apply_rule("1.1.62", s0)
    assert pratyayalakshanam_paribhasha_is_active(s1)
    assert s1.paribhasha_gates.get(PRATYAYALAKSHANAM_GATE) is True
    s2 = apply_rule("1.1.62", s1)
    assert pratyayalakshanam_paribhasha_is_active(s2)
    assert s2.paribhasha_gates.get(PRATYAYALAKSHANAM_GATE) is True
