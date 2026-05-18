"""
1.4.70  अदोऽनुपदेशे  (ado 'nupadeśe)  —  SAMJNA

The word "adas" (that) gets the gati-saṃjñā when not used in formal
grammatical upadeśa (teaching/citation).  When "adas" functions as
a preverb-like element compounding with a root (not in its substantival
sense), it becomes a gati.

v3: registers samjna_registry["gati_adas_anupadesha"] = frozenset({"adas"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_ADAS: frozenset[str] = frozenset({"adas"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_adas_anupadesha") is None


def act(state: State) -> State:
    state.samjna_registry["gati_adas_anupadesha"] = _ADAS
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _ADAS
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.70",
    sutra_type=SutraType.SAMJNA,
    text_slp1="ado 'nupadeśe",
    text_dev="अदोऽनुपदेशे",
    padaccheda_dev="अदः / अनुपदेशे",
    why_dev="अनुपदेशे 'अदस्' गति-संज्ञकः — 'adas' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
