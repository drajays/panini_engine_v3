"""
6.1.93  ओमाङोश्च  —  ANUVADA (placeholder audit)

The JSON spine for ``split_prakriyas_11/P013.json`` includes **6.1.93** as a
no-op placeholder step.  This repository does not currently implement the full
6.1.93 sandhi family; for this demo we provide an **anuvāda audit step** that
records the invocation when recipe-armed.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_P013_6_1_93_arm"):
        return False
    if state.samjna_registry.get("6.1.93_om_angoH_placeholder_P013"):
        return False
    if not any("prakriya_P013_mAtApitarO_demo" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.samjna_registry["6.1.93_om_angoH_placeholder_P013"] = True
    state.meta.pop("prakriya_P013_6_1_93_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.93",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "om ANgoH ca",
    text_dev       = "ओमाङोश्च",
    padaccheda_dev = "ओम् / आङोः / च",
    why_dev        = "P013 JSON placeholder (no mutation in this narrow demo).",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

