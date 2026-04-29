"""
pipelines/krdanta.py — kṛdanta derivation drivers (scaffold).

This pipeline constructs a prātipadika from a dhātu + kṛt pratyaya by
explicitly scheduling sūtras (no inline bundles).

Recipes (step order aligned with pedagogical write-ups ``pachak.md`` /
``nayak.md``):

  • **qupac~z** + **Nvul** → **pAcaka**: saṃjñā / paribhāṣā (1.1.1, 1.1.3, 1.1.7, 1.1.8, 1.1.9, 1.1.10, 1.1.11, 1.1.12, 1.1.13, 1.1.14, 1.1.100, 1.1.15, 1.1.16, 1.1.17, 1.1.18, 1.1.19, 1.1.20, 1.1.21, 1.1.46, 1.1.22, 1.1.23, 1.1.24, 1.1.50) → dhātu
    it‑prakaraṇa → **6.1.65** (no-op) → kṛt adhikāra (**3.1.1**, **3.1.2**,
    **3.1.3**, **3.1.91**) → ``kartari`` meta + **3.4.67** → **3.1.133** → kṛt it →
    **7.1.1** → saṃjñā (**1.4.13**, **1.1.65**) → **6.4.1** → **7.2.116** →
    **7.2.115** (no-op here) → **6.1.78** (no-op) → **1.2.45** → **1.2.46** → structural merge.

  • **RIY** (णीञ्) + **Nvul** → **nAyaka**: same skeleton; **6.1.65** applies
    (``R`` → ``n``) *before* **3.1.133**; **7.2.115** + **6.1.78** yield
    ``nAyaka`` (not **7.2.116** upadhā-``a``).

  • **ciY** + **tfc** → **cetf** → (``pipelines/subanta_trc``) **cetA** / चेता —
    see ``cheta.md``; **7.2.10** blocks **7.2.35**; **7.3.84** guṇa; **7.1.94**
    anaṅ; **6.4.11**; **6.1.66**; **8.2.7**.
"""
from __future__ import annotations

from typing import List

import sutras  # noqa: F401  (ensure registry loaded)

from engine       import apply_rule
from engine.state import State, Term, Varna
from pipelines.preflight_lopa_samjna import apply_preflight_luk_samjna_block
from core.canonical_pipelines import (
    P01_samjna_1_1_15_to_1_1_24,
    P01_samjna_1_1_3_to_1_1_100,
    P00_it_halantyam_lopa_yathasankhyam,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from phonology import HAL
from phonology.pratyahara import is_ekac_upadesha
from phonology.varna import mk_inherent_a, parse_slp1_upadesha_sequence


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
    # Append inherent-a for consonant-final stems (a-stem model). Skip when the
    # merged surface already ends in a vowel (e.g. ``…ana`` from *lyuṭ*).
    if all_varnas and all_varnas[-1].slp1 in HAL:
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


def _structural_merge_trc_pratipadika(state: State, *, upadesha_slp1: str) -> State:
    """
    Merge dhātu + ``tfc`` residue into one prātipadika **without** appending
    inherent-a (ṛ-kāra / ``f``-anta stems like ``cetf``).
    """
    s = state
    if not s.terms:
        return s
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    prat = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga", "krt_tfc"},
        meta={
            "upadesha_slp1": upadesha_slp1,
        },
    )
    before = s.flat_slp1()
    s.terms = [prat]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__KRD_MERGE_TRC__",
        "sutra_type": "STRUCTURAL",
        "type_label": "कृदन्त-मेलनम् (तृच्)",
        "form_before": before,
        "form_after": after,
        "why_dev": "धातु + तृच् → प्रातिपदिकम् (ऋ-अन्त, न कारान्त)।",
        "status": "APPLIED",
    })
    return s


def build_dhatu_state(dhatu_upadesha_slp1: str) -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(dhatu_upadesha_slp1),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": dhatu_upadesha_slp1},
    )
    return State(terms=[dhatu])


def build_dhatu_state_from_varnas(dhatu_varnas: List[Varna], *, upadesha_slp1: str) -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=[v.clone() for v in dhatu_varnas],
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    return State(terms=[dhatu])


