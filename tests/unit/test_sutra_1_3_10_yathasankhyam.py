"""1.3.10 समानामनुदेशः यथासङ्ख्यम् — *yathāsaṅkhyam* paribhāṣā (gate)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State

from sutras.adhyaya_1.pada_3.yathasankhyam_1_3_10 import (
    YATHASANKHYAM_GATE,
    yathasankhyam_paribhasha_is_active,
)


def test_registry() -> None:
    r = SUTRA_REGISTRY["1.3.10"]
    assert r.sutra_type.name == "PARIBHASHA"
    assert r.sutra_id == "1.3.10"
    assert r.text_slp1 == "samAnAm anudeSaH yathAsaNKyam"
    assert r.text_dev == "समानामनुदेशः यथासङ्ख्यम्"
    assert "यथासङ्ख्यम्" in r.padaccheda_dev
    assert r.anuvritti_from == ()


def test_gate_idempotent() -> None:
    s0 = State(terms=[])
    s1 = apply_rule("1.3.10", s0)
    assert yathasankhyam_paribhasha_is_active(s1)
    assert s1.paribhasha_gates.get(YATHASANKHYAM_GATE) is True
    s2 = apply_rule("1.3.10", s1)
    assert yathasankhyam_paribhasha_is_active(s2)
