"""
6.3.31  उषासोषसः  —  VIDHI

Padaccheda: उषासा उषसः

उषासोषसः (6.3.31)
Pāṭha: ashtadhyayi.com data.txt row i=63031 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_31_uzAsozasaH_31"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.31", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uzAsozasaH",
    text_dev              = "उषासोषसः",
    samagra_slp1          = "uttarapade uzAsA uzasaH devatAdvandve ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे उषासा उषसः देवताद्वन्द्वे च",
    padaccheda_dev        = "उषासा उषसः",
    why_dev               = "(सूत्रम् 6.3.31) उषासोषसः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
