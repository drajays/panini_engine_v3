"""
1.4.69  अच्छ गत्यर्थवदेषु  (accha gatyartha-vadeṣu)  —  SAMJNA

The word "accha" gets the gati-saṃjñā when used before roots that mean
going (gati-artha) or roots of saying (vad-ādi).
E.g., "accha-gam" (to go towards), "accha-vad" (to address).

v3: registers samjna_registry["gati_accha"] = frozenset({"acCa"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_ACCHA: frozenset[str] = frozenset({"acCa"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_accha") is None


def act(state: State) -> State:
    state.samjna_registry["gati_accha"] = _ACCHA
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _ACCHA
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.69",
    sutra_type=SutraType.SAMJNA,
    text_slp1="acCa gatyarTavadezu",
    text_dev="अच्छ गत्यर्थवदेषु",
    padaccheda_dev="अच्छ / गति-अर्थ-वदेषु",
    why_dev="गत्यर्थवदेषु 'अच्छ' शब्दो गति-संज्ञकः — 'acCa' गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
