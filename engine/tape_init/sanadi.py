"""engine/tape_init/sanadi.py — the request's vivakṣā (AMENDMENT 25) put on a tape that pipelines/cycle_loop.py built: a stem with its sup, from which kyac is taken (3.1.8, icCA)."""
from __future__ import annotations

from engine.state import State
from engine.vivaksha import set_vivaksha


def with_vivaksha(state: State, **vivaksha: str) -> State:
    set_vivaksha(state, **vivaksha)
    return state
