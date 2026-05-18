"""
5.1.72  पारायणतुरायणचान्द्रायणं वर्तयति  —  VIDHI

Padaccheda: पारायण-तुरायण-चान्द्रायणम् वर्तयति (क्रियापदम्)

पारायणतुरायणचान्द्रायणं वर्तयति (5.1.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_72_pArAyaRatu_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_72_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pArAyaRaturAyaRacAndrAyaRaM vartayati",
    text_dev              = "पारायणतुरायणचान्द्रायणं वर्तयति",
    padaccheda_dev        = "पारायण-तुरायण-चान्द्रायणम् वर्तयति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.1.72) पारायणतुरायणचान्द्रायणं वर्तयति।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
