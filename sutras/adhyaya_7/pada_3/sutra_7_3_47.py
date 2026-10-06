"""
7.3.47  भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि  —  VIDHI

Padaccheda: भस्त्रा-एषा-अजा-ज्ञा-द्वा-स्वाः (षष्ठ्यर्थे प्रथमा) नञ्-पूर्वाणाम् अपि

भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि (7.3.47)
Pāṭha: ashtadhyayi.com data.txt row i=73047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_47_BastrEzAj_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.47", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BastrEzAjAjYAdvAsvAnaYpUrvARAmapi',
    text_dev              = 'भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि',
    samagra_slp1          = "aNgasya BastrEzAjAjYAdvAsvAH naYpUrvARAm api it ataH udIcAm AtaH sTAne",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य भस्त्रैषाऽजाज्ञाद्वास्वाः नञ्पूर्वाणाम् अपि इत् अतः उदीचाम् आतः स्थाने",
    padaccheda_dev        = "भस्त्रा-एषा-अजा-ज्ञा-द्वा-स्वाः (षष्ठ्यर्थे प्रथमा) नञ्-पूर्वाणाम् अपि",
    why_dev               = "(सूत्रम् 7.3.47) भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
