"""
1.3.13  भावकर्मणोः  —  VIDHI

*Padaccheda:* *bhāvakarmaṇoḥ* (षष्ठी-द्विवचन) — "of bhāva and karman".

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* In bhāva (impersonal/passive) and karmaṇi (karma-oriented passive)
constructions, the verb takes ātmanepada endings.

*Engine:* cond checks that (a) pada is not already "Atmanepada" and (b) at least one
dhātu Term carries the tag "bhava_karma_usage" — set by the recipe to signal a
passive/impersonal derivation.  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_13_bhAva_karma_Atmanepada"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    return any(
        "dhatu" in t.tags and "bhava_karma_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.13",
    sutra_type=SutraType.VIDHI,
    text_slp1="BAvakarmaRoH",
    text_dev="भावकर्मणोः",
    padaccheda_dev="भाव-कर्मणोः (षष्ठी-द्विवचन)",
    why_dev=(
        "भावे कर्मणि च प्रयोगे धातोः आत्मनेपद-विभक्तयः भवन्ति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
