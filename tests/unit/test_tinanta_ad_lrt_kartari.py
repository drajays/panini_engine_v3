"""
अद्भक्षणे — lṛṭ kartari parasmaipada (sya + 3.1.33 per clip).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अत्स्यति",
    (3, 2): "अत्स्यतः",
    (3, 3): "अत्स्यन्ति",
    (2, 2): "अत्स्यथः",
    (2, 3): "अत्स्यथ",
    (1, 1): "अत्स्यामि",
    (1, 2): "अत्स्यावः",
    (1, 3): "अत्स्यामः",
}


def test_ad_lrt_kartari_parasmaipada_eight_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "lRT", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
