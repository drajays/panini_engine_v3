"""
6.1.117  यजुष्युरः  —  VIDHI

Padaccheda: यजुषि उरः

यजुष्युरः (6.1.117)
Pāṭha: ashtadhyayi.com data.txt row i=61117 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_117_yajuzyuraH_117"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.117", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajuzyuraH",
    text_dev              = "यजुष्युरः",
    samagra_slp1          = "saMhitAyAm yajuzi uraH aci prakftyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् यजुषि उरः अचि प्रकृत्या",
    padaccheda_dev        = "यजुषि उरः",
    why_dev               = "(सूत्रम् 6.1.117) यजुष्युरः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
