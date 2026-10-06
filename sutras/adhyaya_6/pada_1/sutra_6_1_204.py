"""
6.1.204  संज्ञायामुपमानम्  —  VIDHI

Padaccheda: संज्ञायाम् उपमानम्

संज्ञायामुपमानम् (6.1.204)
Pāṭha: ashtadhyayi.com data.txt row i=61204 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_204_saMjYAyAmu_204"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.204", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.204"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.204",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAmupamAnam",
    text_dev              = "संज्ञायामुपमानम्",
    samagra_slp1          = "saMjYAyAm upamAnam udAttaH AdiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संज्ञायाम् उपमानम् उदात्तः आदिः",
    padaccheda_dev        = "संज्ञायाम् उपमानम्",
    why_dev               = "(सूत्रम् 6.1.204) संज्ञायामुपमानम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
