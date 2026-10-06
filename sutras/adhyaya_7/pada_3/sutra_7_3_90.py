"""
7.3.90  ऊर्णोतेर्विभाषा  —  VIDHI

Padaccheda: ऊर्णोतेः विभाषा

ऊर्णोतेर्विभाषा (7.3.90)
Pāṭha: ashtadhyayi.com data.txt row i=73090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_90_UrRoterviB_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.90", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UrRoterviBAzA",
    text_dev              = "ऊर्णोतेर्विभाषा",
    samagra_slp1          = "aNgasya UrRoteH viBAzA piti sArvaDAtuke vfdDiH hali",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऊर्णोतेः विभाषा पिति सार्वधातुके वृद्धिः हलि",
    padaccheda_dev        = "ऊर्णोतेः विभाषा",
    why_dev               = "(सूत्रम् 7.3.90) ऊर्णोतेर्विभाषा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
