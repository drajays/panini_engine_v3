"""
tests/unit/test_practice_sentences.py
─────────────────────────────────────

Sentence practice (Subhastini's वाक्याभ्यासः) is built only from Saṃsādhanī's analysis and the engine's
verdicts — no model. These tests lock the written-out hint and, when the e-reader snapshot is present, the
record a drill is made from.
"""
from __future__ import annotations

import pytest

from tools import practice_sentences as P
from tools import samsaadhanii_reader as rd


@pytest.mark.parametrize("tag, out", [
    ("क्रीड्1{कर्तरि;लोट्;म;एक;परस्मैपदी;भ्वादिः}", "क्रीड् · कर्तरि · लोट् · मध्यमपुरुषः · एकवचनम् · परस्मैपदम् · भ्वादिः"),
    ("अक्ष{पुं;3;बहु}", "अक्ष · पुंलिङ्गम् · तृतीया · बहुवचनम्"),
    ("(युष्मद्{सर्वनाम;1;एक})", "युष्मद् · प्रथमा · एकवचनम्"),
    ("मा{अव्य}", "मा · अव्ययम्"),
])
def test_hint_writes_the_tag_out(tag, out):
    assert P.hint(tag) == out


_HAVE = rd.available() and any(u["id"] == P.UNIT for u in rd.catalogue())


@pytest.mark.skipif(not _HAVE, reason="run: python3 -m tools.fetch_samsaadhanii_ereaders --all")
def test_sentence_record_for_drills():
    s = P.sentence("01", "001")
    assert s["text"] == "अक्षैः मा क्रीड।"
    by = {w["form"]: w for w in s["words"]}
    assert by["त्वम्"]["implied"] and by["त्वम्"]["role"] == "कर्ता"
    assert by["अक्षैः"]["role"] == "करणम्" and by["अक्षैः"]["engine"]["status"] == "derived"
    assert [x["id"] for x in by["अक्षैः"]["role_sutras"]] == ["1.4.42", "2.3.18"]
    assert by["क्रीड"]["hint"].startswith("क्रीड् · कर्तरि · लोट्")


@pytest.mark.skipif(not _HAVE, reason="e-reader snapshot missing")
def test_sets_cover_the_thousand():
    assert sum(s["count"] for s in P.sets()) >= 990
