"""
T3 precursor — P019 *avartsyat* (वृत् + lṛṅ) vs canonical ``derive``.

Gold: corrected_prakriyas_v2 P019 → ``avartsyat`` / अवर्त्स्यत्.
Canonical ``derive('vftu~', 'lRG', 'kartari', 3, 1)`` uses ``_derive_lRG_ṛ_dhatu`` (P019 spine).
"""
from __future__ import annotations

import pytest

from pipelines.avartsyat_lRG_vf_corrected_P019_demo import (
    derive_avartsyat_lRG_vf_corrected_P019,
)
from pipelines.tinanta import derive

_P019_DEMO_SLP1 = "avartsyat"
_P019_DEMO_DEV = "अवर्त्स्यत्"


def test_p019_demo_surface():
    s = derive_avartsyat_lRG_vf_corrected_P019()
    assert s.flat_slp1() == _P019_DEMO_SLP1
    assert s.flat_dev() == _P019_DEMO_DEV


def test_vftu_canonical_lrg_matches_p019():
    s = derive("vftu~", "lRG", "kartari", 3, 1)
    assert s.flat_slp1() == _P019_DEMO_SLP1
    assert s.flat_dev() == _P019_DEMO_DEV
