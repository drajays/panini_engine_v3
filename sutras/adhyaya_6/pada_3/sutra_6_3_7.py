"""
6.3.7  वैयाकरणाख्यायां चतुर्थ्याः  —  VIDHI

Padaccheda: वैयाकरणाख्यायाम् चतुर्थ्याः

वैयाकरणाख्यायां चतुर्थ्याः (6.3.7)
Pāṭha: ashtadhyayi.com data.txt row i=63007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_7_vEyAkaraRA_7"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.7", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vEyAkaraRAKyAyAM caturTyAH",
    text_dev              = "वैयाकरणाख्यायां चतुर्थ्याः",
    samagra_slp1          = "alug uttarapade vEyAkaraRAKyAyAm caturTyAH AtmanaH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे वैयाकरणाख्यायाम् चतुर्थ्याः आत्मनः च",
    padaccheda_dev        = "वैयाकरणाख्यायाम् चतुर्थ्याः",
    why_dev               = "(सूत्रम् 6.3.7) वैयाकरणाख्यायां चतुर्थ्याः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
