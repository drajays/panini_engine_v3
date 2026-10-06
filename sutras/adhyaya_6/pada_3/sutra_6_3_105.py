"""
6.3.105  ईषदर्थे  —  VIDHI

Padaccheda: ईषत्-अर्थे

ईषदर्थे (6.3.105)
Pāṭha: ashtadhyayi.com data.txt row i=63105 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_105_IzadarTe_105"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.105", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "IzadarTe",
    text_dev              = "ईषदर्थे",
    samagra_slp1          = "uttarapade Izat-arTe koH kA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे ईषत्-अर्थे कोः का",
    padaccheda_dev        = "ईषत्-अर्थे",
    why_dev               = "(सूत्रम् 6.3.105) ईषदर्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
