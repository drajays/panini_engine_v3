"""
1.4.73  उपाजेऽन्वाजे  (upāje 'nvāje)  —  SAMJNA

The words "upāje" and "anvāje" (vocatives/forms related to certain compound
structures) get the gati-saṃjñā.  These are specialised Vedic/grammatical
items that occur as preverb-like elements in specific constructions.

v3: registers samjna_registry["gati_upaje_anvaje"] = frozenset({"upAje","anvAje"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_UPAJE_ANVAJE: frozenset[str] = frozenset({"upAje", "anvAje"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_upaje_anvaje") is None


def act(state: State) -> State:
    state.samjna_registry["gati_upaje_anvaje"] = _UPAJE_ANVAJE
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _UPAJE_ANVAJE
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.73",
    sutra_type=SutraType.SAMJNA,
    text_slp1="upAje 'nvAje",
    text_dev="उपाजेऽन्वाजे",
    padaccheda_dev="उपाजे / अन्वाजे",
    why_dev="'उपाजे' 'अन्वाजे' इत्येते गति-संज्ञकौ — गति-सेटे योज्येते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
