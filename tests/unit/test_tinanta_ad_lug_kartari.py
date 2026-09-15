"""
अद्भक्षणे — luṅ kartari parasmaipada (2.4.37 घस्, 3.1.55 अङ्, 6.4.71 अट्).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अघसत्",
    (3, 2): "अघसताम्",
    (3, 3): "अघसन्",
    (2, 1): "अघसः",
    (2, 2): "अघसतम्",
    (2, 3): "अघसत",
    (1, 1): "अघसम्",
    (1, 2): "अघसाव",
    (1, 3): "अघसाम",
}


def test_ad_lug_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "luG", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"


def test_bhu_lug_unchanged():
    assert derive("BU", "luG", "kartari", 3, 1).flat_dev() == "अभूत्"
