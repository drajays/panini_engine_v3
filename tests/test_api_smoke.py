"""Smoke test for api/main.py — every endpoint returns a real derivation.

Endpoint functions are called directly (no HTTP server, no httpx); FastAPI
only adds routing and validation on top of these.  Query() defaults are not
resolved outside a request, so list endpoints get explicit arguments.
"""
from __future__ import annotations

import pytest
from fastapi import HTTPException

from api import main as api


def test_health_sees_the_registry():
    assert api.health()["sutras"] > 3000


def test_subanta_rama_nom_sg():
    out = api.subanta(api.SubantaReq(stem="rAma", vibhakti=1, vacana=1))
    assert out["surface"] == {"slp1": "rAmaH", "dev": "रामः"}
    assert out["applied_path"], "a derivation must expose the sūtras it applied"
    assert out["stats"]["applied"] > 0
    first = out["steps"][0]
    assert {"sutra_id", "status", "before", "after", "why_dev"} <= set(first)


def test_subanta_paradigm_has_24_cells():
    cells = api.subanta_paradigm(stem="rAma", linga="pulliṅga")["cells"]
    assert len(cells) == 24
    assert cells[0]["dev"] == "रामः"


def test_tinanta_accepts_slp1_and_devanagari():
    a = api.tinanta(api.TinantaReq(dhatu="BU", lakara="laT", purusha=3, vacana=1))
    b = api.tinanta(api.TinantaReq(dhatu="भू", lakara="laT", purusha=3, vacana=1))
    assert a["surface"]["dev"] == b["surface"]["dev"] == "भवति"
    assert a["dhatu"]["mula_dev"] == "भू"


def test_krdanta_both_pratyayas():
    assert api.krdanta(api.KrdantaReq(dhatu_id="BU", krt="tfc"))["surface"]["dev"] == "भविता"
    assert api.krdanta(api.KrdantaReq(dhatu_id="BU", krt="Nvul"))["surface"]["dev"] == "भावक"


def test_sutra_lookup_and_404():
    assert api.get_sutra("1.4.14")["text_dev"] == "सुप्तिङन्तं पदम्"
    with pytest.raises(HTTPException) as ex:
        api.get_sutra("9.9.9")
    assert ex.value.status_code == 404


def test_dhatu_search_and_resolution():
    assert api.list_dhatu(q="BU", gana=None, limit=5, offset=0)["total"] >= 1
    assert api.get_dhatu("01.0001")["mula_dhatu_dev"] == "भू"


def test_unknown_dhatu_is_404_not_500():
    with pytest.raises(HTTPException) as ex:
        api.get_dhatu("no.such.dhatu")
    assert ex.value.status_code == 404


def test_review_roundtrip(tmp_path, monkeypatch):
    """A correction can be filed against a step, listed, and deleted."""
    monkeypatch.setattr(api, "REVIEW_FILE", tmp_path / "corrections.jsonl")
    assert api.list_reviews()["total"] == 0

    rec = api.add_review(api.ReviewIn(
        target='tinanta:{"dhatu":"gam"}', step_n=20, sutra_id="1.3.3",
        observed_form="गमति", expected_form="गच्छ", expected_sutra="7.3.77",
        note="इषुगमियमां छः should fire here",
    ))
    assert api.list_reviews(target='tinanta:{"dhatu":"gam"}')["total"] == 1
    assert api.list_reviews(target="something-else")["total"] == 0

    api.delete_review(rec["id"])
    assert api.list_reviews()["total"] == 0
    with pytest.raises(HTTPException) as ex:
        api.delete_review(rec["id"])
    assert ex.value.status_code == 404


def test_empty_review_is_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "REVIEW_FILE", tmp_path / "corrections.jsonl")
    with pytest.raises(HTTPException) as ex:
        api.add_review(api.ReviewIn(target="x", step_n=1))
    assert ex.value.status_code == 422
