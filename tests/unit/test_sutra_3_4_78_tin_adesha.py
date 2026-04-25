"""
3.4.78 *lasaḥ* *tiptas*… — *lakāra* is replaced by the chosen *tiṅ* *ādeśa*.

Recipe supplies ``state.meta['tin_adesha_slp1']`` and ``tin_adesha_pending``; sūtra does not
read *puruṣa* / *vacana* (CONSTITUTION Art. 2).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from phonology.varna   import parse_slp1_upadesha_sequence


def _dhatu_bhU() -> Term:
    b = mk("B")
    U = mk("U")
    return Term(
        kind="prakriti",
        varnas=[b, U],
        tags={"dhatu"},
        meta={},
    )


def _lakaara_pratyaya() -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya"},
        meta={"upadesha_slp1": "laT"},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["3.4.78"]
    assert r.sutra_id == "3.4.78"
    assert r.sutra_type is SutraType.VIDHI
    assert "3.4.77" in r.anuvritti_from
    assert "3.1.1" in r.anuvritti_from


def test_3_4_78_replaces_lakaara_with_tin_adesha() -> None:
    s0 = State(terms=[_dhatu_bhU(), _lakaara_pratyaya()], meta={})
    s1 = apply_rule("3.4.77", s0)
    s1.meta["tin_adesha_slp1"] = "tip"
    s1.meta["tin_adesha_pending"] = True
    s2 = apply_rule("3.4.78", s1)

    pr = s2.terms[1]
    assert pr.meta.get("upadesha_slp1") == "tip"
    assert "tip" in s2.flat_slp1()
    assert s2.meta.get("tin_adesha_pending") is not True
    assert "tin_adesha_3_4_78" in pr.tags


def test_3_4_78_not_without_adhikara_3_4_77() -> None:
    s0 = State(terms=[_dhatu_bhU(), _lakaara_pratyaya()], meta={})
    s0.meta["tin_adesha_slp1"] = "tip"
    s0.meta["tin_adesha_pending"] = True
    s1 = apply_rule("3.4.78", s0)
    assert s1.terms[1].meta.get("upadesha_slp1") == "laT"


def test_3_4_78_not_without_tin_adesha_pending() -> None:
    s0 = State(terms=[_dhatu_bhU(), _lakaara_pratyaya()], meta={})
    s0 = apply_rule("3.4.77", s0)
    s0.meta["tin_adesha_slp1"] = "tip"
    # tin_adesha_pending missing → no-op
    s1 = apply_rule("3.4.78", s0)
    assert s1.terms[1].meta.get("upadesha_slp1") == "laT"
