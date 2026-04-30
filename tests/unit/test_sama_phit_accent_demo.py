"""``prakriya_17`` — ``sama`` + Phit / **6.1.158** accent demo."""
from __future__ import annotations

from pipelines.sama_phit_accent_demo import (
    derive_non_phit418_phiSa_stem,
    derive_sama_phit_accent,
)


def test_sama_surface_unchanged() -> None:
    s = derive_sama_phit_accent()
    assert s.flat_slp1() == "sama"


def test_sama_phit_418_registry() -> None:
    s = derive_sama_phit_accent()
    assert "sama" in s.samjna_registry.get("phit_418_sarvAnudAtta", frozenset())
    assert "phit_phiSa_anta_udAtta_candidate" not in s.samjna_registry


def test_rAma_phiSa_utsarga_candidate() -> None:
    s = derive_non_phit418_phiSa_stem()
    assert s.flat_slp1() == "rAma"
    assert "rAma" in s.samjna_registry.get("phit_phiSa_anta_udAtta_candidate", frozenset())
    assert "phit_418_sarvAnudAtta" not in s.samjna_registry


def test_trace_has_ordered_sutras() -> None:
    s = derive_sama_phit_accent()
    ids = [row.get("sutra_id") for row in s.trace if row.get("sutra_id")]
    for w in ("6.1.158", "8.1.3", "8.2.1"):
        assert w in ids
    assert ids.index("6.1.158") < ids.index("8.1.3") < ids.index("8.2.1")
