"""3.1.73 *svādibhyaḥ śnuḥ* — *Sap* → *śnu* when recipe-armed."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from phonology.varna import mk, parse_slp1_upadesha_sequence


def test_metadata():
    r = SUTRA_REGISTRY["3.1.73"]
    assert r.sutra_id == "3.1.73"


def test_replace_sap_when_armed():
    sap = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sap"),
        tags={"pratyaya", "vikarana", "upadesha"},
        meta={"upadesha_slp1": "Sap"},
    )
    s0 = State(
        terms=[
            Term(
                kind="prakriti",
                varnas=[mk("c"), mk("i")],
                tags={"dhatu", "anga"},
                meta={},
            ),
            sap,
        ],
        meta={"3_1_73_snu_arm": True},
    )
    s1 = apply_rule("3.1.73", s0)
    assert len(s1.terms) == 2
    assert (s1.terms[1].meta.get("upadesha_slp1") or "").strip() == "Snu"
    assert "kngiti" in s1.terms[1].tags
