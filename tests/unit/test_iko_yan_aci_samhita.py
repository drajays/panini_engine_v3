"""
6.1.77 इको यणचि — pedagogical saṃhitā pipelines (no recipe arms).
"""
from __future__ import annotations

import pytest

from engine import apply_rule
from pipelines.iko_yan_aci_samhita import (
    derive_DhenU_ime_pragRhya,
    derive_F_asya,
    derive_dadhi_atra,
    derive_l_AkRtiH,
    derive_madhu_iti,
    derive_nadI_Urdhvam,
    derive_nadI_iyam_savarNa_dirgha,
    derive_pitf_icCA,
    derive_vadhU_AdesaH,
)


def _statuses(trace, sutra_id: str) -> list[str]:
    return [e.get("status") for e in trace if e.get("sutra_id") == sutra_id]


@pytest.mark.parametrize(
    "derive_fn, gold_slp1",
    [
        (derive_dadhi_atra, "dadhyatra"),
        (derive_nadI_Urdhvam, "nadyUrdhvam"),
        (derive_madhu_iti, "madhviti"),
        (derive_vadhU_AdesaH, "vadhvAdesaH"),
        (derive_pitf_icCA, "pitricCA"),
        (derive_F_asya, "rasya"),
        (derive_l_AkRtiH, "lAkRtiH"),
    ],
)
def test_iko_yan_aci_uttsarga(derive_fn, gold_slp1: str) -> None:
    s = derive_fn()
    assert s.flat_slp1() == gold_slp1
    assert "APPLIED" in _statuses(s.trace, "6.1.77")


def test_nadI_iyam_savarNa_dirgha_not_yan() -> None:
    s = derive_nadI_iyam_savarNa_dirgha()
    assert s.flat_slp1() == "nadIyam"
    assert "APPLIED" in _statuses(s.trace, "6.1.101")
    assert "APPLIED" not in _statuses(s.trace, "6.1.77")


def test_DhenU_ime_pragRhya_no_sandhi() -> None:
    s = derive_DhenU_ime_pragRhya()
    assert s.flat_slp1() == "DhenUime"
    assert s.terms[0].varnas[-1].slp1 == "U"
    assert s.samjna_registry.get("6.1.125_prakRti_aci") == 1
    assert "APPLIED" not in _statuses(s.trace, "6.1.77")
    assert "APPLIED" not in _statuses(s.trace, "6.1.101")


def test_6_1_77_fires_on_ik_before_ac_even_savarNa() -> None:
    """Per Constitution Art. 14: 6.1.77 cond checks IK‖AC only — no apavāda
    self-check. When 6.1.77 is applied alone (no 6.1.101 in the loop), it
    fires: I+i → y+i. The savarṇa-dīrgha result (nadIyam) is produced only
    by P00_samhita_iko_yanaci_spine where 6.1.101 runs first."""
    import sutras  # noqa: F401
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    s = State(
        terms=[
            Term(kind="prakriti", varnas=parse_slp1_upadesha_sequence("nadI"), tags=set(), meta={}),
            Term(kind="prakriti", varnas=parse_slp1_upadesha_sequence("iyam"), tags=set(), meta={}),
        ],
        meta={},
        trace=[],
    )
    s = apply_rule("6.1.77", s)
    assert s.flat_slp1() == "nadyiyam"
