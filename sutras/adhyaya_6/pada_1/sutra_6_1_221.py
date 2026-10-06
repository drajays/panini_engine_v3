"""
6.1.221  ईवत्याः  —  VIDHI

Padaccheda: ईवत्याः

ईवत्याः (6.1.221)
Pāṭha: ashtadhyayi.com data.txt row i=61221 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_221_IvatyAH_221"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.221", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.221"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.221",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "IvatyAH",
    text_dev              = "ईवत्याः",
    samagra_slp1          = "IvatyAH saMjYAyAm striyAm antaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ईवत्याः संज्ञायाम् स्त्रियाम् अन्तः",
    padaccheda_dev        = "ईवत्याः",
    why_dev               = "(सूत्रम् 6.1.221) ईवत्याः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
