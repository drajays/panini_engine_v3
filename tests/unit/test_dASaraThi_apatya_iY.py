"""दाशरथि derivation — दशरथ + इञ् (4.1.95 ata iñ) → दाशरथि."""
from __future__ import annotations

import sutras  # noqa: F401

from engine.trace import TRACE_STATUSES_FIRED
from pipelines.dASaraThi_apatya_iY import derive_dASaraThi


def test_dASaraThi_surface():
    s = derive_dASaraThi()
    assert s.flat_slp1() == "dASaraTi", f"got {s.flat_slp1()!r}"
    assert s.render() == "dASaraTi"


def test_dASaraThi_rule_sequence():
    s = derive_dASaraThi()
    fired = [
        e.get("sutra_id")
        for e in s.trace
        if e.get("status") in TRACE_STATUSES_FIRED and e.get("sutra_id") != "__MERGE__"
    ]
    # Core apatya + suffix attachment
    for need in ("4.1.82", "4.1.92", "4.1.95"):
        assert need in fired, f"missing {need} in {fired}"
    # it-lopa (ñ removed, it_markers set)
    assert "1.3.3" in fired
    assert "1.3.9" in fired
    # vṛddhi of first vowel (a → ā)
    assert "7.2.117" in fired
    # yasyeti ca — final a lopa before i
    assert "6.4.148" in fired
    # Ordering constraints
    assert fired.index("4.1.95") < fired.index("1.3.9")
    assert fired.index("1.3.9") < fired.index("7.2.117")
    assert fired.index("7.2.117") < fired.index("6.4.148")
