"""
5.2.38  पुरुषहस्तिभ्यामण् च  —  VIDHI

Padaccheda: पुरुष-हस्तिभ्याम् अण् च

पुरुषहस्तिभ्यामण् च (5.2.38)
Pāṭha: ashtadhyayi.com data.txt row i=52038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_38_puruzahast_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.38", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puruzahastiByAmaR ca",
    text_dev              = "पुरुषहस्तिभ्यामण् च",
    samagra_slp1          = "tat asya iti pramARe puruzahastiByAM dvayasac-daGnac-mAtrac-aR ca ",
    samagra_dev           = "'तत् अस्य' (इति) प्रमाणे पुरुषहस्तिभ्यां द्वयसच्-दघ्नच्-मात्रच्-अण् च ।",
    padaccheda_dev        = "पुरुष-हस्तिभ्याम् अण् च",
    why_dev               = "(सूत्रम् 5.2.38) पुरुषहस्तिभ्यामण् च।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
