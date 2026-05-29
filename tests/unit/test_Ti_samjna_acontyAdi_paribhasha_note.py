"""Unit tests for ``pipelines/Ti_samjna_acontyAdi_paribhasha_P043_note_demo.py`` (**P043**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.Ti_samjna_acontyAdi_paribhasha_P043_note_demo import (
    derive_Ti_samjna_acontyAdi_paribhasha_P043_note,
)
from sutras.adhyaya_1.pada_1.sutra_1_1_64 import P043_QUEUE_KEY, P043_WORD_META


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def _term_by_p043_word(s, w: str):
    for t in s.terms:
        if t.meta.get(P043_WORD_META) == w:
            return t
    raise AssertionError(w)


def test_P043_trace_order_and_ti_segments():
    s = derive_Ti_samjna_acontyAdi_paribhasha_P043_note()
    assert _trace_ids(s) == ["1.1.68", "1.1.64", "1.1.64", "1.1.64", "1.1.64", "1.1.64"]
    assert s.meta.get("1_1_68_svadrupa_audit_done") is True
    assert s.meta.get(P043_QUEUE_KEY) == []
    assert s.samjna_registry.get("1.1.64_P043_acontyAdi_Ti_paribhasha") is True
    assert s.samjna_registry.get("1.1.64_P043_Ti_samjna_siddhi") is True
    assert s.samjna_registry.get("1.1.64_P043_Ti_bhaga::paceyAtAm") == "Am"
    assert s.samjna_registry.get("1.1.64_P043_Ti_bhaga::agnicit") == "it"
    assert s.samjna_registry.get("1.1.64_P043_Ti_bhaga::somasut") == "ut"

    t1 = _term_by_p043_word(s, "paceyAtAm")
    t2 = _term_by_p043_word(s, "agnicit")
    t3 = _term_by_p043_word(s, "somasut")
    assert t1.meta.get("1_1_64_ti_segment_slp1") == "Am"
    assert t2.meta.get("1_1_64_ti_segment_slp1") == "it"
    assert t3.meta.get("1_1_64_ti_segment_slp1") == "ut"
    assert "Ti" in t1.varnas[7].tags
    assert "Ti" in t2.varnas[5].tags
    assert "Ti" in t3.varnas[5].tags
