"""Ekadesa (6.1.84-6.1.111) replaces BOTH pUrva and para sounds as one unit; 6.1.77 (iko yaN aci) does not.

Surface forms pass.  The trace/State property "one substitution whose sthanin spans both
terms" is a strict xfail: 6.1.87/88/101 put the substitute in Term 1 and delete the first
sound of Term 2, so no step record names the two-sound sthanin (SCHOLARS_FACTCHECK (a);
same weakness as Prasad ISCLS 2024 s.4.1).
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from pipelines.pada_samhita import join

CASES = [
    ("mahA", "ISvaraH", "maheSvaraH", "6.1.87", "e"),    # ad gunah
    ("eva", "aBirakzati", "evABirakzati", "6.1.101", "A"),  # akah savarne dirghah
    ("tava", "eva", "tavEva", "6.1.88", "E"),            # vrddhir eci
]
SPAN_KEYS = {"sthanin", "sthanin_span", "ekadesa_span", "replaced_span"}


def _applied(s):
    return [t["sutra_id"] for t in s.trace if t.get("status") == "APPLIED"]


def _step(s, sid):
    (st,) = [t for t in s.trace if t.get("status") == "APPLIED" and t["sutra_id"] == sid]
    return st


@pytest.mark.parametrize("l,r,want,sid,sub", CASES)
def test_surface_and_single_rule(l, r, want, sid, sub):
    s = join(l, r)
    assert s.flat_slp1() == want
    assert _applied(s) == [sid]


@pytest.mark.parametrize("l,r,want,sid,sub", CASES)
def test_two_sounds_become_one(l, r, want, sid, sub):
    """Characterisation: total sound count drops by exactly one (two sthanin -> one adesa)."""
    s = join(l, r)
    assert len(s.flat_slp1()) == len(l) + len(r) - 1
    tagged = [v for t in s.terms for v in t.varnas if f"origin:{sid}" in v.tags]
    assert len(tagged) == 1 and tagged[0].slp1 == sub


@pytest.mark.parametrize("l,r,want,sid,sub", CASES)
@pytest.mark.xfail(strict=True, reason=(
    "Representation weakness: act() writes the substitute into Term 1 and deletes the first "
    "varna of Term 2; the trace step carries only form_before/after + re-split parts, no "
    "sthanin span covering pUrva+para (1.1.52/6.1.84 'ekah pUrvaparayoh')."))
def test_trace_records_single_substitution_over_both_terms(l, r, want, sid, sub):
    assert SPAN_KEYS & set(_step(join(l, r), sid))


def test_iko_yan_aci_is_not_ekadesa():
    """6.1.77 substitutes only the first sound; the vowel of Term 2 survives untouched."""
    s = join("daDi", "atra")
    assert s.flat_slp1() == "daDyatra"
    assert _applied(s) == ["6.1.77"]
    assert len(s.flat_slp1()) == len("daDi") + len("atra")  # no sound lost
