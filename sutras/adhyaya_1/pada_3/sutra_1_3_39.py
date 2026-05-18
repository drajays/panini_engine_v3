"""
1.3.39  उपपराभ्याम्  —  VIDHI

*Padaccheda:* *upa-parābhyām* (पञ्चमी-द्विवचन).

*Anuvṛtti:* ātmanepada from 1.3.38; kram continues.

*Content:* [Ātmanepada] for [certain roots] preceded by upa or parā.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries the tag "upa_prefix" or the tag "parA_prefix", and
(c) the idempotency stamp "Atmanepada_1_3_39" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_39_upa_parA"
_STAMP_KEY    = "Atmanepada_1_3_39"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and ("upa_prefix" in t.tags or "parA_prefix" in t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.39",
    sutra_type=SutraType.VIDHI,
    text_slp1="upaparAByAm",
    text_dev="उपपराभ्याम्",
    padaccheda_dev="उप-पराभ्याम् (पञ्चमी-द्विवचन)",
    why_dev=(
        "उप-पूर्वकस्य वा परा-पूर्वकस्य धातोः प्रयोगे आत्मनेपदम् — "
        "upakramate, parākramate इत्यादि; "
        "१.३.३८ इत्यतः अनुवर्तते।"
    ),
    anuvritti_from=("1.3.38",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
