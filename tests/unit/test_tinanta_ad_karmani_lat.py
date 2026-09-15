"""
अद्भक्षणे — karmaṇi laṭ ātmanepada (यक् ३.१.६७, भावकर्मणोः १.३.१३).

Clip gold (2026-05-30): अद्यते … अद्यामहे.
API: derive("ada~", "laT", "karmani", purusha, vacana).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अद्यते",
    (3, 2): "अद्येते",
    (3, 3): "अद्यन्ते",
    (2, 1): "अद्यसे",
    (2, 2): "अद्येथे",
    (2, 3): "अद्यध्वे",
    (1, 1): "अद्ये",
    (1, 2): "अद्यावहे",
    (1, 3): "अद्यामहे",
}


def test_ad_karmani_lat_atmanepada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "laT", "karmani", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana}) got {s.flat_dev()!r}"


def test_ad_karmani_lat_not_kartari():
    assert derive("ada~", "laT", "kartari", 3, 1).flat_dev() == "अत्ति"
    assert derive("ada~", "laT", "karmani", 3, 1).flat_dev() == "अद्यते"
