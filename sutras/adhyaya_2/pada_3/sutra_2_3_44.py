"""
2.3.44  प्रसितोत्सुकाभ्यां तृतीया च  —  VIDHI

Padaccheda: प्रसित-उत्सुकाभ्याम् तृतीया च

prasita and utsuka also take tritiya.
Pāṭha: ashtadhyayi.com data.txt row i=23044 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_44_prasita_utsuka"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prasitotsukAByAM tftIyA ca",
    text_dev              = "प्रसितोत्सुकाभ्यां तृतीया च",
    samagra_slp1          = "anaBihite prasita-utsukAByAm tftIyA ca saptamI",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते प्रसित-उत्सुकाभ्याम् तृतीया च सप्तमी",
    padaccheda_dev        = "प्रसित-उत्सुकाभ्याम् तृतीया च",
    why_dev               = "प्रसित-उत्सुकाभ्याम् तृतीया च (२.३.४४)।",
    anuvritti_from        = ('2.3.43',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
