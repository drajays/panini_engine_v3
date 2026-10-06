"""
6.1.13  ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे  —  VIDHI

Padaccheda: ष्यङः सम्प्रसारणम् पुत्र-पत्योः तत्पुरुषे

ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे (6.1.13)
Pāṭha: ashtadhyayi.com data.txt row i=61013 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_13_zyaNaH_13"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.13", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zyaNaH samprasAraRaM putrapatyostatpuruze",
    text_dev              = "ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे",
    samagra_slp1          = "zyaNaH samprasAraRam putra-patyoH tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ष्यङः सम्प्रसारणम् पुत्र-पत्योः तत्पुरुषे",
    padaccheda_dev        = "ष्यङः सम्प्रसारणम् पुत्र-पत्योः तत्पुरुषे",
    why_dev               = "(सूत्रम् 6.1.13) ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
