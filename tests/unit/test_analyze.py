"""core/analyze — proposals are verified by forward derivation (Art. 17); Vidyut is injected, not required."""
from __future__ import annotations

import pytest

from core import analyze as an

SAS = {"aupadeshika": "SAsu~", "gana": "adAdi", "artha": "anuSizwO", "clean": "SAs", "sanadi": [], "prefixes": []}


@pytest.fixture(autouse=True)
def _no_index(monkeypatch):
    """The form index is a build artifact; these tests pin the Vidyut proposals alone."""
    monkeypatch.setattr(an, "_index", lambda slp1: [])


def _tin(dhatu, lakara="la~w", purusha="praTama", vacana="eka"):
    return {"kind": "tinanta", "dhatu": dhatu, "lakara": lakara, "prayoga": "kartari", "purusha": purusha, "vacana": vacana}


def test_tokens_drop_dandas_and_digits():
    assert an.tokens("दण्डः शास्ति ।\nप्रजाः ॥ १ ॥") == ["दण्डः", "शास्ति", "प्रजाः"]


def test_homograph_dhatu_resolved_by_artha():
    assert an.dhatu_ids("SAsu~", "adAdi", "anuSizwO") == ["02.0070"]
    assert an.dhatu_ids("SAsu~", "adAdi", "icCAyAm") == ["02.0012"]
    assert set(an.dhatu_ids("SAsu~", "adAdi", "?")) == {"02.0012", "02.0070"}   # unknown artha: generation decides


def test_vidyut_reading_verified_by_derivation():
    w = an._word("शास्ति", [_tin(SAS)])
    assert w["status"] == "verified"
    r = next(x for x in w["readings"] if x["status"] == "derived")
    assert r["request"]["dhatu_id"] == "02.0070" and r["produced_dev"] == "शास्ति"


def test_wrong_reading_is_a_gap_not_an_answer():
    w = an._word("शास्ति", [_tin(SAS, purusha="uttama")])
    assert w["status"] == "oracle_only"
    assert w["readings"][0]["status"] == "differs" and "शास्मि" in w["readings"][0]["produced_dev"].split(" / ")   # 8.4.47 anaci ca: शास्स्मि is the other reading


def test_avyaya_and_unknown():
    assert an._word("च", [{"kind": "avyaya", "stem": "ca"}])["status"] == "avyaya"
    assert an._word("एवाभिरक्षति", [])["status"] == "unknown"


def test_written_anusvara_names_8_3_23():
    w = an._word("वनं", [{"kind": "subanta", "stem": "vana", "linga": "napuMsaka", "vibhakti": "praTamA", "vacana": "eka"}])
    r = w["readings"][0]
    assert w["status"] == "verified" and "8.3.23" in r["note"]


def test_api_analyze_with_steps(monkeypatch):
    pytest.importorskip("fastapi")
    from api.main import AnalyzeReq, analyze

    monkeypatch.setattr(an, "_kosha", lambda words: [[_tin(SAS)] if w == "SAsti" else [] for w in words])
    word = analyze(AnalyzeReq(text="शास्ति ।", steps=True))["lines"][0][0]
    assert word["status"] == "verified"
    d = next(x for x in word["readings"] if x["status"] == "derived")["derivation"]
    assert d["surface"]["dev"] == "शास्ति" and d["applied_path"]
