"""
6.1.33  अभ्यस्तस्य च  —  VIDHI

Padaccheda: अभ्यस्तस्य च

अभ्यस्तस्य च (6.1.33)
Pāṭha: ashtadhyayi.com data.txt row i=61033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_33_aByastasya_33"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aByastasya ca",
    text_dev              = "अभ्यस्तस्य च",
    samagra_slp1          = "aByastasya ca hvaH samprasAraRam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अभ्यस्तस्य च ह्वः सम्प्रसारणम्",
    padaccheda_dev        = "अभ्यस्तस्य च",
    why_dev               = "(सूत्रम् 6.1.33) अभ्यस्तस्य च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
