"""
5.3.80  प्राचामुपादेरडज्वुचौ च  —  VIDHI

Padaccheda: प्राचाम् उप-आदेः अडच्-वुचौ च

प्राचामुपादेरडज्वुचौ च (5.3.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_80_prAcAmupAd_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAcAmupAderaqajvucO ca",
    text_dev              = "प्राचामुपादेरडज्वुचौ च",
    padaccheda_dev        = "प्राचाम् उप-आदेः अडच्-वुचौ च",
    why_dev               = "(सूत्रम् 5.3.80) प्राचामुपादेरडज्वुचौ च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
