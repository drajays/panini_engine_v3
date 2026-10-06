"""
6.2.130  अकर्मधारये राज्यम्  —  VIDHI

Padaccheda: अ-कर्मधारये राज्यम्

अकर्मधारये राज्यम् (6.2.130)
Pāṭha: ashtadhyayi.com data.txt row i=62130 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_130_akarmaDAra_130"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.130", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akarmaDAraye rAjyam",
    text_dev              = "अकर्मधारये राज्यम्",
    samagra_slp1          = "udAttaH uttarapadAdiH akarmaDAraye rAjyam tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः अकर्मधारये राज्यम् तत्पुरुषे",
    padaccheda_dev        = "अ-कर्मधारये राज्यम्",
    why_dev               = "(सूत्रम् 6.2.130) अकर्मधारये राज्यम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
