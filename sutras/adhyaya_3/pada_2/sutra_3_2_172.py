"""
3.2.172  स्वपितृषोर्नजिङ्  —  VIDHI

Padaccheda: स्वपि-तृषोः नजिङ्

krt-suffix rule: स्वपितृषोर्नजिङ् (172)
Pāṭha: ashtadhyayi.com data.txt row i=32172 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_172_svapitfzor_172"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.172", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.172"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.172",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svapitfzornajiN",
    text_dev              = "स्वपितृषोर्नजिङ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu svapi-tfzoH najiN kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु स्वपि-तृषोः नजिङ् कृत्",
    padaccheda_dev        = "स्वपि-तृषोः नजिङ्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्वपितृषोर्नजिङ्] विहितः (३.२.172)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
