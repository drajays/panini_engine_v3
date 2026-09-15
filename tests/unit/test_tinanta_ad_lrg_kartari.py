"""
अद्भक्षणे — lṛṅ kartari parasmaipada (3.1.33 sya + 6.4.72 आट्, 7.2.10).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "आत्स्यत्",
    (3, 2): "आत्स्यताम्",
    (3, 3): "आत्स्यन्",
    (2, 1): "आत्स्यः",
    (2, 2): "आत्स्यतम्",
    (2, 3): "आत्स्यत",
    (1, 1): "आत्स्यम्",
    (1, 2): "आत्स्याव",
    (1, 3): "आत्स्याम",
}


def test_ad_lrg_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "lRG", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"


def test_bhu_lrg_unchanged():
    assert derive("BU", "lRG", "kartari", 3, 1).flat_dev() == "अभविष्यत्"
