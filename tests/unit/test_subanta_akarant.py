"""Tests for अकारान्त पुंलिङ्ग pipeline helpers."""
from __future__ import annotations

import pytest

from pipelines.subanta import (
    derive_akarant_pullinga,
    stem_slp1_looks_akarant_pullinga,
)


def test_stem_akarant_positive():
    assert stem_slp1_looks_akarant_pullinga("rAma")
    assert stem_slp1_looks_akarant_pullinga("gaja")
    assert stem_slp1_looks_akarant_pullinga("  rAma  ")


def test_stem_akarant_negative():
    assert not stem_slp1_looks_akarant_pullinga("")
    assert not stem_slp1_looks_akarant_pullinga("hari")
    assert not stem_slp1_looks_akarant_pullinga("rAmaH")


def test_derive_akarant_pullinga_rejects_non_a_stem():
    with pytest.raises(ValueError, match="अकारान्त"):
        derive_akarant_pullinga("hari", 1, 1)


def test_derive_akarant_pullinga_matches_derive_rama():
    from pipelines.subanta import derive

    a = derive_akarant_pullinga("rAma", 3, 1)
    b = derive("rAma", 3, 1, linga="pulliṅga")
    assert a.render() == b.render()
