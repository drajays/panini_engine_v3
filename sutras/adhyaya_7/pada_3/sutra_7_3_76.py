"""
7.3.76  क्रमः परस्मैपदेषु  —  VIDHI

क्रम् lengthens before a śit when a parasmaipada ending follows: क्रामति (but क्रमते).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import dhatu_before_sit
from engine.state import State
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _hit(state: State):
    i = dhatu_before_sit(state)
    if i is None or _stem(state.terms[i]) != "kram":
        return None
    return i if any("parasmaipada" in t.tags for t in state.terms[i + 1:]) else None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    t = state.terms[_hit(state)]
    t.varnas[2] = mk("A")
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.76",
    sutra_type=SutraType.VIDHI,
    text_slp1="kramaH parasmEpadezu",
    text_dev="क्रमः परस्मैपदेषु",
    padaccheda_dev="क्रमः परस्मैपदेषु",
    why_dev="क्रम्-धातोः दीर्घः शिति परस्मैपदे परे (क्रामति)।",
    anuvritti_from=("7.3.73",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
