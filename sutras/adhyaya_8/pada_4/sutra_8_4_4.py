"""
8.4.4  वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः  —  VIDHI

Padaccheda: वनम् (षष्ठीस्थाने व्यत्ययेन प्रथमा) पुरगा-मिश्रका-सिध्रका-शारिका-कोटरा-अग्रेभ्यः

वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः (8.4.4)
Pāṭha: ashtadhyayi.com data.txt row i=84004 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_4_vanaM_4"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.4", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'vanaM puragAmiSrakAsiDrakASArikAkowarAgreByaH',
    text_dev              = 'वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm vanam puragA-miSrakA-siDrakA-SArikA-kowarA-agreByaH razAByAm agaH pUrvapadAt saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् वनम् पुरगा-मिश्रका-सिध्रका-शारिका-कोटरा-अग्रेभ्यः रषाभ्याम् अगः पूर्वपदात् संज्ञायाम्",
    padaccheda_dev        = "वनम् (षष्ठीस्थाने व्यत्ययेन प्रथमा) पुरगा-मिश्रका-सिध्रका-शारिका-कोटरा-अग्रेभ्यः",
    why_dev               = "(सूत्रम् 8.4.4) वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
