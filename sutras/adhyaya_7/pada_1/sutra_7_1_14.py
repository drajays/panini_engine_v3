"""
7.1.14  सर्वनाम्नः स्मै  —  VIDHI

For adant sarvanāma aṅgas (e.g. sarva), the sup upadeśa **ṅe** (Ne)
is replaced by **smai** (smE in SLP1).

v3 encoding: we replace the pratyaya varṇas with s + m + E and update
its upadeśa identity so that 7.1.13 (ṅe → ya) will not fire.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "sarvanama" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "Ne":
        return False
    if pr.meta.get("smai_done"):
        return False
    # *adanta* only (same anuvṛtti thread as 7.1.13): *ā*-final stems keep **Ne**
    # for **7.3.114** (*sarvanāmnaḥ syāṭ hr̥asvaś ca*).
    if not anga.varnas or anga.varnas[-1].slp1 != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("s"), mk("m"), mk("E")]
    pr.meta["smai_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Ne")
    pr.meta["upadesha_slp1"] = "smE"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.14",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sarvanAmnaH smE",
    text_dev       = "सर्वनाम्नः स्मै",
    padaccheda_dev = "सर्वनाम्नः स्मै",
    why_dev        = "अदन्त-सर्वनाम-अङ्गात् परस्य ङे-प्रत्ययस्य ‘स्मै’ आदेशः।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

