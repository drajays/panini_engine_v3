"""
अद्भक्षणे — luṭ kartari parasmaipada (tāsi + 2.4.85 per clip).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अत्ता",
    (3, 2): "अत्तारः",
    (2, 1): "अत्तासि",
    (2, 2): "अत्तास्थः",
    (2, 3): "अत्तास्थ",
    (1, 1): "अत्तास्मि",
    (1, 2): "अत्तास्वः",
    (1, 3): "अत्तास्मः",
}


def test_ad_lut_kartari_parasmaipada_eight_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "luT", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
