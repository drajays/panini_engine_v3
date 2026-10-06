"""
7.3.35  जनिवध्योश्च  —  VIDHI

Padaccheda: जनि-वध्योः च

जनिवध्योश्च (7.3.35)
Pāṭha: ashtadhyayi.com data.txt row i=73035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_35_janivaDyoS_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.35", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janivaDyoSca",
    text_dev              = "जनिवध्योश्च",
    samagra_slp1          = "aNgasya janivaDyoH ca vfdDiH YRiti ciRkftoH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य जनिवध्योः च वृद्धिः ञ्णिति चिण्कृतोः न",
    padaccheda_dev        = "जनि-वध्योः च",
    why_dev               = "(सूत्रम् 7.3.35) जनिवध्योश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
