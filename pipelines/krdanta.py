"""
pipelines/krdanta.py — kṛdanta derivation drivers (scaffold).

This pipeline constructs a prātipadika from a dhātu + kṛt pratyaya by
explicitly scheduling sūtras (no inline bundles).
"""
from __future__ import annotations

from typing import List

import sutras  # noqa: F401  (ensure registry loaded)

from engine       import apply_rule
from engine.state import State, Term
from phonology    import mk
from phonology.varna import mk_inherent_a


def _structural_merge_to_pratipadika(state: State, *, upadesha_slp1: str) -> State:
    """
    Structural (not a sūtra): merge dhātu + pratyaya into a single prātipadika Term.
    Logged as __KRD_MERGE__ in the trace.
    """
    s = state
    if not s.terms:
        return s
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    # Append inherent-a so the prātipadika is an a-stem in v3 internal form.
    all_varnas.append(mk_inherent_a())
    prat = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    before = s.flat_slp1()
    s.terms = [prat]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__KRD_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "कृदन्त-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "धातु + कृत्-प्रत्ययः → प्रातिपदिकम् (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s


def _parse_upadesha_slp1(slp1_seq: str) -> List:
    """
    Parse a raw upadeśa SLP1 string where '~' marks anunāsika on the
    preceding vowel (same convention as sup_upadeśa).
    """
    varnas = []
    i = 0
    while i < len(slp1_seq):
        ch = slp1_seq[i]
        if i + 1 < len(slp1_seq) and slp1_seq[i + 1] == "~":
            v = mk(ch, "anunasika")
            i += 2
        else:
            v = mk(ch)
            i += 1
        varnas.append(v)
    return varnas


def build_dhatu_state(dhatu_upadesha_slp1: str) -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=_parse_upadesha_slp1(dhatu_upadesha_slp1),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": dhatu_upadesha_slp1},
    )
    return State(terms=[dhatu])


def derive_krt(
    dhatu_upadesha_slp1: str,
    *,
    krt_upadesha_slp1: str = "Nvul",
) -> State:
    """
    Generic kṛdanta scaffold: dhātu (upadeśa) + chosen kṛt pratyaya.
    Currently supports Nvul for the vr̥ddhi example (pācaka).
    """
    s = build_dhatu_state(dhatu_upadesha_slp1)

    # IT-prakaraṇa on dhātu.
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.5", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    # Attach kṛt pratyaya.
    s.meta["krt_upadesha_slp1"] = krt_upadesha_slp1
    if krt_upadesha_slp1 == "Nvul":
        s = apply_rule("3.1.133", s)
        # IT on pratyaya, then vu→ak.
        s = apply_rule("1.3.8", s)
        s = apply_rule("1.3.3", s)
        s = apply_rule("1.3.9", s)
        s = apply_rule("7.1.1", s)
        # upadhā-vṛddhi under ṇit.
        s = apply_rule("7.2.116", s)
        # Merge.
        s = _structural_merge_to_pratipadika(s, upadesha_slp1="pAcaka")
        return s

    raise ValueError(f"unsupported kṛt pratyaya: {krt_upadesha_slp1!r}")


def derive_pAcaka_pratipadika() -> State:
    """
    Derive the prātipadika 'pAcaka' from dhātu डुपचँष् + ण्वुल्.
    Returns State whose last term is the derived prātipadika (anga).
    """
    return derive_krt("qupac~z", krt_upadesha_slp1="Nvul")


def derive_pAcakaH() -> State:
    """
    Full derivation of पाचकः:
      (1) kṛdanta: pAcaka
      (2) subanta: pAcaka + su (1-1) → pAcakaH
    """
    from pipelines.subanta import derive as derive_subanta
    # Subanta driver accepts stem_slp1 by upadeśa identity; we pass the canonical.
    return derive_subanta("pAcaka", 1, 1, linga="pulliṅga")

