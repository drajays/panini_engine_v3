"""
3.1.147  ण्युट् च  —  VIDHI

Padaccheda: ण्युट् च

Krt suffix rule from dhatu: ण्युट् च (147)
Pāṭha: ashtadhyayi.com data.txt row i=31147 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_147_Ryuw_147"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.147", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ryuw ca",
    text_dev              = "ण्युट् च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Ryuw ca kft Silpini gaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः ण्युट् च कृत् शिल्पिनि गः",
    padaccheda_dev        = "ण्युट् च",
    why_dev               = "धातोः [ण्युट् च]-प्रत्ययः विहितः (३.१.147)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
