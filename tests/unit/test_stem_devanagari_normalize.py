"""देवनागरी / SLP1 प्रातिपदिक नॉर्मलाइज़ेशन।"""
from __future__ import annotations

import pytest

from phonology.tokenizer import devanagari_to_slp1_flat
from streamlit_app.stem_input import (
    normalize_pratipadika_input,
    stem_slp1_to_display_devanagari,
)


def test_devanagari_to_slp1_flat_rama_gaja():
    assert devanagari_to_slp1_flat("राम") == "rAma"
    assert devanagari_to_slp1_flat("गज") == "gaja"
    assert devanagari_to_slp1_flat("रा म") == "rAma"


def test_normalize_slp1_passthrough():
    assert normalize_pratipadika_input("  rAma  ") == "rAma"
    assert normalize_pratipadika_input("gaja") == "gaja"


def test_normalize_devanagari():
    assert normalize_pratipadika_input("राम") == "rAma"
    assert normalize_pratipadika_input("गज") == "gaja"


def test_normalize_mixed_scripts_raises():
    with pytest.raises(ValueError, match="देवनागरी"):
        normalize_pratipadika_input("rआम")


def test_stem_display_roundtrip():
    assert stem_slp1_to_display_devanagari("rAma") == "राम"
    assert stem_slp1_to_display_devanagari("gaja") == "गज"