def derive_krt(
    dhatu_upadesha_slp1: str,
    *,
    krt_upadesha_slp1: str = "Nvul",
    dhatu_varnas: List[Varna] | None = None,
    merge_pratipadika_label: str = "pAcaka",
    prefix_terms: List[Term] | None = None,
    dhatu_meta: dict | None = None,
    extra_state_meta: dict | None = None,
) -> State:
    """
    Generic kṛdanta scaffold: dhātu (upadeśa) + chosen kṛt pratyaya.
    Supports Nvul for agent nouns (e.g. ``pAcaka``, ``nAyaka``).

    ``merge_pratipadika_label`` is stored on the merged Term's ``meta`` and
    should match the expected ``flat_slp1()`` stem (without extra inherent-a
    duplication in the label string — the merge step appends inherent-a).
    """
    if dhatu_varnas is not None:
        s = build_dhatu_state_from_varnas(dhatu_varnas, upadesha_slp1=dhatu_upadesha_slp1)
    else:
        s = build_dhatu_state(dhatu_upadesha_slp1)
    if prefix_terms:
        s.terms = list(prefix_terms) + s.terms
    if dhatu_meta:
        for t in s.terms:
            if "dhatu" in t.tags:
                t.meta.update(dhatu_meta)
                break
    if extra_state_meta:
        s.meta.update(extra_state_meta)

    # Saṃjñā / paribhāṣā used by later vidhi (vṛddhi prayoga, sthānāntara).
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = P01_samjna_1_1_3_to_1_1_100(s=s, include_luk_block=True)
    s = P01_samjna_1_1_15_to_1_1_24(s)
    s = apply_rule("1.1.50", s)

    # Dhātu it‑prakaraṇa (१.३.१ … १.३.९).
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.5", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    # Upasarga-saṃjñā (1.4.59) if applicable (e.g. āṅ + dīdhīṅ ...).
    s = apply_rule("1.4.59", s)

    # ६.१.६५ णो नः — before kṛt attachment (णीञ् → नी…); no-op on e.g. पच्.
    s = apply_rule("6.1.65", s)

    # Kṛt adhikāra block + kartṛ / bhāve scope.
    if krt_upadesha_slp1 == "lyuw":
        s.meta["krt_artha"] = "bhave"
    else:
        s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)

    s.meta["krt_upadesha_slp1"] = krt_upadesha_slp1
    if krt_upadesha_slp1 == "Nvul":
        s = apply_rule("3.4.67", s)
        s = apply_rule("3.1.133", s)
        s = apply_rule("1.3.8", s)
        s = apply_rule("1.3.7", s)
        s = apply_rule("1.3.3", s)
        s = apply_rule("1.3.9", s)
        s = apply_rule("7.1.1", s)
        s = apply_rule("1.4.13", s)
        s = apply_rule("1.1.65", s)
        s = apply_rule("6.4.1", s)
        s = apply_rule("7.2.116", s)
        s = apply_rule("7.2.115", s)
        s = apply_rule("6.1.78", s)
        # Sandhi on the dhātu+kṛt boundary (e.g. dIDhI + ak → dIDhyak).
        s = apply_rule("6.1.77", s)
        s = apply_rule("1.2.45", s)
        s = apply_rule("1.2.46", s)
        s = _structural_merge_to_pratipadika(s, upadesha_slp1=merge_pratipadika_label)
        return s

    if krt_upadesha_slp1 == "lyuw":
        s = apply_rule("3.4.68", s)
        s = apply_rule("3.1.133", s)
        s = apply_rule("1.3.8", s)
        s = apply_rule("1.3.7", s)
        s = apply_rule("1.3.3", s)
        s = apply_rule("1.3.9", s)
        s = apply_rule("3.4.114", s)
        s = apply_rule("1.4.13", s)
        s = apply_rule("1.1.65", s)
        s = apply_rule("6.4.1", s)
        s = apply_rule("7.3.84", s)
        s = apply_rule("7.1.1", s)
        s = apply_rule("7.2.116", s)
        s = apply_rule("7.2.115", s)
        s = apply_rule("6.1.78", s)
        s.meta["6_1_77_ik_yan_aci_general_arm"] = True
        s = apply_rule("6.1.77", s)
        s = apply_rule("1.2.45", s)
        s = apply_rule("1.2.46", s)
        s = _structural_merge_to_pratipadika(s, upadesha_slp1=merge_pratipadika_label)
        return s

    raise ValueError(f"unsupported kṛt pratyaya: {krt_upadesha_slp1!r}")


