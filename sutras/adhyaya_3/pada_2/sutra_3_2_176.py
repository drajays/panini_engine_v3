"""
3.2.176  रदादिभ्यो वरच्  —  VIDHI (narrow: P029 *yāyāvara*)

Teaching JSON **P029** step 9: after the *yaṅ* *abhyāsa* frame, attach the *kṛt*
*varac* (surface *vara*) to form the agent noun of the intensive.

Narrow v3: ``state.meta['P029_3_2_176_varac_arm']`` appends an upadeśa Term
``varac`` tagged ``krt`` / ``pratyaya`` / ``upadesha`` for the **1.3** *it* chain.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("P029_3_2_176_varac_arm"):
        return False
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "varac" for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    varac = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("varac")),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": "varac"},
    )
    state.terms.append(varac)
    state.meta.pop("P029_3_2_176_varac_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.176",
    sutra_type=SutraType.VIDHI,
    text_slp1="rad-Adibhyo varac",
    text_dev="रदादिभ्यो वरच्",
    padaccheda_dev="रदादिभ्यः / वरच्",
    why_dev="इत्यादेभ्यो वरच् — प०२९ (*यायावर*)।",
    anuvritti_from=("3.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
