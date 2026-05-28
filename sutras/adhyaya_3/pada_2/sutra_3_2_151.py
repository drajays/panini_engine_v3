"""
3.2.151  क्रुधमण्डार्थेभ्यश्च  —  VIDHI

Padaccheda: क्रुध-मण्ड-अर्थेभ्यः च

krt-suffix rule: क्रुधमण्डार्थेभ्यश्च (151)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_151_kruDamaRqA_151"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_151_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.151"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kruDamaRqArTeByaSca",
    text_dev              = "क्रुधमण्डार्थेभ्यश्च",
    padaccheda_dev        = "क्रुध-मण्ड-अर्थेभ्यः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [क्रुधमण्डार्थेभ्यश्च] विहितः (३.२.151)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
