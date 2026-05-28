"""
2.4.25  विभाषा सेनासुराछायाशालानिशानाम्  —  VIDHI

Padaccheda: विभाषा सेना-सुरा-छाया-शाला-निशानाम्

Optional for sena, sura, chaya, shala, nisha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_25_sena_sura_vibhasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.25", state, "2.4.19")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA senAsurACAyASAlAniSAnAm",
    text_dev              = "विभाषा सेनासुराछायाशालानिशानाम्",
    padaccheda_dev        = "विभाषा सेना-सुरा-छाया-शाला-निशानाम्",
    why_dev               = "सेना-सुरा-छाया-शाला-निशानाम् विभाषा (२.४.२५)।",
    anuvritti_from        = ('2.4.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
