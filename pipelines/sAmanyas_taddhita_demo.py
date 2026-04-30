"""
pipelines/sAmanyas_taddhita_demo.py — ``prakriya_18`` (*sāmanyaḥ*).

Glass-box spine (corrected JSON / engine narrative):
  ``sAman`` + ``Ni`` → **4.4.98** (*tatra sādhuḥ*) ``+ yat`` → **6.4.168**
  (*ye cābhāvakarmaṇoḥ*) blocks **6.4.144** (*nas taddhite*) → **1.2.46**
  (``META_TADDHITA_AVAYAVA``) → **2.4.71** *luk* on internal ``Ni`` → *it* chain
  on ``yat`` → structural ``sAman`` + ``ya`` → ``sAmanya`` → **6.1.213** /
  **6.1.158** (accent *anuvāda*) → canonical **subanta** prathamā-``su`` finish
  (**sAmanyaH**).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P00_taddhita_it_lopa_chain
from pipelines.subanta import build_initial_state, run_subanta_sup_attach_and_finish
from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA


def _mk_sAman() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("sAman")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "sAman"},
    )


def _mk_Ni_sup() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ni")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "Ni"},
    )


def _structural_sAmanya_merge(s: State) -> State:
    """``sAman`` + ``ya`` (post-*yat* *it*) → ``sAmanya`` (not a sūtra)."""
    form_before = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("sAmanya")),
        tags={"anga", "prātipadika", "pulliṅga"},
        meta={"upadesha_slp1": "sAmanya"},
    )
    s.terms = [merged]
    s.trace.append({
        "sutra_id"    : "__TADDHITA_SAMANYA_MERGE__",
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : "तद्धित-मेलनम्",
        "form_before" : form_before,
        "form_after"  : s.flat_slp1(),
        "why_dev"     : "सामन् + यत्-इत-lopa → सामन्य (संरचनात्मकं)।",
        "status"      : "APPLIED",
    })
    return s


def derive_sAmanyas() -> State:
    s = State(terms=[_mk_sAman(), _mk_Ni_sup()])
    s.meta["prakriya_18_sAmanyas"] = True
    s.meta["prakriya_18_4_4_98_arm"] = True
    s = apply_rule("4.4.98", s)
    s = apply_rule("6.4.168", s)
    s.meta["prakriya_18_6_4_144_attempt_arm"] = True
    s = apply_rule("6.4.144", s)
    s.meta.pop("prakriya_18_6_4_144_attempt_arm", None)

    s.meta[META_TADDHITA_AVAYAVA] = True
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    s = P00_taddhita_it_lopa_chain(s)
    s = _structural_sAmanya_merge(s)

    s_sub = build_initial_state("sAmanya", 1, 1, "pulliṅga")
    s_sub.trace = list(s.trace) + list(s_sub.trace)
    s_sub.meta["prakriya_18_6_1_213_arm"] = True
    s_sub = apply_rule("6.1.213", s_sub)
    s_sub.meta.pop("prakriya_18_6_1_213_arm", None)
    s_sub.meta["prakriya_18_6_1_158_arm"] = True
    s_sub = apply_rule("6.1.158", s_sub)
    s_sub.meta.pop("prakriya_18_6_1_158_arm", None)
    return run_subanta_sup_attach_and_finish(s_sub)


__all__ = ["derive_sAmanyas"]
