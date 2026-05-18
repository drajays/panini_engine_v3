"""
5.4.60  समयाच्च यापनायाम्  —  VIDHI

Padaccheda: समयात् च यापनायाम्

समयाच्च यापनायाम् (5.4.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_60_samayAcca_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samayAcca yApanAyAm",
    text_dev              = "समयाच्च यापनायाम्",
    padaccheda_dev        = "समयात् च यापनायाम्",
    why_dev               = "(सूत्रम् 5.4.60) समयाच्च यापनायाम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
