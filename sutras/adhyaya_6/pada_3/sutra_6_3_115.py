"""
6.3.115  कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य  —  VIDHI

Padaccheda: कर्णे लक्षणस्य अ-विष्ट-अष्ट-पञ्च-मणि-भिन्न-छिन्न-छिद्र-स्रुव-स्वस्तिकस्य

कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य (6.3.115)
Pāṭha: ashtadhyayi.com data.txt row i=63115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_115_karRe_115"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.115", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karRe lakzaRasyAvizwAzwapaYcamaRiBinnaCinnaCidrasruvasvastikasya",
    text_dev              = "कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य",
    samagra_slp1          = "uttarapade saMhitAyAm karRe lakzaRasya a-vizwa-azwa-paYca-maRi-Binna-Cinna-Cidra-sruva-svastikasya dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् कर्णे लक्षणस्य अ-विष्ट-अष्ट-पञ्च-मणि-भिन्न-छिन्न-छिद्र-स्रुव-स्वस्तिकस्य दीर्घः",
    padaccheda_dev        = "कर्णे लक्षणस्य अ-विष्ट-अष्ट-पञ्च-मणि-भिन्न-छिन्न-छिद्र-स्रुव-स्वस्तिकस्य",
    why_dev               = "(सूत्रम् 6.3.115) कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नछिन्नछिद्रस्रुवस्वस्तिकस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
