"""
5.4.58  कृञो द्वितीयतृतीयशम्बबीजात् कृषौ  —  VIDHI

Padaccheda: कृञः द्वितीय-तृतीय-शम्ब-बीजात् कृषौ

कृञो द्वितीयतृतीयशम्बबीजात् कृषौ (5.4.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_58_kfYo_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_58_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfYo dvitIyatftIyaSambabIjAt kfzO",
    text_dev              = "कृञो द्वितीयतृतीयशम्बबीजात् कृषौ",
    padaccheda_dev        = "कृञः द्वितीय-तृतीय-शम्ब-बीजात् कृषौ",
    why_dev               = "(सूत्रम् 5.4.58) कृञो द्वितीयतृतीयशम्बबीजात् कृषौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
