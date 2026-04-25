"""
1.2.45 *arthavadadhāturapratyayaḥ prātipadikam* — *prātipadika* on *avyutpanna* stems.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_metadata():
    r = SUTRA_REGISTRY["1.2.45"]
    assert r.sutra_id == "1.2.45"
    assert r.sutra_type is SutraType.SAMJNA
    assert "प्रातिपदिक" in r.text_dev


def test_subanta_stem_gets_pratipadika_registry():
    from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7

    s = build_initial_state("rAma", 1, 1, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    assert "prātipadika" in s.terms[0].tags
    assert 0 in s.samjna_registry.get("1.2.45_arthavad_pratipadika_indices", frozenset())


def test_dhatu_stem_skipped():
    t = Term(
        kind="prakriti",
        varnas=[mk("p"), mk("a"), mk("c")],
        tags={"prātipadika", "anga", "dhatu"},
        meta={"upadesha_slp1": "pac"},
    )
    s0 = State(terms=[t])
    s1 = apply_rule("1.2.45", s0)
    assert s1.samjna_registry.get("1.2.45_arthavad_pratipadika_indices") in (None, frozenset())


def test_vyutpanna_meta_skipped():
    t = Term(
        kind="prakriti",
        varnas=[mk("g"), mk("a"), mk("j"), mk("a")],
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "gaja", "vyutpanna": True},
    )
    s0 = State(terms=[t])
    s1 = apply_rule("1.2.45", s0)
    assert 0 not in (s1.samjna_registry.get("1.2.45_arthavad_pratipadika_indices") or frozenset())