def derive_tfc_pratipadika(
    dhatu_upadesha_slp1: str,
    *,
    udatta_dhatu: bool = False,
) -> State:
    """
    Build a ``tfc`` (तृच्) prātipadika stem, e.g. ``ciY`` → ``cetf`` (चेतृ्…).

    ``udatta_dhatu`` (seṭ / udātta in JSON ``flags.udatta``): when True with
    ekāc stem, **7.2.10** does **not** block **7.2.35** (iṭ on the kṛt term).

    Scheduling follows ``cheta.md``: dhātu IT → **6.1.65** (no-op unless णीञ्) →
    kṛt adhikāra → **3.4.67** → **3.1.133** (``tfc``) → kṛt IT → **3.4.114** →
    aṅga saṃjñā → **7.2.10** / **7.2.35** → **7.3.84** → **1.1.51** (when ṛ/ḷ) →
    **6.1.78** (``o``+``i`` …) → **1.2.45** → **1.2.46** → merge (no inherent-a).
    """
    s = build_dhatu_state(dhatu_upadesha_slp1)
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = P01_samjna_1_1_3_to_1_1_100(s=s, include_luk_block=True)
    s = P01_samjna_1_1_15_to_1_1_24(s)
    s = apply_rule("1.1.50", s)
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.5", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s.meta["ekac_dhatu"] = is_ekac_upadesha(s.flat_slp1())
    s.meta["udatta_dhatu"] = bool(udatta_dhatu)
    s = apply_rule("6.1.65", s)
    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s.meta["krt_upadesha_slp1"] = "tfc"
    s = apply_rule("3.4.67", s)
    s = apply_rule("3.1.133", s)
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("3.4.114", s)
    s = apply_rule("1.4.13", s)
    s = apply_rule("1.1.65", s)
    s = apply_rule("6.4.1", s)
    s = apply_rule("7.2.10", s)
    s = apply_rule("7.2.35", s)
    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)
    s = apply_rule("6.1.78", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)
    s = _structural_merge_trc_pratipadika(s, upadesha_slp1="tfc")
    return s


def derive_trc(dhatu_id: str) -> State:
    """
    End-to-end **tṛc** nominative singular from a ``dhatupatha_upadesha`` row
    ``id`` (upadeśa + ``tfc`` + ``su`` 1-1).
    """
    from pipelines.dhatupatha import get_dhatu_row
    from pipelines.subanta_trc import derive_trc_nom_sg_from_state

    row = get_dhatu_row(dhatu_id)
    up = row["upadesha_slp1"]
    ud = bool(row.get("flags", {}).get("udatta", False))
    k = derive_tfc_pratipadika(up, udatta_dhatu=ud)
    return derive_trc_nom_sg_from_state(k, vibhakti=1, vacana=1, linga="pulliṅga")


def derive_chetA() -> State:
    """चेता — ``ciY`` + ``tfc`` + ``su`` (1-1), pulliṅga."""
    return derive_trc("BvAdi_ciY")


def derive_pAcaka_pratipadika() -> State:
    """
    Derive the prātipadika 'pAcaka' from dhātu डुपचँष् + ण्वुल्.
    Returns State whose last term is the derived prātipadika (anga).
    """
    return derive_krt("qupac~z", krt_upadesha_slp1="Nvul", merge_pratipadika_label="pAcaka")


def derive_pAcakaH() -> State:
    """
    Full derivation of पाचकः:
      (1) kṛdanta: pAcaka
      (2) subanta: pAcaka + su (1-1) → pAcakaH
    """
    from pipelines.subanta import (
        run_subanta_preflight_through_1_4_7,
        run_subanta_sup_attach_and_finish,
    )

    s = derive_pAcaka_pratipadika()
    # Continue on the same State (no flatten → rebuild), preserving full trace.
    if s.terms:
        s.terms[0].tags.add("pulliṅga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


def derive_nAyaka_pratipadika() -> State:
    """Derive prātipadika ``nAyaka`` from dhātu णीञ् (``RIY``) + ण्वुल्."""
    return derive_krt("RIY", krt_upadesha_slp1="Nvul", merge_pratipadika_label="nAyaka")


def derive_nAyakaH() -> State:
    """
    Full derivation of नायकः:
      (1) kṛdanta: nAyaka
      (2) subanta: nAyaka + su (1-1) → nAyakaH
    """
    from pipelines.subanta import (
        run_subanta_preflight_through_1_4_7,
        run_subanta_sup_attach_and_finish,
    )

    s = derive_nAyaka_pratipadika()
    if s.terms:
        s.terms[0].tags.add("pulliṅga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s
