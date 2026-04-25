from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.state      import State, Term
from engine.sutra_type import SutraType
from phonology         import mk
from phonology.agama_placement_1_1_46 import kit_agama_placement, tit_agama_placement
from sutras.adhyaya_1.pada_1.sutra_1_1_46 import (
    GATE_KEY,
    adyantau_takitau_paribhasha_set,
)


def test_registry_and_type():
    r = SUTRA_REGISTRY["1.1.46"]
    assert r.sutra_id == "1.1.46"
    assert r.sutra_type is SutraType.PARIBHASHA


def test_gate_once_and_helpers():
    t = Term(kind="prakriti", varnas=[mk("a")], tags={"anga"})
    s0 = State(terms=[t])
    assert not adyantau_takitau_paribhasha_set(s0)
    s1 = apply_rule("1.1.46", s0)
    assert adyantau_takitau_paribhasha_set(s1)
    g = s1.paribhasha_gates[GATE_KEY]
    assert g.get("tit_before_agamin") is True
    assert g.get("kit_after_agamin") is True
    s2 = apply_rule("1.1.46", s1)
    assert s2.paribhasha_gates == s1.paribhasha_gates


def test_phonology_constants():
    assert tit_agama_placement() == "before_agamin"
    assert kit_agama_placement() == "after_agamin"
