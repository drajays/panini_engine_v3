"""
tests/unit/test_samsaadhanii_reader.py
──────────────────────────────────────

The e-reader is tools-layer: Saṃsādhanī supplies a tagged hypothesis, the
engine judges it. These tests lock the tag parsers, the kāraka → sūtra map,
and (when the snapshot is present) one Gītā verse through analysis-by-synthesis.
"""
from __future__ import annotations

import pytest

from tools.samsaadhanii_reader import (
    ATTRIBUTION, RELATION_SUTRAS, available, export_rows, search, verse,
    vibhakti_check, _relation, _verse_spans,
)
from tools.samsaadhanii_tags import (
    classify_morph, parse_krdanta_tag, parse_subanta_tag, parse_tinanta_tag,
)


def test_tinanta_tag_round_trip_to_derive_inputs():
    c = parse_tinanta_tag("कृ3{कर्तरि;लङ्;प्र;बहु;आत्मनेपदी;डुकृञ्;तनादिः}")
    assert c.unresolved is None
    assert c.lakara == "laG" and c.prayoga == "kartari" and c.pada == "atmane"
    assert c.purusha == 3 and c.vacana == 3


def test_subanta_tag_reads_linga_vibhakti_vacana():
    c = parse_subanta_tag("क्षेत्र{नपुं;7;एक}")
    assert (c.linga, c.vibhakti, c.vacana) == ("napuṃsaka", 7, 1)
    assert c.unresolved is None


def test_krdanta_ktva_cites_3_4_21():
    c = parse_krdanta_tag("दृश्1{कृत्_प्रत्ययः:क्त्वा;दृशिँर्;भ्वादिः}")
    assert c.krt_dev == "क्त्वा" and c.vidhana_sutra == "3.4.21"


def test_classify_morph_kinds():
    assert classify_morph("कृ3{कर्तरि;लङ्;प्र;बहु;आत्मनेपदी;डुकृञ्;तनादिः}")[0] == "tinanta"
    assert classify_morph("क्षेत्र{नपुं;7;एक}")[0] == "subanta"
    assert classify_morph("च{अव्य}")[0] == "avyaya"
    assert classify_morph("दृश्1{कृत्_प्रत्ययः:क्त्वा;दृशिँर्;भ्वादिः}")[0] == "krdanta"
    assert classify_morph("धर्म")[0] == "samasa_member"


def test_karaka_label_maps_to_registry_sutra():
    rel = _relation("कर्ता,9.1")
    assert rel["key"] == "कर्ता"
    assert any(s["id"] == "1.4.54" for s in rel["sutras"])
    assert "1.4.54" in RELATION_SUTRAS["कर्ता"]


def test_abhihita_kartr_takes_prathama_by_2_3_46():
    word = {"kind": "subanta", "engine": {"inputs": {"vibhakti": 1}}}
    head = {"kind": "tinanta", "engine": {"inputs": {"prayoga": "kartari"}}}
    vc = vibhakti_check(_relation("कर्ता,9.1"), word, head)
    assert vc["ok"] and vc["sutra"]["id"] == "2.3.46"


def test_verse_spans_make_sandhied_words_clickable():
    sents = [{"words": [
        {"sandhied_word": "धर्मक्षेत्रे", "anvaya_no": "1.1"},
        {"sandhied_word": "", "anvaya_no": "1.2"},
    ]}]
    spans = _verse_spans(["धर्मक्षेत्रे कुरुक्षेत्रे"], sents)
    texts = [x["text"] for x in spans[0]]
    assert "धर्मक्षेत्रे" in texts
    hit = next(x for x in spans[0] if x["text"] == "धर्मक्षेत्रे")
    assert hit["keys"] == ["0|1.1"]


@pytest.mark.skipif(not available(), reason="run: python3 -m tools.fetch_samsaadhanii_ereaders --all")
def test_gita_1_1_has_engine_verified_tinanta():
    v = verse("श्रीमद्भगवद्गीता", "01", "001")
    assert v["text"] and v["spans"]
    words = [w for s in v["sentences"] for w in s["words"]]
    tins = [w for w in words if w["kind"] == "tinanta"]
    assert tins, "Gītā 1.1 should contain a tiṅanta"
    assert any(w["engine"]["status"] in ("derived", "differs", "error") for w in tins)
    assert ATTRIBUTION in v["attribution"]
    assert export_rows(v)[0][0] == "Word"


@pytest.mark.skipif(not available(), reason="snapshot missing")
def test_gita_1_1_karaka_tree_has_verb_root():
    v = verse("श्रीमद्भगवद्गीता", "01", "001")
    t = v["sentences"][0]["tree"]
    words = {w["anvaya_no"]: w for w in v["sentences"][0]["words"]}
    assert words[t["roots"][0]]["kind"] == "tinanta"
    assert words[t["roots"][0]]["word_dev"] == "अकुर्वत"
    assert t["children"]["9.1"] == ["2.2", "6.1", "8.1", "10.1"]
    assert t["children"]["6.1"] == ["3.1", "4.1", "5.1", "7.1", "7.1.1"]
    assert t["parent"]["2.2"] == "9.1" and t["parent"]["1.1"] == "1.2"
    assert t["roots"][0] in {e["head"] for e in t["edges"]}
    assert any(e["samasa"] and e["label"].startswith("षष्ठी") for e in t["edges"])


@pytest.mark.skipif(not available(), reason="snapshot missing")
def test_search_finds_akurvata():
    hits = search("श्रीमद्भगवद्गीता", "अकुर्वत", limit=5)
    assert hits and hits[0]["chapter"] == "01"
