"""
2.3.49  एकवचनं संबुद्धिः  —  SAMJNA

Padaccheda: एकवचनम् सम्बुद्धिः

Sambuddhi (vocative) is the singular.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return "2_3_49_sambuddhi" not in state.samjna_registry


def act(state: State) -> State:
    state.samjna_registry["2_3_49_sambuddhi"] = True
    state.samjna_registry["sambuddhi"]        = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.49",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "ekavacanaM saMbudDiH",
    text_dev              = "एकवचनं संबुद्धिः",
    padaccheda_dev        = "एकवचनम् सम्बुद्धिः",
    why_dev               = "सम्बोधनम् एकवचनम् इत्युच्यते — सम्बुद्धि-संज्ञा (२.३.४९)।",
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
