"""
1.4.104 *supas tiṅś ca vibhaktiḥ* — *vibhakti* *sañjñā* on *sup* and *tiṅ* *ādeśa* *pratyaya*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology.varna   import parse_slp1_upadesha_sequence

from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from sutras.adhyaya_1.pada_4.vibhakti_samjna_1_4_104 import (
    TAG_1_4_104_VIBHAKTI,
    is_sup_vibhakti_pratyaya,
    terms_needing_1_4_104_vibhakti,
)
from sutras.adhyaya_3.pada_1.vikarana_sap_3_1_68 import SAP_INSERT_TAG


def _tin(slp1: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp1),
        tags={"pratyaya"},
        meta={"upadesha_slp1": slp1},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(up),
        tags={"pratyaya", "sup"},
        meta={"upadesha_slp1": up},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.104"]
    assert r.sutra_id == "1.4.104"
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.1" in r.anuvritti_from
    assert "1.4.101" in r.anuvritti_from
    assert "1.4.103" in r.anuvritti_from


def test_sup_luk_ghost_not_sup_vibhakti_pratyaya_for_104() -> None:
    ghost = Term(
        kind="pratyaya",
        varnas=[],
        tags={"pratyaya", "sup", LUK_LOPA_GHOST_TAG},
        meta={"upadesha_slp1": "su~"},
    )
    assert is_sup_vibhakti_pratyaya(ghost) is False
    assert terms_needing_1_4_104_vibhakti(State(terms=[ghost])) == []


def test_apply_tags_tip_and_sup() -> None:
    s0 = State(terms=[_tin("tip"), _sup("am")])
    s1 = apply_rule("1.4.104", s0)
    assert TAG_1_4_104_VIBHAKTI in s1.terms[0].tags
    assert TAG_1_4_104_VIBHAKTI in s1.terms[1].tags
    assert s1.samjna_registry.get("1.4.104_sup_vibhakti_triples_slp1") is not None
    assert s1.samjna_registry.get("1.4.104_tin_vibhakti_triples_slp1") is not None
    assert terms_needing_1_4_104_vibhakti(s1) == []


def test_iw_tilde_normalises() -> None:
    s0 = State(terms=[_tin("iw~")])
    s1 = apply_rule("1.4.104", s0)
    assert TAG_1_4_104_VIBHAKTI in s1.terms[0].tags


def test_no_tag_for_sap_vikarana() -> None:
    sap = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sap"),
        tags={"pratyaya", "vikarana", SAP_INSERT_TAG},
        meta={"upadesha_slp1": "Sap"},
    )
    s0 = State(terms=[sap])
    s1 = apply_rule("1.4.104", s0)
    assert TAG_1_4_104_VIBHAKTI not in s1.terms[0].tags


def test_second_pass_r2_registry_still_mutates() -> None:
    s0 = State(terms=[_tin("tip")])
    s1 = apply_rule("1.4.104", s0)
    assert s1.samjna_registry.get("1.4.104_apply_stamp") == 1
    s1.terms.append(_tin("tas"))
    s2 = apply_rule("1.4.104", s1)
    assert s2.samjna_registry.get("1.4.104_apply_stamp") == 2
    assert TAG_1_4_104_VIBHAKTI in s2.terms[-1].tags


def test_no_tag_for_lakara_upadesha() -> None:
    lac = Term(
        kind="pratyaya",
        varnas=[],
        tags={"pratyaya"},
        meta={"upadesha_slp1": "laT"},
    )
    s0 = State(terms=[lac])
    s1 = apply_rule("1.4.104", s0)
    assert TAG_1_4_104_VIBHAKTI not in s1.terms[0].tags
