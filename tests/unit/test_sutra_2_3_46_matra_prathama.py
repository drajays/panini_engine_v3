"""
2.3.46 *prātipadikārtha-liṅga-parimāṇa-vacana-mātre prathamā* — ANUVADA.

Preflight wiring: when ``matra_prathama_2_3_46=True``, **2.3.1** opens the
*anabhihita* adhikāra and **2.3.46** fires (trace).  Default ``derive`` omits
both (no regression to existing subanta traces).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import mk_inherent_a
from pipelines.subanta import (
    build_initial_state,
    derive,
    run_subanta_preflight_through_1_4_7,
)


def test_registry_anuvada_cond():
    r = SUTRA_REGISTRY["2.3.46"]
    assert r.sutra_type.name == "ANUVADA"
    assert "anabhihite" in r.text_slp1


def test_preflight_schedules_2_3_1_and_2_3_46_when_eligible():
    stem = [mk("u"), mk("c"), mk("c"), mk_inherent_a()]
    t = Term(
        kind="prakriti",
        varnas=stem,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "ucca"},
    )
    s0 = State(terms=[t])
    s0.meta["linga"] = "pulliṅga"
    s0.meta["vibhakti_vacana"] = "7-1"
    s0.meta["2_3_46_matra_prathama_eligible"] = True
    s1 = run_subanta_preflight_through_1_4_7(s0)
    ids = [step["sutra_id"] for step in s1.trace]
    assert "2.3.1" in ids
    assert "2.3.46" in ids
    # Later preflight rules (e.g. 4.1.1) are numerically past 2.3.73, so
    # ``purge_closed_adhikaras`` clears the 2.3.1 stack entry — expected.
    assert any(
        step["sutra_id"] == "2.3.1" and step.get("status") == "APPLIED"
        for step in s1.trace
    )


def test_derive_default_has_no_2_3_46():
    s = derive("rAma", 1, 1)
    assert "2.3.46" not in [x["sutra_id"] for x in s.trace]


def test_derive_matra_flag_traces_2_3_46():
    s = derive("rAma", 1, 1, matra_prathama_2_3_46=True)
    ids = [x["sutra_id"] for x in s.trace]
    assert ids.count("2.3.46") == 1
    assert "2.3.1" in ids


def test_2_3_46_cond_false_without_adhikara_even_if_meta_set():
    stem = [mk("r"), mk("A"), mk("m"), mk_inherent_a()]
    t = Term(
        kind="prakriti",
        varnas=stem,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "rAma"},
    )
    s0 = State(terms=[t])
    s0.meta["2_3_46_matra_prathama_eligible"] = True
    s1 = apply_rule("2.3.46", s0)
    assert any(
        step.get("sutra_id") == "2.3.46" and step.get("status") == "SKIPPED"
        for step in s1.trace
    )


def test_build_initial_state_kwarg_sets_meta():
    s = build_initial_state("rAma", 2, 1, matra_prathama_2_3_46=True)
    assert s.meta.get("2_3_46_matra_prathama_eligible") is True
