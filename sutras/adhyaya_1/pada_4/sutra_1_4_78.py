"""
1.4.78  प्राध्वं बन्धने  (prādhvaṃ bandhane)  —  SAMJNA

The word "prādhvam" gets the gati-saṃjñā when used in the sense of
bandhana (binding / fastening).

v3: registers samjna_registry["gati_pradhvam_bandhane"] = frozenset({"prADvam"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_PRADHVAM: frozenset[str] = frozenset({"prADvam"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_pradhvam_bandhane") is None


def act(state: State) -> State:
    state.samjna_registry["gati_pradhvam_bandhane"] = _PRADHVAM
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _PRADHVAM
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.78",
    sutra_type=SutraType.SAMJNA,
    text_slp1="prADvaM banDane",
    text_dev="प्राध्वं बन्धने",
    padaccheda_dev="प्राध्वम् / बन्धने",
    why_dev="बन्धने 'प्राध्वम्' गति-संज्ञकम् — गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
