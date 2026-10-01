import pytest
from tools import kosha

pytestmark = pytest.mark.skipif(not kosha._ROOT.exists(), reason="kosha-master not present")


def test_svarga_synonym_and_headword():
    hits = kosha.lookup("स्वर्ग")
    assert hits
    assert any("नाक" in h["synonyms"] for h in hits)


def test_unknown_word_empty():
    assert kosha.lookup("ऽऽऽ") == []


def test_analyze_inflected_form_reaches_stem():
    r = kosha.analyze("स्वर्गः । नाकेन")
    assert [w["word"] for w in r] == ["स्वर्गः", "नाकेन"]
    assert r[0]["stem"] == "स्वर्ग" and r[0]["entries"]
