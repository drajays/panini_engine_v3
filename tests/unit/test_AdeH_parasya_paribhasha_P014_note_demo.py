"""Unit tests for ``pipelines/AdeH_parasya_paribhasha_P014_note_demo.py`` (**P014**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.AdeH_parasya_paribhasha_P014_note_demo import (
    derive_AdeH_parasya_paribhasha_P014_note,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P014_applies_1_1_54_and_installs_gate():
    s = derive_AdeH_parasya_paribhasha_P014_note()
    ids = _trace_ids(s)
    assert "1.1.54" in ids
    assert s.paribhasha_gates.get("1.1.54_adesh_parasya", {}).get("mode") == "parasya"

