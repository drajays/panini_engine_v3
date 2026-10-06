"""
7.3.8  श्वादेरिञि  —  VIDHI

Padaccheda: श्व-आदेः इञि

श्वादेरिञि (7.3.8)
Pāṭha: ashtadhyayi.com data.txt row i=73008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_8_SvAderiYi_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.8", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SvAderiYi",
    text_dev              = "श्वादेरिञि",
    samagra_slp1          = "aNgasya SvAdeH iYi vfdDiH acaH YRiti tadDitezu AdeH na Ec",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य श्वादेः इञि वृद्धिः अचः ञ्णिति तद्धितेषु आदेः न ऐच्",
    padaccheda_dev        = "श्व-आदेः इञि",
    why_dev               = "(सूत्रम् 7.3.8) श्वादेरिञि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
