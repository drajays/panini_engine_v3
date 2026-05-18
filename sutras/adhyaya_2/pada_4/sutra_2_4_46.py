"""
2.4.46  णौ गमिरबोधने  —  VIDHI

Padaccheda: णौ गमिः अबोधने

gami in nic (causative) when not in bodhana sense.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_46_nau_gami_abodhane"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "RO gamiraboDane",
    text_dev              = "णौ गमिरबोधने",
    padaccheda_dev        = "णौ गमिः अबोधने",
    why_dev               = "णौ गमिः अबोधने (२.४.४६)।",
    anuvritti_from        = ('2.4.45',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
