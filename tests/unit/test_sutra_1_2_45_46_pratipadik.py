"""
State-machine tests for:
  - 1.2.45 arthavadadhāturapratyayaḥ prātipadikam
  - 1.2.46 kṛt-taddhita-samāsāś ca

These tests are **lexicon-backed** (dhātupāṭha + pratyaya inventories) and
avoid manual prātipadika tagging.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _last_step_for(s: State, sutra_id: str):
    hit = [e for e in s.trace if e.get("sutra_id") == sutra_id]
    assert hit, f"missing trace row for {sutra_id}"
    return hit[-1]


def test_1_2_45_salA_becomes_pratipadika():
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("SAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    s0 = State(terms=[t])
    s1 = apply_rule("1.2.45", s0)
    assert "prātipadika" in s1.terms[0].tags
    st = _last_step_for(s1, "1.2.45")
    assert st.get("status") == "APPLIED"


def test_1_2_45_bu_is_dhatu_cond_false():
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("BU"),
        tags={"anga"},
        meta={"upadesha_slp1": "BU"},
    )
    s0 = State(terms=[t])
    s1 = apply_rule("1.2.45", s0)
    assert "prātipadika" not in s1.terms[0].tags
    st = _last_step_for(s1, "1.2.45")
    assert st.get("status") == "SKIPPED"


def test_taddhita_community_1_2_45_skipped_1_2_46_applies():
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("SAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ca"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "Ca"},
    )
    s0 = State(terms=[stem, pr])

    s1 = apply_rule("1.2.45", s0)
    assert "prātipadika" not in s1.terms[0].tags
    st45 = _last_step_for(s1, "1.2.45")
    assert st45.get("status") == "SKIPPED"

    s2 = apply_rule("1.2.46", s1)
    assert len(s2.terms) == 2
    assert s2.samjna_registry.get("1.2.46_anga_taddhita_two_term") is True
    assert "prātipadika" in s2.terms[0].tags
    st46 = _last_step_for(s2, "1.2.46")
    assert st46.get("status") == "APPLIED"

