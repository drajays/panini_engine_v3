"""
3.2.16  चरेष्टः  —  VIDHI (narrow: corrected-v2 **P005-A** *kurucarī*)

*Śāstra (laghu):* after *√car* in an *upapada* frame, the *kṛt* **ṭa** (*ṭ*) is
introduced.

Engine: armed ``corrected_v2_P005_A_3_2_16_arm`` — insert **wa** (ट् + अ) after the
``car`` *dhātu* ``Term`` as a ``kṛt`` *pratyaya* (SLP1 ``w`` = ट्).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_META_ARM = "corrected_v2_P005_A_3_2_16_arm"


def _car_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "car":
            continue
        return i
    return None


def cond(state: State) -> bool:
    i = _car_index(state)
    if i is None:
        return False
    if i + 1 < len(state.terms):
        nxt = state.terms[i + 1]
        if "krt" in nxt.tags and (nxt.meta.get("upadesha_slp1") or "").strip() == "wa":
            return False
    return True


def act(state: State) -> State:
    i = _car_index(state)
    if i is None:
        return state
    ta = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("wa")),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": "wa"},
    )
    state.terms.insert(i + 1, ta)
    state.samjna_registry["3.2.16_P005_A_wa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.16",
    sutra_type=SutraType.VIDHI,
    text_slp1="carezWaH",
    text_dev="चरेष्टः",
    padaccheda_dev="चरेः / टः",
    why_dev="उपपदे चरः परः टः कृत् (प००५-अ)।",
    anuvritti_from=("3.1.25",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
