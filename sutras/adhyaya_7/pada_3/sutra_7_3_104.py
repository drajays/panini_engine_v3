"""
7.3.104  ओसि च  —  VIDHI

अङ्गस्य अतः (7.3.101) … एत् (7.3.103): the final अ of an a-ending aṅga becomes
ए before the sup ``os`` (rAma + os → rAme + os; 6.1.78 then gives rAmayos →
rAmayoH).  Replaces the old 6.1.78 'insert y' hack.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "sup" not in pr.tags:
        return None
    if pr.meta.get("upadesha_slp1") != "os" or anga.meta.get("aNga_e_done"):
        return None
    if not anga.varnas or anga.varnas[-1].slp1 != "a":
        return None
    return len(state.terms) - 2, len(anga.varnas) - 1


def cond(state: State) -> bool:
    return adhikara_in_effect("7.3.104", state, "6.4.1") and _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("e")
    state.terms[ti].meta["aNga_e_done"] = True
    state.terms[ti].meta["aNga_dirgha_done"] = True
    state.meta["__why_now_dev__"] = (
        "ओस्-प्रत्यये परे अदन्त-अङ्गस्य अन्त्य-अकारस्य 'ए'-आदेशः; "
        "यथा राम+ओस् → रामे+ओस् (→ रामयोः)। (७.३.१०४)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.104",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "osi ca",
    text_dev       = "ओसि च",
    padaccheda_dev = "ओसि च",
    why_dev        = "ओस्-प्रत्यये परे अदन्त-अङ्गस्य अन्त्य-अकारस्य 'ए'-आदेशः।",
    anuvritti_from = ("7.1.1", "7.3.101", "7.3.103"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
