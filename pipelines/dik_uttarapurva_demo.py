"""
Rule-based (apply_rule-only) demo: dik-samāsa *uttarā* + *pūrvā* → *uttarapūrvā*,
then strī *caturthī* *ekavacana* (ङे) — two *vikalpa* paths from **1.1.28**.

Śāstra order: **1.2.45** (*arthavad … prātipadikam*) on *avyutpanna* members, then
**1.2.46** prerequisite for **2.4.71** is modelled by tagging members *prātipadika*
and setting ``meta['pratipadika_avayava_ready']`` before arming *luk*; internal *sup*
(**2.4.71**) then **2.2.26** (puṃvat + **1.2.48** *hrasva* on the *bahuvrīhi*);
**1.2.46** again records *prātipadika* on the merged stem.  ``run_subanta_pipeline``
(same sequence as ``pipelines.subanta.derive``)
runs with *cond* blind to *vibhakti* (Constitution Art. 2 — coordinates only in
``build_initial_state`` / **4.1.2** *act*).

Run:
  python3 -m pipelines.dik_uttarapurva_demo
  python3 -m pipelines.dik_uttarapurva_demo caturthi
  python3 -m pipelines.dik_uttarapurva_demo glass
  python3 -m pipelines.dik_uttarapurva_demo glass dakziRA_pUrvA
"""
from __future__ import annotations

import contextlib
import io
import sys
from dataclasses import dataclass
from typing import Literal, Mapping

import sutras  # noqa: F401

from sutras.adhyaya_2.pada_2.sutra_2_2_26 import (
    _PAIR_TO_STEM,
    _dik_surface_invokes_puMvat,
    _dir_name,
)

from engine       import apply_rule
from engine.it_phonetic import term_phonetic_varnas
from engine.state import State, Term
from phonology    import mk
from phonology.joiner import slp1_to_devanagari
from phonology.varna import AC_DEV, HAL_DEV

from pipelines import subanta as _subanta_mod
from pipelines.subanta import (
    PADA_MERGE_STEP,
    SUBANTA_RULE_IDS_POST_4_1_2,
    run_subanta_pipeline,
    run_subanta_post_4_1_2,
    run_subanta_preflight_through_1_4_7,
)

# **7.3.113** / **7.3.114** require an **ā**-final *aṅga* before **Ne**.  The compound
# engine emits **uttarapUrva** (1.2.48 *hrasva*); subanta entry may use **ā**-banta
# *uttarapUrvA* where the demo needs **7.3.114** on **Ne** (see ``_stem_strI_*``).

_TRACE_SEP = "─────────────────────────────────────"
_PHASE_RULE = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

DikCaturthiId = Literal["uttarA_pUrvA", "dakziRA_pUrvA"]


@dataclass(frozen=True)
class DikCaturthiPreset:
    """Vigraha and display strings for one (दिक्+दिक्) *antarāla* द्वन्द्व-style demo pair."""

    id: DikCaturthiId
    m1_slp: str
    m2_slp: str
    m1_dik_line: str
    m2_dik_line: str
    expected_merged_puM: str
    strI_ā_banta: str
    title_short_deva: str
    prathama_sam_dv: str
    st_I_pratipadika_dv: str
    mar_a_dv: str
    mar_b_dv: str
    caturthi_slp1_marA: str
    caturthi_slp1_marB: str
    box_line0_dv: str
    box_line1_dv: str
    box_line2_dv: str
    box_line3_dv: str


# Two teaching presets (2.2.26 pairs from ``_PAIR_TO_STEM``).
_CATURETHI_BY_ID: Mapping[DikCaturthiId, DikCaturthiPreset] = {
    "uttarA_pUrvA": DikCaturthiPreset(
        id="uttarA_pUrvA",
        m1_slp="uttarA",
        m2_slp="pUrvA",
        m1_dik_line="uttarA Ns",
        m2_dik_line="pUrvA Ns",
        expected_merged_puM="uttarapUrva",
        strI_ā_banta="uttarapUrvA",
        title_short_deva="उत्तरपूर्व",
        prathama_sam_dv="उत्तरपूर्व",
        st_I_pratipadika_dv="उत्तरपूर्वा",
        mar_a_dv="उत्तरपूर्वस्यै",
        mar_b_dv="उत्तरपूर्वायै",
        caturthi_slp1_marA="uttarapUrvasyE",
        caturthi_slp1_marB="uttarapUrvAyE",
        box_line0_dv="चतुर्थी एकवचनम् — उत्तरपूर्वा (स्त्री) + ङे",
        box_line1_dv="समास-प्रातिपदिकम्: उत्तरपूर्व",
        box_line2_dv="स्त्री-प्रातिपदिकम्: उत्तरपूर्वा (४.१.४ टाप्-अन्तम्)",
        box_line3_dv="(१.१.२८ विभाषया — मार्गः A / मार्गः B)",
    ),
    "dakziRA_pUrvA": DikCaturthiPreset(
        id="dakziRA_pUrvA",
        m1_slp="dakziRA",
        m2_slp="pUrvA",
        m1_dik_line="dakziRA Ns",
        m2_dik_line="pUrvA Ns",
        expected_merged_puM="dakziRapUrva",
        strI_ā_banta="dakziRapUrvA",
        title_short_deva="दक्षिणपूर्व",
        prathama_sam_dv="दक्षिणपूर्व",
        st_I_pratipadika_dv="दक्षिणपूर्वा",
        mar_a_dv="दक्षिणपूर्वस्यै",
        mar_b_dv="दक्षिणपूर्वायै",
        caturthi_slp1_marA="dakziRapUrvasyE",
        caturthi_slp1_marB="dakziRapUrvAyE",
        box_line0_dv="चतुर्थी एकवचनम् — दक्षिणपूर्वा (स्त्री) + ङे",
        box_line1_dv="समास-प्रातिपदिकम्: दक्षिणपूर्व",
        box_line2_dv="स्त्री-प्रातिपदिकम्: दक्षिणपूर्वा (४.१.४ टाप्-अन्तम्)",
        box_line3_dv="(१.१.२८ विभाषया — मार्गः A / मार्गः B)",
    ),
}


