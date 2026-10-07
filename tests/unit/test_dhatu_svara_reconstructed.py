"""
docs/DHATU_SVARA_RECONSTRUCTION.md — pins the reverse-engineered svara
(udātta/anudātta/svarita) derived from ``pada_label_dev`` + structural ṅit/ñit
in ``data/inputs/dhatu_svara_reconstructed.json``
(``scripts/derive_dhatu_svara_reconstructed.py``). Additive artifact only —
not consumed by the live engine.
"""
from __future__ import annotations

import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]


def _rows() -> list[dict]:
    payload = json.loads((_ROOT / "data/inputs/dhatu_svara_reconstructed.json").read_text())
    return payload["entries"]


def _by_id(rows: list[dict]) -> dict[str, dict]:
    return {r["id"]: r for r in rows}


def test_every_ngit_final_row_is_atmanepadi_with_no_accent_needed():
    rows = _rows()
    ngit_rows = [r for r in rows if r["ngit_final"]]
    assert ngit_rows, "expected at least one ṅit-final (trailing ङ्) row"
    for r in ngit_rows:
        assert r["pada_label_dev"] == "आत्मनेपदी", r
        assert r["reconstructed_svara"] is None, r
        assert r["svara_governed_by"] == "1.3.12", r
        assert r["svara_basis"] == "ngit", r
        assert r["confidence"] == "high", r


def test_atmanepadi_without_ngit_reconstructs_anudatta():
    rows = _rows()
    hits = [r for r in rows if r["pada_label_dev"] == "आत्मनेपदी" and not r["ngit_final"]]
    assert hits
    for r in hits:
        assert r["reconstructed_svara"] == "anudatta", r
        assert r["svara_governed_by"] == "1.3.12", r


def test_ubhayapadi_with_yit_needs_no_accent():
    rows = _rows()
    hits = [r for r in rows if r["pada_label_dev"] == "उभयपदी" and r["yit_final"]]
    assert hits
    for r in hits:
        assert r["reconstructed_svara"] is None, r
        assert r["svara_governed_by"] == "1.3.72", r
        assert r["svara_basis"] == "yit", r


def test_ubhayapadi_without_yit_reconstructs_svarita_at_medium_confidence():
    rows = _rows()
    hits = [r for r in rows if r["pada_label_dev"] == "उभयपदी" and not r["yit_final"]]
    assert hits
    for r in hits:
        assert r["reconstructed_svara"] == "svarita", r
        assert r["svara_governed_by"] == "1.3.72", r
        assert r["confidence"] == "medium", r


def test_parasmaipadi_defaults_to_udatta_via_1_3_78():
    rows = _rows()
    hits = [r for r in rows if r["pada_label_dev"] == "परस्मैपदी" and not (r["ngit_final"] or r["yit_final"])]
    assert hits
    for r in hits:
        assert r["reconstructed_svara"] == "udatta", r
        assert r["svara_governed_by"] == "1.3.78", r
        assert r["confidence"] == "high", r


def test_known_niy_anomaly_is_flagged_low_confidence():
    by_id = _by_id(_rows())
    niy = by_id["BvAdi_nIY"]
    assert niy["pada_label_dev"] == "परस्मैपदी"
    assert niy["yit_final"] is True
    assert niy["confidence"] == "low"
    assert niy["caveat"]


def test_flagged_anomaly_count_is_exactly_four():
    rows = _rows()
    low = [r for r in rows if r["confidence"] == "low"]
    assert len(low) == 4, [r["id"] for r in low]


def test_stats_block_totals_match_entry_count():
    payload = json.loads((_ROOT / "data/inputs/dhatu_svara_reconstructed.json").read_text())
    assert payload["_stats"]["total"] == len(payload["entries"])
    assert sum(payload["_stats"]["by_confidence"].values()) == len(payload["entries"])
