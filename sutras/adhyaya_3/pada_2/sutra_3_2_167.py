"""
3.2.167  नमिकम्पिस्म्यजसकमहिंसदीपो रः  —  VIDHI

Padaccheda: नमि-कम्पि-स्मि-अजस-कम-हिंस-दीपः रः

krt-suffix rule: नमिकम्पिस्म्यजसकमहिंसदीपो रः (167)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_167_namikampis_167"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_167_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "namikampismyajasakamahiMsadIpo raH",
    text_dev              = "नमिकम्पिस्म्यजसकमहिंसदीपो रः",
    padaccheda_dev        = "नमि-कम्पि-स्मि-अजस-कम-हिंस-दीपः रः",
    why_dev               = "धातोः कृत्-प्रत्ययः [नमिकम्पिस्म्यजसकमहिंसदीपो रः] विहितः (३.२.167)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
