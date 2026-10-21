"""
engine/tape_init/krdanta.py — kṛdanta start state: the tape plus the request's vivakṣā (AMENDMENT 25).

A kṛt affix is chosen by the meaning the speaker intends, never named by the request. The absolutive request is
3.4.21 समानकर्तृकयोः पूर्वकाले: the action is the earlier of two that share one agent (Kāśikā: भुक्त्वा व्रजति).
"""
from __future__ import annotations

from collections.abc import Iterable

from engine.state import State, Term
from engine.vivaksha import set_vivaksha

# 3.4.21: पूर्वकाले + समानकर्तृकयोः
PURVAKALA_SAMANAKARTRKA = {"kala": "pUrvakAla", "samAnakartfka": "samAnakartfka"}


def build_krdanta_state(terms: Iterable[Term], **vivaksha: str) -> State:
    """Start state for a kṛdanta: upasargas and dhātu as given, the intended meaning recorded."""
    state = State(terms=list(terms), meta={}, trace=[])
    set_vivaksha(state, **vivaksha)
    return state
