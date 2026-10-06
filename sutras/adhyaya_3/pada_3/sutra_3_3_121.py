"""
3.3.121  हलश्च  —  VIDHI

Padaccheda: हलः च

krt-suffix rule: हलश्च
Pāṭha: ashtadhyayi.com data.txt row i=33121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_121_halaSca_121"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.121", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "halaSca",
    text_dev              = "हलश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karaRADikaraRayoH halaH ca kft karaRa-aDikaraRayoH puMsi GaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः करणाधिकरणयोः हलः च कृत् करण-अधिकरणयोः पुंसि घञ्",
    padaccheda_dev        = "हलः च",
    why_dev               = "धातोः प्रत्ययः (३.3.121)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
