"""
8.2.71  भुवश्च महाव्याहृतेः  —  VIDHI

Padaccheda: भुवः (अविभक्तिकम्) च महाव्याहृतेः

भुवश्च महाव्याहृतेः (8.2.71)
Pāṭha: ashtadhyayi.com data.txt row i=82071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_71_BuvaSca_71"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.71", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BuvaSca mahAvyAhfteH",
    text_dev              = "भुवश्च महाव्याहृतेः",
    samagra_slp1          = "padasya pUrvatrAsidDam BuvaH ca mahAvyAhfteH raH Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् भुवः च महाव्याहृतेः रः छन्दसि",
    padaccheda_dev        = "भुवः (अविभक्तिकम्) च महाव्याहृतेः",
    why_dev               = "(सूत्रम् 8.2.71) भुवश्च महाव्याहृतेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
