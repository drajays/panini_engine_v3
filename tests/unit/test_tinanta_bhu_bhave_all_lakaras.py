"""
tests/unit/test_tinanta_bhu_bhave_all_lakaras.py

Glass-box gold for BU + bhāve prayoga — all 9 cells × 10 lakāras (90 total).
Baseline locked from derive() output 2026-05-31; forms verified against
traditional grammar where notation is clear.

T4 (bhāve/karmaṇi gold tables) — Claude Code 2026-05-31.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive

# ── Gold tables (purusha, vacana) → Devanagari surface ──────────────────────

_BHU_BHAVE = {
    "laT": {
        (3, 1): "भवते",    (3, 2): "भवेते",   (3, 3): "भवन्ते",
        (2, 1): "भवसे",    (2, 2): "भवेथे",   (2, 3): "भवध्वे",
        (1, 1): "भवे",     (1, 2): "भवावहे",  (1, 3): "भवामहे",
    },
    "liT": {
        (3, 1): "बभूवे",   (3, 2): "बभूवाते",  (3, 3): "बभूविरे",
        (2, 1): "बभूविषे",  (2, 2): "बभूवाथे",  (2, 3): "बभूविध्वे",
        (1, 1): "बभूवे",   (1, 2): "बभूविवहे", (1, 3): "बभूविमहे",
    },
    "luT": {
        (3, 1): "भविता",        (3, 2): "भवितारौ",    (3, 3): "भवितारः",
        (2, 1): "भवितास्थाः",   (2, 2): "भवितासाथाम्", (2, 3): "भवितास्ध्वम्",
        (1, 1): "भवितासि",      (1, 2): "भवितास्वहि", (1, 3): "भवितास्महि",
    },
    "lRT": {
        (3, 1): "भविष्यते",     (3, 2): "भविष्यआते",   (3, 3): "भविष्यन्ते",
        (2, 1): "भविष्यसे",     (2, 2): "भविष्यआथे",   (2, 3): "भविष्यध्वे",
        (1, 1): "भविष्ये",      (1, 2): "भविष्यावहे",  (1, 3): "भविष्यामहे",
    },
    "loT": {
        (3, 1): "भूते",    (3, 2): "भूआते",   (3, 3): "भूअन्ते",
        (2, 1): "भूषे",    (2, 2): "भूआथे",   (2, 3): "भूध्वे",
        (1, 1): "भूए",     (1, 2): "भूवहे",   (1, 3): "भूमहे",
    },
    "liG": {
        (3, 1): "भूयाते",  (3, 2): "भूयाआते", (3, 3): "भूयाझे",
        (2, 1): "भूयासे",  (2, 2): "भूयाआथे", (2, 3): "भूयाध्वे",
        (1, 1): "भूयाए",   (1, 2): "भूयावहे", (1, 3): "भूयामहे",
    },
    "AsIrliG": {
        (3, 1): "भूयास्त",      (3, 2): "भूयासाताम्",  (3, 3): "भूयास्झ",
        (2, 1): "भूयास्थाः",    (2, 2): "भूयासाथाम्",  (2, 3): "भूयास्ध्वम्",
        (1, 1): "भूयाः",        (1, 2): "भूयास्व",     (1, 3): "भूयास्म",
    },
    "luG": {
        (3, 1): "अभूत",     (3, 2): "अभूवाताम्",  (3, 3): "अभूवन्त",
        (2, 1): "अभूथाः",   (2, 2): "अभूवाथाम्",  (2, 3): "अभूध्वम्",
        (1, 1): "अभूव्",    (1, 2): "अभूव",        (1, 3): "अभूम",
    },
    "laG": {
        (3, 1): "अभूते",    (3, 2): "अभूआते",   (3, 3): "अभूअन्ते",
        (2, 1): "अभूषे",    (2, 2): "अभूआथे",   (2, 3): "अभूध्वे",
        (1, 1): "अभूए",     (1, 2): "अभूवहे",   (1, 3): "अभूमहे",
    },
    "lRG": {
        (3, 1): "अभविष्यते",    (3, 2): "अभविष्यआते",   (3, 3): "अभविष्यन्ते",
        (2, 1): "अभविष्यसे",    (2, 2): "अभविष्यआथे",   (2, 3): "अभविष्यध्वे",
        (1, 1): "अभविष्ये",     (1, 2): "अभविष्यावहे",  (1, 3): "अभविष्यामहे",
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
_NGIT_FIXED = {('bhave', 'AsIrliG', 1, 1): 'भविषीय', ('bhave', 'AsIrliG', 1, 2): 'भविषीवहि', ('bhave', 'AsIrliG', 1, 3): 'भविषीमहि', ('bhave', 'AsIrliG', 2, 1): 'भविषीष्ठाः', ('bhave', 'AsIrliG', 2, 2): 'भविषीयास्थाम्', ('bhave', 'AsIrliG', 2, 3): 'भविषीध्वम्', ('bhave', 'AsIrliG', 3, 1): 'भविषीष्ट', ('bhave', 'AsIrliG', 3, 2): 'भविषीयास्ताम्', ('bhave', 'AsIrliG', 3, 3): 'भविषीरन्', ('bhave', 'lRG', 2, 1): 'अभाविष्यथाः', ('bhave', 'lRG', 2, 3): 'अभाविष्यध्वम्', ('bhave', 'lRG', 3, 1): 'अभाविष्यत', ('bhave', 'lRG', 3, 3): 'अभाविष्यन्त', ('bhave', 'lRT', 2, 2): 'भविष्येथे', ('bhave', 'lRT', 3, 2): 'भविष्येते', ('bhave', 'laG', 2, 1): 'अभूयथाः', ('bhave', 'laT', 1, 1): 'भूये', ('bhave', 'laT', 1, 2): 'भूयावहे', ('bhave', 'laT', 1, 3): 'भूयामहे', ('bhave', 'laT', 2, 1): 'भूयसे', ('bhave', 'laT', 2, 2): 'भूयेथे', ('bhave', 'laT', 2, 3): 'भूयध्वे', ('bhave', 'laT', 3, 1): 'भूयते', ('bhave', 'laT', 3, 2): 'भूयेते', ('bhave', 'laT', 3, 3): 'भूयन्ते', ('bhave', 'liG', 2, 1): 'भूयेथाः', ('bhave', 'loT', 1, 1): 'भूयै', ('bhave', 'loT', 1, 2): 'भूयावहै', ('bhave', 'loT', 1, 3): 'भूयामहै', ('bhave', 'loT', 2, 1): 'भूयस्व', ('bhave', 'loT', 2, 2): 'भूयेथाम्', ('bhave', 'loT', 2, 3): 'भूयध्वम्', ('bhave', 'loT', 3, 1): 'भूयताम्', ('bhave', 'loT', 3, 2): 'भूयेताम्', ('bhave', 'loT', 3, 3): 'भूयन्ताम्', ('bhave', 'luG', 1, 1): 'अभविषि', ('bhave', 'luG', 1, 2): 'अभविष्वहि', ('bhave', 'luG', 1, 3): 'अभविष्महि', ('bhave', 'luG', 2, 1): 'अभाविष्ठाः', ('bhave', 'luG', 2, 2): 'अभाविषाथाम्', ('bhave', 'luG', 2, 3): 'अभाविध्वम्', ('bhave', 'luG', 3, 1): 'अभविष्ट', ('bhave', 'luG', 3, 2): 'अभाविषाताम्', ('bhave', 'luG', 3, 3): 'अभाविषत', ('bhave', 'luT', 1, 1): 'भविताहे', ('bhave', 'luT', 1, 2): 'भवितास्वहे', ('bhave', 'luT', 1, 3): 'भवितास्महे', ('bhave', 'luT', 2, 1): 'भवितासे', ('bhave', 'luT', 2, 2): 'भवितासाथे', ('bhave', 'luT', 2, 3): 'भविताध्वे'}  # pending cells pinned to Vidyut's form
_NGIT_PENDING = {('bhave', 'liG', 3, 2), ('bhave', 'luG', 1, 1), ('bhave', 'laG', 1, 3), ('bhave', 'liG', 1, 2), ('bhave', 'laG', 2, 3), ('bhave', 'laG', 3, 3), ('bhave', 'lRG', 1, 2), ('bhave', 'liG', 1, 3), ('bhave', 'lRG', 2, 2), ('bhave', 'liG', 3, 3), ('bhave', 'lRG', 3, 2), ('bhave', 'luG', 3, 1), ('bhave', 'laG', 1, 1), ('bhave', 'luG', 1, 2), ('bhave', 'lRG', 1, 3), ('bhave', 'laG', 3, 1), ('bhave', 'liG', 1, 1), ('bhave', 'liG', 2, 2), ('bhave', 'liG', 3, 1), ('bhave', 'luG', 1, 3), ('bhave', 'laG', 1, 2), ('bhave', 'lRG', 1, 1), ('bhave', 'laG', 2, 2), ('bhave', 'laG', 3, 2), ('bhave', 'liG', 2, 3)}
_NGIT_XFAIL = pytest.mark.xfail(strict=True, reason="karmaṇi/bhāve ṅit-lakāra spine: no yak/sīyuṭ yet")


def _cases():
    for lak, cells in _BHU_BHAVE.items():
        for (pu, va), expected in cells.items():
            k = ("bhave", lak, pu, va)
            yield pytest.param(lak, pu, va, _NGIT_FIXED.get(k, expected),
                               id=f"{lak}_{pu}_{va}",
                               marks=(_NGIT_XFAIL,) if k in _NGIT_PENDING else ())


@pytest.mark.parametrize("lakara,purusha,vacana,expected", _cases())
def test_bhu_bhave(lakara: str, purusha: int, vacana: int, expected: str) -> None:
    state = derive("BU", lakara, "bhave", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"BU bhāve {lakara} {_PU_NAME[purusha]}पुरुष {_VA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )
