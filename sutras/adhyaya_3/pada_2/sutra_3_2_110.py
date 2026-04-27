"""
3.2.110  अद्यतने लुङ्  —  VIDHI (narrow: lakāra placeholder attach)

Engine scope (v3 glass-box): attach the lakāra upadeśa placeholder ``luG`` when
the recipe sets ``state.meta['lakara'] == 'luG'`` (lūṅ).  Actual tiṅ substitution
is performed by **3.4.77** + **3.4.78** using ``state.meta['tin_adesha_*']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    # Glass-box arming: pipelines must opt-in (CONSTITUTION: cond() may not read paradigm selectors).
    if not state.meta.get("3_2_110_luG_arm", False):
        return False
    # Only once.
    return not any(
        t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "luG"
        for t in state.terms
    )


def act(state: State) -> State:
    t = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("luG"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "luG"},
    )
    state.terms.append(t)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.110",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "adyatane luG",
    text_dev       = "अद्यतने लुङ्",
    padaccheda_dev = "अद्यतने / लुङ्",
    why_dev        = "अद्यतन-भूते लुङ्-लकार-स्थापनम् (इह 'luG' प्लेसहोल्डर्) ।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

