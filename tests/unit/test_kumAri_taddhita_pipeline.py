"""Glass-box: *kumArI* + *tarap* / *tamap* (**5.3.55** / **5.3.57**) + **6.3.43**."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.kumAri_itarA_tamA_taddhita import derive_kumAritama, derive_kumAritara


def test_kumAri_tarap_taddhita_anta():
    s = derive_kumAritara()
    assert s.flat_slp1().strip() == "kumAritara"
    assert s.samjna_registry.get("gha") is not None
    assert any(
        e.get("sutra_id") == "1.2.46" and e.get("status") == "APPLIED" for e in s.trace
    )


def test_kumAri_tamap_taddhita_anta():
    s = derive_kumAritama()
    assert s.flat_slp1().strip() == "kumAritama"


def test_6_3_43_fires_in_tarap_path():
    s = derive_kumAritara()
    steps = [e for e in s.trace if e.get("sutra_id") == "6.3.43" and e.get("status") == "APPLIED"]
    assert steps, "6.3.43 must hrasva *ī* on *kumArI* before *it*-*lopa*"
    st = steps[0]
    before = st.get("form_before") or ""
    after = st.get("form_after") or ""
    assert "I" in before
    assert "i" in after