def caturthi_preset(preset_id: DikCaturthiId) -> DikCaturthiPreset:
    return _CATURETHI_BY_ID[preset_id]


def _varnas_from_slp1(slp1: str) -> list:
    out: list = []
    i = 0
    while i < len(slp1):
        ch = slp1[i]
        if ch in HAL_DEV or ch in AC_DEV:
            out.append(mk(ch))
        i += 1
    return out


def build_dik_caturthi_vigraha(p: DikCaturthiPreset) -> State:
    """Like ``build_vigraha_uttarapurva_state`` but for any 2.2.26-registered दिक् pair."""
    t1 = Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(p.m1_slp),
        tags={"prātipadika", "samasa_member"},
        meta={"dik_name": p.m1_dik_line, "upadesha_slp1": p.m1_slp},
    )
    sup1 = Term(
        kind="pratyaya",
        varnas=[],
        tags={"sup"},
        meta={"upadesha_slp1": "suP", "internal_sup_pending": True},
    )
    t2 = Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(p.m2_slp),
        tags={"prātipadika", "samasa_member"},
        meta={"dik_name": p.m2_dik_line, "upadesha_slp1": p.m2_slp},
    )
    sup2 = Term(
        kind="pratyaya",
        varnas=[],
        tags={"sup"},
        meta={"upadesha_slp1": "suP", "internal_sup_pending": True},
    )
    return State(terms=[t1, sup1, t2, sup2])


def _state_has_internal_sup_pending(s: State) -> bool:
    return any(t.meta.get("internal_sup_pending") for t in s.terms)


def _flat_slp1_for_display(s: State) -> str:
    """Serialize pending internal *sup* as ``[SUP]``, not as phoneme *varṇa*."""
    if not _state_has_internal_sup_pending(s):
        return s.flat_slp1()
    parts: list[str] = []
    for t in s.terms:
        if "sup" in t.tags and t.meta.get("internal_sup_pending"):
            parts.append("[SUP]")
        else:
            parts.append("".join(v.slp1 for v in t.varnas))
    return "".join(parts)


def _surface_dev_for_display(s: State) -> str:
    if _state_has_internal_sup_pending(s):
        return "[ABSTRACT_CONCATENATION]"
    return _surface_dev(s)


def _is_dik_two_member_after_internal_luk(s: State) -> bool:
    """True after **2.4.71** on this demo: two *samāsa-member* *prakṛti*, *sup* deleted."""
    if len(s.terms) != 2:
        return False
    if s.meta.get("2_4_71_luk") is not True:
        return False
    for t in s.terms:
        if t.kind != "prakriti":
            return False
        if not {"prātipadika", "samasa_member"}.issubset(t.tags):
            return False
    return True


def _term_line_dik_post_luk_member(i: int, t: Term) -> str:
    slp = "".join(v.slp1 for v in t.varnas)
    tags = sorted(t.tags)
    return f"  [{i}] prakriti  slp1={slp!r}   tags={tags!r}"


def _term_line_dik_luk_placeholder(idx: int) -> str:
    return (
        f"  [{idx}] pratyaya  slp1=∅ (luk)   tags={['sup', 'luk_2_4_71']!r}"
    )


def _flat_slp1_display_two_members(s: State) -> str:
    return " + ".join("".join(v.slp1 for v in t.varnas) for t in s.terms)


def _flat_slp1_display_two_members_spaced(s: State) -> str:
    """Two *prakṛti* members separated by `` | `` (not merged)."""
    return " | ".join("".join(v.slp1 for v in t.varnas) for t in s.terms)


def _surface_dev_two_members(s: State) -> str:
    return " | ".join(
        slp1_to_devanagari(term_phonetic_varnas(t)) for t in s.terms
    )


def _print_state_engine_internal_post_luk(s: State) -> None:
    """Step 2b: ``apply_rule('2.1.3')`` only re-pushes *samāsa* adhikāra for **2.2.26**."""
    print("   STATUS: engine bookkeeping — not a Pāṇinian rule")
    print("   luk-tagged pratyayas purged from token list")
    print(f"   flat_slp1() = {_flat_slp1_display_two_members_spaced(s)!r}")
    print()


