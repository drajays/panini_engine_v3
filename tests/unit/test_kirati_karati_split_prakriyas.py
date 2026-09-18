"""Unit tests for ``pipelines/kirati_karati_split_prakriyas.py`` (**P009**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.kirati_karati_split_prakriyas import (
    derive_girati_P009_sibling,
    derive_kirati_karati_split_prakriyas_P009,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def _applied(s, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and e.get("status") == "APPLIED" for e in s.trace
    )


def test_P009_kirati_via_7_1_100_not_7_3_84_guna():
    """
    कॄ (विक्षेपे, तुदादिः) + तिप् → किरति — 7.1.100 (ॠ→इ) fires, not 7.3.84's
    guṇa (Mīmāṃsaka Aṣṭādhyāyī-Bhāṣya pariśiṣṭa, PDF p.643-644).
    """
    s = derive_kirati_karati_split_prakriyas_P009()
    ids = _trace_ids(s)

    assert ids.index("3.4.78") < ids.index("3.1.77")
    assert ids.index("3.1.77") < ids.index("1.3.8") < ids.index("7.1.100")
    assert ids.index("7.1.100") < ids.index("7.3.84") < ids.index("1.1.51")
    assert ids.index("1.1.51") < ids.index("1.3.3")

    assert _applied(s, "7.1.100")
    assert not _applied(s, "7.3.84")  # declines: 7.1.100 already marked the aṅga done

    assert s.flat_slp1() == "kirati"


def test_P009_girati_sibling_same_mechanism():
    """गॄ (निगरणे) + तिप् → गिरति — identical F→i mechanism, different root."""
    s = derive_girati_P009_sibling()
    assert _applied(s, "7.1.100")
    assert not _applied(s, "7.3.84")
    assert s.flat_slp1() == "girati"
