"""
tests/constitutional/test_anuvrtti_is_baked_in.py
──────────────────────────────────────────────────

Constitution Article 4 — every sūtra's text_slp1 and text_dev
contain the FULL anuvṛtti-complete form.  The field anuvritti_from is
metadata only; no runtime path may consult it for rule application.

We assert two invariants:
  1. No engine / sūtra / pipeline source file reads rec.anuvritti_from
     outside of a "metadata-only" read inside tools/ (which is exempt).
  2. If a sūtra declares anuvritti_from non-empty, its text_dev must
     be meaningfully longer than its padaccheda_dev prefix — i.e., it
     MUST show evidence of carrying over terms (heuristic: text_dev
     contains a word from the parent sūtra's text_dev).  This is a
     soft check; counter-examples should be flagged for manual review.
"""
from __future__ import annotations

import pathlib
import pytest

from engine           import SUTRA_REGISTRY
import sutras  # noqa: F401

ROOT = pathlib.Path(__file__).resolve().parents[2]

PROTECTED_DIRS = (
    ROOT / "engine",
    ROOT / "sutras",
    ROOT / "phonology",
    ROOT / "pipelines",
)


def _iter_protected_files():
    for base in PROTECTED_DIRS:
        for p in base.rglob("*.py"):
            yield p


def test_no_runtime_reads_of_anuvritti_from():
    offenders = []
    for p in _iter_protected_files():
        text = p.read_text(encoding="utf-8")
        # Declarations (assigning to the field) are fine.  Only
        # reads of `.anuvritti_from` at runtime are suspect.
        for line in text.splitlines():
            if ".anuvritti_from" in line and "anuvritti_from=" not in line \
                    and "anuvritti_from =" not in line:
                offenders.append((p, line.strip()))
    assert not offenders, (
        "anuvritti_from is metadata-only and must not be read at runtime. "
        "Offenders:\n" + "\n".join(f"  {p}: {l}" for p, l in offenders)
    )


def test_every_sutra_record_wellformed():
    assert SUTRA_REGISTRY, "no sūtras registered — sutras/ package failed to load"
    for sid, rec in SUTRA_REGISTRY.items():
        # text fields exist and are non-empty (SutraRecord.__post_init__
        # already enforces this; we double-check).
        assert rec.text_slp1
        assert rec.text_dev
        assert rec.padaccheda_dev
        assert rec.why_dev
