"""
5.3.35  एनबन्यतरस्यामदूरेऽपञ्चम्याः  —  VIDHI

Padaccheda: एनप् अन्यतरस्याम् अदूरे अ-पञ्चम्याः

एनबन्यतरस्यामदूरेऽपञ्चम्याः (5.3.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_35_enabanyata_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "enabanyatarasyAmadUre'paYcamyAH",
    text_dev              = "एनबन्यतरस्यामदूरेऽपञ्चम्याः",
    padaccheda_dev        = "एनप् अन्यतरस्याम् अदूरे अ-पञ्चम्याः",
    why_dev               = "(सूत्रम् 5.3.35) एनबन्यतरस्यामदूरेऽपञ्चम्याः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
