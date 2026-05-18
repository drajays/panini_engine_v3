"""
6.3.85  ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु  —  VIDHI

Padaccheda: ज्योतिः-जनपद-रात्रि-नाभि-नाम-गोत्र-रूप-स्थान-वर्ण-वयः-वचन-बन्धुषु

ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु (6.3.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_85_jyotirjana_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jyotirjanapadarAtrinABinAmagotrarUpasTAnavarRavayovacanabanDuzu",
    text_dev              = "ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु",
    padaccheda_dev        = "ज्योतिः-जनपद-रात्रि-नाभि-नाम-गोत्र-रूप-स्थान-वर्ण-वयः-वचन-बन्धुषु",
    why_dev               = "(सूत्रम् 6.3.85) ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
