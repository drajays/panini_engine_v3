"""
tests/unit/test_advaita_sharada_reader.py
─────────────────────────────────────────

The Prasthānatrayī reader is tools-layer: Advaita Sharada supplies text and
structure (local cache, never committed), Tamal Maharaj's CC BY deposit
supplies word analyses, the engine judges them. These tests lock the page
parser, the passage grouping, the grammar-string → tag rewrite and (when both
caches are present) one Īśa mantra through analysis-by-synthesis.
"""
from __future__ import annotations

import json

import pytest

from tools import advaita_sharada_reader as ar
from tools.fetch_advaita_sharada import parse_page, parse_vyakhya, text_of

_PAGE = (
    '<main class="text" lang="sa" data-work="isha-bhashya" data-chunk="1" data-worktitle="ईशावास्योपनिषद्भाष्यम्" '
    'data-astro-cid-x><p class="chapter-head chrome" id="IS_C01" data-astro-cid-x>१ विभागः</p>'
    '<button class="vy-chip chrome" data-vy="AIS" data-slug="anandagiri-isha" data-title="आनन्दगिरिटीका" '
    'aria-pressed="false">आनन्दगिरिटीका</button>'
    '<p class="unit prose kind-prose" id="IS_C01_I01">‘ईशा वास्यम्’ इत्यादयो मन्त्राः कर्म\u00adस्व\u00adवि\u00adनि\u00adयुक्ताः ।</p>'
    '<div class="unit verse" id="IS_C01_V01"><p class="verse-text">ईशा वास्यमिदं सर्वं ।<br />तेन त्यक्तेन ॥ १ ॥</p>'
    '<span class="verse-no">१</span></div>'
    '<p class="unit prose kind-bhashya" id="IS_C01_V01_B01">ईशा ईष्टे इति ईट् । <a class="ullekha" '
    'href="/read/isha-bhashya/1#IS_C01_V09" target="_blank">‘अन्धं तमः’</a> इति ।</p>'
    '<p class="unit prose kind-avatarika" id="IS_C01_V02_I01">अथेतरस्य इदमुपदिशति मन्त्रः —</p>'
    '<div class="unit verse" id="IS_C01_V02"><p class="verse-text">कुर्वन्नेवेह कर्माणि ॥ २ ॥</p></div>'
    '<p class="unit colophon" id="IS_C01_E001">इति ईशावास्योपनिषद्भाष्यम् ॥</p></main>'
)


def test_text_of_drops_tags_and_soft_hyphens():
    assert text_of("कर्म\u00adस्व<br />इति <b>च</b>") == "कर्मस्व\nइति च"


def test_parse_page_kinds_ids_and_tika_chip():
    p = parse_page(_PAGE)
    assert (p["work"], p["chunk"]) == ("isha-bhashya", "1")
    assert [(u["id"], u["kind"]) for u in p["units"]] == [
        ("IS_C01", "heading"), ("IS_C01_I01", "prose"), ("IS_C01_V01", "mula"), ("IS_C01_V01_B01", "bhashya"),
        ("IS_C01_V02_I01", "avatarika"), ("IS_C01_V02", "mula"), ("IS_C01_E001", "colophon")]
    mula = p["units"][2]
    assert mula["text"] == "ईशा वास्यमिदं सर्वं ।\nतेन त्यक्तेन ॥ १ ॥" and mula["verse_no"] == "१"
    assert "कर्मस्वविनियुक्ताः" in p["units"][1]["text"]
    assert p["units"][3]["citations"][0]["anchor"] == "IS_C01_V09"
    assert p["vyakhya"] == [{"code": "AIS", "slug": "anandagiri-isha", "title": "आनन्दगिरिटीका"}]


def test_parse_vyakhya_keeps_pratika():
    rows = parse_vyakhya(json.dumps({"IS_C01_V01_B01": [{
        "id": "AIS_C01_Q0013", "chunk": "1", "lemma": "सर्व",
        "html": 'इत्याशङ्क्याऽऽह -<br /><span class="pratika">सर्व\u00adज\u00adन्तू\u00adना\u00adमात्मा सन्</span>निति ।'}]}).encode())
    r = rows["IS_C01_V01_B01"][0]
    assert r["pratika"] == ["सर्वजन्तूनामात्मा सन्"] and r["lemma"] == "सर्व"


