"""
6.1.98  अव्यक्तानुकरणस्यात इतौ  —  VIDHI

Padaccheda: अव्यक्त-अनुकरणस्य अतः इतौ

अव्यक्तानुकरणस्यात इतौ (6.1.98)
Pāṭha: ashtadhyayi.com data.txt row i=61098 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_98_avyaktAnuk_98"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.98", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'avyaktAnukaraRasyAta itO',
    text_dev              = 'अव्यक्तानुकरणस्यात इतौ',
    samagra_slp1          = "avyaktAnukaraRasya ataH itO pUrvaparayoH ekaH pararUpam",
    samagra_dev           = "अव्यक्तानुकरणस्य अतः इतौ पूर्वपरयोः एकः पररूपम्",
    padaccheda_dev        = "अव्यक्त-अनुकरणस्य अतः इतौ",
    why_dev               = "(सूत्रम् 6.1.98) अव्यक्तानुकरणस्यात इतौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
