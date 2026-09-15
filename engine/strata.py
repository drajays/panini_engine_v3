"""
engine/strata.py — असिद्धत्व as a visibility matrix, not a flag.

Ask it one question: **when rule A is being evaluated, can it see what rule B
did?** Three sūtras answer it, and the engine has been answering only part of
the first with a boolean (``state.tripadi_zone``):

    8.2.1  पूर्वत्रासिद्धम्      what a tripāḍī rule does is asiddha for
                                 everything earlier — including earlier
                                 tripāḍī rules, which is what stops
                                 8.2.66 (s → ru) and 8.3.34 (ru → s) from
                                 undoing each other forever
    6.4.22 असिद्धवदत्राभात्      inside 6.4.22–6.4.129 the rules are
                                 asiddhavat to one another
    6.1.86 षत्वतुकोरसिद्धः       the ekādeśa is asiddha for ṣatva and for tuk

The domains, their ranges and the authority for each range live in
``data/inputs/asiddha_strata.json`` — including a ``not_modelled`` list, so
what this matrix does *not* yet distinguish is written down rather than
implied (Art. 18).

This module decides nothing on its own: it is the model the gates and the
autonomous loop consult, and it can be asked to explain any answer.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

_DATA = Path(__file__).resolve().parent.parent / "data" / "inputs" / "asiddha_strata.json"


@dataclass(frozen=True)
class Visibility:
    """Whether one rule's work is visible to another, and on whose authority."""

    visible: bool
    by: str | None = None            # the sūtra that hides it
    reason_dev: str = ""

    def __bool__(self) -> bool:
        return self.visible


def _tuple(sutra_id: str) -> tuple[int, ...]:
    try:
        return tuple(int(part) for part in sutra_id.split("."))
    except ValueError:
        return (0, 0, 0)


@lru_cache(maxsize=1)
def domains() -> dict[str, dict[str, Any]]:
    return json.loads(_DATA.read_text(encoding="utf-8"))["domains"]


@lru_cache(maxsize=1)
def not_modelled() -> list[str]:
    return json.loads(_DATA.read_text(encoding="utf-8"))["not_modelled"]


def _in_range(sutra_id: str, domain: dict[str, Any]) -> bool:
    low, high = (_tuple(x) for x in domain["range"])
    return low <= _tuple(sutra_id) <= high


def in_tripadi(sutra_id: str) -> bool:
    return _in_range(sutra_id, domains()["tripadi"])


def visible(observer: str, effect_of: str) -> Visibility:
    """Can ``observer`` see what ``effect_of`` did?

    ``observer`` is the rule now being evaluated; ``effect_of`` is a rule that
    has already applied in this derivation.
    """
    if observer == effect_of:
        return Visibility(True)

    tripadi = domains()["tripadi"]
    if _in_range(effect_of, tripadi) and (
        not _in_range(observer, tripadi) or _tuple(observer) < _tuple(effect_of)
    ):
        return Visibility(False, tripadi["sutra"], tripadi["reading"])

    abhiya = domains()["abhiya"]
    if _in_range(observer, abhiya) and _in_range(effect_of, abhiya):
        return Visibility(False, abhiya["sutra"], abhiya["reading"])

    ekadesha = domains()["ekadesha_for_satva_tuk"]
    observers = {sid for group in ekadesha["observers"].values() for sid in group}
    if _in_range(effect_of, ekadesha) and observer in observers:
        return Visibility(False, ekadesha["sutra"], ekadesha["reading"])

    return Visibility(True)


def explain(observer: str, effect_of: str) -> str:
    verdict = visible(observer, effect_of)
    if verdict.visible:
        return f"{observer} sees {effect_of}: no asiddha domain separates them."
    return (f"{observer} cannot see {effect_of} — {verdict.by} "
            f"{domains()[_domain_of(verdict.by)]['dev']}: {verdict.reason_dev}")


def _domain_of(sutra_id: str | None) -> str:
    for key, domain in domains().items():
        if domain["sutra"] == sutra_id:
            return key
    raise KeyError(sutra_id)
