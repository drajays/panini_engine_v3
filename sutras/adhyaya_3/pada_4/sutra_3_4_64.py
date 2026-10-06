"""
3.4.64  अन्वच्यानुलोम्ये  —  VIDHI

Padaccheda: अन्वचि आनुलोम्ये

krt-suffix rule: अन्वच्यानुलोम्ये
Pāṭha: ashtadhyayi.com data.txt row i=34064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_64_anvacyAnul_64"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.64", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anvacyAnulomye",
    text_dev              = "अन्वच्यानुलोम्ये",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH anvaci Anulomye kft ktvA-RamulO BuvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अन्वचि आनुलोम्ये कृत् क्त्वा-णमुलौ भुवः",
    padaccheda_dev        = "अन्वचि आनुलोम्ये",
    why_dev               = "धातोः प्रत्ययः (३.4.64)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
