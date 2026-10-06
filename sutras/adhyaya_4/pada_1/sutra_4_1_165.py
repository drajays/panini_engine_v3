"""
4.1.165  वान्यस्मिन् सपिण्डे स्थविरतरे जीवति  —  VIDHI

Padaccheda: वा अन्यस्मिन् सपिण्डे स्थविरतरे जीवति

वाऽन्यस्मिन् सपिण्डे स्थविरतरे जीवति (4.1.165)
Pāṭha: ashtadhyayi.com data.txt row i=41165 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_165_vAnyasmin_165"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.165", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.165"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.165",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = 'vAnyasmin sapiRqe sTaviratare jIvati',
    text_dev              = 'वान्यस्मिन् सपिण्डे स्थविरतरे जीवति',
    samagra_slp1          = "BrAtari anyasmin sapiRqe sTaviratare jIvati pOtrapraBfteH apatyam jIvati eva yuvA vA ",
    samagra_dev           = "भ्रातरि अन्यस्मिन् सपिण्डे स्थविरतरे जीवति पौत्रप्रभृतेः अपत्यम् जीवति (एव) युवा वा ।",
    padaccheda_dev        = "वा अन्यस्मिन् सपिण्डे स्थविरतरे जीवति",
    why_dev               = "(सूत्रम् 4.1.165) वाऽन्यस्मिन् सपिण्डे स्थविरतरे जीवति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
