"""
pipelines/vaipASaH_vipAS_tatra_bhava.py — वैपाशः (*vipāś* + *Ni* + *aṇ*, *tatra-bhava*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/वैपाशः.md``

Semantic contract: *vipASi BavaH* (fish etc. of the Vipāś (Vyās) river) under
**4.3.53** *tatra bhavaḥ* with **aṇ** (**4.1.82** / **4.1.83**), internal *saptamī*
*Ni*, **2.4.71** *luk*, **7.2.117** *ādi-vṛddhi*, **1.4.18** *bha*, **6.4.129**;
**6.4.148** is scheduled for *śāstra* parity (vacuous here: **ś** + **a** is not
the *i* / *ī* *yasyeti* slice, and *ac*–*hal* is not *savarṇa* per **1.1.10** in
``phonology.savarna``).

Target SLP1: **vEpASaH** (वैपाशः; *vṛddhi* **E** = *ai* of *vi-*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_adi_vrddhi_then_bha_then_bhasya,
    P00_taddhita_aR_it_hal_antyam_slice,
    P00_taddhita_internal_Ni_luk_1_2_46_2_4_71,
    P00_taddhita_Ni_locative_then_tatra_bhava_adhikara,
    P12_anga_aa_lopa,
)
from pipelines.subanta import (
    run_subanta_preflight_through_1_4_7,
    run_subanta_sup_attach_and_finish,
)

from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA
from sutras.adhyaya_4.pada_3.sutra_4_3_53 import META_ELIGIBLE as META_TATRA_BHAVA


def _make_vipAS_state() -> State:
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vipAS"),
        tags={"anga"},
        meta={"upadesha_slp1": "vipAS"},
    )
    t.tags.add("prātipadika")
    return State(terms=[t], meta={"linga": "pulliṅga"}, trace=[])


def _append_aR(s: State) -> None:
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("aN"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "aN"},
    )
    s.terms.append(pr)


def _structural_merge_to_pratipadika(s: State, *, upadesha_slp1: str) -> State:
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    before = s.flat_slp1()
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__VAIPASA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "वैपाश-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "विपाश् + अण्-शेष → एकं प्रातिपदिकम् (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s


def derive_vaipASa_pratipadika() -> State:
    """
    *Taddhita* leg: *vipAS* + internal *Ni* + *aṇ* → *vEpASa* (prātipadika surface).
    """
    s = _make_vipAS_state()

    s = P00_taddhita_Ni_locative_then_tatra_bhava_adhikara(s)
    _append_aR(s)

    s = P00_taddhita_internal_Ni_luk_1_2_46_2_4_71(s)

    s = P00_taddhita_aR_it_hal_antyam_slice(s)

    s = P00_adi_vrddhi_then_bha_then_bhasya(s)
    s = P12_anga_aa_lopa(s)

    return _structural_merge_to_pratipadika(s, upadesha_slp1=s.flat_slp1().strip())


def derive_vaipASaH() -> State:
    """Full run: *taddhita* stem + *subanta* prathamā-ekavacana (*puṃ*) → *vEpASaH*."""
    s = derive_vaipASa_pratipadika()
    # Continue in the same State (no flatten → rebuild), preserving full trace.
    if s.terms:
        s.terms[0].tags.add("pulliṅga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta.pop(META_TADDHITA_AVAYAVA, None)
    s.meta.pop(META_TATRA_BHAVA, None)
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = ["derive_vaipASa_pratipadika", "derive_vaipASaH"]
