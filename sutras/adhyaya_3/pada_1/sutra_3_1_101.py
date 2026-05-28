"""
3.1.101  अवद्यपण्यवर्या गर्ह्यपणितव्यानिरोधेषु  —  VIDHI

Padaccheda: अवद्य-पण्य-वर्याः गर्ह्य-पणितव्य-अनिरोधेषु

Krt suffix rule from dhatu: अवद्यपण्यवर्या गर्ह्यपणितव्यानिरोधेषु (101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_101_avadyapaRyav_101"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avadyapaRyavaryA garhyapaRitavyAniroDezu",
    text_dev              = "अवद्यपण्यवर्या गर्ह्यपणितव्यानिरोधेषु",
    padaccheda_dev        = "अवद्य-पण्य-वर्याः गर्ह्य-पणितव्य-अनिरोधेषु",
    why_dev               = "धातोः [अवद्यपण्यवर्या गर्ह्यपणितव्यानिरोधेषु]-प्रत्ययः विहितः (३.१.101)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
