"""pipelines/pada_samhita — the resolver picks the 6.1 ac-sandhi sūtra at a pada seam; core/analyze accepts
a Chedaka split only when the engine derives every part and re-joins them (Art. 17)."""
from __future__ import annotations

import pytest

from core import analyze as an
from pipelines.pada_samhita import join, seam_kind


def _applied(s):
    return [t["sutra_id"] for t in s.trace if t.get("status") == "APPLIED"]


@pytest.mark.parametrize("left,right,want,sutra", [
    ("eva", "aBirakzati", "evABirakzati", "6.1.101"),   # akaḥ savarṇe dīrghaḥ — apavāda of 6.1.87
    ("mahA", "ISvaraH", "maheSvaraH", "6.1.87"),         # ād guṇaḥ
    ("tava", "eva", "tavEva", "6.1.88"),                 # vṛddhir eci — apavāda of 6.1.87
    ("vane", "api", "vanepi", "6.1.109"),                # eṅaḥ padāntād ati — apavāda of 6.1.78
    ("te", "iti", "tayiti", "6.1.78"),                   # eco 'yavāyāvaḥ
    ("daDi", "atra", "daDyatra", "6.1.77"),              # iko yaṇ aci
])
def test_resolver_picks_the_seam_sutra(left, right, want, sutra):
    s = join(left, right)
    assert s.flat_slp1() == want and _applied(s) == [sutra]


def test_non_vowel_seams_are_refused_not_joined():
    assert seam_kind("aDikAraH", "te") == "visarga" and seam_kind("vAk", "atra") == "hal"
    with pytest.raises(ValueError, match="tripāḍī"):
        join("aDikAraH", "te")


def _stub(monkeypatch, cheda):
    table = {
        "eva": [{"kind": "avyaya", "stem": "eva"}],
        "aBirakzati": [{"kind": "tinanta", "dhatu": {"aupadeshika": "rakza~", "gana": "BvAdi", "artha": "pAlane",
                        "clean": "rakz", "sanadi": [], "prefixes": ["aBi"]},
                        "lakara": "la~w", "prayoga": "kartari", "purusha": "praTama", "vacana": "eka"}],
    }
    monkeypatch.setattr(an, "_index", lambda slp1: [])
    monkeypatch.setattr(an, "_kosha", lambda words: [table.get(w, []) for w in words])
    monkeypatch.setattr(an, "_cheda", lambda words: [cheda.get(w, []) for w in words])


def test_split_accepted_when_engine_rejoins(monkeypatch):
    _stub(monkeypatch, {"evABirakzati": ["eva", "aBirakzati"]})
    w = an.analyze(["एवाभिरक्षति"])["words"][0]
    assert w["status"] == "split"
    assert w["split"]["seams"][0]["sutras"] == ["6.1.101"]


def test_wrong_split_stays_unknown(monkeypatch):
    _stub(monkeypatch, {"evABirakzati": ["evA", "Birakzati"]})   # parts nobody derives, seam not a vowel seam
    w = an.analyze(["एवाभिरक्षति"])["words"][0]
    assert w["status"] == "unknown" and w["split"]["verified"] is False
