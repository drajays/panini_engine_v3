"""
3.1.68 *sārvadhātake kartari dhātoḥ śap* — *vikaraṇa* *śap* before *tiṅ* / *kṛt-śit*, not before *śyan*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import AC_DEV, HAL_DEV


def _varnas_from_slp1(slp1: str) -> list:
    out: list = []
    for ch in slp1:
        if ch in HAL_DEV or ch in AC_DEV or ch in "fF":
            out.append(mk(ch))
    return out


def _dhatu(slp1: str = "paT") -> Term:
    return Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(slp1),
        tags={"dhatu"},
        meta={"karmakatva": "sakarmaka"},
    )


def _pratyaya_upa(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=[],
        tags={"pratyaya"},
        meta={"upadesha_slp1": up},
    )


def _prep(s: State) -> State:
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.4.69", s)
    return s


def test_registry() -> None:
    r = SUTRA_REGISTRY["3.1.68"]
    assert r.sutra_id == "3.1.68"


def test_inserts_sap_before_tip() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_upa("tip")])
    s1 = _prep(s0)
    n0 = len(s1.terms)
    fb = s1.flat_slp1()
    s2 = apply_rule("3.1.68", s1)
    assert len(s2.terms) == n0 + 1
    assert s2.terms[1].meta.get("upadesha_slp1") == "Sap"
    assert "3_1_68_sap" in s2.terms[1].tags
    assert "upadesha" in s2.terms[1].tags
    assert s2.flat_slp1() != fb


def test_inserts_sap_before_satf() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_upa("Satf")])
    s1 = _prep(s0)
    s2 = apply_rule("3.1.68", s1)
    assert s2.terms[1].meta.get("upadesha_slp1") == "Sap"


def test_no_sap_before_syan_apavada() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_upa("Syan")])
    s1 = _prep(s0)
    n = len(s1.terms)
    s2 = apply_rule("3.1.68", s1)
    assert len(s2.terms) == n


def test_skipped_without_adhikara() -> None:
    s0 = State(terms=[_dhatu(), _pratyaya_upa("tip")])
    s0.paribhasha_gates["prayoga_3_4_69_licenses_kartari"] = True
    s1 = apply_rule("3.1.68", s0)
    assert len(s1.terms) == 2


def test_recipe_kartari_without_3_4_69() -> None:
    s0 = State(
        terms=[_dhatu(), _pratyaya_upa("tip")],
        meta={"3_1_68_kartari_recipe": True},
    )
    s1 = apply_rule("3.1.91", s0)
    s2 = apply_rule("3.1.68", s1)
    assert s2.terms[1].meta.get("upadesha_slp1") == "Sap"
