"""
1.4.101 *tiṅaḥ trīṇi trīṇi prathama-madhyam-uttamāḥ* — *tiṅ* *ādeśa* *tripartite* (A/B/C) tags.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology.varna   import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_4.tin_tripartite_1_4_101 import (
    TIN_101_TAG_TRIPARTITE_A,
    TIN_101_TAG_TRIPARTITE_B,
    TIN_101_TAG_TRIPARTITE_C,
    terms_needing_tin_101_tripartite,
    tripartite_101_tag_for_tin_adesha,
)


def _pr(slp1: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp1),
        tags={"pratyaya"},
        meta={"upadesha_slp1": slp1},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.101"]
    assert r.sutra_id == "1.4.101"
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.1" in r.anuvritti_from


def test_tripartite_map_parasmai() -> None:
    assert tripartite_101_tag_for_tin_adesha("tip") == TIN_101_TAG_TRIPARTITE_A
    assert tripartite_101_tag_for_tin_adesha("sip") == TIN_101_TAG_TRIPARTITE_B
    assert tripartite_101_tag_for_tin_adesha("mip") == TIN_101_TAG_TRIPARTITE_C


def test_tripartite_map_atmane() -> None:
    assert tripartite_101_tag_for_tin_adesha("ta") == TIN_101_TAG_TRIPARTITE_A
    assert tripartite_101_tag_for_tin_adesha("TAs") == TIN_101_TAG_TRIPARTITE_B
    assert tripartite_101_tag_for_tin_adesha("iw") == TIN_101_TAG_TRIPARTITE_C


def test_apply_101() -> None:
    s0 = State(terms=[_pr("tip"), _pr("sip")], meta={})
    s1 = apply_rule("1.4.101", s0)
    assert s1.terms[0].tags & {TIN_101_TAG_TRIPARTITE_A}
    assert s1.terms[1].tags & {TIN_101_TAG_TRIPARTITE_B}
    assert s1.samjna_registry.get("1.4.101_tiN_tripartite_abc") is not None
    assert terms_needing_tin_101_tripartite(s1) == []


def test_iw_tilde() -> None:
    assert tripartite_101_tag_for_tin_adesha("iw~") == TIN_101_TAG_TRIPARTITE_C
