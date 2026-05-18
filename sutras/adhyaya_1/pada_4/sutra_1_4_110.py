"""
1.4.110  विरामोऽवसानम्  —  SAMJNA

*Virāma* (pause / end of utterance) is called *avasāna* — one of the
conditions for **8.3.15** visarga at word-final *r*.

Engine: fires once the form has been merged into a *pada* Term (post sandhi,
post pada-merge) and before entering the Tripāḍī zone (**8.2.1**).
Registers ``samjna_registry['1.4.110_avasana']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.samjna_registry.get("1.4.110_avasana") is not None:
        return False
    return any("pada" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.samjna_registry["1.4.110_avasana"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.110",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "virAmo avasAnam",
    text_dev       = "विरामोऽवसानम्",
    padaccheda_dev = "विरामः अवसानम्",
    why_dev        = "विरामः अवसान-संज्ञकः — खर्-अवसानयोः विसर्जनीये प्रसङ्गः।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
