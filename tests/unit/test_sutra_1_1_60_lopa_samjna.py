"""1.1.60 स्थाने अदर्शनं लोपः — *lopa* saṃjñā; links to 1.3.9 *vidhi* (doc)."""
from __future__ import annotations

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State

import sutras  # noqa: F401

from sutras.adhyaya_1.pada_1.lopa_samjna_1_1_60 import LOPA_REGISTER_VALUE, lopa_samjna_is_registered


def test_registry() -> None:
    r = SUTRA_REGISTRY["1.1.60"]
    assert r.sutra_id == "1.1.60"
    assert r.text_slp1 == "sTAne adarSanam lopaH"
    assert "1.1.50" in r.anuvritti_from


def test_samjna_idempotent() -> None:
    s0 = State(terms=[])
    s1 = apply_rule("1.1.60", s0)
    assert lopa_samjna_is_registered(s1)
    assert s1.samjna_registry.get("lopa") == LOPA_REGISTER_VALUE
    s2 = apply_rule("1.1.60", s1)
    assert s2 is not None
    # Second apply: cond false → skip (no double registry requirement)
    assert s2.samjna_registry.get("lopa") == LOPA_REGISTER_VALUE
