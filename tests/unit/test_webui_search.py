"""The one search (webui/search.py, GET /api/search) against the real stem / dhātu / rūpa data."""
from __future__ import annotations

import pytest

from webui.search import search


def top(q, kind="all", n=30):
    return [(r["type"], r["dev"], r["match"]) for r in search(q, kind, n)]


@pytest.mark.parametrize("q", ["फल", "धन", "हरि", "phala", "Pala", "dhana", "Dana", "hari", "vizRu", "विष्णु", "viShnu", "krishna"])
def test_stems_found_in_every_script(q):
    assert any(t == "shabda" for t, _, _ in top(q)), q


def test_devanagari_and_latin_agree():
    assert ("shabda", "फल", "exact") in top("फल") and ("shabda", "फल", "exact") in top("Pala")
    assert ("shabda", "फल", "normalised") in top("phala")          # plain Latin: aspirate digraph, no case
    assert ("shabda", "धन", "normalised") in top("dhana")


def test_rank_exact_first_then_prefix_then_substring():
    r = search("फल", "shabda", 500)
    assert r[0]["match"] == "exact" and r[0]["dev"] == "फल"
    order = [x["match"] for x in r]
    assert order.index("prefix") < order.index("substring")


def test_bare_consonant_is_a_prefix():
    assert all(m in ("prefix", "exact") or d.startswith("फ") for _, d, m in top("फ", "shabda"))


def test_dhatu_by_upadesha_translit_devanagari_and_meaning():
    for q in ("भू", "BU", "bhu"):
        assert ("dhatu", "भू") in {(t, d) for t, d, _ in top(q, "dhatu")}, q
    assert any(d == "गम्" for _, d, _ in top("gam", "dhatu")) and any(d == "गम्" for _, d, _ in top("गम्", "dhatu"))
    assert any(t == "dhatu" for t, _, _ in top("to go", "dhatu"))          # meaning text
    assert top("to be", "dhatu")[0][2] == "meaning"


def test_verb_form_rupa_and_ids():
    for q in ("भवति", "Bavati", "bhavati"):
        r = search(q, "rupa", 5)
        assert r and r[0]["dev"] == "भवति" and r[0]["id"] == "BU", q


def test_near_match_and_stem_of_form():
    assert ("shabda", "फल", "near") in top("phalm", "shabda", 200)         # edit distance 1
    assert any(d == "धन" and m == "stem-of" for _, d, m in top("धनम्", "shabda"))   # inflected form -> its stem


def test_blank_and_garbage_do_not_raise():
    assert search("") == [] and isinstance(search("???"), list)


def test_endpoint():
    from webui.app import app
    r = app.test_client().get("/api/search", query_string={"q": "फल", "kind": "shabda"}).get_json()
    assert r and r[0]["dev"] == "फल"
