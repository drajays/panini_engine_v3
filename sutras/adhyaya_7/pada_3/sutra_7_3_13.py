"""
7.3.13  दिशोऽमद्राणाम्  —  VIDHI

Padaccheda: दिशः अमद्राणाम्

दिशोऽमद्राणाम् (7.3.13)
Pāṭha: ashtadhyayi.com data.txt row i=73013 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_13_diSomadrA_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.13", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'diSomadrARAm',
    text_dev              = 'दिशोऽमद्राणाम्',
    samagra_slp1          = "aNgasya uttarapadasya diSaH amadrARAm vfdDiH YRiti acaH tadDitezu AdeH SvAdeH janapadasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य दिशः अमद्राणाम् वृद्धिः ञ्णिति अचः तद्धितेषु आदेः श्वादेः जनपदस्य",
    padaccheda_dev        = "दिशः अमद्राणाम्",
    why_dev               = "(सूत्रम् 7.3.13) दिशोऽमद्राणाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
