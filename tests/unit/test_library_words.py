"""/v1/library/words — Saṃsādhanī's word analysis with the engine's verdict per word (docs/INTEGRATION_CLIENTS.md)."""
from __future__ import annotations

import pytest

from tools import library_providers as lib
from tools import samsaadhanii_reader as rd

GITA = "scl:श्रीमद्भगवद्गीता"
pytestmark = pytest.mark.skipif(not rd.available(), reason="Saṃsādhanī e-reader snapshot not fetched")


def test_covers_reads_grouped_and_ranged_items():
    assert lib._covers("001_002_003") == {1, 2, 3}
    assert lib._covers("004-006") == {4, 5, 6}
    assert lib._covers("012") == {12}
    assert lib._covers("1.2") == set()


def test_words_at_finds_the_item_holding_a_numbered_verse():
    r = lib.words_at(GITA, 16, 2)
    assert (r["section"], r["item"]) == ("16", "001_002_003")
    assert r["attribution"] == rd.ATTRIBUTION


def test_every_word_carries_the_engine_verdict():
    r = lib.words_at(GITA, 16, 1)
    by = {w["word"]: w for w in r["words"]}
    assert by["भयम्"]["status"] == "derived" and by["भयम्"]["produced"] == "भयम्"
    assert by["भवन्ति"]["kind"] == "tinanta" and by["भवन्ति"]["status"] == "derived"
    assert by["च"]["status"] == "not_attempted"
    assert sum(w["status"] == "derived" for w in r["words"]) == r["counts"]["derived"]


def test_unknown_verse_and_wordless_provider_are_not_found():
    with pytest.raises(KeyError):
        lib.words_at(GITA, 16, 999)
    with pytest.raises(KeyError):
        lib.words("ac:ashtadhyayi", "1", "1")
