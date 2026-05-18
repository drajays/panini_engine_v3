"""
5.4.86  तत्पुरुषस्याङ्गुलेः संख्याऽव्ययादेः  —  VIDHI

Padaccheda: तत्पुरुषस्य अङ्‍गुलेः सङ्‍ख्या-अव्यय-आदेः

तत्पुरुषस्याङ्गुलेः संख्याऽव्ययादेः (5.4.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_86_tatpuruzas_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_86_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatpuruzasyANguleH saMKyA'vyayAdeH",
    text_dev              = "तत्पुरुषस्याङ्गुलेः संख्याऽव्ययादेः",
    padaccheda_dev        = "तत्पुरुषस्य अङ्‍गुलेः सङ्‍ख्या-अव्यय-आदेः",
    why_dev               = "(सूत्रम् 5.4.86) तत्पुरुषस्याङ्गुलेः संख्याऽव्ययादेः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
