"""
2.2.34  अल्पाच्तरम्  —  ANUVADA (narrow ordering note)

Śāstra: provides a default ordering preference among compound members.

Engine (narrow): for ``split_prakriyas_11/P013.json`` the JSON lists this as an
ordering step but also notes a special sanctioned reversal for the pair.
We therefore record only an **anuvāda audit step** when the recipe arms it,
without mutating the tape.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("2_2_34_dvandva_arm"):
        return False
    if state.samjna_registry.get("2.2.34_alpActaram"):
        return False
    return True


def act(state: State) -> State:
    state.samjna_registry["2.2.34_alpActaram"] = True
    state.meta.pop("2_2_34_dvandva_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.34",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "alpActaram",
    text_dev       = "अल्पाच्तरम्",
    padaccheda_dev = "अल्प-अच्-तरम्",
    why_dev        = "समासे पदक्रम-नियमः (narrow audit stamp for P013).",
    anuvritti_from = ("2.2.29",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

