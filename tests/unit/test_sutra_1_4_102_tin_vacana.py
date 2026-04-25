"""
1.4.102 *tāni trīṇi trīṇi …* — *ekavacana* / *dvivacana* / *bahuvacana* on each *tiṅ* triplet.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology.varna   import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_4.tin_vacana_1_4_102 import (
    TIN_102_TAG_BAHU,
    TIN_102_TAG_DVI,
    TIN_102_TAG_EKA,
    terms_needing_tin_102_vacana,
    vacana_102_tag_for_tin_adesha,
)


def _pr(slp1: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp1),
        tags={"pratyaya"},
        meta={"upadesha_slp1": slp1},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.102"]
    assert r.sutra_id == "1.4.102"
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.101" in r.anuvritti_from
    assert "1.4.1" in r.anuvritti_from


def test_map_parasmai_block() -> None:
    assert vacana_102_tag_for_tin_adesha("tip") == TIN_102_TAG_EKA
    assert vacana_102_tag_for_tin_adesha("tas") == TIN_102_TAG_DVI
    assert vacana_102_tag_for_tin_adesha("jhi") == TIN_102_TAG_BAHU


def test_map_atmane_block() -> None:
    assert vacana_102_tag_for_tin_adesha("ta") == TIN_102_TAG_EKA
    assert vacana_102_tag_for_tin_adesha("ATAm") == TIN_102_TAG_DVI
    assert vacana_102_tag_for_tin_adesha("Dvam") == TIN_102_TAG_BAHU


def test_apply_102() -> None:
    s0 = State(terms=[_pr("tip"), _pr("tas")], meta={})
    s1 = apply_rule("1.4.102", s0)
    assert s1.terms[0].tags & {TIN_102_TAG_EKA}
    assert s1.terms[1].tags & {TIN_102_TAG_DVI}
    assert s1.samjna_registry.get("1.4.102_tin_vacana") is not None
    assert terms_needing_tin_102_vacana(s1) == []


def test_iw_tilde() -> None:
    assert vacana_102_tag_for_tin_adesha("iw~") == TIN_102_TAG_EKA
