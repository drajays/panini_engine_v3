"""
2.4.5  अध्ययनतोऽविप्रकृष्टाख्यानाम्  —  VIDHI

Padaccheda: अध्ययनतः / अविप्रकृष्ट-आख्यानाम्

Śāstra: from the standpoint of recitation (adhyayana), dvandva compounds of
non-remote (aviprākṛṣṭa) named Vedic texts take ekavacana.

Engine: sets gate "2_4_5_adhyayana_avipraksrta_ekavacana".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_5_adhyayana_avipraksrta_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.5",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "aDyayanato 'vipraksRtAKyAnAm",
    text_dev       = "अध्ययनतोऽविप्रकृष्टाख्यानाम्",
    padaccheda_dev = "अध्ययनतः / अविप्रकृष्ट-आख्यानाम्",
    why_dev        = "अध्ययन-दृष्ट्या अविप्रकृष्ट-नामधेय-द्वन्द्वे एकवचनम्।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
