"""
1.4.99 *l̥ parasmaipadam* — *parasmaipada* *sañjñā* on *lakārāpāda* *pratyaya*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology.varna   import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_4.parasmaipada_1_4_99 import (
    is_parasmaipada_upadesha_slp1,
)


def _pratyaya(slp1: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp1),
        tags={"pratyaya"},
        meta={"upadesha_slp1": slp1},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.99"]
    assert r.sutra_id == "1.4.99"
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.1" in r.anuvritti_from


def test_parasmaipada_on_tip() -> None:
    s0 = State(terms=[_pratyaya("tip")], meta={})
    s1 = apply_rule("1.4.99", s0)
    assert "parasmaipada" in s1.terms[0].tags
    assert s1.samjna_registry.get("1.4.99_parasmaipada_adesha_slp1") is not None


def test_not_on_atmanepada_ta() -> None:
    s0 = State(terms=[_pratyaya("ta")], meta={})
    s1 = apply_rule("1.4.99", s0)
    assert "parasmaipada" not in s1.terms[0].tags
    # cond false → no registry write (R2 not triggered if act not run; check registry empty or unchanged)
    assert s1.samjna_registry.get("1.4.99_parasmaipada_adesha_slp1") is None


def test_idempotent() -> None:
    s0 = State(terms=[_pratyaya("tip")], meta={})
    s1 = apply_rule("1.4.99", s0)
    s2 = apply_rule("1.4.99", s1)
    assert s1.flat_slp1() == s2.flat_slp1()
    assert "parasmaipada" in s2.terms[0].tags


def test_kvasu_tilde() -> None:
    assert is_parasmaipada_upadesha_slp1("kvasu~") is True


def test_two_pratyaya_both_tagged() -> None:
    s0 = State(terms=[_pratyaya("tip"), _pratyaya("mas")], meta={})
    s1 = apply_rule("1.4.99", s0)
    assert "parasmaipada" in s1.terms[0].tags
    assert "parasmaipada" in s1.terms[1].tags
