"""
4.2.134  मनुष्यतत्स्थयोर्वुञ्  —  VIDHI

Padaccheda: मनुष्य-तत्स्थयोः वुञ्

मनुष्यतत्स्थयोर्वुञ् (4.2.134)
Pāṭha: ashtadhyayi.com data.txt row i=42134 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_134_manuzyatat_134"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.134", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "manuzyatatsTayorvuY",
    text_dev              = "मनुष्यतत्स्थयोर्वुञ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA manuzya-tat-sTayoH vuY kacCa-AdiByaH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा मनुष्य-तत्-स्थयोः वुञ् कच्छ-आदिभ्यः च",
    padaccheda_dev        = "मनुष्य-तत्स्थयोः वुञ्",
    why_dev               = "(सूत्रम् 4.2.134) मनुष्यतत्स्थयोर्वुञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
