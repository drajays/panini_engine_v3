"""Unit tests for ``pipelines/bhaNguram_Ghurac_corrected_P007_demo.py`` (**P007** *kṛdanta*)."""

from __future__ import annotations

from pipelines.bhaNguram_Ghurac_corrected_P007_demo import (
    derive_bhaNgura_pratipadika_corrected_P007,
    derive_bhaNguram_corrected_P007,
)


def test_P007_pratipadika_surface():
    assert derive_bhaNgura_pratipadika_corrected_P007().flat_slp1() == "BaNgura"


def test_P007_full_pada_bhaNguram():
    assert derive_bhaNguram_corrected_P007().flat_slp1() == "BaNguram"
