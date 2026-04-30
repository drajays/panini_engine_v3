"""
pipelines/devam_krt_prakriya_20_demo.py — ``prakriya_20`` **Part 1** (*devam*).

Glass-box spine (``panini_engine_pipeline`` in the JSON):
  ``divi~`` + **3.1.134** (*nandi-grahi-pacādibhyo …* **ac**) → *it* (**1.3.x**)
  → **7.3.86** *guṇa* → ``deva`` → **1.2.46** → **6.1.163** / **6.1.158** (*anuvāda*)
  → **subanta** preflight + **4.1.2** + **3.1.4** (``suppita``; not in the default
  P13–P15 tuple) + ``subanta_post_4_1_2`` (**6.1.107**, Tripāḍī) → **8.2.5**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P00_bhuvadi_dhatu_it_anunasik_hal
from core.canonical_pipelines import subanta_post_4_1_2
from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7


def _mk_divi_dhatu() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("divi~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "divi~"},
    )


def _structural_merge_deva(s: State) -> State:
    """``div`` + ``a`` (``ac`` residue) → ``deva`` (not a sūtra)."""
    fb = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("deva")),
        tags={"anga", "prātipadika", "krt", "pulliṅga"},
        meta={"upadesha_slp1": "deva"},
    )
    s.terms = [merged]
    s.trace.append({
        "sutra_id"    : "__KRDANTA_DEVA_MERGE__",
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : "कृदन्त-मेलनम्",
        "form_before" : fb,
        "form_after"  : s.flat_slp1(),
        "why_dev"     : "दिव् + अ → देव (संरचनात्मकं)।",
        "status"      : "APPLIED",
    })
    return s


def derive_devam_prakriya_20() -> State:
    s = State(
        terms=[_mk_divi_dhatu()],
        meta={
            "prakriya_20_devam"       : True,
            "prakriya_20_nandi_pacadi": True,
        },
        trace=[],
    )
    s = apply_rule("3.1.91", s)
    s.meta["prakriya_20_3_1_134_arm"] = True
    s = apply_rule("3.1.134", s)
    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    s = apply_rule("1.1.6", s)
    s = apply_rule("7.3.86", s)
    s = _structural_merge_deva(s)
    s = apply_rule("1.2.46", s)

    s.meta["prakriya_20_6_1_163_arm"] = True
    s = apply_rule("6.1.163", s)
    s.meta.pop("prakriya_20_6_1_163_arm", None)
    s.meta["prakriya_20_devam_6_1_158_arm"] = True
    s = apply_rule("6.1.158", s)
    s.meta.pop("prakriya_20_devam_6_1_158_arm", None)

    s_sub = build_initial_state("deva", 2, 1, "pulliṅga")
    s_sub.trace = list(s.trace) + list(s_sub.trace)
    s_sub = run_subanta_preflight_through_1_4_7(s_sub)
    s_sub = apply_rule("4.1.2", s_sub)
    s_sub = apply_rule("3.1.4", s_sub)
    s_sub = subanta_post_4_1_2(s_sub)
    s_sub.meta["prakriya_20_devam_8_2_5_arm"] = True
    s_sub = apply_rule("8.2.5", s_sub)
    return s_sub


__all__ = ["derive_devam_prakriya_20"]
