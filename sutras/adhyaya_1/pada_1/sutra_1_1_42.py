"""
1.1.42  शि सर्वनामस्थानम्  —  SAMJNA

Operational role (v3.6):
  - If a sup-pratyaya has upadeśa identity 'Si' (शि),
    tag it as `sarvanamasthana`.

This enables 7.1.72 / 6.4.8 style operations to key off a technical
term rather than paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _eligible(state: State):
    for t in state.terms:
        if "sup" not in t.tags:
            continue
        if t.meta.get("upadesha_slp1") != "Si":
            continue
        if "sarvanamasthana" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("sarvanamasthana")
    state.samjna_registry["sarvanamasthana_shi"] = frozenset({"Si"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.42",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "Si sarvanAmasthAnam",
    text_dev       = "शि सर्वनामस्थानम्",
    padaccheda_dev = "शि सर्वनामस्थानम्",
    why_dev        = "शि-प्रत्ययः सर्वनामस्थान-संज्ञकः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

