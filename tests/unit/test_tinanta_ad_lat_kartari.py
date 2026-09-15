"""
अद्भक्षणे — laṭ kartari parasmaipada 9-cell paradigm (clip gold).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अत्ति",
    (3, 2): "अत्तः",
    (3, 3): "अदन्ति",
    (2, 1): "अत्सि",
    (2, 2): "अत्थः",
    (2, 3): "अत्थ",
    (1, 1): "अद्मि",
    (1, 2): "अद्वः",
    (1, 3): "अद्मः",
}


def test_ad_lat_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "laT", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
