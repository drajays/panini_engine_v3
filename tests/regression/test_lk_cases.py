"""The LK case gate as part of the suite (CONSTITUTION Art. 16: a sūtra is invoked "by at least one derivation in the test suite").

Always: the committed verdicts (sig/lk_case_verdicts/) agree with the fixtures and with tools.lk_cases.grade — nobody edits a grade by hand.
With LK=1 (make lk-ledger, and the firing ledger run): every sūtra the gate grades confident or working is re-derived, and its fresh
grade may not fall below the committed one. Grades only rise; a fall is a regression, never a reason to edit the verdict.
"""
from __future__ import annotations

import os

import pytest

from tools import lk_cases

RANK = {"FAIL": 0, "NO_POSITIVE": 0, "UNRUNNABLE": 0, "working": 1, "confident": 2}
FIXTURES = lk_cases.load()
VERDICTS = lk_cases.verdicts()
HELD = sorted((s for s, v in VERDICTS.items() if RANK.get(v["grade"], 0) > 0), key=lk_cases._key)


def test_every_verdict_matches_its_fixture_and_its_grade():
    bad = []
    for sid, v in VERDICTS.items():
        cases = FIXTURES.get(sid)
        if cases is None or len(cases) != len(v["cases"]):
            bad.append(f"{sid}: {len(v['cases'])} verdict rows for {len(cases or [])} cases")
        elif lk_cases.grade(v["cases"], cases) != v["grade"]:
            bad.append(f"{sid}: stored {v['grade']} ≠ graded {lk_cases.grade(v['cases'], cases)}")
    assert not bad, "rerun `python3 -m tools.lk_cases run <ids>`:\n" + "\n".join(bad)


@pytest.mark.skipif(os.environ.get("LK") != "1", reason="slow: set LK=1 (make lk-ledger) to re-derive the held LK grades")
@pytest.mark.parametrize("sid", HELD)
def test_lk_grade_does_not_fall(sid):
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    typ = SUTRA_REGISTRY[sid].sutra_type.name
    rows = [lk_cases.check(sid, c, typ, mutate=False) for c in FIXTURES[sid]]
    fresh = lk_cases.grade(rows, FIXTURES[sid])
    assert RANK[fresh] >= RANK[VERDICTS[sid]["grade"]], f"{sid}: {VERDICTS[sid]['grade']} → {fresh}: " + "; ".join(
        r.get("why", "") for r in rows if r["result"] == "fail")
