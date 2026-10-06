"""
3.3.63  यमः समुपनिविषु च  —  VIDHI

Padaccheda: यमः सम्-उप-नि-विषु

krt-suffix rule: यमः समुपनिविषु
Pāṭha: ashtadhyayi.com data.txt row i=33063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_63_yamaH_63"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.63", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yamaH samupanivizu ca',
    text_dev              = 'यमः समुपनिविषु च',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm yamaH sam-upa-ni-vizu ca kft ap anupasarge vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् यमः सम्-उप-नि-विषु च कृत् अप् अनुपसर्गे वा",
    padaccheda_dev        = "यमः सम्-उप-नि-विषु",
    why_dev               = "धातोः प्रत्ययः (३.3.63)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
