"""
8.2.26  झलो झलि  —  VIDHI (narrow: P033 *ghas*+*ta* span)

Teaching JSON **P033** step 8: in a *jhal*+*jhal* contact, the first *jhal* is *lopa*
when the second is *jhal* — here **s** (first) between **G** and **t** drops,
yielding **Gta**.

Arms: ``state.meta['P033_8_2_26_jhalo_jhali_arm']``; Tripāḍī zone; single *pada*
with flat ``Gsta``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _flat_pada(state: State) -> str:
    if len(state.terms) != 1 or "pada" not in state.terms[0].tags:
        return ""
    return "".join(v.slp1 for v in state.terms[0].varnas)


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    if not state.meta.get("P033_8_2_26_jhalo_jhali_arm"):
        return False
    if state.terms[0].meta.get("P033_8_2_26_done"):
        return False
    return _flat_pada(state) == "Gsta"


def act(state: State) -> State:
    if not cond(state):
        return state
    t = state.terms[0]
    vs = t.varnas
    if (
        len(vs) >= 4
        and vs[0].slp1 == "G"
        and vs[1].slp1 == "s"
        and vs[2].slp1 == "t"
        and vs[3].slp1 == "a"
    ):
        del t.varnas[1]
    t.meta["P033_8_2_26_done"] = True
    state.meta.pop("P033_8_2_26_jhalo_jhali_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.26",
    sutra_type=SutraType.VIDHI,
    text_slp1="jhalo Jhali",
    text_dev="झलो झलि",
    padaccheda_dev="झलः / झलि",
    why_dev="झलो झलि परे लोपः — प०३३ (घ्स्-त-)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
