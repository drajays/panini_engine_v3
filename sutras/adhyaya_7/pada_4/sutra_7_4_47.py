"""
7.4.47  अच उपसर्गात्तः  —  VIDHI

Padaccheda: अचः उपसर्गात् तः

अच उपसर्गात्तः (7.4.47)
Pāṭha: ashtadhyayi.com data.txt row i=74047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_47_aca_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.47", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aca upasargAttaH",
    text_dev              = "अच उपसर्गात्तः",
    samagra_slp1          = "aNgasya acaH upasargAt taH ti kiti daH GoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अचः उपसर्गात् तः ति किति दः घोः",
    padaccheda_dev        = "अचः उपसर्गात् तः",
    why_dev               = "(सूत्रम् 7.4.47) अच उपसर्गात्तः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
