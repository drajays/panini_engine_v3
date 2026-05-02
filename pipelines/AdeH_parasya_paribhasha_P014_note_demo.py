"""
pipelines/AdeH_parasya_paribhasha_P014_note_demo.py — **P014** paribhāṣā note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P014.json``.

This JSON is an illustration note for:
  - **1.1.54** *ādeḥ parasya* (gate: substitution applies to the following element)
and cites **1.3.12** as a common cross-reference in discussion.

No derivation is reconstructible from this JSON alone, so this demo only applies
the relevant paribhāṣā(s) and asserts their gates are installed.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_AdeH_parasya_paribhasha_P014_note() -> State:
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P014_AdeH_parasya_note"},
        meta={"upadesha_slp1": "a"},
    )
    s = State(terms=[t], meta={}, trace=[])
    s.meta["prakriya_P014_paribhasha_note_only"] = True

    s = apply_rule("1.1.54", s)

    # Cross-reference demo gate (does not depend on 1.1.54, but is cited in JSON).
    s.meta["1_3_12_arm"] = True
    s.meta["1_3_12_target_upadesha_slp1"] = "__none__"
    s = apply_rule("1.3.12", s)
    return s


__all__ = ["derive_AdeH_parasya_paribhasha_P014_note"]

