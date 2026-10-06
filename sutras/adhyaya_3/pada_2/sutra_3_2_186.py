"""
3.2.186  कर्तरि चर्षिदेवतयोः  —  VIDHI

Padaccheda: कर्तरि च ऋषि-देवतयोः

krt-suffix rule: कर्तरि चर्षिदेवतयोः (186)
Pāṭha: ashtadhyayi.com data.txt row i=32186 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_186_kartari_186"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.186", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.186"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.186",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartari carzidevatayoH",
    text_dev              = "कर्तरि चर्षिदेवतयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne kartari ca fzi-devatayoH kft karaRe itraH puvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने कर्तरि च ऋषि-देवतयोः कृत् करणे इत्रः पुवः",
    padaccheda_dev        = "कर्तरि च ऋषि-देवतयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्तरि चर्षिदेवतयोः] विहितः (३.२.186)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
