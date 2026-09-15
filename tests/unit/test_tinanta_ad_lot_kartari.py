"""
अद्भक्षणे — loṭ kartari parasmaipada (śap luk + loṭ tiṅ per clip).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अत्तु",
    (3, 2): "अत्ताम्",
    (3, 3): "अदन्तु",
    (2, 1): "अद्धि",
    (2, 2): "अत्तम्",
    (2, 3): "अत्त",
    (1, 1): "अदानि",
    (1, 2): "अदाव",
    (1, 3): "अदाम",
}


def test_ad_lot_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "loT", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
