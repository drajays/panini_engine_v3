"""
tests/regression/test_shabda_paradigms.py
─────────────────────────────────────────

Attested śabda-rūpa tables (ashtadhyayi.com, vendored under
``data/reference/shabda_gold/``) as a gate. Art. 19: the forms are not ours to
judge, and this is a second opinion independent of Vidyut.

Twelve of the thirteen paradigms are complete. नदी is not, and its seven cells
are named here rather than excluded — a known gap that must not grow, and that
should shrink.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401

from tools.shabda_table import paradigms, table

# नदी, 2026-09-15: the ī-stem cells that need 7.3.112 ṅit-ādeśa (ङे → यै),
# 7.1.54 nuṭ (नदीनाम्), 7.3.116/117 (नद्याम्) and the sambodhana 7.3.107.
KNOWN_GAPS = {"nadI": {"2-3", "4-1", "5-1", "6-1", "6-3", "7-1", "8-1"}}


@pytest.mark.parametrize("stem", sorted(paradigms()))
def test_paradigm_matches_the_attested_table(stem):
    result = table(stem)
    missed = {m["cell"] for m in result["misses"]}
    allowed = KNOWN_GAPS.get(stem, set())
    assert result["refused"] == 0, f"{stem}: the engine refused a cell"
    assert missed <= allowed, (
        f"{stem}: new cells disagree with the attested paradigm: "
        f"{sorted(missed - allowed)}"
    )


def test_the_known_gaps_do_not_quietly_disappear():
    """If नदी is fixed, this test should be updated — not the gap list padded."""
    missed = {m["cell"] for m in table("nadI")["misses"]}
    assert missed, "नदी now derives fully — remove it from KNOWN_GAPS"
    assert missed <= KNOWN_GAPS["nadI"]


def test_every_vendored_paradigm_carries_its_provenance():
    import json
    from tools.shabda_table import GOLD_DIR

    for path in GOLD_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["_provenance"]["source_repo"] == "github.com/ashtadhyayi-com/data"
        assert len(data["cells"]) == 24