def test_passages_group_under_their_mula(monkeypatch):
    page = {**parse_page(_PAGE), "url": "x"}
    page["vyakhya"][0]["aligned"] = {"IS_C01_V01_B01": [{"id": "AIS_C01_Q0012", "text": "ईशेति ।", "pratika": []}]}
    monkeypatch.setattr(ar, "_doc", lambda slug: {"pages": [page], "title": "t"})
    ar._verses.cache_clear()
    try:
        v1, v2 = ar._verses("isha-bhashya", "1")
    finally:
        ar._verses.cache_clear()
    assert (v1["id"], v1["ref"]) == ("IS_C01_V01", "1.1")
    assert [p["id"] for p in v1["pre"]] == ["IS_C01", "IS_C01_I01"]
    assert [p["id"] for p in v1["post"]] == ["IS_C01_V01_B01"]
    assert v1["post"][0]["tika"][0]["rows"][0]["id"] == "AIS_C01_Q0012"
    assert [p["id"] for p in v2["pre"]] == ["IS_C01_V02_I01"]
    assert [p["id"] for p in v2["post"]] == ["IS_C01_E001"]


def test_work_without_mula_is_read_paragraph_by_paragraph(monkeypatch):
    units = [{"id": "VPS_C01", "kind": "heading", "text": "प्रथमं वर्णकम्"},
             {"id": "VPS_C01_S01_M01", "kind": "mangala", "text": "नमः"},
             {"id": "VPS_C01_S01_B01", "kind": "bhashya", "text": "अथातो ब्रह्मजिज्ञासा ।"},
             {"id": "VPS_C01_S01_B02", "kind": "bhashya", "text": "अत्र अथशब्दः ।"},
             {"id": "VPS_C01_S01_E001", "kind": "colophon", "text": "इति ।"}]
    page = {"chunk": "1", "vyakhya": [], "units": units, "url": "x"}
    monkeypatch.setattr(ar, "_doc", lambda slug: {"pages": [page], "title": "t"})
    ar._verses.cache_clear()
    try:
        items = ar._verses("vivaranaprameyasangraha", "1")
    finally:
        ar._verses.cache_clear()
    assert [v["id"] for v in items] == ["VPS_C01_S01_B01", "VPS_C01_S01_B02"]
    assert [p["id"] for p in items[0]["pre"]] == ["VPS_C01", "VPS_C01_S01_M01"]
    assert [p["id"] for p in items[1]["post"]] == ["VPS_C01_S01_E001"]


def test_ref_of_matches_deposit_keys():
    assert ar.ref_of("IS_C01_V01") == "1.1"
    assert ar.ref_of("BR_C01_S05_V16") == "1.5.16"
    assert ar.ref_of("BS_C04_S04_V22") == "4.4.22"


@pytest.mark.parametrize("g, kind, tag", [
    ("ईश · तृतीया·एकवचन·पुंल्लिङ्ग", "subanta", "ईश{पुं;3;एक}"),
    ("सर्व · नपुं·प्रथमा·एकवचन", "subanta", "सर्व{नपुं;1;एक}"),
    ("च अव्यय", "avyaya", "च{अव्य}"),
    ("√कृ (तनादिगण) · लृट्·प्रथमपुरुष·एकवचन·परस्मैपद", "tinanta", "कृ{कर्तरि;लृट्;प्र;एक;परस्मैपदी;तनादिः}"),
    ("√विश् (प्र) · लट्·प्रथमपुरुष·एकवचन·परस्मैपद", "tinanta", "प्र_विश्{कर्तरि;लट्;प्र;एक;परस्मैपदी;तुदादिः}"),
    ("√जीव् (१) · लोट्·मध्यम·एक·परस्मैपद", "tinanta", "जीव्{कर्तरि;लोट्;म;एक;परस्मैपदी;भ्वादिः}"),
])
def test_grammar_string_to_samsaadhanii_tag(g, kind, tag):
    k, tags, why = ar.tags_for(g)
    assert (k, why) == (kind, None)
    assert tag in tags


def test_participle_without_stem_is_unresolved():
    k, tags, why = ar.tags_for("√ग्रह् (क्त) · प्रथमा·एकवचन·पुंलिङ्ग")
    assert k == "subanta" and not tags and "kṛdanta" in why


def test_indeclinable_krt_names_its_pratyaya():
    k, tags, _ = ar.tags_for("√दृश् · ल्यबन्त")
    assert k == "krdanta" and tags == ["दृश्{कृत्_प्रत्ययः:ल्यप्}"]


_HAVE = ar.available() and (ar.WORDS_RAW / "prasthan-words-Isha.json").is_file()


@pytest.mark.skipif(not _HAVE, reason="run: python3 -m tools.fetch_advaita_sharada && "
                                       "python3 -m tools.fetch_prasthanatrayi_words")
def test_isha_1_is_judged_by_the_engine():
    v = ar.verse("as:isha-bhashya", "1", "IS_C01_V01")
    parts = {p["word_dev"]: p for w in v["words"] for p in w["parts"]}
    assert parts["जगत्याम्"]["engine"]["status"] == "derived"
    assert parts["भुञ्जीथाः"]["engine"]["status"] == "derived"     # gaṇa inferred by derivation
    assert v["counts"]["derived"] >= 10
    assert v["post"][0]["kind"] == "bhashya" and v["post"][0]["tika"]
