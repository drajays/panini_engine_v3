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
_NGIT_FIXED = {('bhave', 'AsIrliG', 1, 1): 'पक्षीय', ('bhave', 'AsIrliG', 1, 2): 'पक्षीवहि', ('bhave', 'AsIrliG', 1, 3): 'पक्षीमहि', ('bhave', 'AsIrliG', 2, 1): 'पक्षीष्ठाः', ('bhave', 'AsIrliG', 2, 2): 'पक्षीयास्थाम्', ('bhave', 'AsIrliG', 2, 3): 'पक्षीध्वम्', ('bhave', 'AsIrliG', 3, 1): 'पक्षीष्ट', ('bhave', 'AsIrliG', 3, 2): 'पक्षीयास्ताम्', ('bhave', 'AsIrliG', 3, 3): 'पक्षीरन्', ('bhave', 'lRG', 1, 1): 'अपक्ष्ये', ('bhave', 'lRG', 1, 2): 'अपक्ष्यावहि', ('bhave', 'lRG', 1, 3): 'अपक्ष्यामहि', ('bhave', 'lRG', 2, 1): 'अपक्ष्यथाः', ('bhave', 'lRG', 2, 2): 'अपक्ष्येथाम्', ('bhave', 'lRG', 2, 3): 'अपक्ष्यध्वम्', ('bhave', 'lRG', 3, 1): 'अपक्ष्यत', ('bhave', 'lRG', 3, 2): 'अपक्ष्येताम्', ('bhave', 'lRG', 3, 3): 'अपक्ष्यन्त', ('bhave', 'lRT', 1, 1): 'पक्ष्ये', ('bhave', 'lRT', 1, 2): 'पक्ष्यावहे', ('bhave', 'lRT', 1, 3): 'पक्ष्यामहे', ('bhave', 'lRT', 2, 1): 'पक्ष्यसे', ('bhave', 'lRT', 2, 2): 'पक्ष्येथे', ('bhave', 'lRT', 2, 3): 'पक्ष्यध्वे', ('bhave', 'lRT', 3, 1): 'पक्ष्यते', ('bhave', 'lRT', 3, 2): 'पक्ष्येते', ('bhave', 'lRT', 3, 3): 'पक्ष्यन्ते', ('bhave', 'laG', 1, 1): 'अपच्ये', ('bhave', 'laG', 1, 2): 'अपच्यावहि', ('bhave', 'laG', 1, 3): 'अपच्यामहि', ('bhave', 'laG', 2, 1): 'अपच्यथाः', ('bhave', 'laG', 2, 2): 'अपच्येथाम्', ('bhave', 'laG', 2, 3): 'अपच्यध्वम्', ('bhave', 'laG', 3, 1): 'अपच्यत', ('bhave', 'laG', 3, 2): 'अपच्येताम्', ('bhave', 'laG', 3, 3): 'अपच्यन्त', ('bhave', 'laT', 1, 1): 'पच्ये', ('bhave', 'laT', 1, 2): 'पच्यावहे', ('bhave', 'laT', 1, 3): 'पच्यामहे', ('bhave', 'laT', 2, 1): 'पच्यसे', ('bhave', 'laT', 2, 2): 'पच्येथे', ('bhave', 'laT', 2, 3): 'पच्यध्वे', ('bhave', 'laT', 3, 1): 'पच्यते', ('bhave', 'laT', 3, 2): 'पच्येते', ('bhave', 'laT', 3, 3): 'पच्यन्ते', ('bhave', 'liG', 1, 1): 'पच्येय', ('bhave', 'liG', 1, 2): 'पच्येवहि', ('bhave', 'liG', 1, 3): 'पच्येमहि', ('bhave', 'liG', 2, 1): 'पच्येथाः', ('bhave', 'liG', 2, 2): 'पच्येयाथाम्', ('bhave', 'liG', 2, 3): 'पच्येध्वम्', ('bhave', 'liG', 3, 1): 'पच्येत', ('bhave', 'liG', 3, 2): 'पच्येयाताम्', ('bhave', 'liG', 3, 3): 'पच्येरन्', ('bhave', 'liT', 1, 1): 'पेचे', ('bhave', 'liT', 1, 2): 'पेचिवहे', ('bhave', 'liT', 1, 3): 'पेचिमहे', ('bhave', 'liT', 2, 1): 'पेचिषे', ('bhave', 'liT', 2, 2): 'पेचाथे', ('bhave', 'liT', 2, 3): 'पेचिध्वे', ('bhave', 'liT', 3, 1): 'पेचे', ('bhave', 'liT', 3, 2): 'पेचाते', ('bhave', 'liT', 3, 3): 'पेचिरे', ('bhave', 'loT', 1, 1): 'पच्यै', ('bhave', 'loT', 1, 2): 'पच्यावहै', ('bhave', 'loT', 1, 3): 'पच्यामहै', ('bhave', 'loT', 2, 1): 'पच्यस्व', ('bhave', 'loT', 2, 2): 'पच्येथाम्', ('bhave', 'loT', 2, 3): 'पच्यध्वम्', ('bhave', 'loT', 3, 1): 'पच्यताम्', ('bhave', 'loT', 3, 2): 'पच्येताम्', ('bhave', 'loT', 3, 3): 'पच्यन्ताम्', ('bhave', 'luG', 1, 1): 'अपक्षि', ('bhave', 'luG', 1, 2): 'अपक्ष्वहि', ('bhave', 'luG', 1, 3): 'अपक्ष्महि', ('bhave', 'luG', 2, 1): 'अपक्थाः', ('bhave', 'luG', 2, 2): 'अपक्षाथाम्', ('bhave', 'luG', 2, 3): 'अपग्ध्वम्', ('bhave', 'luG', 3, 1): 'अपाचि', ('bhave', 'luG', 3, 2): 'अपक्षाताम्', ('bhave', 'luG', 3, 3): 'अपक्षत', ('bhave', 'luT', 1, 1): 'पक्ताहे', ('bhave', 'luT', 1, 2): 'पक्तास्वहे', ('bhave', 'luT', 1, 3): 'पक्तास्महे', ('bhave', 'luT', 2, 1): 'पक्तासे', ('bhave', 'luT', 2, 2): 'पक्तासाथे', ('bhave', 'luT', 2, 3): 'पक्ताध्वे', ('bhave', 'luT', 3, 1): 'पक्ता', ('bhave', 'luT', 3, 2): 'पक्तारौ', ('bhave', 'luT', 3, 3): 'पक्तारः', ('karmani', 'AsIrliG', 1, 1): 'पक्षीय', ('karmani', 'AsIrliG', 1, 2): 'पक्षीवहि', ('karmani', 'AsIrliG', 1, 3): 'पक्षीमहि', ('karmani', 'AsIrliG', 2, 1): 'पक्षीष्ठाः', ('karmani', 'AsIrliG', 2, 2): 'पक्षीयास्थाम्', ('karmani', 'AsIrliG', 2, 3): 'पक्षीध्वम्', ('karmani', 'AsIrliG', 3, 1): 'पक्षीष्ट', ('karmani', 'AsIrliG', 3, 2): 'पक्षीयास्ताम्', ('karmani', 'AsIrliG', 3, 3): 'पक्षीरन्', ('karmani', 'lRG', 1, 1): 'अपक्ष्ये', ('karmani', 'lRG', 1, 2): 'अपक्ष्यावहि', ('karmani', 'lRG', 1, 3): 'अपक्ष्यामहि', ('karmani', 'lRG', 2, 1): 'अपक्ष्यथाः', ('karmani', 'lRG', 2, 2): 'अपक्ष्येथाम्', ('karmani', 'lRG', 2, 3): 'अपक्ष्यध्वम्', ('karmani', 'lRG', 3, 1): 'अपक्ष्यत', ('karmani', 'lRG', 3, 2): 'अपक्ष्येताम्', ('karmani', 'lRG', 3, 3): 'अपक्ष्यन्त', ('karmani', 'lRT', 1, 1): 'पक्ष्ये', ('karmani', 'lRT', 1, 2): 'पक्ष्यावहे', ('karmani', 'lRT', 1, 3): 'पक्ष्यामहे', ('karmani', 'lRT', 2, 1): 'पक्ष्यसे', ('karmani', 'lRT', 2, 2): 'पक्ष्येथे', ('karmani', 'lRT', 2, 3): 'पक्ष्यध्वे', ('karmani', 'lRT', 3, 1): 'पक्ष्यते', ('karmani', 'lRT', 3, 2): 'पक्ष्येते', ('karmani', 'lRT', 3, 3): 'पक्ष्यन्ते', ('karmani', 'laG', 1, 1): 'अपच्ये', ('karmani', 'laG', 1, 2): 'अपच्यावहि', ('karmani', 'laG', 1, 3): 'अपच्यामहि', ('karmani', 'laG', 2, 1): 'अपच्यथाः', ('karmani', 'laG', 2, 2): 'अपच्येथाम्', ('karmani', 'laG', 2, 3): 'अपच्यध्वम्', ('karmani', 'laG', 3, 1): 'अपच्यत', ('karmani', 'laG', 3, 2): 'अपच्येताम्', ('karmani', 'laG', 3, 3): 'अपच्यन्त', ('karmani', 'laT', 1, 1): 'पच्ये', ('karmani', 'laT', 1, 2): 'पच्यावहे', ('karmani', 'laT', 1, 3): 'पच्यामहे', ('karmani', 'laT', 2, 1): 'पच्यसे', ('karmani', 'laT', 2, 2): 'पच्येथे', ('karmani', 'laT', 2, 3): 'पच्यध्वे', ('karmani', 'laT', 3, 1): 'पच्यते', ('karmani', 'laT', 3, 2): 'पच्येते', ('karmani', 'laT', 3, 3): 'पच्यन्ते', ('karmani', 'liG', 1, 1): 'पच्येय', ('karmani', 'liG', 1, 2): 'पच्येवहि', ('karmani', 'liG', 1, 3): 'पच्येमहि', ('karmani', 'liG', 2, 1): 'पच्येथाः', ('karmani', 'liG', 2, 2): 'पच्येयाथाम्', ('karmani', 'liG', 2, 3): 'पच्येध्वम्', ('karmani', 'liG', 3, 1): 'पच्येत', ('karmani', 'liG', 3, 2): 'पच्येयाताम्', ('karmani', 'liG', 3, 3): 'पच्येरन्', ('karmani', 'liT', 1, 1): 'पेचे', ('karmani', 'liT', 1, 2): 'पेचिवहे', ('karmani', 'liT', 1, 3): 'पेचिमहे', ('karmani', 'liT', 2, 1): 'पेचिषे', ('karmani', 'liT', 2, 2): 'पेचाथे', ('karmani', 'liT', 2, 3): 'पेचिध्वे', ('karmani', 'liT', 3, 1): 'पेचे', ('karmani', 'liT', 3, 2): 'पेचाते', ('karmani', 'liT', 3, 3): 'पेचिरे', ('karmani', 'loT', 1, 1): 'पच्यै', ('karmani', 'loT', 1, 2): 'पच्यावहै', ('karmani', 'loT', 1, 3): 'पच्यामहै', ('karmani', 'loT', 2, 1): 'पच्यस्व', ('karmani', 'loT', 2, 2): 'पच्येथाम्', ('karmani', 'loT', 2, 3): 'पच्यध्वम्', ('karmani', 'loT', 3, 1): 'पच्यताम्', ('karmani', 'loT', 3, 2): 'पच्येताम्', ('karmani', 'loT', 3, 3): 'पच्यन्ताम्', ('karmani', 'luG', 1, 1): 'अपक्षि', ('karmani', 'luG', 1, 2): 'अपक्ष्वहि', ('karmani', 'luG', 1, 3): 'अपक्ष्महि', ('karmani', 'luG', 2, 1): 'अपक्थाः', ('karmani', 'luG', 2, 2): 'अपक्षाथाम्', ('karmani', 'luG', 2, 3): 'अपग्ध्वम्', ('karmani', 'luG', 3, 1): 'अपाचि', ('karmani', 'luG', 3, 2): 'अपक्षाताम्', ('karmani', 'luG', 3, 3): 'अपक्षत', ('karmani', 'luT', 1, 1): 'पक्ताहे', ('karmani', 'luT', 1, 2): 'पक्तास्वहे', ('karmani', 'luT', 1, 3): 'पक्तास्महे', ('karmani', 'luT', 2, 1): 'पक्तासे', ('karmani', 'luT', 2, 2): 'पक्तासाथे', ('karmani', 'luT', 2, 3): 'पक्ताध्वे', ('karmani', 'luT', 3, 1): 'पक्ता', ('karmani', 'luT', 3, 2): 'पक्तारौ', ('karmani', 'luT', 3, 3): 'पक्तारः'}  # every cell: our form if Vidyut agrees, else Vidyut's form (xfail)
# bhāve luṅ 3sg is अपाचि: 3.1.66 चिण् भावकर्मणोः covers bhāve (Kāśikā "भावे तावत् —
# अशायि भवता"); Vidyut's अपक्त for sakarmaka पच् in bhāve departs from Kāśikā.
_NGIT_PENDING: set = set()
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
            marks = (_NGIT_XFAIL,) if k in _NGIT_PENDING else ()
            yield pytest.param(lak, pu, va, _NGIT_FIXED.get(k, expected), id=f"bhave_{lak}_{pu}_{va}", marks=marks)


@pytest.mark.parametrize("lakara,purusha,vacana,expected", list(_cases_karmani()))
def test_pac_karmani(lakara: str, purusha: int, vacana: int, expected: str) -> None:
    state = derive("pac", lakara, "karmani", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"pac karmaṇi {lakara} {_PU_NAME[purusha]}पुरुष {_VA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


@pytest.mark.parametrize("lakara,purusha,vacana,expected", list(_cases_bhave()))
def test_pac_bhave(lakara: str, purusha: int, vacana: int, expected: str) -> None:
    state = derive("pac", lakara, "bhave", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"pac bhāve {lakara} {_PU_NAME[purusha]}पुरुष {_VA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )
