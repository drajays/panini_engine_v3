"""
6.2.131  वर्ग्यादयश्च  —  VIDHI

Padaccheda: वर्ग्य-आदयः च

वर्ग्यादयश्च (6.2.131)
Pāṭha: ashtadhyayi.com data.txt row i=62131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_131_vargyAdaya_131"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.131", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vargyAdayaSca",
    text_dev              = "वर्ग्यादयश्च",
    samagra_slp1          = "udAttaH uttarapadAdiH vargyAdayaH ca tatpuruze akarmaDAraye",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः वर्ग्यादयः च तत्पुरुषे अकर्मधारये",
    padaccheda_dev        = "वर्ग्य-आदयः च",
    why_dev               = "(सूत्रम् 6.2.131) वर्ग्यादयश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
