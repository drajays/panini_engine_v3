"""
3.1.127  आनाय्योऽनित्ये  —  VIDHI

Padaccheda: आनाय्यः अनित्ये

Krt suffix rule from dhatu: आनाय्योऽनित्ये (127)
Pāṭha: ashtadhyayi.com data.txt row i=31127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_127_AnAyyonitye_127"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.127", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'AnAyyonitye',
    text_dev              = 'आनाय्योऽनित्ये',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH AnAyyaH anitye kft Ryat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः आनाय्यः अनित्ये कृत् ण्यत्",
    padaccheda_dev        = "आनाय्यः अनित्ये",
    why_dev               = "धातोः [आनाय्योऽनित्ये]-प्रत्ययः विहितः (३.१.127)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
