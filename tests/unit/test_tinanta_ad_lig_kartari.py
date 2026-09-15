"""
अद्भक्षणे — vidhi-liṅ kartari parasmaipada (yāsuṭ + 3.4.103 per clip).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अद्यात्",
    (3, 2): "अद्याताम्",
    (3, 3): "अद्युः",
    (2, 1): "अद्याः",
    (2, 2): "अद्यातम्",
    (2, 3): "अद्यात",
    (1, 1): "अद्याम्",
    (1, 2): "अद्याव",
    (1, 3): "अद्याम",
}


def test_ad_lig_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "liG", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
