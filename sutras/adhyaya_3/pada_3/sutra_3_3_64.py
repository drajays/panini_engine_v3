"""
3.3.64  नौ गदनदपठस्वनः  —  VIDHI

Padaccheda: नौ गद-नद-पठ-स्वनः

krt-suffix rule: नौ गदनदपठस्वनः
Pāṭha: ashtadhyayi.com data.txt row i=33064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_64_nO_64"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.64", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nO gadanadapaWasvanaH",
    text_dev              = "नौ गदनदपठस्वनः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm nO gada-nada-paWa-svanaH kft ap anupasarge vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् नौ गद-नद-पठ-स्वनः कृत् अप् अनुपसर्गे वा",
    padaccheda_dev        = "नौ गद-नद-पठ-स्वनः",
    why_dev               = "धातोः प्रत्ययः (३.3.64)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
