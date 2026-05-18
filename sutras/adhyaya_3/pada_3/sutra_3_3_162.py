"""
3.3.162  लोट् च  —  VIDHI (narrow: loṭ lakāra attachment)

Two operational paths:
  1. ``P031_3_3_162_loT_adhikara_arm``: legacy P031 adhikāra push.
  2. ``3_3_162_loT_arm``: glass-box loṭ pipeline — fires as a trace marker;
     the loT placeholder Term is appended inline in the calling pipeline
     (following the same pattern as 3.3.13 for lṛṭ).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.meta.get("3_3_162_loT_arm"):
        return not state.meta.get("3_3_162_loT_done")
    if not state.meta.get("P031_3_3_162_loT_adhikara_arm"):
        return False
    return not any(e.get("id") == "3.3.162" for e in state.adhikara_stack)


def act(state: State) -> State:
    if state.meta.get("3_3_162_loT_arm"):
        state.meta["3_3_162_loT_done"] = True
        state.meta.pop("3_3_162_loT_arm", None)
        return state
    state.adhikara_stack.append({
        "id": "3.3.162",
        "scope_end": "3.3.162",
        "text_dev": "लोट् च",
    })
    state.meta.pop("P031_3_3_162_loT_adhikara_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.162",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="loT ca",
    text_dev="लोट् च",
    padaccheda_dev="लोट् / च",
    why_dev="आज्ञार्थे धातोः लोट्-लकारः (आज्ञा/अनुज्ञा/प्रार्थना-पक्षे)।",
    anuvritti_from=("3.3.161",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
