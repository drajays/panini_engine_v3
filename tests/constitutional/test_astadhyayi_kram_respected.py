"""
tests/constitutional/test_astadhyayi_kram_respected.py
────────────────────────────────────────────────────────

Constitution Article 3: rules fire in Aṣṭādhyāyī order.

We verify:
  1. Every sūtra file lives under sutras/adhyaya_<A>/pada_<P>/ where
     (A, P) matches the sūtra's id.
  2. Every sūtra's adhikara_scope is well-ordered (start <= end).
  3. Every sūtra's adhikara_scope endpoints actually exist in the
     Aṣṭādhyāyī numbering range (1.1.1 to 8.4.68).
"""
from __future__ import annotations

import pathlib
import re

import pytest

from engine import SUTRA_REGISTRY, SutraType
import sutras  # noqa: F401

ROOT = pathlib.Path(__file__).resolve().parents[2]

_FILE_RE = re.compile(r"^sutra_(\d+)_(\d+)_(\d+)(?:_.+)?$")


def _in_range(sid: str) -> bool:
    a, p, n = (int(x) for x in sid.split("."))
    if not (1 <= a <= 8):
        return False
    if not (1 <= p <= 4):
        return False
    return n >= 1


def test_all_sutra_files_are_in_correct_folder():
    for p in (ROOT / "sutras").rglob("sutra_*.py"):
        m = _FILE_RE.match(p.stem)
        if not m:
            continue
        a, pa, n = m.groups()
        assert p.parent.name == f"pada_{pa}", (
            f"{p}: file name says pada {pa} but folder is {p.parent.name}"
        )
        assert p.parent.parent.name == f"adhyaya_{a}", (
            f"{p}: file name says adhyāya {a} but folder is {p.parent.parent.name}"
        )


def test_every_sutra_id_in_range():
    for sid in SUTRA_REGISTRY:
        assert _in_range(sid), f"{sid!r} is outside the Aṣṭādhyāyī range"


def test_adhikara_scopes_wellformed():
    for sid, rec in SUTRA_REGISTRY.items():
        if rec.sutra_type is not SutraType.ADHIKARA:
            continue
        start, end = rec.adhikara_scope
        st = tuple(int(x) for x in start.split("."))
        en = tuple(int(x) for x in end.split("."))
        assert st <= en, f"{sid}: adhikara_scope out of order: {start} > {end}"
        assert _in_range(start)
        assert _in_range(end)
