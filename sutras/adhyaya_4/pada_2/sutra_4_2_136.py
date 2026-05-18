"""
4.2.136  गोयवाग्वोश्च  —  VIDHI

Padaccheda: गो-यवाग्वोः च

गोयवाग्वोश्च (4.2.136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_136_goyavAgvoS_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_136_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "goyavAgvoSca",
    text_dev              = "गोयवाग्वोश्च",
    padaccheda_dev        = "गो-यवाग्वोः च",
    why_dev               = "(सूत्रम् 4.2.136) गोयवाग्वोश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
