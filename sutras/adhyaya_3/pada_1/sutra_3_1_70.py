"""
3.1.70  वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः  —  VIDHI

Padaccheda: वा भ्राश-भ्लाश-भ्रमु-क्रमु-क्लमु-त्रसि-त्रुटि-लषः

Krt suffix rule from dhatu: वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः (70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_70_vA_70"


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
    state.meta["krt_kind"] = "3.1.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA BrASaBlASaBramukramuklamutrasitruwilazaH",
    text_dev              = "वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः",
    padaccheda_dev        = "वा भ्राश-भ्लाश-भ्रमु-क्रमु-क्लमु-त्रसि-त्रुटि-लषः",
    why_dev               = "धातोः [वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः]-प्रत्ययः विहितः (३.१.70)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