def _print_state_dik_post_internal_luk(s: State) -> None:
    print("   ACTION: luk of internal sups [1] and [3]")
    print()
    print(_term_line_dik_post_luk_member(0, s.terms[0]))
    print(_term_line_dik_luk_placeholder(1))
    print(_term_line_dik_post_luk_member(2, s.terms[1]))
    print(_term_line_dik_luk_placeholder(3))
    print()
    spaced = _flat_slp1_display_two_members_spaced(s)
    print(f"  flat_slp1() = {spaced!r} (members not yet merged)")
    print(f"  surface_dev  = {_surface_dev_two_members(s)!r}")
    lk = s.meta.get("2_4_71_luk")
    if lk is not None:
        print(f"  meta: {{'2_4_71_luk': {lk!r}}}")
    print()


def _term_line(i: int, t: Term) -> str:
    up = t.meta.get("upadesha_slp1", "")
    up_s = f" meta[upadesha_slp1]={up!r}" if up else ""
    if "vartika_sarvanAma_puMvat_vrtti" in t.meta:
        up_s += f" meta[vartika_sarvanAma_puMvat_vrtti]={t.meta['vartika_sarvanAma_puMvat_vrtti']!r}"
    if "sup" in t.tags and t.meta.get("internal_sup_pending"):
        slp1_disp = repr("[SUP:pending]")
    else:
        slp1_disp = repr("".join(v.slp1 for v in t.varnas))
    return (
        f"  [{i}] kind={t.kind!r} tags={sorted(t.tags)!s}{up_s} "
        f"slp1={slp1_disp}"
    )


def _print_phase1_step0_uttarapurva_table(s: State) -> None:
    """Fixed vigraha layout matching the uttarā+pūrvā demo spec."""
    for i, t in enumerate(s.terms):
        up = t.meta.get("upadesha_slp1", "")
        tags = sorted(t.tags)
        if t.kind == "prakriti":
            slp = "".join(v.slp1 for v in t.varnas)
            print(f"  [{i}] prakriti   upadesha={up!r}  slp1={slp!r}")
            print(f"      tags={tags!r}")
        else:
            if t.meta.get("internal_sup_pending"):
                slp_disp = "[SUP:pending]"
            else:
                slp_disp = "".join(v.slp1 for v in t.varnas)
            print(f"  [{i}] pratyaya   upadesha={up!r}  slp1={slp_disp!r}")
            print(f"      tags={tags!r}")


def _print_state(
    title: str,
    s: State,
    *,
    internal_sup_note: bool = False,
    samasa_adhikara_marker: bool = False,
    dik_post_internal_luk: bool = False,
    engine_internal_adhikara_reopen: bool = False,
) -> None:
    print(title)
    if dik_post_internal_luk and _is_dik_two_member_after_internal_luk(s):
        _print_state_dik_post_internal_luk(s)
        return
    if engine_internal_adhikara_reopen and _is_dik_two_member_after_internal_luk(s):
        _print_state_engine_internal_post_luk(s)
        return
    if samasa_adhikara_marker:
        print("   STATUS: adhikāra-sūtra (Domain: 2.1.4 – 2.2.38)")
        print("   ACTION: none (morphological change pending)")
        if s.adhikara_stack:
            print(f"   adhikāra_stack = {[e.get('id') for e in s.adhikara_stack]}")
        print()
        return
    if internal_sup_note and _state_has_internal_sup_pending(s):
        print(
            "   Abstract sups held as internal tokens [suP_abstract]"
        )
    print(f"  flat_slp1() = {_flat_slp1_for_display(s)!r}")
    print(f"  surface_dev  = {_surface_dev_for_display(s)!r}")
    for i, t in enumerate(s.terms):
        print(_term_line(i, t))
    if s.samjna_registry:
        print(f"  samjna_registry = {dict(s.samjna_registry)}")
    if s.meta:
        print(f"  meta = {dict(s.meta)}")
    print()


def _surface_dev(s: State) -> str:
    """Joiner-based Devanagarī (per-term, then concatenated); omits *it* varṇas."""
    return "".join(slp1_to_devanagari(term_phonetic_varnas(t)) for t in s.terms)


# Classical vibhakti labels for *sup* upadeśa (demo trace — avoids pseudo-surface
# like उत्तरपूर्वाङे where **ṅ** is *it*, not a pronounced onset).
_UPADESHA_DEVA_ABSTRACT: dict[str, str] = {
    "Ne": "ङे",
}


def _dev_abstract_concat_two_terms(s: State) -> str:
    """
    ``stem_dev + ' + ' + affix_dev`` for teaching (two *Term* vigraha), not a
    pronounceable *pada* surface.
    """
    if len(s.terms) != 2:
        return _surface_dev(s)
    t0, t1 = s.terms[0], s.terms[1]
    stem_dev = slp1_to_devanagari(term_phonetic_varnas(t0))
    up = (t1.meta.get("upadesha_slp1") or "").strip()
    if up in _UPADESHA_DEVA_ABSTRACT:
        aff_dev = _UPADESHA_DEVA_ABSTRACT[up]
    else:
        aff_dev = slp1_to_devanagari(term_phonetic_varnas(t1))
    return f"{stem_dev} + {aff_dev}"


def _flat_term_concat(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _devanagari_from_flat_slp1(slp: str) -> str:
    return slp1_to_devanagari(_varnas_from_slp1(slp))


def _print_uttarapurva_step_3_unpacked(s_before: State, s_after: State) -> None:
    """
    Verbose-only narrative: **2.2.26** demo bundles merge, vārttika puṃvat, and
    **1.2.48** *hrasva* in one ``apply_rule`` call — unpack into 3a–3d for trace.
    """
    if len(s_before.terms) != 2 or len(s_after.terms) != 1:
        _print_state("3) 2.2.26 दिङ्नामान्यन्तराले (+ Kāś. पुंवद्-वृत्ति-सङ्केतः meta)", s_after)
        return

    t0, t1 = s_before.terms[0], s_before.terms[1]
    m0, m1 = t0.meta.get("dik_name"), t1.meta.get("dik_name")
    flat_0, flat_1 = _flat_term_concat(t0), _flat_term_concat(t1)
    flat_3ab = flat_0 + flat_1

    d0, d1 = _dir_name(t0), _dir_name(t1)
    pair = frozenset({d0, d1}) if d0 and d1 else None
    flat_3c = _PAIR_TO_STEM.get(pair, "") if pair else flat_3ab
    if not flat_3c:
        flat_3c = flat_3ab

    flat_3d = s_after.flat_slp1()

    print("3a) 2.2.26 दिङ्नामान्यन्तराले")
    print("    ACTION: compound formation (merger)")
    print(f"    flat_slp1() = {flat_3ab!r}")
    print(f"    surface_dev  = {_devanagari_from_flat_slp1(flat_3ab)!r}")
    print()

    print("3b) 1.2.43 प्रथमानिर्दिष्टं समास उपसर्जनम्")
    print(f"    ACTION: pūrvapada {flat_0!r} tagged as upasarjana")
    print(f"    flat_slp1() = {flat_3ab!r}")
    print(f"    surface_dev  = {_devanagari_from_flat_slp1(flat_3ab)!r}")
    print()

    cond_pum = _dik_surface_invokes_puMvat(m0) or _dik_surface_invokes_puMvat(m1)
    print("3c) VĀRTTIKA: सर्वनाम्नो वृत्तिमात्रे पुंवद्भावो वक्तव्यः")
    print("    CONDITION: pūrvapada = sarvanāma + upasarjana")
    print(f"    (engine check → {cond_pum!r})")
    print("    ACTION: puṃvadbhāva — पूर्वपद-दिङ्-नाम् पुंवद्-आकारः (Kāś. २.२.२६ वा.)")
    print(f"    flat_slp1() = {flat_3c!r}")
    print(f"    surface_dev  = {_devanagari_from_flat_slp1(flat_3c)!r}")
    print()

    print("3d) 1.2.48 गोस्त्रियोरुपसर्जनस्य")
    print(
        "    NOTE: Applied to strī-ending uttarapada 'pUrvA' in dik-samāsa tradition"
    )
    print("    ACTION: hrasva → 'pUrvA' becomes 'pUrva'")
    print(f"    flat_slp1() = {flat_3d!r}")
    print(f"    surface_dev  = {_devanagari_from_flat_slp1(flat_3d)!r}")
    merged = s_after.terms[0]
    if s_after.meta:
        m = dict(s_after.meta)
        print("    meta: {")
        print(f"        'diksamasa_compound': {m.get('diksamasa_compound')!r},")
        print(f"        'vartika_puMvat_applied': {m.get('vartika_puMvat_applied')!r},")
        print(f"        '1_2_48_hrasva_applied': {m.get('1_2_48_hrasva_applied')!r},")
        print("    }")
    print(
        f"    (engine merged term: tags={sorted(merged.tags)!s}; "
        f"meta[vartika_sarvanAma_puMvat_vrtti]={merged.meta.get('vartika_sarvanAma_puMvat_vrtti')!r})"
    )
    print()


def build_vigraha_uttarapurva_state() -> State:
    """
    Four-term vigraha: *uttarā* / *pūrvā* + internal *ṅas* (*sup*) slots.

    Internal *sup* are **abstract**: empty ``varnas``, ``meta['internal_sup_pending']``,
    ``upadesha_slp1='suP'`` (class label, not a realized cell like **NAs**) — so
    ``State.flat_slp1()`` does not splice phantom vowels; the demo uses
    ``_flat_slp1_for_display`` / ``_print_state`` to show ``uttarA[SUP]pUrvA[SUP]``
    until **2.4.71** removes the *sup* terms.
    """
    return build_dik_caturthi_vigraha(caturthi_preset("uttarA_pUrvA"))


def derive_dik_caturthi_compound(
    p: DikCaturthiPreset, *, verbose: bool = True
) -> State:
    """
    2.1.3 → 2.4.71 → **2.1.3** (stack bookkeeping only) → 2.2.26 → 1.2.45 → 1.2.46.

    The second ``apply_rule('2.1.3')`` re-opens *samāsa* adhikāra after **2.4.71**
    (``purge_closed_adhikaras`` can drop **2.1.3**); it is **not** a second śāstrīya
    domain step — see verbose step **2b** label in this module.
    """
    s = build_dik_caturthi_vigraha(p)
    if verbose:
        print(
            f"=== {p.st_I_pratipadika_dv} (दिक्-समास) — apply_rule only ===\n"
        )
        print(_PHASE_RULE)
        print("PHASE 1: ALAUKIKA VIGRAHA + SAMĀSA")
        print(f"{_PHASE_RULE}\n")
        print("0) आरम्भः — विग्रहः (अलौकिकः)")
        print()
        print("   Abstract sups held as internal tokens [suP_abstract]")
        print()
        _print_phase1_step0_uttarapurva_table(s)
        print(f"  flat_slp1() = {_flat_slp1_for_display(s)!r}")
        print(f"  surface_dev  = {_surface_dev_for_display(s)!r}\n")

    s = apply_rule("2.1.3", s)
    if verbose:
        print(_TRACE_SEP)
        _print_state("1) 2.1.3 समासाधिकारः", s, samasa_adhikara_marker=True)

    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    if verbose:
        print(_TRACE_SEP)
        _print_state(
            "2) 2.4.71 सुपो धातुप्रातिपदिकयोः (लुक्)",
            s,
            dik_post_internal_luk=True,
        )

    # Re-push **2.1.3** on ``adhikara_stack`` so **2.2.26** ``cond`` sees *samāsa*
    # adhikāra (implementation; not a second Pāṇinian “application” of 2.1.3).
    s = apply_rule("2.1.3", s)
    if verbose:
        print(_TRACE_SEP)
        _print_state(
            "2b) [ENGINE INTERNAL] luk-token cleanup",
            s,
            engine_internal_adhikara_reopen=True,
        )

    s.meta["diksamasa_compound"] = True
    s_before_226 = s.clone()
    s = apply_rule("2.2.26", s)
    if verbose:
        print(_TRACE_SEP)
        _print_uttarapurva_step_3_unpacked(s_before_226, s)

    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)
    if verbose:
        print(_TRACE_SEP)
        print("4) 1.2.45 → 1.2.46 (अर्थवत् … प्रातिपदिकम् ; कृत्तद्धितसमासाश्च)")
        t0 = s.terms[0]
        print(f"   ACTION: assign prātipadika-saṃjñā to {s.flat_slp1()!r}")
        print(f"   tags = {sorted(t0.tags)!s}")
        reg = {"1.2.46_dik_pratipadika": s.samjna_registry.get("1.2.46_dik_pratipadika")}
        print(f"   samjna_registry = {reg!s}")
        print()

    return s


def derive_uttarapurva_compound(*, verbose: bool = True) -> State:
    return derive_dik_caturthi_compound(caturthi_preset("uttarA_pUrvA"), verbose=verbose)


def _print_caturthi_step_5_transition_strI_tap_narrative(
    p: DikCaturthiPreset, s_merged: State
) -> None:
    """
    Verbose-only: **5.4.68–5.4.160** *samāsānta* does not apply; **4.1.1** is *adhikāra*
    for strī-pratyayas; **4.1.4** *ṭāp* (**wAp**), *it*-lopa, then **1.2.45** for
    *prātipadika* (see ``run_caturthi_prakriya``).
    """
    st_anga_slp1 = p.strI_ā_banta
    merged = s_merged.flat_slp1()
    dev_anga = _devanagari_from_flat_slp1(st_anga_slp1)
    print(_PHASE_RULE)
    print("PHASE 2: STRĪ-PRATYAYA")
    print(f"{_PHASE_RULE}\n")
    print(
        f"   (samāsa-prātipadika **{merged}** — no *samāsānta* here, 5.4.68–5.4.160)\n"
    )
    print("5a) 4.1.1 ङ्याप्प्रातिपदिकात्")
    print("    STATUS: adhikāra for strī-pratyayas\n")
    print("5b) 4.1.4 अजाद्यतष्टाप्")
    print(f"    ACTION: add ṭāp (engine upadeśa: wAp) to {merged!r}")
    print(f"    intermediate = {merged!r} + wAp\n")
    print("5c) it-lopa of wAp (ṭāp):")
    print("    1.3.7 चुटू → initial 'w' (ṭ) = it")
    print("    1.3.3 हलन्त्यम् → final 'p' = it")
    print("    1.3.9 तस्य लोपः → 'w' and 'p' removed")
    print("    remaining affix: 'A'")
    print(f"    flat_slp1() = {st_anga_slp1!r}")
    print(f"    surface_dev  = {dev_anga!r}")
    print()
    print("5d) 1.2.45 अर्थवदधातुरप्रत्ययः प्रातिपदिकम्")
    print(f"    ACTION: {st_anga_slp1!r} gets secondary prātipadika-saṃjñā")
    print("    tags += ['TAp_anta', 'strīliṅga']")
    print()


def _stem_strI_merged_for_ne_subanta(s_merged: State) -> Term:
    """
    *Strī* *aṅga* (१.२.४८-ह्रस्वान्त + ४.१.४) before **4.1.2** *Ne* — ā-banta
    (…**pUrvA**) for **7.3.113/114** + **6.1.88**.
    """
    t0 = s_merged.terms[0].clone()
    t0.tags.add("strīliṅga")
    m = t0.meta.get("upadesha_slp1") or ""
    if m.endswith("pUrva"):
        slp = m.replace("pUrva", "pUrvA", 1)
        t0.varnas = _varnas_from_slp1(slp)
        t0.meta["upadesha_slp1"] = slp
    return t0


def _stem_strI_uttarapurva_for_ne_subanta(s_merged: State) -> Term:
    return _stem_strI_merged_for_ne_subanta(s_merged)


def _demo_syat_slice_uttarapurva_ne(p: DikCaturthiPreset) -> None:
    """
    Śāstrīya trace: **1.3.2–1.3.9** on **Ne** immediately after **4.1.2** (same
    position as ``run_subanta_pipeline``), then Path A **1.1.28**, then **6.4.1**
    (*adhikāra* only), then **7.3.114** + **6.1.88** (slice focus).
    """
    print(f"\n{_PHASE_RULE}")
    print("APPENDIX: Path A — engine-internal rule sequence")
    print("          (śāstrīya order; for reference only)")
    print(f"{_PHASE_RULE}\n")
    # Same stem/meta as ``run_caturthi_prakriya`` Path A so preflight + *it* behave
    # like the full engine (manual *aṅga*+*Ne* two-term state skips *it* markers).
    s_comp = derive_dik_caturthi_compound(p, verbose=False)
    stem = _stem_strI_merged_for_ne_subanta(s_comp)
    s = State(
        terms=[stem.clone()],
        meta={"vibhakti_vacana": "4-1", "linga": "strīliṅga"},
        trace=[],
    )
    print(
        "  (पूर्वकूलम् — ``run_subanta_preflight_through_1_4_7``: engine runs the pre-**४.१.२** "
        "block through **१.४.७**; "
        "विभक्ति *cond* न पठति; अन्तर्वर्तते **१.१.४६** आद्यन्तौ टकितौ — *āgama-sthāna* gate.)\n"
        "  NOTE: 1.4.1–1.4.7 = saṃjñā-sūtras for vibhakti/vacana;\n"
        "        no morphological change; engine confirms aṅga-saṃjñā here\n"
    )
    s = run_subanta_preflight_through_1_4_7(s)
    print(f"  → after preflight  flat_slp1() = {_sl(s)!r}  |  Dev {_surface_dev(s)!r}")
    s = apply_rule("4.1.2", s)
    print(
        f"  4.1.2 *sup* + **Ne** (ङे)  →  flat_slp1() = {_sl(s)!r}  "
        f"|  dev_abstract = '{_dev_abstract_concat_two_terms(s)}'"
    )

    print(
        "  **१.३.२–१.३.९** — *it* prakaraṇa on **Ne** (same slot as ``run_subanta_pipeline``: "
        "immediately after **४.१.२**, before **६.४.१**).\n"
    )
    for rid in ("1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8"):
        s = apply_rule(rid, s)
    a_ne = p.strI_ā_banta + "Ne"
    print(
        "  1.3.2–1.3.8 — it-saṃjñā assigned on Ne:\n"
        "                'N' tagged by 1.3.8 लशकवतद्धिते\n"
        f"                flat_slp1() = {a_ne!r} (N still present)\n"
    )
    s = apply_rule("1.3.9", s)
    print(
        "  1.3.9 तस्य लोपः — it-letters removed\n"
        f"                flat_slp1() = {_sl(s)!r}\n"
        f"                dev_joiner_concat (abstract) = {_surface_dev(s)!r}\n"
    )

    s = apply_rule("1.1.28", s, {"vibhasha_choice": True})
    print(
        "  1.1.28 विभाषा दिक्समासे बहुव्रीहौ (Path A — not part of ``run_subanta_pipeline``; "
        "applied here so **7.3.114** has ``sarvanama`` on the *aṅga*)\n"
        f"     tags (aṅga): {sorted(s.terms[0].tags)!s}  |  flat_slp1() = {_sl(s)!r}\n"
    )

    before_641 = _sl(s)
    s = apply_rule("6.4.1", s)
    after_641 = _sl(s)
    assert before_641 == after_641
    print(
        "  [6.4.1 अङ्गस्य — *adhikāra* only; no morphological change]\n"
        f"  [Shape {before_641!r} already from **4.1.2** + **१.३.९**; "
        f"dev_joiner_concat (abstract) = {_surface_dev(s)!r}]\n"
    )
    s = apply_rule("7.3.114", s)
    print(
        f"  7.3.114 सर्वनाम्नः स्याट् ह्रस्वश्च  →  SLP1 {_sl(s)!r}  |  "
        f"dev_joiner_concat (abstract) = {_surface_dev(s)!r}"
    )
    s = apply_rule("6.1.88", s)
    print(
        f"  6.1.88 वृद्धिरेचि  →  SLP1 {_sl(s)!r}  |  "
        f"surface_dev (joiner) = {_surface_dev(s)!r}\n"
    )


def _sl(s: State) -> str:
    return s.flat_slp1()


def _apply_subanta_post_ne_slice(s: State, lo: int, hi: int) -> State:
    """Apply ``SUBANTA_RULE_IDS_POST_4_1_2[lo:hi]`` (``hi`` exclusive)."""
    tup = SUBANTA_RULE_IDS_POST_4_1_2
    for k in range(lo, hi):
        rid = tup[k]
        if rid == PADA_MERGE_STEP:
            _subanta_mod._pada_merge(s)
        else:
            s = apply_rule(rid, s)
    return s


