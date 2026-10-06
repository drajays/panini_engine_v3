"""
6.2.119  आद्युदात्तं द्व्यच् छन्दसि  —  VIDHI

Padaccheda: आदि-उदात्तम् द्वि-अच् छन्दसि

आद्युदात्तं द्व्यच् छन्दसि (6.2.119)
Pāṭha: ashtadhyayi.com data.txt row i=62119 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_119_AdyudAttaM_119"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.119", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AdyudAttaM dvyac Candasi",
    text_dev              = "आद्युदात्तं द्व्यच् छन्दसि",
    samagra_slp1          = "udAttaH uttarapadAdiH AdyudAttam dvyac Candasi bahuvrIhO soH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः आद्युदात्तम् द्व्यच् छन्दसि बहुव्रीहौ सोः",
    padaccheda_dev        = "आदि-उदात्तम् द्वि-अच् छन्दसि",
    why_dev               = "(सूत्रम् 6.2.119) आद्युदात्तं द्व्यच् छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
