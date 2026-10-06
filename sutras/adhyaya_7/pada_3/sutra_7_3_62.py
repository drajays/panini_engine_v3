"""
7.3.62  प्रयाजानुयाजौ यज्ञाङ्गे  —  VIDHI

Padaccheda: प्रयाज-अनुयाजौ यज्ञाङ्गे

प्रयाजानुयाजौ यज्ञाङ्गे (7.3.62)
Pāṭha: ashtadhyayi.com data.txt row i=73062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_62_prayAjAnuy_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.62", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prayAjAnuyAjO yajYANge",
    text_dev              = "प्रयाजानुयाजौ यज्ञाङ्गे",
    samagra_slp1          = "aNgasya prayAjAnuyAjO yajYANge cajoH ku na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य प्रयाजानुयाजौ यज्ञाङ्गे चजोः कु न",
    padaccheda_dev        = "प्रयाज-अनुयाजौ यज्ञाङ्गे",
    why_dev               = "(सूत्रम् 7.3.62) प्रयाजानुयाजौ यज्ञाङ्गे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
