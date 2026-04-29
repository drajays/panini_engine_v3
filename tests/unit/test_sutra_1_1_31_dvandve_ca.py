"""
**1.1.31** *dvandve ca* — revoke **1.1.27** *sarvanāma* inside *dvandva* samāsa.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_31 import TAG_DVANDVA_SAMASA


def test_1_1_31_strips_sarvanama_in_dvandva() -> None:
    # Choose a known sarvādi item (pUrva) to trigger **1.1.27**.
    anga = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pUrva")),
        tags={"anga", "prātipadika", TAG_DVANDVA_SAMASA},
        meta={"upadesha_slp1": "pUrva"},
    )
    s0 = State(terms=[anga])

    s1 = apply_rule("1.1.27", s0)
    assert "sarvanama" in s1.terms[0].tags

    s2 = apply_rule("1.1.31", s1)
    assert "sarvanama" not in s2.terms[0].tags


def test_1_1_31_blocks_7_1_52_sut_on_Am() -> None:
    # Same aṅga as above, but now put it before Am to test **7.1.52** gating.
    anga = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pUrva")),
        tags={"anga", "prātipadika", TAG_DVANDVA_SAMASA},
        meta={"upadesha_slp1": "pUrva"},
    )
    am = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Am")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "Am"},
    )
    s0 = State(terms=[anga, am])

    s1 = apply_rule("1.1.27", s0)
    assert "sarvanama" in s1.terms[0].tags

    s2 = apply_rule("1.1.31", s1)
    assert "sarvanama" not in s2.terms[0].tags

    s3 = apply_rule("7.1.52", s2)
    assert s3.terms[-1].meta.get("sut_agama_done") is not True
    assert s3.terms[-1].meta.get("upadesha_slp1") == "Am"

