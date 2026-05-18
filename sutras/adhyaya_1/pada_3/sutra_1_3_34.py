"""
1.3.34  वेः शब्दकर्मणः  —  VIDHI

*Padaccheda:* *veḥ* (पञ्चमी-एकवचन) / *śabdakarmaṇaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for roots taking śabda (sound) as their karma
(object) when preceded by the prefix vi (e.g. viśabdate — he sounds forth).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries both the tag "vi_prefix" (encoding prefix vi) and
the tag "Sabda_karma_usage" (encoding the śabda-karma semantic context),
and (c) the idempotency stamp "Atmanepada_1_3_34" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_34_vi_Sabda_karma"
_STAMP_KEY    = "Atmanepada_1_3_34"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "vi_prefix" in t.tags
        and "Sabda_karma_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.34",
    sutra_type=SutraType.VIDHI,
    text_slp1="veH SabdakarmaRaH",
    text_dev="वेः शब्दकर्मणः",
    padaccheda_dev="वेः (पञ्चमी-एकवचन) / शब्दकर्मणः (षष्ठी-एकवचन)",
    why_dev=(
        "वि-पूर्वस्य शब्द-कर्मकस्य धातोः प्रयोगे आत्मनेपदम् — "
        "viśabdate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
