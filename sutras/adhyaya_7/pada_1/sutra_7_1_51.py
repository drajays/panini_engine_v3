"""
7.1.51  अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि  —  VIDHI

Padaccheda: अश्व-क्षीर-वृष-लवणानाम् आत्म-प्रीतौ क्यचि

अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि (7.1.51)
Pāṭha: ashtadhyayi.com data.txt row i=71051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_51_aSvakzIrav_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.51", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aSvakzIravfzalavaRAnAmAtmaprItO kyaci",
    text_dev              = "अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि",
    samagra_slp1          = "aNgasya aSva-kzIra-vfza-lavaRAnAm AtmaprItO kyaci asuk At",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अश्व-क्षीर-वृष-लवणानाम् आत्मप्रीतौ क्यचि असुक् आत्",
    padaccheda_dev        = "अश्व-क्षीर-वृष-लवणानाम् आत्म-प्रीतौ क्यचि",
    why_dev               = "(सूत्रम् 7.1.51) अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
