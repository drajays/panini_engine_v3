"""
3.4.113 *tiṅ-śit* *sārvadhātukam* — *sārvadhātuka* *sañjñā* for *tiṅ* and *śit* after *dhātu*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from phonology.varna   import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import (
    SARVADHATUKA_INVENTORY_N,
    is_sarvadhatuka_upadesha_slp1,
)
from sutras.adhyaya_3.pada_4.sutra_3_4_113 import SARVADHATUKA_113


def _dhatu() -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("B"), mk("A"), mk("l")],
        tags={"dhatu"},
        meta={},
    )


def _pratyaya_tip() -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("tip"),
        tags={"pratyaya"},
        meta={"upadesha_slp1": "tip"},
    )


def _pratyaya_tfc() -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("tfc"),
        tags={"pratyaya", "krt"},
        meta={"upadesha_slp1": "tfc"},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["3.4.113"]
    assert r.sutra_id == "3.4.113"
    assert r.sutra_type is SutraType.SAMJNA
    assert "3.1.91" in r.anuvritti_from
    assert SARVADHATUKA_INVENTORY_N >= 32


def test_tip_sarvadhatuka() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_tip()], meta={})
    s1 = apply_rule("3.4.113", s0)
    assert SARVADHATUKA_113 in s1.terms[1].tags
    assert s1.samjna_registry.get("3.4.113_sarvadhatuka_slp1") is not None


def test_tfc_not_in_inventory() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_tfc()], meta={})
    s1 = apply_rule("3.4.113", s0)
    assert SARVADHATUKA_113 not in s1.terms[1].tags
    # registry still set on act if we had a hit — here cond false, act not run; registry empty
    assert s1.samjna_registry.get("3.4.113_sarvadhatuka_slp1") is None


def test_sap_sarvadhatuka() -> None:
    t = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sap"),
        tags={"pratyaya"},
        meta={"upadesha_slp1": "Sap"},
    )
    assert is_sarvadhatuka_upadesha_slp1("Sap")
    s0 = State(terms=[_dhatu(), t], meta={})
    s1 = apply_rule("3.4.113", s0)
    assert SARVADHATUKA_113 in s1.terms[1].tags


def test_idempotent() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_tip()], meta={})
    s1 = apply_rule("3.4.113", s0)
    s2 = apply_rule("3.4.113", s1)
    assert s1.flat_slp1() == s2.flat_slp1()
