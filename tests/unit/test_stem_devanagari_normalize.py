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


def test_devanagari_shyama_cluster_to_slp1():
    """श्याम must stay ``SyAma`` (श्+य्+…), never ``SayAma`` (श+अ+य+…)."""
    shy = "\u0936\u094d\u092f\u093e\u092e"  # श + ् + य + ा + म
    assert devanagari_to_slp1_flat(shy) == "SyAma"


def test_build_initial_state_preserves_consonant_clusters():
    """Regression: stem parser must not insert schwa between hal-s (see ``SyAma``)."""
    from pipelines.subanta import build_initial_state
    from phonology.joiner import slp1_to_devanagari

    st = build_initial_state("SyAma", 1, 1)
    assert "".join(v.slp1 for v in st.terms[0].varnas) == "SyAma"
    assert slp1_to_devanagari(st.terms[0].varnas) == "श्याम"


def test_derive_shyama_prathama_karta():
    import sutras  # noqa: F401 — registry

    from pipelines.subanta import derive
    from phonology.joiner import slp1_to_devanagari

    s = derive("SyAma", 1, 1)
    assert slp1_to_devanagari(s.terms[0].varnas) == "श्यामः"
