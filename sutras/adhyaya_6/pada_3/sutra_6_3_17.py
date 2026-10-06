"""
6.3.17  घकालतनेषु कालनाम्नः  —  VIDHI

Padaccheda: घ-काल-तनेषु काल-नाम्नः

घकालतनेषु कालनाम्नः (6.3.17)
Pāṭha: ashtadhyayi.com data.txt row i=63017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_17_GakAlatane_17"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.17", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GakAlatanezu kAlanAmnaH",
    text_dev              = "घकालतनेषु कालनाम्नः",
    samagra_slp1          = "alug uttarapade Ga-kAla-tanezu kAlanAmnaH haladantAt saptamyAH viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे घ-काल-तनेषु कालनाम्नः हलदन्तात् सप्तम्याः विभाषा",
    padaccheda_dev        = "घ-काल-तनेषु काल-नाम्नः",
    why_dev               = "(सूत्रम् 6.3.17) घकालतनेषु कालनाम्नः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
