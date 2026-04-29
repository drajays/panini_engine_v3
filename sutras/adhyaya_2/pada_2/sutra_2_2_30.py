"""
2.2.30  उपसर्जनं पूर्वम्  —  VIDHI

Narrow v3 slice: in a samāsa, the upasarjana member is placed first.

Engine: reorder ``state.terms`` so that any term tagged ``upasarjana`` precedes
other samāsa members (stable among upasarjanas).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _has_move(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ups = [t for t in state.terms if "upasarjana" in t.tags]
    if not ups:
        return False
    # If first term is already an upasarjana, treat as done.
    return "upasarjana" not in state.terms[0].tags


def cond(state: State) -> bool:
    return _has_move(state)


def act(state: State) -> State:
    if not _has_move(state):
        return state
    ups = [t for t in state.terms if "upasarjana" in t.tags]
    rest = [t for t in state.terms if "upasarjana" not in t.tags]
    state.terms = ups + rest
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.30",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1      = "upasarjanaM pUrvam",
    text_dev       = "उपसर्जनं पूर्वम्",
    padaccheda_dev = "उपसर्जनम् / पूर्वम्",
    why_dev        = "समासे उपसर्जनस्य पूर्वनिपातः।",
    anuvritti_from = ("2.2.29",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

