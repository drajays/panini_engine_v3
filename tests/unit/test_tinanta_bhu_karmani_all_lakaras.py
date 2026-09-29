"""
tests/unit/test_tinanta_bhu_karmani_all_lakaras.py

Glass-box gold for BU + karmaṇi prayoga — all 9 cells × 10 lakāras (90 total).
Baseline locked from derive() output 2026-05-31.

T4 (bhāve/karmaṇi gold tables) — Claude Code 2026-05-31.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive

_BHU_KARMANI = {
    "laT": {
        (3, 1): "भूयते",    (3, 2): "भूयेते",   (3, 3): "भूयन्ते",
        (2, 1): "भूयसे",    (2, 2): "भूयेथे",   (2, 3): "भूयध्वे",
        (1, 1): "भूये",     (1, 2): "भूयावहे",  (1, 3): "भूयामहे",
    },
    "liT": {
        (3, 1): "बभूवे",    (3, 2): "बभूवाते",  (3, 3): "बभूविरे",
        (2, 1): "बभूविषे",   (2, 2): "बभूवाथे",  (2, 3): "बभूविध्वे",
        (1, 1): "बभूवे",    (1, 2): "बभूविवहे",  (1, 3): "बभूविमहे",
    },
    "luT": {
        (3, 1): "भविता",        (3, 2): "भवितारौ",     (3, 3): "भवितारः",
        (2, 1): "भवितासे",      (2, 2): "भवितासाथे",   (2, 3): "भविताध्वे",
        (1, 1): "भविताहे",      (1, 2): "भवितास्वहे",  (1, 3): "भवितास्महे",
    },
    "lRT": {
        (3, 1): "भाविष्यते",    (3, 2): "भाविष्येते",   (3, 3): "भाविष्यन्ते",
        (2, 1): "भाविष्यसे",    (2, 2): "भाविष्येथे",   (2, 3): "भाविष्यध्वे",
        (1, 1): "भाविष्ये",     (1, 2): "भाविष्यावहे",  (1, 3): "भाविष्यामहे",
    },
    "loT": {
        (3, 1): "भूयते",    (3, 2): "भूयेते",   (3, 3): "भूयन्ते",
        (2, 1): "भूयस्व",   (2, 2): "भूयेथे",   (2, 3): "भूयध्वम्",
        (1, 1): "भूये",     (1, 2): "भूयवहे",   (1, 3): "भूयमहे",
    },
    "liG": {
        (3, 1): "भूयेत",    (3, 2): "भूयेयाताम्",  (3, 3): "भूयेरन्",
        (2, 1): "भूयेथाः",  (2, 2): "भूयेयाथाम्",  (2, 3): "भूयेध्वम्",
        (1, 1): "भूयेयि",   (1, 2): "भूयेवहि",    (1, 3): "भूयेमहि",
    },
    "AsIrliG": {
        (3, 1): "भविषीष्ट",      (3, 2): "भविषीयास्ताम्",  (3, 3): "भविषीरन्",
        (2, 1): "भविषीष्ठाः",  # 8.4.41 (ashtadhyayi.com, Vidyut)    (2, 2): "भविषीयास्थाम्",  (2, 3): "भविषीध्वम्",
        (1, 1): "भविषीय",        (1, 2): "भविषीवहि",       (1, 3): "भविषीमहि",
    },
    "luG": {  # ashtadhyayi.com (6.4.62 ciṇvad-iṭ अभाविषाताम्… is the optional other)
        (3, 1): "अभावि",  (3, 2): "अभविषाताम्",  (3, 3): "अभविषत",
        (2, 1): "अभविष्ठाः",  (2, 2): "अभविषाथाम्",  (2, 3): "अभविध्वम्",
        (1, 1): "अभविषि",  (1, 2): "अभविष्वहि",  (1, 3): "अभविष्महि",
    },
    "laG": {
        (3, 1): "अभूयत",    (3, 2): "अभूयेताम्",  (3, 3): "अभूयन्त",
        (2, 1): "अभूयथाः",  (2, 2): "अभूयेथाम्",  (2, 3): "अभूयध्वम्",
        (1, 1): "अभूये",    (1, 2): "अभूयावहि",   (1, 3): "अभूयामहि",
    },
    "lRG": {  # ashtadhyayi.com first form (6.4.62 ciṇvad-iṭ अभाविष्यत is the optional other)
        (3, 1): "अभविष्यत",     (3, 2): "अभविष्येताम्",  (3, 3): "अभविष्यन्त",
        (2, 1): "अभविष्यथाः",   (2, 2): "अभविष्येथाम्",  (2, 3): "अभविष्यध्वम्",
        (1, 1): "अभविष्ये",     (1, 2): "अभविष्यावहि",   (1, 3): "अभविष्यामहि",
    },
}

_PU_NAME  = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


# 2026-09-28 — 3.4.79 टित आत्मनेपदानां टेरे now requires a ṭit sthānī, so it no
# longer turns ta → te in ṅit lakāras (laṅ, liṅ, lṛṅ). The pins below were
# "baseline locked" engine output that relied on that bug:
#   _NGIT_FIXED   — our new form is among Vidyut's; pin corrected.
#   _NGIT_PENDING — old pin and new output are both wrong (the karmaṇi/bhāve
#                   ṅit-lakāra spine has no yak / sīyuṭ: भवेत for भूयेत).
#                   xfail(strict) until that spine exists.
_NGIT_FIXED = {('karmani', 'lRT', 1, 1): 'भविष्ये', ('karmani', 'lRT', 1, 2): 'भविष्यावहे', ('karmani', 'lRT', 1, 3): 'भविष्यामहे', ('karmani', 'lRT', 2, 1): 'भविष्यसे', ('karmani', 'lRT', 2, 2): 'भविष्येथे', ('karmani', 'lRT', 2, 3): 'भविष्यध्वे', ('karmani', 'lRT', 3, 1): 'भविष्यते', ('karmani', 'lRT', 3, 2): 'भविष्येते', ('karmani', 'lRT', 3, 3): 'भविष्यन्ते', ('karmani', 'liG', 1, 1): 'भूयेय', ('karmani', 'loT', 1, 1): 'भूयै', ('karmani', 'loT', 1, 2): 'भूयावहै', ('karmani', 'loT', 1, 3): 'भूयामहै', ('karmani', 'loT', 2, 2): 'भूयेथाम्', ('karmani', 'loT', 3, 1): 'भूयताम्', ('karmani', 'loT', 3, 2): 'भूयेताम्', ('karmani', 'loT', 3, 3): 'भूयन्ताम्'}  # pending cells pinned to Vidyut's form
_NGIT_PENDING = set()
_NGIT_XFAIL = pytest.mark.xfail(strict=True, reason="karmaṇi/bhāve ṅit-lakāra spine: no yak/sīyuṭ yet")


def _cases():
    for lak, cells in _BHU_KARMANI.items():
        for (pu, va), expected in cells.items():
            k = ("karmani", lak, pu, va)
            yield pytest.param(lak, pu, va, _NGIT_FIXED.get(k, expected),
                               id=f"{lak}_{pu}_{va}",
                               marks=(_NGIT_XFAIL,) if k in _NGIT_PENDING else ())


@pytest.mark.parametrize("lakara,purusha,vacana,expected", _cases())
def test_bhu_karmani(lakara: str, purusha: int, vacana: int, expected: str) -> None:
    state = derive("BU", lakara, "karmani", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"BU karmaṇi {lakara} {_PU_NAME[purusha]}पुरुष {_VA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )
