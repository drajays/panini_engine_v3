"""
tests/regression/test_shabda_paradigms.py
─────────────────────────────────────────

Attested śabda-rūpa tables (ashtadhyayi.com, vendored under
``data/reference/shabda_gold/``) as a gate. Art. 19: the forms are not ours to
judge, and this is a second opinion independent of Vidyut.

All thirteen paradigms are complete: **312/312 cells**. नदी was 17/24 when the
tables were first vendored on 2026-09-15; the seven missing cells were the ङित्
block (7.3.112 आण् नद्याः · 7.3.116 ङेराम् · 7.3.107 अम्बार्थनद्योर्ह्रस्वः),
7.1.54 नुट्, and a 6.1.103 that ignored its own पुंसि. They were implemented the
same day, and this test is what keeps them.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401

from tools.shabda_table import paradigms, table

# Empty, and it should stay that way: a cell that stops deriving is a
# regression, not a new entry here.
KNOWN_GAPS: dict[str, set[str]] = {}


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


def test_the_nadi_paradigm_is_complete():
    """नदी was the ī-stem gap; all 24 cells now match the attested table."""
    result = table("nadI")
    assert result["misses"] == [], result["misses"]
    assert result["hits"] == 24


def test_no_paradigm_carries_an_allowance():
    """KNOWN_GAPS is empty. Adding to it would be how 312/312 quietly rots."""
    assert KNOWN_GAPS == {}


def test_every_vendored_paradigm_carries_its_provenance():
    import json
    from tools.shabda_table import GOLD_DIR

    for path in GOLD_DIR.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["_provenance"]["source_repo"] == "github.com/ashtadhyayi-com/data"
        assert len(data["cells"]) == 24
