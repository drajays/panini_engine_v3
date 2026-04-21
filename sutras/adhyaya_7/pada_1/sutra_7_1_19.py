"""
7.1.19  नपुंसकाच्च  —  VIDHI

Operational role (v3.6, napuṃsaka a-stems):
  For a **napuṃsaka** aṅga, the dual pratyaya **au / auṭ** (SLP1: O / Ow)
  is replaced by **SI** (śī), i.e. varṇas [S, I].

After it-lopa removes S, the boundary a + I resolves by 6.1.87 to 'e'
giving forms like **ज्ञाने**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_TARGETS = frozenset({"O", "Ow"})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags or "napuṃsaka" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") not in _TARGETS:
        return False
    if pr.meta.get("au_to_SI_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("S"), mk("I")]
    pr.meta["au_to_SI_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", pr.meta.get("upadesha_slp1"))
    pr.meta["upadesha_slp1"] = "SI"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.19",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "napuMsakAt ca (O SI)",
    text_dev       = "नपुंसकाच्च",
    padaccheda_dev = "नपुंसकात् च",
    why_dev        = "नपुंसक-अङ्गात् परस्य औ/औट्-प्रत्ययस्य ‘शी’-आदेशः (ज्ञाने)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

