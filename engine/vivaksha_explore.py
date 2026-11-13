"""
engine/vivaksha_explore.py — AMENDMENT 30: explore every applicable meaning (probe and replay), outside the derivation.

A request is ``vivaksha={key: value | OPEN | DEFAULT}``. A value is fixed by the caller; ``OPEN`` asks to explore the key; ``DEFAULT`` (or
leaving the key out) is the key's unmarked value, which is "not set". The probe runs the derivation with every open key at its default and
records which keys a sūtra's ``vivaksita(...)`` asked about (engine.vivaksha.record_asked: a read-only trace). For each asked open key the
derivation is run again once per schema value of that key (plus the default); the value is placed on the tape at tape init by the entry
point itself (``set_vivaksha`` stays in engine/tape_init). Only asked keys are explored, never a product over the schema.

Each reading is a ``vikalpa.Branch`` whose ``choices`` begin with ``("vivaksha", key, value)`` entries, then the vibhāṣā choices.
A derivation that asks no open key is one ``vikalpa.explore`` of today's call: exactly today's branches.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any, Callable

from engine.vikalpa import Branch, explore
from engine.vivaksha import key_meta, record_asked, schema

OPEN = "OPEN"
DEFAULT = "DEFAULT"
MAX_RUNS = 256            # an auditable ceiling on replays, as vikalpa.MAX_OPTIONAL_RULES is for the vibhāṣā


def _check(request: dict[str, str], entry: str) -> None:
    for key, value in request.items():
        if key not in schema():
            raise ValueError(f"vivakṣā key {key!r} is not in data/inputs/vivaksha_schema.json")
        if value == OPEN:
            meta = key_meta(key)
            if meta["kind"] != "intent":
                raise ValueError(f"vivakṣā {key!r} is a context key: the caller supplies it, it is never OPEN")
            if entry not in meta["applies_to"]:
                raise ValueError(f"vivakṣā {key!r} does not apply to {entry} (applies_to {meta['applies_to']})")
        elif value != DEFAULT and value not in schema()[key]:
            raise ValueError(f"vivakṣā {key}={value!r} is not in data/inputs/vivaksha_schema.json")


def explore_vivaksha(run: Callable[[dict[str, str]], Any], request: dict[str, str] | None, entry: str) -> list[Branch]:
    """Every reading of ``run`` under the request. ``run(fixed)`` performs one derivation with those vivakṣā values on its tape."""
    from engine import scheduler

    request = dict(request or {})
    _check(request, entry)
    fixed = {k: v for k, v in request.items() if v not in (OPEN, DEFAULT)}
    opens = [k for k, v in request.items() if v == OPEN]
    scheduler._EFFECTIVE_MEMO.clear()       # a memoised cond answer would hide the question from the probe
    out: list[Branch] = []
    todo: list[dict[str, str | None]] = [{}]
    runs = 0
    while todo:
        assign = todo.pop(0)
        runs += 1
        if runs > MAX_RUNS:
            raise RuntimeError(f"vivakṣā exploration passed {MAX_RUNS} replays")
        chosen = {**fixed, **{k: v for k, v in assign.items() if v is not None}}
        with record_asked() as asked:
            branches = explore(lambda: run(chosen))
        fresh = [k for k in opens if k in asked and k not in assign]
        if fresh:
            key = fresh[0]
            todo[:0] = [{**assign, key: v} for v in (None, *schema()[key])]       # default first, then the schema's values
            continue
        tags = tuple(("vivaksha", k, v) for k, v in chosen.items())
        out += [replace(b, choices=tags + b.choices) for b in branches]
    return out


def derive_all(entry: str, *args: Any, vivaksha: dict[str, str] | None = None, **kw: Any) -> list[Branch]:
    """Every reading of a tiṅanta or kṛdanta cell. ``entry`` is "tinanta" (args of pipelines.tinanta.derive) or "krdanta" (args of
    pipelines.krdanta.derive_krdanta); the rest is that function's own."""
    if entry == "tinanta":
        from pipelines.tinanta import derive
        return explore_vivaksha(lambda fixed: derive(*args, vivaksha=fixed, **kw), vivaksha, entry)
    if entry == "krdanta":
        from pipelines.krdanta import derive_krdanta
        return explore_vivaksha(lambda fixed: derive_krdanta(*args, **kw, **fixed), vivaksha, entry)
    raise ValueError(f"entry must be 'tinanta' or 'krdanta', got {entry!r}")
