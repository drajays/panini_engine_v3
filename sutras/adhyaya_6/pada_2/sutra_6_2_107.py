"""
6.2.107  उदराश्वेषुषु  —  VIDHI

Padaccheda: उदरअश्व-इषुषु

उदराश्वेषुषु (6.2.107)
Pāṭha: ashtadhyayi.com data.txt row i=62107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_107_udarASvezu_107"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.107", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udarASvezuzu",
    text_dev              = "उदराश्वेषुषु",
    samagra_slp1          = "udAttaH antaH udara-aSva-izuzu pUrvapadam viSvam bahuvrIhO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः अन्तः उदर-अश्व-इषुषु पूर्वपदम् विश्वम् बहुव्रीहौ",
    padaccheda_dev        = "उदरअश्व-इषुषु",
    why_dev               = "(सूत्रम् 6.2.107) उदराश्वेषुषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
