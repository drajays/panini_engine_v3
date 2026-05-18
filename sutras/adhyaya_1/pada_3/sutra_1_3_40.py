"""
1.3.40  आङ उद्गमने  —  VIDHI

*Padaccheda:* *āṅ* (पञ्चमी-एकवचन) / *udgamane* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] in the sense of udgamana (rising/emerging) with
the prefix ā (āṅ). For example: ākramate — he rises/emerges.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries the tag "A_prefix" and the tag "udgamana_usage",
and (c) the idempotency stamp "Atmanepada_1_3_40" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_40_A_udgamana"
_STAMP_KEY    = "Atmanepada_1_3_40"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "A_prefix" in t.tags
        and "udgamana_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.40",
    sutra_type=SutraType.VIDHI,
    text_slp1="AV udgamane",
    text_dev="आङ उद्गमने",
    padaccheda_dev="आङ (पञ्चमी-एकवचन) / उद्गमने (सप्तमी-एकवचन)",
    why_dev=(
        "आ-पूर्वकस्य धातोः उद्गमन-अर्थे प्रयोगे आत्मनेपदम् — "
        "ākramate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
