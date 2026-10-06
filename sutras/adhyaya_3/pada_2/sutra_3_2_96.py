"""
3.2.96  सहे च  —  VIDHI

Padaccheda: सहे च

krt-suffix rule: सहे च (96)
Pāṭha: ashtadhyayi.com data.txt row i=32096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_96_sahe_96"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.96", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sahe ca",
    text_dev              = "सहे च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte sahe ca kft kvanip yuDi-kfYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते सहे च कृत् क्वनिप् युधि-कृञः",
    padaccheda_dev        = "सहे च",
    why_dev               = "धातोः कृत्-प्रत्ययः [सहे च] विहितः (३.२.96)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
