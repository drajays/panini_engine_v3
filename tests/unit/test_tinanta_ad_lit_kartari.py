"""
अद्भक्षणे — liṭ kartari parasmaipada (2.4.40 *ghas* + reduplication).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "जघास",
    (3, 2): "जक्षतुः",
    (3, 3): "जक्षुः",
    (2, 1): "जघसिथ",
    (2, 2): "जक्षथुः",
    (2, 3): "जक्ष",
    (1, 1): "जघास",
    (1, 2): "जक्षिव",
    (1, 3): "जक्षिम",
}


def test_ad_lit_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "liT", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
