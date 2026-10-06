"""Unit tests for 1.2.3 विभाषोर्णोः — ऊर्णु (upadeśa UrRuY) luṭ 3sg, the iṭ-ādi
pratyaya optionally ṅit-vat (no guṇa).

Kāśikā: "ऊर्णुञ् आच्छादने, अस्मात् परः इडादिः प्रत्ययो विभाषा ङित्वद् भवति।
प्रोर्णुविता। प्रोर्णविता।" (docs/PARKED_ISSUES_RESOLVED.md item e).

Scope note: the ṅit branch here correctly blocks guṇa (7.3.84 SKIPPED) and
matches the engine's existing vibhāṣā-fork plumbing (engine/vikalpa.py), but
the uvaṅ glide (6.4.77) does not yet reach this term in the luṭ tāsi
environment (a pre-existing 6.4.77 adjacency gap, not introduced here) — so
this test pins the morphological branch (guṇa blocked / not blocked), not the
fully sandhi'd प्रोर्णुविता surface. Tracked as a follow-up.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.vikalpa import choose, explore
from pipelines.dhatupatha import resolve_dhatu_identifier
from pipelines.tinanta import derive


def _row():
    return resolve_dhatu_identifier("UrRuY")


def _derive():
    return derive(_row()["id"], "luT", "kartari", 3, 1, pada="parasmai")


def test_1_2_3_declined_branch_keeps_guna() -> None:
    with choose({"1.2.3": False}):
        s = _derive()
    assert s.flat_slp1() == "UrRavitA"
    ids = [e.get("sutra_id") for e in s.trace]
    assert "7.3.84" in ids
    guna_step = next(e for e in s.trace if e.get("sutra_id") == "7.3.84")
    assert guna_step["status"] == "APPLIED"


def test_1_2_3_applied_branch_blocks_guna() -> None:
    with choose({"1.2.3": True}):
        s = _derive()
    guna_step = next(e for e in s.trace if e.get("sutra_id") == "7.3.84")
    assert guna_step["status"] == "SKIPPED"
    assert "UrRu" in s.flat_slp1()           # u retained, not guṇa-ed to o


def test_1_2_3_both_branches_are_distinct_and_explored() -> None:
    branches = explore(_derive)
    surfaces = {b.surface_slp1 for b in branches}
    assert len(branches) == 2
    assert "UrRavitA" in surfaces            # declined: guṇa, ऊर्णविता
    assert all(s.startswith("UrRu") for s in surfaces if s != "UrRavitA")
