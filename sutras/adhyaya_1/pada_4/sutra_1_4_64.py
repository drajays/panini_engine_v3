"""
1.4.64  भूषणेऽलम्  (bhūṣaṇe 'lam)  —  SAMJNA

The word "alam" gets the gati-saṃjñā when used in the sense of bhūṣaṇa
(ornament / decoration), e.g., "alam-kṛ" (to ornament).

v3: registers samjna_registry["gati_alam_bhusane"] = frozenset({"alam"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_ALAM: frozenset[str] = frozenset({"alam"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_alam_bhusane") is None


def act(state: State) -> State:
    state.samjna_registry["gati_alam_bhusane"] = _ALAM
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _ALAM
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.64",
    sutra_type=SutraType.SAMJNA,
    text_slp1="BUzaRe 'lam",
    text_dev="भूषणेऽलम्",
    padaccheda_dev="भूषणे / अलम्",
    why_dev="भूषणे 'अलम्' शब्दो गति-संज्ञकः — 'alam' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
