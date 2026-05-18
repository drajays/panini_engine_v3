"""
5.3.34  उत्तराधरदक्षिणादातिः  —  VIDHI

Padaccheda: उत्तर-अधर-दक्षिणात् आतिः

उत्तराधरदक्षिणादातिः (5.3.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_34_uttarADara_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttarADaradakziRAdAtiH",
    text_dev              = "उत्तराधरदक्षिणादातिः",
    padaccheda_dev        = "उत्तर-अधर-दक्षिणात् आतिः",
    why_dev               = "(सूत्रम् 5.3.34) उत्तराधरदक्षिणादातिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
