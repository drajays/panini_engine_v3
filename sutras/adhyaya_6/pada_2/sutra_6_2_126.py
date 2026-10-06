"""
6.2.126  चेलखेटकटुककाण्डं गर्हायाम्  —  VIDHI

Padaccheda: चेल-खेट-कटुक-काण्डम् गर्हायाम्

चेलखेटकटुककाण्डं गर्हायाम् (6.2.126)
Pāṭha: ashtadhyayi.com data.txt row i=62126 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_126_celaKewaka_126"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.126", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "celaKewakawukakARqaM garhAyAm",
    text_dev              = "चेलखेटकटुककाण्डं गर्हायाम्",
    samagra_slp1          = "udAttaH uttarapadAdiH cela-Kewa-kawuka-kARqam garhAyAm tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः चेल-खेट-कटुक-काण्डम् गर्हायाम् तत्पुरुषे",
    padaccheda_dev        = "चेल-खेट-कटुक-काण्डम् गर्हायाम्",
    why_dev               = "(सूत्रम् 6.2.126) चेलखेटकटुककाण्डं गर्हायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
