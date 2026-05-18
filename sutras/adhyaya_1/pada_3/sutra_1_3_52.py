"""
1.3.52  समः प्रतिज्ञाने  —  VIDHI

*Padaccheda:* *samaḥ* (पञ्चमी-एकवचन) / *pratijñāne* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada applies] after the prefix sam in the sense of
pratijñāna (making a promise/vow, acknowledging/assenting). When any root
preceded by sam is used in the sense of promising or declaring/assenting,
ātmanepada is mandated. For example: sampratijānīte (he promises/assents).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_1_3_52" is absent, and (c) a dhātu Term
carries the tag "sam_prefix" and also the tag "pratijYAna_usage" (indicating
the promise/assent sense).
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_52_sam_pratijYAna"
_STAMP_KEY    = "Atmanepada_1_3_52"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "sam_prefix" in t.tags
        and "pratijYAna_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.52",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="samaH pratijYAne",
    text_dev="समः प्रतिज्ञाने",
    padaccheda_dev="समः (पञ्चमी-एकवचन) / प्रतिज्ञाने (सप्तमी-एकवचन)",
    why_dev=(
        "सम्-पूर्वकस्य धातोः प्रतिज्ञान-अर्थे आत्मनेपदम् — "
        "saMpratijAnIte इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
