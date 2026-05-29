"""
6.1.125 प्लुतप्रगृह्याच्च नित्यम् अचि — pluta + ac-initial = prakṛti-bhāva.

Test suite for pipelines/kRzRa3_atra_pluta_pragraha_demo.py:
  1. Surface: "kRzRa3 atra" (pluta marker '3' appended, no sandhi)
  2. 6.1.125 fires (APPLIED in trace)
  3. samjna_registry records the boundary
  4. atra term's _META_ACK is stamped (guards 6.1.101 suppression)
  5. Negative: without "pluta" tag, 6.1.125 does NOT fire
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from engine.trace import TRACE_STATUSES_FIRED
from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.kRzRa3_atra_pluta_pragraha_demo import (
    derive_kRzRa3_atra_pluta_pragraha,
    render_kRzRa3_atra,
    _render_pluta_vakya,
)

# The meta-ack key from 6.1.125
_META_ACK = "6_1_125_prakRti_aci_ack"
_REGISTRY_KEY = "6.1.125_prakRti_aci"


class TestPlutaSurface:
    def test_render_includes_pluta_mark(self):
        assert render_kRzRa3_atra() == "kRzRa3 atra"

    def test_state_flat_slp1_has_no_sandhi(self):
        s = derive_kRzRa3_atra_pluta_pragraha()
        # Forms should stay separate; no a+a → ā merger
        flat = s.flat_slp1()
        assert "kRzRa" in flat
        assert "atra" in flat
        assert "kRzRAtra" not in flat  # no savarna-dīrgha sandhi


class TestRule6_1_125Fires:
    def test_6_1_125_applied(self):
        s = derive_kRzRa3_atra_pluta_pragraha()
        fired = {
            e.get("sutra_id")
            for e in s.trace
            if e.get("status") in TRACE_STATUSES_FIRED
        }
        assert "6.1.125" in fired, f"6.1.125 not in fired: {fired}"

    def test_samjna_registry_records_boundary(self):
        s = derive_kRzRa3_atra_pluta_pragraha()
        assert s.samjna_registry.get(_REGISTRY_KEY, 0) >= 1

    def test_atra_ack_stamped(self):
        s = derive_kRzRa3_atra_pluta_pragraha()
        # atra is terms[1]; its _META_ACK should be set
        assert s.terms[1].meta.get(_META_ACK), (
            "6.1.125 should stamp _META_ACK on the ac-initial term"
        )


class TestPlutagRender:
    def test_pluta_tag_gives_3_suffix(self):
        t = Term(
            kind="prakriti",
            varnas=parse_slp1_upadesha_sequence("kRzRa"),
            tags={"prātipadika", "pluta"},
            meta={},
        )
        s = State(terms=[t], meta={}, trace=[])
        assert _render_pluta_vakya(s) == "kRzRa3"

    def test_no_pluta_tag_no_suffix(self):
        t = Term(
            kind="prakriti",
            varnas=parse_slp1_upadesha_sequence("kRzRa"),
            tags={"prātipadika"},
            meta={},
        )
        s = State(terms=[t], meta={}, trace=[])
        assert _render_pluta_vakya(s) == "kRzRa"


class TestNegative:
    """Without 'pluta' tag, 6.1.125 should NOT fire."""

    def test_no_pluta_tag_6_1_125_skipped(self):
        kRzRa_nonpluta = Term(
            kind="prakriti",
            varnas=parse_slp1_upadesha_sequence("kRzRa"),
            tags={"prātipadika"},          # no "pluta"
            meta={"upadesha_slp1": "kRzRa"},
        )
        atra = Term(
            kind="prakriti",
            varnas=parse_slp1_upadesha_sequence("atra"),
            tags={"avyaya"},
            meta={"upadesha_slp1": "atra"},
        )
        s = State(terms=[kRzRa_nonpluta, atra], meta={}, trace=[])
        s2 = apply_rule("6.1.125", s)
        fired = {
            e.get("sutra_id")
            for e in s2.trace
            if e.get("status") in TRACE_STATUSES_FIRED
        }
        assert "6.1.125" not in fired
        # ack should NOT be stamped
        assert not s2.terms[1].meta.get(_META_ACK)
