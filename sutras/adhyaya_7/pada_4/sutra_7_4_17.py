"""
7.4.17  अस्यतेस्थुक्  —  VIDHI

Padaccheda: अस्यतेः थुक्

अस्यतेस्थुक् (7.4.17)
Pāṭha: ashtadhyayi.com data.txt row i=74017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_17_asyatesTuk_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.17", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asyatesTuk",
    text_dev              = "अस्यतेस्थुक्",
    samagra_slp1          = "aNgasya asyateH Tuk aNi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अस्यतेः थुक् अङि",
    padaccheda_dev        = "अस्यतेः थुक्",
    why_dev               = "(सूत्रम् 7.4.17) अस्यतेस्थुक्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
