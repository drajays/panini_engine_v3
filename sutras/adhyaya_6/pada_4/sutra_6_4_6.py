"""
6.4.6  नृ च  —  VIDHI

Padaccheda: नृ (लुप्तषष्ठ्यन्तनिर्देशः) च

नृ च (6.4.6)
Pāṭha: ashtadhyayi.com data.txt row i=64006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_6_nf_6"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.6", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nf ca",
    text_dev              = "नृ च",
    samagra_slp1          = "nf-aNgasya nAmi dIrGaH uBayaTA",
    samagra_dev           = "नृ-अङ्गस्य नामि दीर्घः उभयथा",
    padaccheda_dev        = "नृ (लुप्तषष्ठ्यन्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 6.4.6) नृ च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
