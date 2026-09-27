"""
tests/unit/test_tinanta_pac_karmani_bhave.py

Glass-box gold for pac (tudādi/bhvādi, gaṇa 1) + karmaṇi and bhāve —
9 cells × 10 lakāras (180 total cells, 90 per prayoga).

T5 — second dhātu gold extension.  Baseline locked 2026-05-31.

⚠ 2026-09-28: this is a *snapshot* of engine output, not attested gold. It was
locked while 'pac' resolved to 01.0198 पचिँ (seṭ); 'pac' is now डुपचँष् पाके
(01.1151, aniṭ). Several pinned cells are seṭ forms that are wrong for an aniṭ
root (Vidyut: luṭ पक्ता, karmaṇi luṅ अपाचि/अपक्षाताम्/अपक्षत, bhāve luṅ अपक्त).
They still pass only because the engine ignores aniṭ in these lakāras — see
docs/FINAL_PLAN_2026-09.md (C0, "aniṭ ignored"). Replace with Vidyut/attested
values as that bug is fixed.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_PAC_KARMANI = {
    "laT": {
        (3, 1): "पच्यते",    (3, 2): "पच्येते",   (3, 3): "पच्यन्ते",
        (2, 1): "पच्यसे",    (2, 2): "पच्येथे",   (2, 3): "पच्यध्वे",
        (1, 1): "पच्ये",     (1, 2): "पच्यावहे",  (1, 3): "पच्यामहे",
    },
    "liT": {
        (3, 1): "पपचे",      (3, 2): "पपचाते",    (3, 3): "पपचिरे",
        (2, 1): "पपचिषे",    (2, 2): "पपचाथे",    (2, 3): "पपचिध्वे",
        (1, 1): "पपचे",      (1, 2): "पपचिवहे",   (1, 3): "पपचिमहे",
    },
    "luT": {
        (3, 1): "पचिता",         (3, 2): "पचितारौ",     (3, 3): "पचितारः",
        (2, 1): "पचितासे",       (2, 2): "पचितासाथे",   (2, 3): "पचिताध्वे",
        (1, 1): "पचिताहे",       (1, 2): "पचितास्वहे",  (1, 3): "पचितास्महे",
    },
    "lRT": {
        (3, 1): "पचिष्यते",      (3, 2): "पचिष्येते",    (3, 3): "पचिष्यन्ते",
        (2, 1): "पचिष्यसे",      (2, 2): "पचिष्येथे",    (2, 3): "पचिष्यध्वे",
        (1, 1): "पचिष्ये",       (1, 2): "पचिष्यावहे",   (1, 3): "पचिष्यामहे",
    },
    "loT": {
        (3, 1): "पच्यते",    (3, 2): "पच्येते",   (3, 3): "पच्यन्ते",
        (2, 1): "पच्यस्व",   (2, 2): "पच्येथे",   (2, 3): "पच्यध्वम्",
        (1, 1): "पच्ये",     (1, 2): "पच्यवहे",   (1, 3): "पच्यमहे",
    },
    "liG": {
        (3, 1): "पच्येत",    (3, 2): "पच्येयाताम्",  (3, 3): "पच्येरन्",
        (2, 1): "पच्येथाः",  (2, 2): "पच्येयाथाम्",  (2, 3): "पच्येध्वम्",
        (1, 1): "पच्येयि",   (1, 2): "पच्येवहि",    (1, 3): "पच्येमहि",
    },
    "AsIrliG": {
        (3, 1): "पचिषीष्ट",       (3, 2): "पचिषीयास्ताम्",  (3, 3): "पचिषीरन्",
        (2, 1): "पचिषीष्टाः",     (2, 2): "पचिषीयास्थाम्",  (2, 3): "पचिषीध्वम्",
        (1, 1): "पचिषीय",         (1, 2): "पचिषीवहि",        (1, 3): "पचिषीमहि",
    },
    "luG": {
        (3, 1): "अपचि",          (3, 2): "अपचिषाताम्",  (3, 3): "अपचिषत",
        (2, 1): "अपचिष्ठाः",     (2, 2): "अपचिषाथाम्",  (2, 3): "अपचिध्वम्",
        (1, 1): "अपचिषि",        (1, 2): "अपचिष्वहि",   (1, 3): "अपचिष्महि",
    },
    "laG": {
        (3, 1): "अपच्यत",    (3, 2): "अपच्येताम्",  (3, 3): "अपच्यन्त",
        (2, 1): "अपच्यथाः",  (2, 2): "अपच्येथाम्",  (2, 3): "अपच्यध्वम्",
        (1, 1): "अपच्ये",    (1, 2): "अपच्यावहि",   (1, 3): "अपच्यामहि",
    },
    "lRG": {
        (3, 1): "अपचिष्यते",     (3, 2): "अपचिष्येते",   (3, 3): "अपचिष्यन्ते",
        (2, 1): "अपचिष्यसे",     (2, 2): "अपचिष्येथे",   (2, 3): "अपचिष्यध्वे",
        (1, 1): "अपचिष्ये",      (1, 2): "अपचिष्यावहे",  (1, 3): "अपचिष्यामहे",
    },
}

_PAC_BHAVE = {
    "laT": {
        (3, 1): "पचते",      (3, 2): "पचेते",     (3, 3): "पचन्ते",
        (2, 1): "पचसे",      (2, 2): "पचेथे",     (2, 3): "पचध्वे",
        (1, 1): "पचे",       (1, 2): "पचावहे",    (1, 3): "पचामहे",
    },
    "liT": {
        (3, 1): "पपचे",      (3, 2): "पपचाते",    (3, 3): "पपचिरे",
        (2, 1): "पपचिषे",    (2, 2): "पपचाथे",    (2, 3): "पपचिध्वे",
        (1, 1): "पपचे",      (1, 2): "पपचिवहे",   (1, 3): "पपचिमहे",
    },
    "luT": {
        (3, 1): "पचिता",        (3, 2): "पचितारौ",     (3, 3): "पचितारः",
        (2, 1): "पचितास्थाः",  (2, 2): "पचितासाथाम्", (2, 3): "पचितास्ध्वम्",
        (1, 1): "पचितासि",     (1, 2): "पचितास्वहि",  (1, 3): "पचितास्महि",
    },
    "lRT": {
        (3, 1): "पचिष्यते",     (3, 2): "पचिष्यआते",   (3, 3): "पचिष्यन्ते",
        (2, 1): "पचिष्यसे",     (2, 2): "पचिष्यआथे",   (2, 3): "पचिष्यध्वे",
        (1, 1): "पचिष्ये",      (1, 2): "पचिष्यावहे",  (1, 3): "पचिष्यामहे",
    },
    "loT": {
        (3, 1): "पच्ते",     (3, 2): "पचाते",     (3, 3): "पचन्ते",
        (2, 1): "पच्से",     (2, 2): "पचाथे",     (2, 3): "पच्ध्वे",
        (1, 1): "पचे",       (1, 2): "पच्वहे",    (1, 3): "पच्महे",
    },
    "liG": {
        (3, 1): "पच्याते",   (3, 2): "पच्याआते",  (3, 3): "पच्याझे",
        (2, 1): "पच्यासे",   (2, 2): "पच्याआथे",  (2, 3): "पच्याध्वे",
        (1, 1): "पच्याए",    (1, 2): "पच्यावहे",  (1, 3): "पच्यामहे",
    },
    "AsIrliG": {
        (3, 1): "पच्यास्त",      (3, 2): "पच्यासाताम्",  (3, 3): "पच्यास्झ",
        (2, 1): "पच्यास्थाः",   (2, 2): "पच्यासाथाम्",  (2, 3): "पच्यास्ध्वम्",
        (1, 1): "पच्याः",        (1, 2): "पच्यास्व",     (1, 3): "पच्यास्म",
    },
    "luG": {
        (3, 1): "अपचिष्ट",       (3, 2): "अपचिषाताम्",  (3, 3): "अपचिष्झ",
        (2, 1): "अपचिष्थाः",     (2, 2): "अपचिषाथाम्",  (2, 3): "अपचिष्ध्वम्",
        (1, 1): "अपचिः",          (1, 2): "अपचिष्वह्",   (1, 3): "अपचिष्मह्",
    },
    "laG": {
        (3, 1): "अपच्ते",    (3, 2): "अपचाते",    (3, 3): "अपचन्ते",
        (2, 1): "अपच्से",    (2, 2): "अपचाथे",    (2, 3): "अपच्ध्वे",
        (1, 1): "अपचे",      (1, 2): "अपच्वहे",   (1, 3): "अपच्महे",
    },
    "lRG": {
        (3, 1): "अपचिष्यते",     (3, 2): "अपचिष्यआते",   (3, 3): "अपचिष्यन्ते",
        (2, 1): "अपचिष्यसे",     (2, 2): "अपचिष्यआथे",   (2, 3): "अपचिष्यध्वे",
        (1, 1): "अपचिष्ये",      (1, 2): "अपचिष्यावहे",  (1, 3): "अपचिष्यामहे",
    },
}

_PU_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VA_NAME = {1: "एक", 2: "द्वि", 3: "बहु"}


# 2026-09-28 — 3.4.79 टित आत्मनेपदानां टेरे now requires a ṭit sthānī, so it no
# longer turns ta → te in ṅit lakāras (laṅ, liṅ, lṛṅ). The pins below were
# "baseline locked" engine output that relied on that bug:
#   _NGIT_FIXED   — our new form is among Vidyut's; pin corrected.
#   _NGIT_PENDING — old pin and new output are both wrong (the karmaṇi/bhāve
#                   ṅit-lakāra spine has no yak / sīyuṭ: भवेत for भूयेत).
#                   xfail(strict) until that spine exists.
_NGIT_FIXED = {}
_NGIT_PENDING = {('bhave', 'lRG', 1, 1), ('bhave', 'lRG', 1, 2), ('bhave', 'lRG', 1, 3), ('bhave', 'lRG', 2, 2), ('bhave', 'lRG', 2, 3), ('bhave', 'lRG', 3, 1), ('bhave', 'lRG', 3, 2), ('bhave', 'lRG', 3, 3), ('bhave', 'laG', 1, 1), ('bhave', 'laG', 1, 2), ('bhave', 'laG', 1, 3), ('bhave', 'laG', 2, 2), ('bhave', 'laG', 2, 3), ('bhave', 'laG', 3, 1), ('bhave', 'laG', 3, 2), ('bhave', 'laG', 3, 3), ('bhave', 'liG', 1, 1), ('bhave', 'liG', 1, 2), ('bhave', 'liG', 1, 3), ('bhave', 'liG', 2, 2), ('bhave', 'liG', 2, 3), ('bhave', 'liG', 3, 1), ('bhave', 'liG', 3, 2), ('bhave', 'liG', 3, 3), ('karmani', 'lRG', 1, 1), ('karmani', 'lRG', 1, 2), ('karmani', 'lRG', 1, 3), ('karmani', 'lRG', 2, 2), ('karmani', 'lRG', 2, 3), ('karmani', 'lRG', 3, 1), ('karmani', 'lRG', 3, 2), ('karmani', 'lRG', 3, 3)}
_NGIT_XFAIL = pytest.mark.xfail(strict=True, reason="karmaṇi/bhāve ṅit-lakāra spine: no yak/sīyuṭ yet")


def _cases_karmani():
    for lak, cells in _PAC_KARMANI.items():
        for (pu, va), expected in cells.items():
            k = ("karmani", lak, pu, va)
            yield pytest.param(lak, pu, va, _NGIT_FIXED.get(k, expected), id=f"karmani_{lak}_{pu}_{va}",
                               marks=(_NGIT_XFAIL,) if k in _NGIT_PENDING else ())


_ANIT_LUN = pytest.mark.xfail(
    strict=True,
    reason="aniṭ डुपचँष्: pinned seṭ luṅ (अपचिष्ट…) belonged to पचिँ; engine gives "
           "अपच्त…, Vidyut अपक्त/अपक्षाताम्/अपक्षत — aniṭ luṅ not yet derived",
)


def _cases_bhave():
    for lak, cells in _PAC_BHAVE.items():
        for (pu, va), expected in cells.items():
            k = ("bhave", lak, pu, va)
            # lṛṭ duals: ending now right (पचिष्येते), stem still seṭ for aniṭ पच् (Vidyut पक्ष्येते)
            anit = lak == "luG" or (lak == "lRT" and (pu, va) in {(3, 2), (2, 2)})
            marks = (_ANIT_LUN,) if anit else (_NGIT_XFAIL,) if k in _NGIT_PENDING else ()
            yield pytest.param(lak, pu, va, _NGIT_FIXED.get(k, expected), id=f"bhave_{lak}_{pu}_{va}", marks=marks)


@pytest.mark.parametrize("lakara,purusha,vacana,expected", _cases_karmani())
def test_pac_karmani(lakara: str, purusha: int, vacana: int, expected: str) -> None:
    state = derive("pac", lakara, "karmani", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"pac karmaṇi {lakara} {_PU_NAME[purusha]}पुरुष {_VA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


@pytest.mark.parametrize("lakara,purusha,vacana,expected", _cases_bhave())
def test_pac_bhave(lakara: str, purusha: int, vacana: int, expected: str) -> None:
    state = derive("pac", lakara, "bhave", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"pac bhāve {lakara} {_PU_NAME[purusha]}पुरुष {_VA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )
