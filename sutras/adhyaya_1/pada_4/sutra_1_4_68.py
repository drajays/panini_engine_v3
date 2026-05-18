"""
1.4.68  अस्तं च  (astaṃ ca)  —  SAMJNA

The word "astam" also gets the gati-saṃjñā.
E.g., "astam-ita" (set, as in the sun), "astam-gam" (to go to setting).
The word "astam" (the western mountain where the sun sets) functions as a gati
when compounded with roots of motion.

v3: registers samjna_registry["gati_astam"] = frozenset({"astam"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_ASTAM: frozenset[str] = frozenset({"astam"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_astam") is None


def act(state: State) -> State:
    state.samjna_registry["gati_astam"] = _ASTAM
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _ASTAM
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.68",
    sutra_type=SutraType.SAMJNA,
    text_slp1="astaM ca",
    text_dev="अस्तं च",
    padaccheda_dev="अस्तम् / च",
    why_dev="'अस्तम्' अपि गति-संज्ञकम् — 'astam' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60", "1.4.67"),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
