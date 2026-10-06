"""
6.1.138  समवाये च  —  VIDHI

Padaccheda: समवाये च

समवाये च (6.1.138)
Pāṭha: ashtadhyayi.com data.txt row i=61138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_138_samavAye_138"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.138", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samavAye ca",
    text_dev              = "समवाये च",
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH samavAye ca sam-pari-upeByaH karotO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः समवाये च सम्-परि-उपेभ्यः करोतौ",
    padaccheda_dev        = "समवाये च",
    why_dev               = "(सूत्रम् 6.1.138) समवाये च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