def _caturthi_subanta_meta() -> dict:
    return {"vibhakti_vacana": "4-1", "linga": "strīliṅga"}


def _caturthi_state_through_4_1_2(stem: Term) -> State:
    """Shared *subanta* entry: preflight + **4.1.2** (ङे → **Ne**)."""
    s = State(terms=[stem.clone()], meta=_caturthi_subanta_meta(), trace=[])
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    return s


def _print_verbose_subanta_uttarapurva_path_a(s412: State) -> State:
    """Path A from state already past **4.1.2** (see shared step **6**)."""
    ids = SUBANTA_RULE_IDS_POST_4_1_2
    j_114 = ids.index("7.3.114")
    j_88 = ids.index("6.1.88")

    sub = s412.clone()
    a_slp = "".join(v.slp1 for v in s412.terms[0].varnas)
    a_hr = a_slp.replace("pUrvA", "pUrva", 1)

    print("7) 1.1.28 विभाषा दिक्समासे बहुव्रीहौ")
    print("    OPTION: sarvanāma-saṃjñā = YES")
    print("    tags += ['sarvanama']")
    sub = apply_rule("1.1.28", sub, {"vibhasha_choice": True})
    print(f"    tags (aṅga): {sorted(sub.terms[0].tags)!s}\n")

    print("8) 7.3.114 सर्वनाम्नः स्याड् ह्रस्वश्च")
    print(f"    ACTION-1: base hrasva → {a_slp!r} → {a_hr!r}")
    print("    ACTION-2: add augment 'syAw' to suffix 'Ne'")
    print(f"    intermediate = {a_hr!r} + syAw + Ne\n")
    sub = _apply_subanta_post_ne_slice(sub, 0, j_114 + 1)

    print("9) 1.1.46 आद्यन्तौ टकितौ")
    print("    syAw is ṭit (w-it) → placed BEFORE 'Ne'")
    print(f"    form = {a_hr!r} + syAw + Ne\n")

    print("10) it-lopa of syAw + Ne:")
    print("    1.3.3 हलन्त्यम् → 'w' = it")
    print("    1.3.8 लशकवतद्धिते → 'N' = it")
    print("    1.3.9 तस्य लोपः → 'w' and 'N' removed")
    print(f"    result = {a_hr!r} + syA + e")
    print(f"    flat_slp1() = {_sl(sub)!r}\n")

    print("11) 6.1.88 वृद्धिरेचि")
    print("    ACTION: 'A' + 'e' = 'E' (ai)")
    sub = _apply_subanta_post_ne_slice(sub, j_114 + 1, j_88)
    sub = apply_rule("6.1.88", sub)
    print(f"    flat_slp1() = {_sl(sub)!r}")
    print(f"    surface_dev  = {_surface_dev(sub)!r}          ✓\n")
    print(
        f"    NOTE: Path A trace before 7.3.114 has {a_hr!r}e (after 1.3.9, before syāṭ).\n"
        f"          Path B (after 7.3.113) shows {a_slp!r}yAe in the same slot.\n"
    )

    sub = _apply_subanta_post_ne_slice(sub, j_88 + 1, len(ids))
    return sub


def _print_verbose_subanta_uttarapurva_path_b(s412: State) -> State:
    """Path B from state already past **4.1.2**."""
    ids = SUBANTA_RULE_IDS_POST_4_1_2
    j_139 = ids.index("1.3.9")
    j_113 = ids.index("7.3.113")
    j_88 = ids.index("6.1.88")

    sub = s412.clone()
    a_slp = "".join(v.slp1 for v in s412.terms[0].varnas)

    print("7) 1.1.28 विभाषा — OPTION: sarvanāma = NO\n")

    print("8) 7.3.113 याडापः")
    print("    ACTION: add augment 'yAw' to suffix 'Ne'")
    print(f"    intermediate = {a_slp!r} + yAw + Ne\n")
    sub = _apply_subanta_post_ne_slice(sub, 0, j_139 + 1)
    sub = _apply_subanta_post_ne_slice(sub, j_139 + 1, j_113)
    sub = apply_rule("7.3.113", sub)

    print("9) 1.1.46 आद्यन्तौ टकितौ")
    print("    yAw is ṭit → placed BEFORE 'Ne'")
    print(f"    form = {a_slp!r} + yAw + Ne\n")

    print("10) it-lopa of yAw + Ne:")
    print("    1.3.3 हलन्त्यम् → 'w' = it")
    print("    1.3.8 लशकवतद्धिते → 'N' = it")
    print("    1.3.9 तस्य लोपः → 'w' and 'N' removed")
    print(f"    result = {a_slp!r} + yA + e")
    sub = _apply_subanta_post_ne_slice(sub, j_113 + 1, j_88)
    print(f"    flat_slp1() = {_sl(sub)!r}\n")

    print("11) 6.1.88 वृद्धिरेचि")
    print("    'A' + 'e' = 'E'")
    sub = apply_rule("6.1.88", sub)
    print(f"    flat_slp1() = {_sl(sub)!r}")
    print(f"    surface_dev  = {_surface_dev(sub)!r}          ✓\n")

    sub = _apply_subanta_post_ne_slice(sub, j_88 + 1, len(ids))
    return sub


