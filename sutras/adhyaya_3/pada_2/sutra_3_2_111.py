"""
3.2.111  अनद्यतने लङ्  —  VIDHI (narrow: lakāra placeholder attach)

Engine scope (v3 glass-box): attach the lakāra upadeśa placeholder ``laG`` when
the recipe sets ``state.meta['3_2_111_laG_arm']`` and records ``state.meta['lakara'] == 'laG'``.
Tiṅ substitution is performed by **3.4.77** + **3.4.78** using ``state.meta['tin_adesha_*']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("3_2_111_laG_arm", False):
        return False
    if (state.meta.get("lakara") or "").strip() != "laG":
        return False
    return not any(
        t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "laG"
        for t in state.terms
    )


def act(state: State) -> State:
    t = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laG"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laG"},
    )
    # Match *laṭ*-placeholder demos: peel the final consonant letter of the lakāra
    # name so the tape carries *lac* (here **la**) until **3.4.77** applies.
    if t.varnas and t.varnas[-1].slp1 == "G":
        del t.varnas[-1]
    state.terms.append(t)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.111",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "anadyatane laG",
    text_dev       = "अनद्यतने लङ्",
    padaccheda_dev = "अनद्यतने / लङ्",
    why_dev        = "अनद्यतन-भूते लङ्-लकार-स्थापनम् (इह 'laG' प्लेसहोल्डर्) ।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
