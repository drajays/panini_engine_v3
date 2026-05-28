"""
2.4.83  नाव्ययीभावादतोऽम्त्वपञ्चम्याः  —  VIDHI

Padaccheda: न अव्ययीभावात् अतः अम् तु अ-पञ्चम्याः

NOT avyayibhava from a, but am (not pancami) is retained.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_83_navyayibhava_atam"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_83_lup_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["lup_kind"]             = "2.4.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAvyayIBAvAdato'mtvapaYcamyAH",
    text_dev              = "नाव्ययीभावादतोऽम्त्वपञ्चम्याः",
    padaccheda_dev        = "न अव्ययीभावात् अतः अम् तु अ-पञ्चम्याः",
    why_dev               = "न अव्ययीभावात् अतः अम् तु अ-पञ्चम्याः (२.४.८३)।",
    anuvritti_from        = ('2.4.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
