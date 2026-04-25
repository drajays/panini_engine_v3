"""
1.4.100 *l̥ taṅānāv ātmanepadam* — *ātmanepada* *sañjñā*; *bādhana* of *parasmaipada* on same *Term*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology.varna   import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_4.atmanepada_1_4_100 import is_atmanepada_upadesha_slp1


def _pratyaya(slp1: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp1),
        tags={"pratyaya"},
        meta={"upadesha_slp1": slp1},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.100"]
    assert r.sutra_id == "1.4.100"
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.1" in r.anuvritti_from
    assert "1.4.99" in r.anuvritti_from


def test_atmanepada_on_ta() -> None:
    s0 = State(terms=[_pratyaya("ta")], meta={})
    s1 = apply_rule("1.4.100", s0)
    assert "atmanepada" in s1.terms[0].tags
    assert s1.samjna_registry.get("1.4.100_atmanepada_adesha_slp1") is not None


def test_not_on_tip() -> None:
    s0 = State(terms=[_pratyaya("tip")], meta={})
    s1 = apply_rule("1.4.100", s0)
    assert "atmanepada" not in s1.terms[0].tags
    assert s1.samjna_registry.get("1.4.100_atmanepada_adesha_slp1") is None


def test_cond_false_trace_has_skip_detail() -> None:
    s0 = State(terms=[_pratyaya("tip")], meta={})
    s1 = apply_rule("1.4.100", s0)
    e = s1.trace[-1]
    assert e.get("sutra_id") == "1.4.100"
    assert e.get("skip_reason") == "COND-FALSE"
    assert e.get("skip_detail")
    assert "तिप्" in e.get("skip_detail", "")
    assert SUTRA_REGISTRY["1.4.100"].skip_detail_cond_false


def test_badhana_removes_parasmaipada() -> None:
    t = _pratyaya("Ja")
    t.tags.add("parasmaipada")
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.4.100", s0)
    assert "atmanepada" in s1.terms[0].tags
    assert "parasmaipada" not in s1.terms[0].tags


def test_SAnac_kAnac() -> None:
    assert is_atmanepada_upadesha_slp1("SAnac") is True
    assert is_atmanepada_upadesha_slp1("kAnac") is True


def test_idempotent() -> None:
    s0 = State(terms=[_pratyaya("mahiG")], meta={})
    s1 = apply_rule("1.4.100", s0)
    s2 = apply_rule("1.4.100", s1)
    assert "atmanepada" in s2.terms[0].tags
