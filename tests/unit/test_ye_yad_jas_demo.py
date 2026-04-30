"""Unit tests for ``pipelines/ye_yad_jas_demo.py`` (यद् + जस् → ये)."""
from __future__ import annotations

from pipelines.ye_yad_jas_demo import derive_ye_yad_jas


def test_ye_yad_jas_surface() -> None:
    s = derive_ye_yad_jas()
    assert s.flat_slp1() == "ye"


def test_ye_yad_jas_suppita_registry() -> None:
    s = derive_ye_yad_jas()
    assert "jas" in s.samjna_registry.get("suppita", frozenset())


def test_ye_yad_jas_trace_order() -> None:
    s = derive_ye_yad_jas()
    ids = [row.get("sutra_id") for row in s.trace if row.get("sutra_id")]
    # Structural / audit rows use the same ``sutra_id`` field when present.
    want = (
        "6.4.1",
        "3.1.4",
        "7.2.102",
        "6.1.84",
        "6.1.97",
        "7.1.17",
        "1.3.7",
        "1.3.9",
        "6.1.87",
        "8.2.1",
        "8.2.5",
    )
    positions = []
    for w in want:
        assert w in ids, f"missing {w} in trace"
        positions.append(ids.index(w))
    assert positions == sorted(positions), "expected monotonic sūtra order in trace"


def test_ye_yad_jas_tripadi_accent_samjna() -> None:
    s = derive_ye_yad_jas()
    assert "ye" in s.samjna_registry.get("ekadesa_udatta_8_2_5", frozenset())
