"""
pipelines/katarakatamA_vibhASa_jasi_demo.py — विभाषा जसि (1.1.32) demo.

Targets (from user's note):
  - Option A (accept vibhāṣā): ``katarakatame`` (jas→śī, then a+ī→e)
  - Option B (decline vibhāṣā): ``katarakatamAH`` (jas→as, then a+a→A, then visarga)

This demo is intentionally small and uses only ``apply_rule`` for sūtras; the
dvandva merge is structural (trace ``__DVANDVA_MERGE__``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_31 import TAG_DVANDVA_SAMASA


def _mk_member(stem_slp1: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem_slp1)),
        tags={"anga", "prātipadika", "samasa_member"},
        meta={"upadesha_slp1": stem_slp1},
    )


def _mk_sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def _structural_merge_dvandva(st1: Term, st2: Term) -> State:
    # Apply 1.1.27 on members so sarvanāma can be inherited onto the compound.
    s = State(terms=[st1, st2], meta={}, trace=[])
    s = apply_rule("1.1.27", s)
    merged_slp1 = "".join("".join(v.slp1 for v in t.varnas) for t in s.terms)
    tags = {"anga", "prātipadika", TAG_DVANDVA_SAMASA}
    if any("sarvanama" in t.tags for t in s.terms):
        tags.add("sarvanama")
    merged = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(merged_slp1)),
        tags=tags,
        meta={"upadesha_slp1": merged_slp1},
    )
    s0 = State(terms=[merged], meta={}, trace=s.trace)
    s0.trace.append({
        "sutra_id": "__DVANDVA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "द्वन्द्व-मेलनम्",
        "form_before": merged_slp1,
        "form_after": merged_slp1,
        "why_dev": "कतर + कतम → कतरकतम (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s0


def derive_katarakatame(*, vibhasha_choice: bool) -> State:
    """
    If ``vibhasha_choice=True``: expect ``katarakatame``.
    If ``vibhasha_choice=False``: expect ``katarakatamAH``.
    """
    # Build dvandva aṅga.
    s = _structural_merge_dvandva(_mk_member("katara"), _mk_member("katama"))

    # Attach jas (prathamā-bahu).
    s.terms.append(_mk_sup("jas"))
    s = apply_rule("6.4.1", s)

    # dvandva strict denial then optional restoration.
    s = apply_rule("1.1.31", s)
    s = apply_rule("1.1.32", s, {"vibhasha_choice": vibhasha_choice})

    # If sarvanāma is present, jas→śī then a+ī→e (6.1.87).
    s = apply_rule("7.1.17", s)
    # it chain on inserted śī opener (S).
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("6.1.87", s)

    # Else-path: jas opener j is cuṭu-it and will be loped, then 6.1.102 handles a+a.
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("6.1.102", s)

    # Merge to one pada and apply ru + visarga tail (8.2.66 / 8.3.15) if applicable.
    from pipelines.subanta import _pada_merge
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_katarakatame"]

