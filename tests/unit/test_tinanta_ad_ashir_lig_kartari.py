"""
अद्भक्षणे — āśīr-liṅ kartari parasmaipada (3.4.104 KIT yāsuṭ, 8.2.29 per clip).
"""
from __future__ import annotations

from pipelines.tinanta import derive

_GOLD_DEV: dict[tuple[int, int], str] = {
    (3, 1): "अद्यात्",
    (3, 2): "अद्यास्ताम्",
    (3, 3): "अद्यासुः",
    (2, 1): "अद्याः",
    (2, 2): "अद्यास्तम्",
    (2, 3): "अद्यास्त",
    (1, 1): "अद्यासम्",
    (1, 2): "अद्यास्व",
    (1, 3): "अद्यास्म",
}


def test_ad_ashir_lig_kartari_parasmaipada_nine_cells():
    for (purusha, vacana), dev in _GOLD_DEV.items():
        s = derive("ada~", "AsIrliG", "kartari", purusha, vacana)
        assert s.flat_dev() == dev, f"({purusha},{vacana})"
