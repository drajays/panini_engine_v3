"""
2.4.51  णौ च सँश्चङोः  —  VIDHI

Padaccheda: णौ च सन्-चङोः

Also in nic with san and can.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_51_nau_san_cana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.51", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "RO ca sa~ScaNoH",
    text_dev              = "णौ च सँश्चङोः",
    padaccheda_dev        = "णौ च सन्-चङोः",
    why_dev               = "णौ च सन्-चङोः (२.४.५१)।",
    anuvritti_from        = ('2.4.49',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
