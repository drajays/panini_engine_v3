"""
tests/unit/test_library_api.py
──────────────────────────────

/v1/library is the one catalogue reading clients (Subhastini) use. These tests lock the
uniform shapes, ashtadhyayi.com markup cleaning, and the local-only guard on Advaita
Sharada (a reading copy that must never be served off this machine). Sources not present
on the machine are skipped, as the providers skip them.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi import HTTPException

from api import main as api
from tools import library_providers as lib

LOCAL = SimpleNamespace(client=SimpleNamespace(host="127.0.0.1"))
REMOTE = SimpleNamespace(client=SimpleNamespace(host="203.0.113.7"))


def test_clean_drops_markup_and_keeps_sutra_refs():
    assert lib.clean("<x>अथ</x> [[1.1.1]] <<वृद्धिरादैच्>>") == "अथ (1.1.1) «वृद्धिरादैच्»"


def test_catalogue_shape():
    body = api.library_catalogue()
    assert set(body["providers"]) >= {"as", "scl", "ac"}
    for w in body["works"]:
        assert {"id", "provider", "title", "rights", "local_only"} <= set(w)
        assert w["id"].startswith(w["provider"] + ":")


@pytest.mark.parametrize("wid", ["ac:no-such-grantha", "zz:x", "nocolon"])
def test_unknown_work_is_404(wid):
    with pytest.raises(HTTPException) as e:
        api.library_work(wid, LOCAL)
    assert e.value.status_code == 404


_AC = any(w["id"] == "ac:ashtadhyayi" for w in lib.catalogue())


@pytest.mark.skipif(not _AC, reason="~/data-master (ashtadhyayi.com data) not on this machine")
def test_ashtadhyayi_sutra_with_its_vrttis():
    sec = api.library_section("ac:ashtadhyayi", "1.1", REMOTE)
    assert sec["items"][0]["id"] == "1.1.1" and sec["items"][0]["text"] == "वृद्धिरादैच्"
    assert sec["next"] == "1.2" and sec["prev"] is None
    it = api.library_item("ac:ashtadhyayi", "1.1", "1.1.1", REMOTE)
    titles = [c["title"] for c in it["commentaries"]]
    assert "काशिकावृत्तिः" in titles and "महाभाष्यम्" in titles


_AS = any(w["provider"] == "as" for w in lib.catalogue())


@pytest.mark.skipif(not _AS, reason="Advaita Sharada cache not on this machine")
def test_advaita_sharada_is_served_to_this_machine_only():
    with pytest.raises(HTTPException) as e:
        api.library_work("as:isha-bhashya", REMOTE)
    assert e.value.status_code == 403
    it = api.library_item("as:isha-bhashya", "1", "IS_C01_V01", LOCAL)
    assert it["ref"] == "1.1" and any(p["kind"] == "bhashya" for p in it["passages"])
    assert it["links"]["source"].startswith("https://advaitasharada.sringeri.net/")


def test_search_finds_across_providers():
    hits = api.library_search("ब्रह्म", 5, None)["hits"]
    assert all({"work", "section", "item", "snippet"} <= set(h) for h in hits)
