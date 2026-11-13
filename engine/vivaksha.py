"""
engine/vivaksha.py — AMENDMENT 25: the speaker's intended meaning as a closed, cited input.

The vocabulary is data/inputs/vivaksha_schema.json (tools/build_vivaksha_schema.py): every value is a meaning that a
sūtra itself names in its samagra text, with those sūtras listed. `set_vivaksha` is called only by engine/tape_init
from the request; a sūtra's cond() asks `vivaksita(state, key, value)` only for a value whose word form stands in its
own samagra (tests/constitutional/test_vivaksha_named_in_samagra.py).
"""
from __future__ import annotations

import json
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from functools import lru_cache
from pathlib import Path
from typing import Any

_SCHEMA = Path(__file__).resolve().parent.parent / "data" / "inputs" / "vivaksha_schema.json"


@lru_cache(maxsize=1)
def schema() -> dict[str, dict[str, Any]]:
    return json.loads(_SCHEMA.read_text(encoding="utf-8"))["keys"]


def forms(key: str, value: str) -> list[str]:
    """The samagra word forms in which Pāṇini states this meaning."""
    return schema()[key][value]["forms"]


def set_vivaksha(state: Any, **choices: Any) -> None:
    """Record the request's vivakṣā on the state (engine/tape_init only). Unknown keys or values are refused."""
    for key, value in choices.items():
        if value is None:
            continue
        if key not in schema() or value not in schema()[key]:
            raise ValueError(f"vivakṣā {key}={value!r} is not in data/inputs/vivaksha_schema.json")
        state.vivaksha[key] = value


def vivaksita(state: Any, key: str, value: str) -> bool:
    """Is this meaning intended? The only way a cond() may read the vivakṣā."""
    if key not in schema() or value not in schema()[key]:
        raise ValueError(f"vivakṣā {key}={value!r} is not in data/inputs/vivaksha_schema.json")
    asked = _ASKED.get()
    if asked is not None:           # AMENDMENT 30: a read-only trace for engine.vivaksha_explore; the answer is unchanged
        asked.add(key)
    return state.vivaksha.get(key) == value


# AMENDMENT 30 — what each key is (kind / default / applies_to / requires / glosses), and the read-only trace of the keys a derivation asked.
@lru_cache(maxsize=1)
def _meta() -> dict[str, dict[str, Any]]:
    return json.loads(_SCHEMA.read_text(encoding="utf-8"))["meta"]


def key_meta(key: str) -> dict[str, Any]:
    return _meta()[key]


_ASKED: ContextVar[set | None] = ContextVar("vivaksha_asked", default=None)


@contextmanager
def record_asked() -> Iterator[set]:
    """Collect the keys that vivaksita() is asked about while the block runs (engine.vivaksha_explore only). Read-only: no state is touched."""
    asked: set = set()
    token = _ASKED.set(asked)
    try:
        yield asked
    finally:
        _ASKED.reset(token)