def run_caturthi_prakriya(preset_id: DikCaturthiId = "uttarA_pUrvA") -> None:
    p = caturthi_preset(preset_id)
    print(
        "\n╔══════════════════════════════════════════════════════════════╗\n"
        f"║  {p.box_line0_dv}\n"
        f"║  {p.box_line1_dv}\n"
        f"║  {p.box_line2_dv}\n"
        f"║  {p.box_line3_dv}\n"
        "╚══════════════════════════════════════════════════════════════╝\n"
    )

    s_comp = derive_dik_caturthi_compound(p, verbose=True)
    assert s_comp.flat_slp1() == p.expected_merged_puM
    assert {"hrasva_final", "upasarjana"}.issubset(s_comp.terms[0].tags)
    assert "TAp_anta" not in s_comp.terms[0].tags

    _print_caturthi_step_5_transition_strI_tap_narrative(p, s_comp)
    stem = _stem_strI_merged_for_ne_subanta(s_comp)
    print(
        "   SLP1 (subanta handoff — same surface as Phase 2 step 5c): "
        f"{''.join(v.slp1 for v in stem.varnas)!r}  |  "
        f"Devanagarī (stem joiner only): {slp1_to_devanagari(stem.varnas)!r}\n"
    )

    print(_PHASE_RULE)
    print("PHASE 3: VIBHAKTI — CATURTHĪ EKAVACANA")
    print(f"{_PHASE_RULE}\n")
    s_412 = _caturthi_state_through_4_1_2(stem)
    print("6) 4.1.2 स्वौजसमौट्…")
    print("    ACTION: select caturthī-ekavacana suffix = Ne (ङे)")
    print(f"    flat_slp1() = {p.strI_ā_banta!r} + Ne  →  {_sl(s_412)!r}")
    da = _dev_abstract_concat_two_terms(s_412)
    print(f"    dev_abstract = {da!r}\n")

    def _branch(name_hi: str, with_sarvanama_vibhasha: bool) -> None:
        print(_PHASE_RULE)
        print(f"── {name_hi} ──")
        print(f"{_PHASE_RULE}\n")
        if with_sarvanama_vibhasha:
            out = _print_verbose_subanta_uttarapurva_path_a(s_412)
            chk = s_412.clone()
            chk = apply_rule("1.1.28", chk, {"vibhasha_choice": True})
            chk = run_subanta_post_4_1_2(chk)
        else:
            out = _print_verbose_subanta_uttarapurva_path_b(s_412)
            chk = s_412.clone()
            chk = run_subanta_post_4_1_2(chk)
        assert _sl(out) == _sl(chk), (_sl(out), _sl(chk))
        print("    [audit] final form confirmed: no further sandhi changes applicable")

    _branch("मार्गः A — सर्वनाम-संज्ञा (१.१.२८ = True)", True)
    _branch("मार्गः B — सर्वनाम-संज्ञा नास्ति", False)

    print(_PHASE_RULE)
    print("SUMMARY")
    print(f"{_PHASE_RULE}")
    print(f"मार्गः A (sarvanāma) → {p.mar_a_dv}")
    print(f"मार्गः B (no sarvanāma) → {p.mar_b_dv}")
    print(f"{_PHASE_RULE}\n")

    _demo_syat_slice_uttarapurva_ne(p)


def capture_caturthi_prakriya_stdout(preset_id: DikCaturthiId = "uttarA_pUrvA") -> str:
    """
    Return the full verbose text of ``run_caturthi_prakriya(preset_id)`` (same as CLI
    ``python3 -m pipelines.dik_uttarapurva_demo caturthi`` for default *preset_id*), for
    Streamlit / tests.
    """
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        run_caturthi_prakriya(preset_id)
    return buf.getvalue()


def derive_uttarapurva_from_vigraha() -> State:
    """Backward-compatible name: compound only, with prints."""
    return derive_uttarapurva_compound(verbose=True)


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("glass", "kachapeti", "kAcapetI"):
        from pipelines.dik_caturthi_glassbox_text import glassbox_for_id

        pid: DikCaturthiId = "uttarA_pUrvA"
        if len(sys.argv) > 2 and sys.argv[2] in _CATURETHI_BY_ID:
            pid = sys.argv[2]  # type: ignore[assignment]
        print(glassbox_for_id(pid), end="")
        return
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("caturthi", "caturthI", "4"):
        run_caturthi_prakriya()
        return
    s = derive_uttarapurva_from_vigraha()
    assert s.flat_slp1() == "uttarapUrva"
    assert len(s.terms) == 1
    assert {"bahuvrihi", "diksamasa", "prātipadika", "hrasva_final", "upasarjana"}.issubset(
        s.terms[0].tags
    )
    assert "TAp_anta" not in s.terms[0].tags
    assert s.samjna_registry.get("1.2.46_dik_pratipadika") is True
    assert s.meta.get("2_4_71_luk") is True
    print("OK: one-word stem uttarapUrva (hrasva-anta) with expected tags and registry.")


if __name__ == "__main__":
    main()
