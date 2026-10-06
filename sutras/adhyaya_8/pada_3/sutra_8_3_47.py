"""
8.3.47  अधःशिरसी पदे  —  VIDHI

Padaccheda: अधः · शिरसी · पदे

अधःशिरसी पदे (8.3.47)
Pāṭha: ashtadhyayi.com data.txt row i=83047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_47_aDaHSirasI_47"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.47", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDaHSirasI pade",
    text_dev              = "अधःशिरसी पदे",
    samagra_slp1          = "aDaH-SirasoH samAse visarjanIyasya nityam saH pade anuttarapadasTasya",
    samagra_dev           = "अधः-शिरसोः समासे विसर्जनीयस्य नित्यम् सः पदे, अनुत्तरपदस्थस्य",
    padaccheda_dev        = "अधः · शिरसी · पदे",
    why_dev               = "(सूत्रम् 8.3.47) अधःशिरसी पदे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
