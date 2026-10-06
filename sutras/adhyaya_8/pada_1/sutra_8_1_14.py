"""
8.1.14  यथास्वे यथायथम्  —  VIDHI

Padaccheda: यथास्वे यथायथम्

यथास्वे यथायथम् (8.1.14)
Pāṭha: ashtadhyayi.com data.txt row i=81014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_14_yaTAsve_14"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.14", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaTAsve yaTAyaTam",
    text_dev              = "यथास्वे यथायथम्",
    samagra_slp1          = "sarvasya dve yaTAsve yaTAyaTam karmaDArayavat",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "सर्वस्य द्वे यथास्वे यथायथम् कर्मधारयवत्",
    padaccheda_dev        = "यथास्वे यथायथम्",
    why_dev               = "(सूत्रम् 8.1.14) यथास्वे यथायथम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
