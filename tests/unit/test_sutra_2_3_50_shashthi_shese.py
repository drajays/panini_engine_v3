"""
2.3.50 *ṣaṣṭhī śeṣe* — vibhakti selection helper (opt-in meta flag).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology.varna import mk_inherent_a
from phonology import mk

from pipelines.subanta import (
    build_initial_state,
    run_subanta_preflight_through_1_4_7,
)
from sutras.adhyaya_2.pada_3.sutra_2_3_50 import META_OVERRIDE_VV, META_SHESE_ELIGIBLE


def test_registry():
    r = SUTRA_REGISTRY["2.3.50"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "zazWI" in r.text_slp1
    assert "शेषे" in r.text_dev
    assert "2.3.1" in r.anuvritti_from


def test_preflight_sets_vibhakti_vacana_to_6_1_when_opted_in():
    s0 = build_initial_state("rAma", 1, 1, sheSa_shashthi_2_3_50=True)
    assert s0.meta.get(META_SHESE_ELIGIBLE) is True
    # Caller may have supplied any coordinate; 2.3.50 overrides by default.
    assert s0.meta.get("vibhakti_vacana") == "1-1"

    s1 = run_subanta_preflight_through_1_4_7(s0)
    ids = [step["sutra_id"] for step in s1.trace]
    assert "2.3.1" in ids
    assert "2.3.50" in ids
    assert s1.meta.get("vibhakti_vacana") == "6-1"


def test_4_1_2_attaches_genitive_singular_Nas_after_2_3_50():
    s0 = build_initial_state("rAma", 1, 1, sheSa_shashthi_2_3_50=True)
    s1 = run_subanta_preflight_through_1_4_7(s0)
    s2 = apply_rule("4.1.2", s1)
    sup_terms = [t for t in s2.terms if t.kind == "pratyaya" and "sup" in t.tags]
    assert len(sup_terms) == 1
    assert sup_terms[0].meta.get("upadesha_slp1") == "Nas"


def test_no_override_mode_respects_existing_vibhakti_vacana():
    # Minimal state (avoid full subanta preflight): open adhikara and apply 2.3.50.
    stem = Term(
        kind="prakriti",
        varnas=[mk("r"), mk("A"), mk("m"), mk_inherent_a()],
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "rAma"},
    )
    s0 = State(terms=[stem])
    s0.meta["vibhakti_vacana"] = "7-1"
    s0.meta[META_SHESE_ELIGIBLE] = True
    s0.meta[META_OVERRIDE_VV] = False

    s1 = apply_rule("2.3.1", s0)
    s2 = apply_rule("2.3.50", s1)
    assert s2.meta.get("vibhakti_vacana") == "7-1"

