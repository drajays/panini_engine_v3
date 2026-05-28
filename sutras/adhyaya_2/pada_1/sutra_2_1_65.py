"""
2.1.65  पोटायुवतिस्तोककतिपयगृष्टिधेनुवशावेहत्बष्कयणीप्रवक्तॄश्रोत्रियाध्यापकधूर्तैर्जातिः  —  VIDHI

Padaccheda: पोटा-युवति-स्तोक-कतिपय-गृष्टि-धेनु-वशा-वेहद्-बष्कयणी-प्रवक्तॄ-श्रोत्रिय-अध्यापक-धूर्तैः जातिः

pota, yuvati, stoka, katipaya etc. with jati form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_65_pota_jati"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "powAyuvatistokakatipayagfzwiDenuvaSAvehatbazkayaRIpravaktFSrotriyADyApakaDUrtErjAtiH",
    text_dev              = "पोटायुवतिस्तोककतिपयगृष्टिधेनुवशावेहत्बष्कयणीप्रवक्तॄश्रोत्रियाध्यापकधूर्तैर्जातिः",
    padaccheda_dev        = "पोटा-युवति-स्तोक-कतिपय-गृष्टि-धेनु-वशा-वेहद्-बष्कयणी-प्रवक्तॄ-श्रोत्रिय-अध्यापक-धूर्तैः जातिः",
    why_dev               = "पोटा-युवति-आदिभिः जाति-वाचिभिः सह कर्मधारयः (२.१.६५)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
