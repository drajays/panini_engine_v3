"""
6.2.124  कन्था च  —  VIDHI

Padaccheda: कन्था च

कन्था च (6.2.124)
Pāṭha: ashtadhyayi.com data.txt row i=62124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_124_kanTA_124"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.124", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kanTA ca",
    text_dev              = "कन्था च",
    samagra_slp1          = "udAttaH uttarapadAdiH kanTA ca napuMsake tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः कन्था च नपुंसके तत्पुरुषे",
    padaccheda_dev        = "कन्था च",
    why_dev               = "(सूत्रम् 6.2.124) कन्था च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
