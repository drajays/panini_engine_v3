"""
pipelines/vAyavaH_prakriya_24_demo.py — ``prakriya_24`` (*vāyavaḥ*).

Glass-box spine (JSON ``ordered_sutra_sequence`` + corrected ``panini_engine_pipeline``):

  * *Dhātu* ``vA`` (गतिगन्धनयोः) → **3.1.1** / **3.1.2** → **1.3.1** → **3.1.91** →
    **3.1.3** → **3.3.174** (*uṇ* append) → *it* slice (**1.3.3** … **1.3.10**) →
    **7.3.33** (*āto yuk*) → structural ``vAyu`` → canonical **subanta** prathamā
    *jas* finish (**vAyavaH**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + structural merge only; subanta tail
reuses ``build_initial_state`` / ``run_subanta_preflight_through_1_4_7`` /
``subanta_post_4_1_2`` (cf. ``agnI_iti_pragRhya_demo``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import subanta_post_4_1_2
from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7

_IT_AFTER_uR: tuple[str, ...] = (
    "1.3.3",
    "1.3.2",
    "1.3.7",
    "1.3.8",
    "1.3.9",
    "1.3.10",
)


def _mk_vA_dhatu() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("vA")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "vA"},
    )


def _structural_merge_vAyu(s: State) -> State:
    """``vA`` + ``y`` + ``u`` → ``vAyu`` (not a sūtra)."""
    b = s.flat_slp1()
    acc: list = []
    for t in s.terms:
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "pulliṅga"},
        meta={"upadesha_slp1": "vAyu"},
    )
    s.terms = [merged]
    s.trace.append(
        {
            "sutra_id": "__VAYU_KRT_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "वायु-प्रातिपदिक-मेलनम्",
            "form_before": b,
            "form_after": s.flat_slp1(),
            "why_dev": "वा + य् + उ → वायु (संरचनात्मकं)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_vAyavaH_prakriya_24() -> State:
    s = State(terms=[_mk_vA_dhatu()], meta={}, trace=[])

    for sid in ("3.1.1", "3.1.2"):
        s = apply_rule(sid, s)
    s = apply_rule("1.3.1", s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.1.3", s)

    s.meta["prakriya_24_uR_arm"] = True
    s = apply_rule("3.3.174", s)
    for sid in _IT_AFTER_uR:
        s = apply_rule(sid, s)

    s.meta["prakriya_24_7_3_33_arm"] = True
    s = apply_rule("7.3.33", s)
    s = _structural_merge_vAyu(s)

    s_sub = build_initial_state("vAyu", 1, 3, "pulliṅga")
    s_sub.trace = list(s.trace) + list(s_sub.trace)
    s_sub.meta["linga"] = "pulliṅga"
    s_sub.meta["vibhakti_vacana"] = "1-3"
    s_sub = run_subanta_preflight_through_1_4_7(s_sub)
    s_sub = apply_rule("4.1.2", s_sub)
    s_sub = subanta_post_4_1_2(s_sub)
    return s_sub


__all__ = ["derive_vAyavaH_prakriya_24", "_mk_vA_dhatu"]
