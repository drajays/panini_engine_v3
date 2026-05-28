"""
4.4.91  नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु  —  VIDHI

Padaccheda: नौ-वयो-धर्म-विष-मूल-मूल-सीता-तुलाभ्यः तार्य-तुल्य-प्राप्य-वध्य-आनाम्य-सम-समित-सम्मितेषु

नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु (4.4.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_91_nOvayoDarm_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.91", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nOvayoDarmavizamUlamUlasItAtulAByastAryatulyaprApyavaDyAnAmyasamasamitasammitezu",
    text_dev              = "नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु",
    padaccheda_dev        = "नौ-वयो-धर्म-विष-मूल-मूल-सीता-तुलाभ्यः तार्य-तुल्य-प्राप्य-वध्य-आनाम्य-सम-समित-सम्मितेषु",
    why_dev               = "(सूत्रम् 4.4.91) नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
