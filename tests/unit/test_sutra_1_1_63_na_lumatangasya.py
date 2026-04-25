"""1.1.63 लुमता प्रत्ययलोपे अङ्गस्य प्रत्ययलक्षणं न — *apavāda* to 1.1.62 (gate)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State

from sutras.adhyaya_1.pada_1.na_lumatangasya_1_1_63 import (
    NA_LUMATANGASYA_GATE,
    na_lumatangasya_paribhasha_is_active,
)


def test_registry() -> None:
    r = SUTRA_REGISTRY["1.1.63"]
    assert r.sutra_type.name == "PARIBHASHA"
    assert r.sutra_id == "1.1.63"
    assert r.text_slp1 == "lumatA pratyayalope aNgasya pratyayalakzaRaM na"
    assert r.text_dev == "लुमता प्रत्ययलोपे अङ्गस्य प्रत्ययलक्षणं न"
    assert "अव्ययम्" in r.padaccheda_dev
    assert r.anuvritti_from == ("1.1.62",)


def test_requires_1_1_62_before_firing() -> None:
    s0 = State(terms=[])
    s1 = apply_rule("1.1.63", s0)
    assert not na_lumatangasya_paribhasha_is_active(s1)


def test_paribhasha_gate_after_62_then_idempotent() -> None:
    s0 = State(terms=[])
    s1 = apply_rule("1.1.62", s0)
    s2 = apply_rule("1.1.63", s1)
    assert na_lumatangasya_paribhasha_is_active(s2)
    assert s2.paribhasha_gates.get(NA_LUMATANGASYA_GATE) is True
    s3 = apply_rule("1.1.63", s2)
    assert na_lumatangasya_paribhasha_is_active(s3)
