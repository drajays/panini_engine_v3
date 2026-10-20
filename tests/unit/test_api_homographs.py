"""/v1/tinanta never hides a homograph: a bare upadeśa shared by several dhātus lists the others with their forms."""
from __future__ import annotations

import pytest

pytest.importorskip("fastapi")
from api.main import TinantaReq, tinanta, tinanta_paradigm  # noqa: E402


def test_bare_upadesha_lists_the_other_dhatu_with_its_form():
    out = tinanta(TinantaReq(dhatu="SAsu~", lakara="laT"))
    assert out["dhatu"]["dhatupatha_id"] == "02.0012" and out["surface"]["dev"] == "शास्ते"
    alt = {h["dhatupatha_id"]: h for h in out["homographs"]}
    assert alt["02.0070"]["artha_dev"] == "अनुशिष्टौ" and alt["02.0070"]["surface"]["dev"] == "शास्ति"
    assert "02.0070" in out["note"] or "pāṭha id" in out["note"]


def test_patha_id_chooses_and_has_no_homographs():
    out = tinanta(TinantaReq(dhatu="02.0070", lakara="laT"))
    assert out["surface"]["dev"] == "शास्ति" and "homographs" not in out


def test_paradigm_names_the_row_it_used():
    out = tinanta_paradigm(dhatu="SAsu~", lakara="laT")
    assert out["dhatupatha_id"] == "02.0012" and [h["dhatupatha_id"] for h in out["homographs"]] == ["02.0070"]
