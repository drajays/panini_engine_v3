"""
3.1.27  कण्ड्वादिभ्यो यक्  —  VIDHI

Padaccheda: कण्डू-आदिभ्यः यक्

Krt suffix rule from dhatu: कण्ड्वादिभ्यो यक् (27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_27_kaRqvAdiByo_27"


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
    state.meta["krt_kind"] = "3.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaRqvAdiByo yak",
    text_dev              = "कण्ड्वादिभ्यो यक्",
    padaccheda_dev        = "कण्डू-आदिभ्यः यक्",
    why_dev               = "धातोः [कण्ड्वादिभ्यो यक्]-प्रत्ययः विहितः (३.१.27)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
