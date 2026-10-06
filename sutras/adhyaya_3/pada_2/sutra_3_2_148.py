"""
3.2.148  चलनशब्दार्थादकर्मकाद्युच्  —  VIDHI

Padaccheda: चलन-शब्द-अर्थात् अकर्मकात् युच्

krt-suffix rule: चलनशब्दार्थादकर्मकाद्युच् (148)
Pāṭha: ashtadhyayi.com data.txt row i=32148 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_148_calanaSabd_148"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.148", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "calanaSabdArTAdakarmakAdyuc",
    text_dev              = "चलनशब्दार्थादकर्मकाद्युच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu calanaSabdArTAt akarmakAt yuc kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु चलनशब्दार्थात् अकर्मकात् युच् कृत्",
    padaccheda_dev        = "चलन-शब्द-अर्थात् अकर्मकात् युच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [चलनशब्दार्थादकर्मकाद्युच्] विहितः (३.२.148)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
