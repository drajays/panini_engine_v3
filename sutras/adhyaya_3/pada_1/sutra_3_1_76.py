"""
3.1.76  तनूकरणे तक्षः  —  VIDHI

Padaccheda: तनूकरणे तक्षः

Krt suffix rule from dhatu: तनूकरणे तक्षः (76)
Pāṭha: ashtadhyayi.com data.txt row i=31076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_76_tanUkaraRe_76"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.76", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tanUkaraRe takzaH",
    text_dev              = "तनूकरणे तक्षः",
    samagra_slp1          = "karttari sArvaDAtuke tanUkaraRe takzaH SnuH anyatarasyAm",
    samagra_dev           = "कर्त्तरि सार्वधातुके तनूकरणे तक्षः श्नुः अन्यतरस्याम्",
    padaccheda_dev        = "तनूकरणे तक्षः",
    why_dev               = "धातोः [तनूकरणे तक्षः]-प्रत्ययः विहितः (३.१.76)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
