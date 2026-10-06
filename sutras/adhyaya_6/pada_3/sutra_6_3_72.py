"""
6.3.72  रात्रेः कृति विभाषा  —  VIDHI

Padaccheda: रात्रेः कृति विभाषा

रात्रेः कृति विभाषा (6.3.72)
Pāṭha: ashtadhyayi.com data.txt row i=63072 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_72_rAtreH_72"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.72", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAtreH kfti viBAzA",
    text_dev              = "रात्रेः कृति विभाषा",
    samagra_slp1          = "uttarapade rAtreH kfti viBAzA mum",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे रात्रेः कृति विभाषा मुम्",
    padaccheda_dev        = "रात्रेः कृति विभाषा",
    why_dev               = "(सूत्रम् 6.3.72) रात्रेः कृति विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
