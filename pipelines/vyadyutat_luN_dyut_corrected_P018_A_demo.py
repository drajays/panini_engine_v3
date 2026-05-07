"""
pipelines/vyadyutat_luN_dyut_corrected_P018_A_demo.py — **P018-A** *vyadyutat*.

Upasarga ``vi`` + dhātu ``dyut`` (+ meta ``dyut~`` origin) + luṅ *parasmaipada*
3 sg.: **1.3.1**, **3.1.91** + ``P06a``, **3.2.110**/**3.4.69**, **3.1.43** ``cli``,
**3.1.55** ``aG``, *it*, *tiṅ* **tip**, **3.4.100**, **6.4.71**, **6.1.77**,
``_pada_merge``, **8.2.1** — ``corrected_prakriyas_v2`` **P018-A** (**``vyadyutat``**).

*Śástra note:* bundle rows **n1–n2** (``dyut~`` → ``dyut``) are **phonologically
invisible** in SLP1 rendering (anusvara is not orthographically distinct here), so
the recipe starts from surface **``dyut``** with lexical **``dyut~``** in meta;
all later steps are ``apply_rule``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_it_halantyam_lopa_yathasankhyam,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_vyadyutat_luN_dyut_corrected_P018_A() -> State:
    upa = Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("vi")),
        tags={"upasarga"},
        meta={"upadesha_slp1": "vi"},
    )
    # Surface **dyut** ≡ *dyut~* after **1.3.2**/**1.3.9** (see module docstring).
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("dyut")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "dyut~", "karmakatva": "akarmaka"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P018_A_demo"] = True
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"

    s = apply_rule("1.3.1", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.terms.insert(0, upa)

    # Drop ``upadesha`` on dhātu so **1.3.3** *halantyam* does not delete ``dyut``’s
    # final ``t`` during the ``aG`` *it*-pass (**P00_it_halantyam_lopa_*); cf.
    # ``avaDIt_luN_han`` note.
    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")

    s.meta["3_2_110_luG_arm"] = True
    s = apply_rule("3.2.110", s)
    s = apply_rule("3.4.69", s)

    s.meta["3_1_43_cli_luG_arm"] = True
    s = apply_rule("3.1.43", s)

    s.meta["corrected_v2_P018_A_3_1_55_arm"] = True
    s = apply_rule("3.1.55", s)

    s = P00_it_halantyam_lopa_yathasankhyam(s)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tip"
    s = apply_rule("3.4.78", s)
    s = apply_rule("1.4.99", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("3.4.100", s)
    s = apply_rule("1.2.41", s)

    s = apply_rule("6.4.71", s)
    s = apply_rule("6.1.77", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    return s


__all__ = ["derive_vyadyutat_luN_dyut_corrected_P018_A"]
