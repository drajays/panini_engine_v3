"""data/inputs/sutra_context.json — shape, spot values, overrides, determinism."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
CTX = ROOT / "data/inputs/sutra_context.json"


@pytest.fixture(scope="module")
def ctx():
    return json.loads(CTX.read_text(encoding="utf-8"))


def test_every_ashtadhyayi_id_present(ctx):
    sutras = ctx["sutras"]
    assert len(sutras) == 3983
    assert set(ctx["extras"]) == {"9.1.1", "9.1.2"}, "workbook helper rows stay outside `sutras`"
    for p, n in {"1.1": 75, "3.4": 117, "6.4": 175, "8.4": 68}.items():
        assert f"{p}.{n}" in sutras and f"{p}.{n + 1}" not in sutras


def test_spot_values(ctx):
    s = ctx["sutras"]
    assert s["1.1.1"]["term"] == "वृद्धिः" and s["1.1.1"]["type"] == ["संज्ञा"]
    assert s["1.1.1"]["padaccheda"][1] == {"word": "आदैच्", "vibhakti": 1, "vacana": 1, "note": None}
    assert s["1.1.3"]["type"] == ["परिभाषा"]
    assert [a["source_sutra"] for a in s["1.1.3"]["anuvritti"]] == ["1.1.1", "1.1.2"]
    assert s["6.4.1"]["adhikara_range"] == ["6.4.1", "7.4.97"]
    assert s["6.4.1"]["anuvritti"] == []
    assert {"word": "गुणः", "source_sutra": "7.3.82"} in s["7.3.84"]["anuvritti"]
    assert "6.4.1" in s["7.3.84"]["adhikara_heads"]


def test_unknown_is_null_not_empty(ctx):
    s = ctx["sutras"]
    assert s["1.1.3"]["adhikara_heads"] is None      # no corpus file
    assert s["1.1.1"]["adhikara_heads"] == []        # corpus file says "-"
    assert s["7.3.84"]["adhikara_range"] is None     # not a head


def test_overrides_applied_with_provenance(ctx):
    over = [sid for sid, r in ctx["sutras"].items() if "override" in r["provenance"].values()]
    assert len(over) == 93
    r = ctx["sutras"]["2.4.72"]
    assert r["pada_tags"] == "अदिप्रभृतिभ्यः अदादिभ्यः ५/३" and r["provenance"]["pada_tags"] == "override"


def test_build_is_deterministic(tmp_path):
    from scripts import build_sutra_context as b
    if not (b.WORKBOOK.exists() and b.ASHTADHYAYI.exists()):
        pytest.skip("source workbook / ~/ashtadhyayi not available")
    one, two = tmp_path / "a.json", tmp_path / "b.json"
    b.main(["--out", str(one)])
    b.main(["--out", str(two)])
    assert one.read_bytes() == two.read_bytes() == CTX.read_bytes()
