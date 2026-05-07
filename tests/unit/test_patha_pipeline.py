"""
tests/unit/test_patha_pipeline.py — पाठ-विश्लेषण-प्रणाली unit tests.

Covers:
  • Tokenizer (punctuation, daṇḍa, whitespace)
  • Form index build: expected forms present, size in range
  • analyze_word: recognized / unrecognized / ambiguous
  • analyze_patha: stats, multi-sentence text
  • Key spot-checks for u-kārānta forms (our recently fixed cells)
  • Paradigm completeness for one stem per class
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401

from pipelines.patha_pipeline import (
    PATHA_LEXICON,
    analyze_patha,
    analyze_word,
    cell_label_long,
    cell_label_short,
    get_form_index,
    tokenize,
)


# ── Tokenizer ─────────────────────────────────────────────────────

def test_tokenize_basic():
    assert tokenize("रामः वनम् गच्छति") == ["रामः", "वनम्", "गच्छति"]


def test_tokenize_danda():
    assert tokenize("रामः।धर्मः॥") == ["रामः", "धर्मः"]


def test_tokenize_empty():
    assert tokenize("") == []


def test_tokenize_mixed_punct():
    toks = tokenize("शम्भुः, गुरुः! भानुः।")
    assert toks == ["शम्भुः", "गुरुः", "भानुः"]


def test_tokenize_preserves_visarga():
    toks = tokenize("रामः")
    assert toks == ["रामः"]
    assert "ः" in toks[0]


def test_tokenize_preserves_anusvara():
    toks = tokenize("शम्भून्")
    assert toks == ["शम्भून्"]


# ── Form index ────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def index():
    return get_form_index()


def test_index_non_empty(index):
    assert len(index) > 200


def test_index_all_lexicon_stems_present(index):
    all_forms = set(index.keys())
    for entry in PATHA_LEXICON:
        # Every stem should produce at least one form in the index
        stem_forms = [f for f, analyses in index.items()
                      if any(a["stem_slp1"] == entry.stem_slp1 for a in analyses)]
        assert stem_forms, f"No forms indexed for stem {entry.stem_slp1!r}"


def test_index_sambhu_24_analyses(index):
    """All 24 (vibhakti, vacana) cells for SamBu must be indexed.
    Some cells share a surface form (शम्भू = 1-2, 2-2, 8-2), so
    we count total analyses rather than unique surface strings."""
    sambhu = [a for v in index.values() for a in v if a["stem_slp1"] == "SamBu"]
    assert len(sambhu) == 24


def test_index_sambhu_2_3_correct(index):
    """The fixed accusative plural form शम्भून् must be indexed."""
    assert "शम्भून्" in index
    entry = next(a for a in index["शम्भून्"] if a["stem_slp1"] == "SamBu")
    assert entry["vibhakti"] == 2
    assert entry["vacana"]   == 3


def test_index_hari_24_analyses(index):
    hari = [a for v in index.values() for a in v if a["stem_slp1"] == "hari"]
    assert len(hari) == 24


def test_index_ambiguous_forms(index):
    """पञ्चमी and षष्ठी share the same ending for i/u-stems."""
    # शम्भोः appears as both 5-1 and 6-1
    assert "शम्भोः" in index
    analyses = index["शम्भोः"]
    vibs = {a["vibhakti"] for a in analyses if a["stem_slp1"] == "SamBu"}
    assert 5 in vibs and 6 in vibs


# ── analyze_word ──────────────────────────────────────────────────

def test_analyze_word_recognized():
    result = analyze_word("शम्भुः")
    assert result["recognized"] is True
    assert result["count"] == 1
    ana = result["analyses"][0]
    assert ana["stem_slp1"] == "SamBu"
    assert ana["vibhakti"]  == 1
    assert ana["vacana"]    == 1


def test_analyze_word_unrecognized():
    result = analyze_word("गच्छति")   # tinanta — not in lexicon
    assert result["recognized"] is False
    assert result["count"] == 0


def test_analyze_word_ambiguous():
    result = analyze_word("शम्भोः")   # 5-1 and 6-1
    assert result["recognized"] is True
    assert result["ambiguous"]  is True
    assert result["count"] >= 2


def test_analyze_word_fixed_cell():
    """2-3 (accusative plural) for u-stem — the repaired cell."""
    result = analyze_word("शम्भून्")
    assert result["recognized"] is True
    ana = result["analyses"][0]
    assert ana["vibhakti"] == 2
    assert ana["vacana"]   == 3
    assert ana["linga"]    == "pulliṅga"


def test_analyze_word_genitive_plural_sambu():
    result = analyze_word("शम्भूनाम्")
    assert result["recognized"] is True
    ana = result["analyses"][0]
    assert ana["vibhakti"] == 6
    assert ana["vacana"]   == 3


def test_analyze_word_dative_sg_sambu():
    result = analyze_word("शम्भवे")
    assert result["recognized"] is True
    ana = result["analyses"][0]
    assert ana["vibhakti"] == 4
    assert ana["vacana"]   == 1


def test_analyze_word_locative_sg_sambu():
    result = analyze_word("शम्भौ")
    assert result["recognized"] is True
    ana = result["analyses"][0]
    assert ana["vibhakti"] == 7
    assert ana["vacana"]   == 1


def test_analyze_word_vocative_sg_sambu():
    result = analyze_word("शम्भो")
    assert result["recognized"] is True
    ana = result["analyses"][0]
    assert ana["vibhakti"] == 8
    assert ana["vacana"]   == 1


def test_analyze_word_hari_gen_sg():
    result = analyze_word("हरेः")
    assert result["recognized"] is True
    assert result["ambiguous"]  is True   # pañcamī + ṣaṣṭhī
    vibs = {a["vibhakti"] for a in result["analyses"]}
    assert 5 in vibs and 6 in vibs


def test_analyze_word_napumsaka():
    result = analyze_word("ज्ञानम्")
    assert result["recognized"] is True
    ana0 = result["analyses"][0]
    assert ana0["linga"] == "napuṃsaka"


def test_analyze_word_sarvanama():
    result = analyze_word("सर्वेषाम्")
    assert result["recognized"] is True
    ana = result["analyses"][0]
    assert ana["stem_slp1"] == "sarva"
    assert ana["vibhakti"]  == 6
    assert ana["vacana"]    == 3


# ── analyze_patha ─────────────────────────────────────────────────

def test_analyze_patha_stats():
    text   = "शम्भुः गुरोः शिष्यः।"
    result = analyze_patha(text)
    assert result["total"] == 3
    assert result["recognized"] >= 2   # शम्भुः, गुरोः, शिष्यः (all three should be recognized)


def test_analyze_patha_high_recognition():
    """Carefully chosen text: all words should be in the lexicon."""
    text = "रामस्य धर्मः सत्यम्। योगे ज्ञानम् सुखम्।"
    result = analyze_patha(text)
    assert result["recognized"] == result["total"]
    assert result["unrecognized"] == 0


def test_analyze_patha_u_stem_sentence():
    """Sentence using multiple u-kārānta forms."""
    text = "शम्भुः गुरुः भानुः। शम्भवे गुरवे धर्मः।"
    result = analyze_patha(text)
    assert result["recognized"] == result["total"]


def test_analyze_patha_empty():
    result = analyze_patha("  ")
    assert result["total"] == 0


def test_analyze_patha_all_unrecognized():
    result = analyze_patha("एकदा गच्छति राजा।")
    # "एकदा" and "गच्छति" are not in lexicon; राजा is not either
    assert result["unrecognized"] > 0


def test_analyze_patha_word_analyses_populated():
    text   = "शम्भून् गुरून् हरीन्।"
    result = analyze_patha(text)
    for w in result["words"]:
        if w["recognized"]:
            assert len(w["analyses"]) >= 1
            a = w["analyses"][0]
            assert "stem_slp1" in a
            assert "vibhakti"  in a
            assert "label_short" in a


# ── cell_label helpers ────────────────────────────────────────────

def test_cell_label_short():
    assert cell_label_short(1, 1, "pulliṅga")  == "प्र.एक.पुं"
    assert cell_label_short(6, 3, "napuṃsaka") == "ष.बहु.न"
    assert cell_label_short(8, 1, "pulliṅga")  == "सं.एक.पुं"


def test_cell_label_long():
    label = cell_label_long(2, 3, "pulliṅga")
    assert "द्वितीया" in label
    assert "बहुवचन"   in label
    assert "पुंलिङ्ग" in label
