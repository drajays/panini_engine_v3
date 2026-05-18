"""
2.4.7  विशिष्टलिङ्गो नदी देशोऽग्रामाः  —  VIDHI

Padaccheda: विशिष्ट-लिङ्गः / नदी / देशः / अ-ग्रामाः

Śāstra: a dvandva compound denoting rivers (nadī), regions (deśa), or
non-village localities (agrāma) that have a specific gender (viśiṣṭaliṅga)
takes ekavacana.

Engine: sets gate "2_4_7_visisthalinga_nadi_desa_agrama_ekavacana".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_7_visisthalinga_nadi_desa_agrama_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.7",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "viSizTaliGgo nadI deSo 'grAmAH",
    text_dev       = "विशिष्टलिङ्गो नदी देशोऽग्रामाः",
    padaccheda_dev = "विशिष्ट-लिङ्गः / नदी / देशः / अ-ग्रामाः",
    why_dev        = "विशिष्टलिङ्ग-नदी-देश-अग्राम-द्वन्द्वे एकवचनम्।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
