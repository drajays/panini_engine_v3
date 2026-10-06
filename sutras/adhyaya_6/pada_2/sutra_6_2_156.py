"""
6.2.156  ययतोश्चातदर्थे  —  VIDHI

Padaccheda: य-यतोः च अतदर्थे

ययतोश्चातदर्थे (6.2.156)
Pāṭha: ashtadhyayi.com data.txt row i=62156 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_156_yayatoScAt_156"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.156", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yayatoScAtadarTe",
    text_dev              = "ययतोश्चातदर्थे",
    samagra_slp1          = "antaH yayatoH ca atadarTe guRapratizeDe naYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अन्तः ययतोः च अतदर्थे गुणप्रतिषेधे नञः",
    padaccheda_dev        = "य-यतोः च अतदर्थे",
    why_dev               = "(सूत्रम् 6.2.156) ययतोश्चातदर्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
