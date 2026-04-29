"""
pipelines/pUrvaparANAm_dvandva_demo.py — पूर्वपराणाम् (dvandva + ṣaṣṭhī-bahuvacana) demo.

This is a **demo pipeline** aligned to the user's 1.1.30.md note narrative:

  - internal *jas* on both members are *luk*'d by **2.4.71** (now as zero-width ghosts)
  - dvandva context revokes *sarvanāma* via **1.1.31** so **7.1.52** *suṭ* does not apply
  - **7.1.54** inserts nuṭ before **Am**
  - **6.4.3** lengthens the aṅga-final vowel before nAm (a→A) producing …RAnAm
  - **8.4.2** applies ṇatva (tripāḍī) because r…n with only allowed vyavāya.

Constitutional notes:
  - Sūtra applications go ONLY via ``apply_rule``.
  - Samāsa merge is **STRUCTURAL** (trace id ``__DVANDVA_MERGE__``), not a sūtra.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.lopa_ghost import term_is_sup_luk_ghost
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


def _structural_merge_dvandva_to_single_anga(s: State) -> State:
    """
    Structural merge: [pUrva, sup, para, sup] → [pUrvapara] (keeping dvandva tag).
    Internal *sup* ghosts are not carried forward; this is a teaching merge step.
    """
    before = s.flat_slp1()
    members = [t for t in s.terms if t.kind == "prakriti"]
    if len(members) != 2:
        return s
    merged_slp1 = "".join("".join(v.slp1 for v in t.varnas) for t in members)
    tags = {"anga", "prātipadika", TAG_DVANDVA_SAMASA}
    # Glass-box: if any member got sarvanāma from 1.1.27, the compound would
    # inherit that status unless 1.1.31 revokes it.
    if any("sarvanama" in t.tags for t in members):
        tags.add("sarvanama")
    merged = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(merged_slp1)),
        tags=tags,
        meta={"upadesha_slp1": merged_slp1},
    )
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__DVANDVA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "द्वन्द्व-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "पूर्व + पर (द्वन्द्व) → एकं प्रातिपदिकम् (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s


def derive_pUrvaparANAm() -> State:
    """
    Returns final state for SLP1 ``pUrvaparARAm`` (पूर्वपराणाम्).
    """
    # Stage 0: two members with internal jas (as in the note).
    pUrva = _mk_member("pUrva")
    para = _mk_member("para")
    jas1 = _mk_sup("jas")
    jas2 = _mk_sup("jas")
    s = State(terms=[pUrva, jas1, para, jas2], meta={}, trace=[])

    # Stage 1: sarvanāma-saṃjñā on the sarvādi member(s) prior to dvandva merge.
    s = apply_rule("1.1.27", s)

    # Stage 2: internal sup-luk (2.4.71) → ghosts (zero-width).
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    # Stage 3: structural dvandva merge to a single aṅga.
    s = _structural_merge_dvandva_to_single_anga(s)

    # Stage 4: strip sarvanāma in dvandva (1.1.31) so suṭ is blocked.
    s = apply_rule("1.1.31", s)

    # Stage 5: attach Am (ṣaṣṭhī-bahuvacana sup). Run relevant aṅgādhikāra.
    s.terms.append(_mk_sup("Am"))
    s = apply_rule("6.4.1", s)

    # Stage 6: suṭ would apply if sarvanāma survived; must be skipped now.
    s = apply_rule("7.1.52", s)

    # Stage 7: nuṭ + nāmi + tripāḍī ṇatva.
    s = apply_rule("7.1.54", s)
    s = apply_rule("6.4.3", s)
    # ṇatva rules operate *samānapade*; merge to one term before tripāḍī scan.
    from pipelines.subanta import _pada_merge
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.2", s)
    return s


__all__ = ["derive_pUrvaparANAm"]

