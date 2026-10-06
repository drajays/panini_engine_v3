"""
6.1.207  आशितः कर्ता  —  VIDHI

Padaccheda: आशितः कर्ता

आशितः कर्ता (6.1.207)
Pāṭha: ashtadhyayi.com data.txt row i=61207 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_207_ASitaH_207"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.207", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.207"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.207",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASitaH kartA",
    text_dev              = "आशितः कर्ता",
    samagra_slp1          = "ASitaH kartA udAttaH AdiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आशितः कर्ता उदात्तः आदिः",
    padaccheda_dev        = "आशितः कर्ता",
    why_dev               = "(सूत्रम् 6.1.207) आशितः कर्ता।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
