"""
1.4.22 *dvi-ekayoḥ divivacana-ekavacane* — *dvi* / *eka* *affix* *niyama* *paribhāṣā*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk

from sutras.adhyaya_1.pada_4.dvi_eka_1_4_22 import (
    DVI_EKA_NIMITTA_KEY,
    GATE_KEY,
    dvi_eka_22_licences,
)


def _dhatu() -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("B"), mk("A"), mk("l")],
        tags={"dhatu"},
        meta={"karmakatva": "sakarmaka"},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.22"]
    assert r.sutra_id == "1.4.22"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "1.4.1" in r.anuvritti_from


def test_gate_dvi() -> None:
    t = _dhatu()
    t.meta[DVI_EKA_NIMITTA_KEY] = "dvi"
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.4.22", s0)
    g = s1.paribhasha_gates[GATE_KEY]
    assert g["active"] is True
    assert g["nimitta"] == "dvi"
    assert dvi_eka_22_licences(s1) is True


def test_gate_eka() -> None:
    t = _dhatu()
    t.meta[DVI_EKA_NIMITTA_KEY] = "eka"
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.4.22", s0)
    assert s1.paribhasha_gates[GATE_KEY]["nimitta"] == "eka"
    assert dvi_eka_22_licences(s1) is True


def test_r3_idempotent() -> None:
    t = _dhatu()
    t.meta[DVI_EKA_NIMITTA_KEY] = "dvi"
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.4.22", s0)
    s2 = apply_rule("1.4.22", s1)
    assert s1.paribhasha_gates == s2.paribhasha_gates


def test_no_meta_no_gate() -> None:
    s0 = State(terms=[_dhatu()], meta={})
    s1 = apply_rule("1.4.22", s0)
    assert GATE_KEY not in s1.paribhasha_gates
