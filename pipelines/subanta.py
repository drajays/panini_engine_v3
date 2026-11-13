"""
pipelines/subanta.py — subanta derivation driver.
──────────────────────────────────────────────────

Given:
  stem_slp1    : str, e.g. "rAma" (Velthuis / SLP1-style; अकारान्त = ends in hrasa ``a``)
                 or "rADA" (ध = SLP1 ``D``; stem ends in long ``A`` for ``ā``-anta strī).
  vibhakti     : 1..8
  vacana       : 1..3
  linga        : "pulliṅga" | "strīliṅga" | "napuṃsaka"

अकारान्त पुंलिङ्ग (a-stem masculine) helpers:
  • ``stem_slp1_looks_akarant_pullinga`` — shape check (pipeline/UI only).
  • ``derive_akarant_pullinga`` — same recipe as ``derive(..., linga="pulliṅga")``
    after validating stem shape (raises ``ValueError`` if not a-kāra-anta).

आकारान्त स्त्रीलिङ्ग (ā-stem feminine) helpers:
  • ``stem_slp1_looks_Akarant_strilinga`` — stem ends in SLP1 long ``A`` (``ā``).
  • ``derive_akarant_strilinga`` — ``derive(..., linga="strīliṅga")`` with optional shape guard.

*Sarvādi* सर्वनाम (e.g. **अन्य**, ``anya`` — listed in ``data/inputs/sarvadi_slp1.json`` for **1.1.27**):
  • ``derive_anya_pullinga`` — thin wrapper; gold lives under the test/UI gold corpus.

Returns:
  State  — with full trace in state.trace and rendered surface in
           state.flat_dev()  (uses phonology.joiner for Devanāgarī).

This is the ONLY place (vibhakti, vacana) enters the engine — and it
enters via state.meta.  Every downstream cond() reads ONLY phonemic /
saṃjñā / tag / adhikāra signals (CONSTITUTION Art. 2).

Recipe (Aṣṭādhyāyī order; one step per apply_rule call):

    STAGE 1: saṃjñā preflight
        1.4.14  sup saṃjñā
        (optional) 2.3.1 + 2.3.46 — when ``build_initial_state(...,
        matra_prathama_2_3_46=True)`` / matching ``state.meta``:
        *anabhihita* adhikāra opens, then **2.3.46** ANUVADA (trace) for
        *prātipadikārtha* / *liṅga* / *parimāṇa* / *vacana*-*mātra* with
        *prathamā* (cond is blind to ``vibhakti_vacana`` per Art. 2).
        4.1.1   ngyāp anuvāda
        1.1.1   vṛddhi saṃjñā (definition {A,E,O}; prayoga in vidhi sūtras)
                [recipe schedules this early; vṛddhi *prayoga* not applied here—
                 no vidhi invokes operational vṛddhi at this step, only saṃjñā]
        1.1.73  *vṛddha-pada* saṃjñā (first *ac* in *vṛddhi* ⇒ *vṛddham* pada)
        1.1.2   guṇa saṃjñā   (available for later sandhi)
        1.1.3   *ik* *sthāyin* under *guṇa* / *vṛddhi* (paribhāṣā gate)
        1.1.7   *saṃyoga* (contiguous *hal*; paribhāṣā-śāstrīya cluster term)
        1.1.60  *lopa* (sthāne *adarśanam*; names deletion — **1.3.9** *vidhi* applies *lopa* to *it*)
        1.1.61  *luk* / *ślu* / *lup* saṃjñā (*pratyayādarśana* subtypes; needs **1.1.60**)
        1.1.62  *pratyayalakṣaṇam* paribhāṣā (*pratyayāśrita* *kārya* after *lopa*)
        1.1.63  *na lumatā …* — *luk*/*ślu*/*lup*-*lopa* blocks *aṅga*-*pratyayalakṣaṇa* (**1.1.62** *apavāda*)
        1.1.8   *anunāsika* (mukha–*nāsikā* *avacana*; *anusvāra* / *chandrabindu* class)
        1.1.9   *savarṇa* (*tulya* *āśya*–*prayatna*; ``phonology.savarna``)
        1.1.10  *nājjhalau* ( *it* / *upadeśa* paribhāṣā before 1.3.2)
        1.1.11  *pragṛhya* ( *ī, ū, e, ai, o, au* in *dvivacana*)
        1.1.12  *adaso māt* ( *it* / *upadeśa* paribhāṣā: *aś* in *sarvān.* *adas* / *māt* )
        1.1.13  *śe* ( *pragṛhya* *prayoga* off in *aś* / *ś* *locus*; *Kāśikā* *vṛtti* )
        1.1.14  *nipāta ekājanāṅ* ( *pragṛhya* for *ekāc* *nipāta*; ashtadhyayi *i* 11014)
        1.1.15  *ot* ( *O* in *nipāta*; *i* 11015)
        1.1.16  *sambuddhau śākalyasya* … ( *Kāśikā*; *i* 11016)
        1.1.17  *uÞ* *aḥ* ( *i* 11017)
        1.1.18  *ū̐* / *Ū* + nasal ( *Oṅkāra*; *i* 11018)
        1.1.19  *Ī*/*Ū* + *tau* *saptamī*-*artha* ( *pragṛhya* extension; *i* 11019)
        1.1.20  *dā* / *dhā* + *ad*+**āp** → *ghu* ( *i* 11020)
        1.1.21  *ādyantavad* *ekasmin* ( *i* 11021; *paribhāṣā* *gate* for *atideśa*)
        1.1.46  *ādyantau* *ṭakitau* (*ṭit* before / *kit* after *āgamin*; *āgama-sthāna*)
        1.1.22  *tarap* + *tamap* → *gha* (taddhita; *i* 11022; distinct from *ghu* **1.1.20**)
        1.1.23  *bahu* / *gaṇa* / *vatu* / *ḍati* → *saṅkhyā* ( *i* 11023)
        1.1.24  *ṣṇānta* → *ṣaṭ* ( *i* 11024; under 1.1.23 *saṅkhyā* anuvṛtti)

    STAGE 2: attach sup
        4.1.2   ADHIKARA + attaches the (v,v) pratyaya to state.terms

    STAGE 3: it-prakaraṇa on the pratyaya upadeśa
        1.3.3–1.3.8  it-saṃjñā (halantyam, tusma block, ñiṭuḍu, ṣaḥ, cuṭu, laśakvat)
        1.3.9   tasya lopaḥ (delete tagged it-varṇas)
        1.3.10  *samānām anudeśaḥ yathāsaṅkhyam* (paribhāṣā gate after first *it*-*lopa* pass)

    STAGE 4: aṅgakārya
        6.4.1   aṅgasya adhikāra
        1.4.17 / 1.4.16 / 1.4.18  *prakṛti* saṃjñā (*pada* / *bha* *bādhyabādaka*)
        after **1.1.42** (recipe order: **1.4.17** → **1.4.16** → **1.4.18**)
      (conditional) 7.1.54  nuṭ āgama for (6,3)
      (then)  1.3.9 again to lose the ṭ it-marker of nuṭ
        6.4.129 *bhasya* (recipe: pushed just before **6.4.130** so **7.** rules do
                not purge it via ``purge_closed_adhikaras``)
        6.4.130 / 6.4.134 / 6.4.146 / 6.4.148 — *bhādhikāra* *aṅgakārya* slice

    STAGE 5: sandhi
        6.1.87  āt guṇaḥ  (e.g. a+i → e for (3,1))
        6.1.101 akaḥ savarṇe dīrghaḥ

    STAGE 6: pada merge — recipe marks state.terms joined as 'pada'
             (structural, not a sūtra)

    STAGE 7: tripāḍī
        8.2.1   pūrvatrāsiddham (enter zone)
        8.2.66  sasajuṣo ruḥ  (final s → ru)
        8.3.15  ru → visarga at end
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

from typing import List

from engine            import apply_rule
from pipelines.it_prakarana import IT_PRAKARANA_SEQUENCE
from engine.state      import State, Term
from engine.strata     import sees_later_tripadi
from phonology         import mk
from phonology.varna   import mk_inherent_a

# Canonical *prakriyā* spines (single *apply_rule* scheduling).
from core.canonical_pipelines import (  # noqa: PLC0415
    P01_subanta_bootstrap        as run_subanta_preflight_through_1_4_7,
    run_subanta_sup_attach_and_finish,
    subanta_post_4_1_2,
)

# Backward-compatible name (imported by ``taddhita_itika_etikAyana``, *dik* demo, etc.).
run_subanta_post_4_1_2 = subanta_post_4_1_2

def derive_from_state(
    state: State,
    vibhakti: int,
    vacana: int,
    *,
    linga: str | None = None,
    matra_prathama_2_3_46: bool = False,
    nAmadheya_vrddha_term_indices: tuple[int, ...] | frozenset[int] | None = None,
) -> State:
    """
    Zero-patchwork entry point when a `State` already exists upstream
    (kṛdanta/taddhita/samāsa): do not flatten+rebuild; do not staple saṃjñā tags
    via boolean args.

    This only injects the *semantic* cell request into `state.meta`:
    `vibhakti_vacana` (and optionally `linga`). All morphological work still
    proceeds through `apply_rule()` only.
    """
    if linga is not None:
        state.meta["linga"] = linga
    state.meta["vibhakti_vacana"] = f"{vibhakti}-{vacana}"
    if matra_prathama_2_3_46:
        state.meta["2_3_46_matra_prathama_eligible"] = True
    if nAmadheya_vrddha_term_indices is not None:
        from sutras.adhyaya_1.pada_1.sutra_1_1_73 import META_NAMADHEYA_VRDDHA_INDICES

        state.meta[META_NAMADHEYA_VRDDHA_INDICES] = frozenset(nAmadheya_vrddha_term_indices)
    return run_subanta_pipeline(state)


def build_initial_state(stem_slp1: str, vibhakti: int, vacana: int,
                        linga: str = "pulliṅga",
                        *,
                        matra_prathama_2_3_46: bool = False,
                        sheSa_shashthi_2_3_50: bool = False,
                        nAmadheya_vrddha_term_indices: tuple[int, ...] | frozenset[int] | None = None,
                        derived_pratipadika: bool = False,
                        ) -> State:
    """Build the initial state for a subanta derivation.

    ``derived_pratipadika`` — the stem was derived upstream (kṛt/taddhita/samāsa)
    and already holds the prātipadika saṃjñā by **1.2.46**; it carries that
    saṃjñā over (1.2.45 rightly refuses a vyutpanna stem).

    ``matra_prathama_2_3_46`` — when True, sets
    ``state.meta['2_3_46_matra_prathama_eligible']`` so the subanta recipe
    may schedule **2.3.1** + **2.3.46** in preflight (caller opts into this
    *śāstra* slice; default subanta behaviour is unchanged).

    ``sheSa_shashthi_2_3_50`` — when True, sets
    ``state.meta['2_3_50_sheSa_shashthi_eligible']`` so the subanta recipe
    may schedule **2.3.1** + **2.3.50** in preflight (opt-in semantic flag
    for *śeṣa* relation → *ṣaṣṭhī* selection; default behaviour unchanged).

    ``nAmadheya_vrddha_term_indices`` — optional indices for **1.1.73**
    *vārttika* for *nāmadheya*; stored as
    ``state.meta['1_1_73_nAmadheya_vrddha_term_indices']`` for **1.1.73**.

    NOTE (anti-patchwork): do NOT inject samāsa saṃjñās via boolean flags here.
    If a stem is a *bahuvrīhi* or *tṛtīyā-tatpuruṣa*, those tags must already be
    present on the incoming `State` via the samāsa module, and subanta should be
    invoked via `derive_from_state(...)`.
    """
    # Each consonant gets inherent-a unless immediately followed by a
    # vowel character in the stem.  We emit in canonical internal form:
    # consonant halanta + vowel/inherent-a.  Simple loop:
    varnas: List = []
    from phonology.varna import AC_DEV, HAL_DEV
    i = 0
    while i < len(stem_slp1):
        ch = stem_slp1[i]
        if ch in HAL_DEV:
            varnas.append(mk(ch))
            # We do NOT auto-append inherent 'a' after a final consonant.
            # If a stem needs a final vowel, it must be explicit in the input
            # (e.g. rAma, gaja). This keeps consonant-ending stems like `tad`
            # well-formed.
            i += 1
            continue
        if ch in AC_DEV or ch in "MH":  # M anusvāra, H visarga: ayogavāhas inside a stem (saMSaya, duHKa)
            varnas.append(mk(ch))
            i += 1
            continue
        # Skip unknown.
        i += 1

    # आदेशप्रत्यययोः (8.3.59): the *s* of a stem is neither ādeśa nor pratyaya — पुस्तकम्, कुसुमम्, हिंसा keep it. The stem-final
    # *s* of the as / is / us stems (मनस्, हविस्, चक्षुस्, विद्वस्, श्रेयस्) is itself a suffix s, so that one stays eligible.
    for k, v in enumerate(varnas):
        if v.slp1 == "s" and (k < len(varnas) - 1 or (k >= 1 and varnas[k - 1].slp1 not in "aiu")):
            v.tags.add("mula_prakrti_v")      # (a final s not after a/i/u — पुंस् — is no suffix s either)

    stem = Term(
        kind   = "prakriti",
        varnas = varnas,
        # The stem is NOT a pratyaya upadeśa; do not tag it 'upadesha'.
        # This prevents it-prakaraṇa rules like 1.3.3 from wrongly stripping
        # stem-final consonants (critical for consonant-ending stems like `tad`).
        # no saṃjñā yet: 1.2.45 makes it a prātipadika, 1.4.13 an aṅga
        tags   = set(),
        meta   = {"upadesha_slp1": stem_slp1},
    )
    if derived_pratipadika:
        stem.tags.add("prātipadika")
        stem.meta["vyutpanna"] = True
    if stem_slp1.endswith("n"):
        # न्-अन्त प्रातिपदिक (राजन्, आत्मन् …) — lets 8.2.7 tell a stem-final
        # n (प्रातिपदिकान्तस्य) from a sup-derived one (रामान्, सर्वान्); a tag,
        # not state.meta, since meta does not survive sup attachment/merge.
        stem.tags.add("an_pratipadika")
    # Encode liṅga as a Term tag so sūtra cond() can remain blind to
    # state.meta (CONSTITUTION Art. 2).
    if linga == "napuṃsaka":
        stem.tags.add("napuṃsaka")
    elif linga == "strīliṅga":
        stem.tags.add("strīliṅga")
    else:
        stem.tags.add("pulliṅga")
    state = State(terms=[stem])
    state.meta["linga"]            = linga
    state.meta["vibhakti_vacana"]  = f"{vibhakti}-{vacana}"
    if matra_prathama_2_3_46:
        state.meta["2_3_46_matra_prathama_eligible"] = True
    if sheSa_shashthi_2_3_50:
        state.meta["2_3_50_sheSa_shashthi_eligible"] = True
    if nAmadheya_vrddha_term_indices is not None:
        from sutras.adhyaya_1.pada_1.sutra_1_1_73 import (
            META_NAMADHEYA_VRDDHA_INDICES,
        )
        state.meta[META_NAMADHEYA_VRDDHA_INDICES] = frozenset(
            nAmadheya_vrddha_term_indices
        )
    return state


def stem_slp1_looks_akarant_pullinga(stem_slp1: str) -> bool:
    """
    True if ``stem_slp1`` (non-empty, stripped) ends in hrasa ``a`` — the usual
    SLP1 shape for अकारान्त पुंलिङ्ग prātipadikas like ``rAma``, ``gaja``.

    This is *not* a full morphological analysis; it guards UI and
    ``derive_akarant_pullinga`` from obvious non–a-stem input. Does not read
    external gold corpora (CONSTITUTION Art. 6).
    """
    s = stem_slp1.strip()
    if len(s) < 1:
        return False
    return s[-1] == "a"


def stem_slp1_looks_ikarant_pullinga(stem_slp1: str) -> bool:
    """
    True if ``stem_slp1`` (non-empty, stripped) ends in hrasa ``i`` — the usual
    SLP1 shape for इकारान्त पुंलिङ्ग prātipadikas like ``hari``.

    Pipeline/UI guard only; not a full morphological analysis.
    """
    s = stem_slp1.strip()
    if len(s) < 1:
        return False
    return s[-1] == "i"


def derive_ikarant_pullinga(
    stem_slp1: str,
    vibhakti: int,
    vacana: int,
    *,
    strict_stem: bool = True,
) -> State:
    """
    Run the subanta recipe for **इकारान्त पुंलिङ्ग** (i-stem masculine).

    Same as ``derive(..., linga="pulliṅga")`` but optionally validates stem shape
    (``strict_stem=True``).
    """
    if strict_stem and not stem_slp1_looks_ikarant_pullinga(stem_slp1):
        raise ValueError(
            "इकारान्त पुंलिङ्ग हेतु प्रातिपदिक अन्त में ह्रस्व 'i' (SLP1) चाहिए — "
            f"उदाहरण: hari। प्राप्त: {stem_slp1!r}"
        )
    return derive(stem_slp1, vibhakti, vacana, linga="pulliṅga")


def derive_akarant_pullinga(
    stem_slp1: str,
    vibhakti: int,
    vacana: int,
    *,
    strict_stem: bool = True,
) -> State:
    """
    Run the subanta recipe for **अकारान्त पुंलिङ्ग** (a-stem masculine).

    Same as ``derive(stem_slp1, vibhakti, vacana, linga="pulliṅga")`` but
    optionally validates that the stem ends in ``a`` (``strict_stem=True``).
    """
    if strict_stem and not stem_slp1_looks_akarant_pullinga(stem_slp1):
        raise ValueError(
            "अकारान्त पुंलिङ्ग हेतु प्रातिपदिक अन्त में ह्रस्व 'a' (SLP1) चाहिए — "
            f"उदाहरण: rAma, gaja। प्राप्त: {stem_slp1!r}"
        )
    return derive(stem_slp1, vibhakti, vacana, linga="pulliṅga")


def stem_slp1_looks_Akarant_strilinga(stem_slp1: str) -> bool:
    """
    True if ``stem_slp1`` ends in long ``A`` (SLP1 = ā) — the usual shape for
    आकारान्त स्त्रीलिङ्ग prātipadikas like ``rADA`` (राधा, ध = ``D``).

    Pipeline/UI guard only; does not read any gold corpus (CONSTITUTION Art. 6).
    """
    s = stem_slp1.strip()
    if len(s) < 1:
        return False
    return s[-1] == "A"


def derive_akarant_strilinga(
    stem_slp1: str,
    vibhakti: int,
    vacana: int,
    *,
    strict_stem: bool = True,
) -> State:
    """
    Run the subanta recipe for **आकारान्त स्त्रीलिङ्ग** (ā-stem feminine).

    Same as ``derive(stem_slp1, vibhakti, vacana, linga="strīliṅga")`` but
    optionally validates that the stem ends in ``A`` (``strict_stem=True``).
    """
    if strict_stem and not stem_slp1_looks_Akarant_strilinga(stem_slp1):
        raise ValueError(
            "आकारान्त स्त्रीलिङ्ग हेतु प्रातिपदिक अन्त में दीर्घ 'A' (SLP1) चाहिए — "
            f"उदाहरण: rADA (राधा)। प्राप्त: {stem_slp1!r}"
        )
    return derive(stem_slp1, vibhakti, vacana, linga="strīliṅga")


def derive_anya_pullinga(vibhakti: int, vacana: int) -> State:
    """
    **अन्य** — *sarvanāma* (1.1.27 *sarvādi* list), *a*-stem masculine.

    Thin wrapper around ``derive("anya", ...)``.  Gold surfaces live in the
    test/UI gold corpus only (CONSTITUTION Art. 6).
    """
    return derive("anya", vibhakti, vacana, linga="pulliṅga")


# A final -han is the root हन् (kvip / kvun compounds: ब्रह्महन्, वृत्रहन्, शत्रुहन्, वीरहन्, तमिस्रहन्) except the few words that merely
# end that way: अहन् (day) and its -āhan compounds (दीर्घाहन्), and प्लीहन्. A lexical fact, so a short named list, not a spelling rule.
# Structural step in ``run_subanta_post_4_1_2`` (not a sūtra id).
PADA_MERGE_STEP = "__PADA_MERGE__"

# *Śālīyaḥ* (``derive_salIyaH``): taddhita ``derive_salIya`` already ran **1.1.60**–
# **1.1.63** in *luk* order after **2.4.71**; subanta preflight must not re-apply
# (avoids a spurious SKIPPED **1.1.61** before the real *luk* block in the *trace*).
META_SALIYA_TADDHITA_SUBANTA_CONTINUATION = "sAlIya_taddhita_subanta_continuation"

# Canonical ``apply_rule`` ids from **1.3.2** through tripāḍī, in engine order,
# after **4.1.2** has attached *sup*.  Demos may iterate this tuple for verbose
# traces; keep in sync with ``run_subanta_post_4_1_2``.
SUBANTA_RULE_IDS_POST_4_1_2: tuple[str, ...] = (
    "3.1.1",
    "3.1.2",
    "1.4.102",
    "1.1.43",
    "1.4.103",
    "1.4.13",
    "1.4.14",
    "1.1.23",  # बहुगणवतुडति संख्या — the laukika numerals the Kāśikā names (ṣaṣ, pañcan, saptan, aṣṭan, navan, daśan) …
    "1.1.24",  # ष्णान्ता षट् — … get the saṃjñā ṣaṭ (tag zat_samjna), read by 7.1.22, 7.1.55, 4.1.10
    "1.1.40",  # क्त्वातोसुन्कसुनः — a ktvā / tumun-anta kṛdanta stem is avyaya, so 2.4.82 lops its sup (gatvā, never *gatvāḥ*)
    "2.4.82",  # अव्ययादाप्सुपः — the sup after an avyaya (a taddhitānta 1.1.38 gave the saṃjñā: tatra, kutaḥ) is luk'd
    *IT_PRAKARANA_SEQUENCE,  # 1.3.2–1.3.8 saṃjñā, then 1.3.9 lopa
    "1.3.10",
    "7.1.84",  # दिव औत् — div + su: v → au (द्यौः)
    "7.1.85",  # पथिमथ्यृभुक्षामात् — su: the n of पथिन् / मथिन् / ऋभुक्षिन् → ā (पन्थाः)
    "7.1.86",  # इतोऽत् सर्वनामस्थाने — its i → a
    "7.1.87",  # थो न्थः — th → nth (पन्थानौ)
    "7.1.88",  # भस्य टेर्लोपः — पथः, पथा
    "7.4.48",   # अपो भि — ap + bh…: p → t (adbhiḥ)
    "7.2.84",   # अष्टन आ विभक्तौ (vikalpa) — aṣṭan → aṣṭā …
    "7.1.21",   # अष्टाभ्य औश् — … + jas / śas → auś (apavāda of 7.1.22)
    "7.1.22",   # षड्भ्यो लुक् — jas / śas luk after a ṣaṭ numeral: pañca, sapta, nava, daśa, aṣṭa. Before 6.4.8 (vipratiṣedha: the luk removes the jas that 6.4.8 needs)
    "7.1.93",  # anang sau: sakhī 1sg → sakhān (i → an; arm-gated)
    "6.4.13",  # सौ च — in / han / pūṣan / aryaman: dīrgha in the nominative singular (योगी, वृत्रहा)
    "6.4.8",   # dīrgha before sarvananāmasthāna (fires here for anang; idempotent)
    "1.1.34",   # पूर्वपरावर… व्यवस्थायामसंज्ञायाम् — jas optional: the saṃjñā goes (pūrvāḥ) or stays (pūrve, 7.1.17); before 7.1.17
    "1.4.7",
    "1.2.41",
    "7.2.107",  # adas + su: s → au (then 7.2.106 d→s, 6.1.88 → asau)
    "7.2.106",  # tad/tyad t→s before su (must precede 6.1.68 su-lopa; 7.2.106 checks sup still present)
    "2.4.34",   # द्वितीयाटौस्स्वेनः — anvādeśa idam / etad → ena (stem tag ``anvadesha``); before 7.2.10x
    "7.2.108",  # इदमो मः — idam + su keeps its m (apavāda of 7.2.102, tried first)
    "7.2.111",  # इदोऽय् पुंसि — apavāda of 7.2.110
    "7.2.110",  # यः सौ — iyam
    "7.2.103",  # kim → ka (apavāda of 7.2.102, so it is tried first)
    "7.2.102",  # tyadādi final hal→a (must precede 6.1.68; after substitution stem is vowel-final)
    "6.4.1",    # अङ्गस्य — the aṅgakārya adhikāra must be open before 6.4.14 (it is also re-opened harmlessly below)
    "7.1.89",   # पुंसोऽसुङ् — पुंस् → पुमस्: ugit, so 7.1.70 gives nuṃ (पुमान्, पुमांसौ)
    "7.1.98",   # चतुरनडुहोरामुदात्तः — अनडु + आ + ह्, चतु + आ + र्
    "7.1.99",   # अम् सम्बुद्धौ — हे अनड्वन्
    "7.2.99",   # त्रिचतुरोः स्त्रियां तिसृचतसृ
    "7.2.100",  # अचि र ऋतः — तिस्रः, चतस्रः
    "7.1.82",   # सावनडुहः — नुम् in su: अनड्वान्
    "7.1.78",   # नाभ्यस्ताच्छतुः — bars 7.1.70 for an abhyasta Śatṛ stem (before it, its utsarga)
    "7.2.101",  # जराया जरसन्यतरस्याम् — jarA → jaras before a vowel-initial vibhakti (vā)
    "6.4.127",  # अर्वणस्त्रसावनञः — arvan→arvantr (tṛ for n) except before su; the resolver orders it against 6.4.8 (para)
    "7.1.70",   # उगिदचां सर्वनामस्थानेऽधातोः — nuṃ for an ugit stem; before su-lopa (भवान्त्+स्): भवन्तौ, भवान्
    "6.4.14",   # अत्वसन्तस्य चाधातोः — nominative singular only: भवान्त्
    "6.3.46",   # आन्महतः समानाधिकरणजातीययोः — mahat as a samānādhikaraṇa pūrvapada: mahā (maharṣi), before the seam's sandhi
    "6.3.128",  # विश्वस्य वसुराटोः — viśva + rāj (a padas lexicon stem): ā before the rāṭ it will become, ahead of su-lopa (6.1.68)
    "6.1.68",
    "6.4.1",
    "7.1.94",
    "7.3.110",  # ऋतो ङिसर्वनामस्थानयोः — guṇa for ṛ-stems before ṅi/sarvanāmasthāna (mātari, mātarau, mātaraḥ...)
    "1.1.51",   # uraṇ rapara — consumes 7.3.110's pending r (and 7.1.100's, if either fired)
    "6.4.11",
    "6.1.66",
    "7.1.2",
    "6.1.97",
    "4.1.3",    # स्त्रियाम् — feminine adhikāra
    "4.1.4",    # अजाद्यतष्टाप् — feminine sarvanāma: ṭāp after the a-ending stem (ida + ṭāp → idā, tā); strīliṅga only
    "1.4.3",    # यू स्त्र्याख्यौ नदी — the ī of a ṅīp that 4.1.6 attached (its ṅ, p go by it-lopa after 4.1.2): nuṃ 7.1.80–81 and 7.3.107 read nadī
    "1.4.4",    # नेयङुवङ्स्थानावस्त्री — śrī, bhrū, nī (iyaṅuvaṅsthāna) lose it (hē śrīḥ) …
    "1.4.5",    # वाऽऽमि — … back before Ām (śrīṇām / śriyām)
    "1.4.6",    # ङिति ह्रस्वश्च — hrasva strī i/u and iyaṅuvaṅsthāna yU: nadī before ṅit, optionally (matyai / mataye); withdraws 1.4.7's ghi
    "7.1.81",   # शप्श्यनोर्नित्यम् — nuṃ of a Śatṛ-anta aṅga before the nadī (pacantī); before 7.1.80, its utsarga
    "7.1.80",   # आच्छीनद्योर्नुम् — vā, after Sa (tudantī / tudatī)
    "7.3.44",   # प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः — pāṭhaka + ā → pāṭhikā (the ṭāp is already in the aṅga, S2)
    "7.3.106",
    # 7.3.107 must precede 6.1.69: the सु is dropped *after* a hrasva,
    # and it is this rule that makes नदी short in सम्बुद्धि.
    "7.3.107",
    "6.1.69",
    "7.1.15",
    "7.1.16",   # pūrvādibhyo navabhyo vā — the nine take smāt/smin only optionally (pūrvāt / pūrvasmāt)
    "7.1.12",
    "7.2.112",  # अनाप्यकः — idam: id → an before ṭā(ina) / os
    "7.1.14",
    "7.3.116",  # ङेराम्नद्याम्नीभ्यः — ṅi → ām after an āp-anta sarvanāma, before its syāṭ (7.3.114): अस्याम्
    "7.3.113",
    "7.3.114",
    "7.1.13",
    "7.1.11",   # नेदमदसोरकोः — blocks 7.1.9 for idam / adas
    "7.1.9",
    "7.1.17",
    "7.1.18",   # औङ आपः — au/auṭ → śī after an āp-anta aṅga (राधे)
    "7.1.24",
    "7.1.25",  # अद्ड् for tyadādi napuṃsaka (तत्, not पदवत् अम्)
    "6.1.97",  # अतो गुणे after अद् (त + अत् → तत्)
    "7.1.28",  # ङे प्रथमयोरम् — asmad/yuṣmad su→am
    "7.2.94",  # त्वाहौ सौ — asmad→aha
    "6.1.97",  # अह + अम् leftover a-pair after 7.2.94
    "7.2.90",  # शेषे लोपः
    "7.1.19",
    "7.1.20",
    "7.1.23",
    "1.1.42",
    "1.4.17",
    "1.4.16",
    "1.4.18",
    "7.1.53",   # त्रेस्त्रयः — त्रयाणाम्
    "7.1.54",
    "7.1.55",   # षट्चतुर्भ्यश्च — नुट् for चतुर्, षट्: चतुर्णाम्
    "7.1.52",
    # it-prakaraṇa over substitutes / āgamas (śī, śi, suṭ): 1.3.8 names their ś it.
    *IT_PRAKARANA_SEQUENCE,
    # 7.2.113 needs the sup's real first letter (śī / śi are vowel-initial only once their ś is gone),
    # and every sup ādeśa (smai, smāt, smin, sya, sām) is in final shape by now: अस्मै, अस्य, एषाम्
    "7.2.113",  # हलि लोपः — once every sup is in final shape (smai, smāt, smin, sya, sām): अस्मै, अस्य, एषाम्
    "7.2.85",   # रायो हलि विभक्तौ आः — राभ्याम्, रासु
    "7.2.109",  # दश्च — the d that 7.2.112 / 7.2.113 left: इमौ, इमे, इमम्, इमानि
    "7.1.72",
    "7.1.79",   # वा नपुंसकस्य — nuṃ optionally for the neuter abhyasta Śatṛ stem (dadanti / dadati)
    "7.1.73",   # इकोऽचि विभक्तौ — nuṃ for a neuter ik-final aṅga before an ac-initial vibhakti (vāriṇā, madhunī)
    "7.1.75",   # अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः — asthi / dadhi / sakthi / akṣi: i → an before an ac-initial sup of the third vibhakti on (apavāda of 7.1.73)
    "6.4.10",   # upadhā dīrgha after num insertion (dhanuṣ bahu: u→U before n+s)
    "6.4.8",
    # Second 6.1.68 attempt (idempotent, same pattern as 6.4.8's own second
    # occurrence above): ṛ-stem kinship/agent nouns (mAtf, pitf, bhrAtf...)
    # only become hal-final *here*, after 7.1.94's ṛ→an substitution — the
    # earlier 6.1.68 slot (before 7.1.94) permanently skips them since this
    # is a single linear walk, not a scan-to-fixpoint. Already-resolved
    # stems (rAjan, kumArI...) re-check harmlessly: their sup term is gone,
    # so _find_eligible_boundary has nothing to match.
    "6.1.68",
    "6.4.4",    # न तिसृचतसृ — blocks 6.4.3 for तिसृ / चतसृ
    "6.4.3",
    "6.4.7",    # नोपधायाः — the upadhā of an n-final aṅga before the nuṭ of Ām: पञ्चानाम्
    "7.3.103",
    "7.3.104",  # ओसि च — a → e before os (then 6.1.78: rAmayoH)
    "7.3.112",  # आट् for ṅit sups after नदी — नद्यै · नद्याः
    "7.3.116",  # ङि → आम् after नदी — नद्याम्
    "7.3.117",  # इदुद्भ्याम् — ṅi → ām after a hrasva i/u nadī — matyām, dhenvām
    "7.3.102",
    "6.4.129",
    "6.4.130",
    "6.4.137",
    "6.4.136",  # vibhāṣā ṅiśyoḥ: tried before 6.4.134 (ORDER_BEFORE)
    "6.4.134",
    "6.4.146",
    "6.4.148",
    "7.3.108",
    "7.3.109",
    "7.3.111",
    "7.3.105",  # आङि चापः — āp-anta sarvanāma + ṭā: ā → e (इदा → अने + आ), then 6.1.78
    "7.3.118",  # इदुद्भ्यामङ्गात् ङेः औत् — after the nadī (7.3.116/117) and ghi (7.3.119) cases: सख्यौ
    "7.3.119",
    "7.3.120",
    "6.1.104",  # नादिचि — निषेध of 6.1.102 when the pūrva is आत्
    "6.1.102",
    "1.1.11",
    "6.1.103",
    "7.1.92",  # सख्युरसम्बुद्धौ: the sarvanāmasthāna sup is ṇit by atideśa
    "7.1.90",  # गोतो णित् — the sarvanāmasthāna after go (dyo) is ṇit by atideśa
    "7.2.115",  # अचो ञ्णिति: …so the aṅga's final i takes vṛddhi (सखि → सखै), then 6.1.78 → सखाय्
    "6.1.78",
    "6.1.93",   # औतोऽम्शसोः — गां, गाः, द्याम् (para over 6.1.78)
    "6.1.107",
    "6.1.125",
    "6.1.111",  # ऋत उत् — pitṛ + ṅasi/ṅas → पितुः (the apavāda must precede yaṇ)
    "1.1.51",   # uraṇ raparaḥ — the r of that ut
    "6.4.80",   # वाऽम्शसोः — the ī-keeping reading (स्त्रीम्, स्त्रीः); declined by default, both read by explore()
    "6.4.133",  # श्वयुवमघोनामतद्धिते — शुनः, यूनः, मघोनः
    "6.4.132",  # वाह ऊठ् — a bha aṅga …vāh → …ūh (viśvavāh: viśvauhaḥ); before 6.1.89
    "6.4.139",  # उद ईत् — the a of the bha ac after ud becomes ī (udīcaḥ); apavāda of 6.4.138, so tried first
    "6.4.138",  # अचः — the a of a bha ac (añcu, n lost at the stem stage by 6.4.24) goes: prācaḥ
    "6.3.93",   # समः समि — sam → sami before the añcu of a kvin-anta (samyaṅ, samīcaḥ); the whole is replaced (1.1.55)
    "6.3.94",   # तिरसस्तिर्यलोपे — tiras → tiri when the a of añcu stays (not a bha stem: tiryaṅ, tiryagbhyām; tiraścaḥ keeps tiras)
    "6.3.138",  # चौ — the aṇ before the bare c lengthens: prā-c, prati → pratī-c (before 6.1.101 / 6.1.97 would join the a's)
    "6.4.79",   # स्त्रियाः — स्त्री + ac-sup: iyaṅ (स्त्रियौ, स्त्रियः)
    "6.4.84",   # वर्षाभ्वश्च — वर्षाभ्वः
    "6.4.85",   # न भूसुधियोः — blocks 6.4.82 / 6.4.83 for भू, सुधी
    "6.4.82",   # एरनेकाचोऽसंयोगपूर्वस्य — ग्रामण्यौ
    "6.4.83",   # ओः सुपि — खलप्वौ
    "6.4.77",   # अचि श्नुधातुभ्रुवां — नियौ, भ्रुवौ, स्वयम्भुवः
    "6.1.131",  # दिव उत् — द्युभ्याम्, द्युषु: the v of div → u at pada end, then yaṇ
    "6.1.77",
    "6.1.112",  # ख्यत्यात् परस्य — सख्युः, पत्युः: the a of ṅasi / ṅas after the yaṇ of khi / ti becomes u
    "6.1.89",   # एत्येधत्यूठ्सु — a / ā + the ū of ūṭh: vṛddhi (viśva + ūh → viśvauh); apavāda of 6.1.88 / 6.1.94
    "6.1.87",
    "6.1.88",
    "6.1.110",
    "6.1.101",
    PADA_MERGE_STEP,
    "1.4.110",
    "8.2.1",
    "8.2.8",    # na NisambudDyoH — the prohibition is settled before 8.2.7 (Art. 21 Ladder 1)
    "8.2.7",    # nalopaH prAtipadikAntasya — rAjan/Atman-final n-lopa at pada-end
    "8.2.23",   # संयोगान्तस्य लोपः — pada-final cluster loses its last letter (भवान्त् → भवान्)
    "8.2.29",   # skoH saMyogAdyorante ca — lagna (lasj+ta), magna: the cluster-initial s before a jhal
    "8.2.57",   # na DyAKyApUmUrcCimadAm — the prohibition first (Art. 21): dhyāta, khyāta, pūrta, mūrta, matta
    "8.2.42", "8.2.43", "8.2.44", "8.2.45", "8.2.46",   # niṣṭhā-ta → na: bhinna, mlāna, lūna, līna, kṣīṇa
    "8.2.51", "8.2.52", "8.2.53",   # śuṣka, pakva, kṣāma
    "8.2.56",   # nud, vid, und, trā, ghrā, hrī: na vibhāṣā (vinna / vitta)
    "8.2.30",   # coH kuH — c/j-vargIya pada-final -> k-vargIya before jhal (vAc+Bis)
    "8.2.80",   # adaso'ser dAd u do maH — d → m, following vowel → u/U
    "8.2.81",   # eta Id bahuvacane — e → I (amI), d → m
    "8.2.63",   # naśer vā — naś: the final → ku, or not (nak / naṭ)
    "8.2.39",   # JalAM jaSo'nte — jhal pada-final -> jaS (vAk -> vAg, etc.)
    "8.2.66",
    "8.2.68",   # ahan → ahaH / aho- (the n is not 8.2.7's)
    "8.3.14",   # ro ri
    "8.3.15",   # ru → visarga at avasāna or before khar
    "8.3.16",   # roḥ supi (trace/ANUVADA; structural work done by 8.3.15)
    "8.3.24",   # n → anusvāra before jhal
    "8.3.36",
    "8.3.111", "8.3.58", "8.3.59",   # ṣatva: scans back through M/H so fires correctly after 8.3.24/8.3.15
    "8.4.1",
    "8.4.2",
    "8.4.12",   # एकाजुत्तरपदे णः — the ṇatva across a samāsa's pūrvapada | uttarapada seam (vṛtrahaṇau)
    "8.4.40",   # stoH ScunA ScuH — n→Y (rAjYA etc.), only the j+n slice
    "8.4.41",
)


def _subanta_scanner_winner_by_spine_order(candidates: list[str], spine_ids: list[str], state: State) -> str:
    """
    When several post-4.1.2 sūtras *cond* true together, ``engine.resolver`` decides
    (Art. 21 Ladder 1: apavāda → antaraṅga → para) and the beaten rules are recorded as
    BLOCKED. ``SUBANTA_RULE_IDS_POST_4_1_2`` is the candidate *pool* and the phase order
    of the pools — it no longer breaks ties (ROADMAP C2/C4).
    """
    if not candidates:
        raise ValueError("subanta scanner needs at least one candidate")
    if len(candidates) == 1:
        return candidates[0]
    from engine.sutra_type import SutraType as _STp
    from engine.registry import get_sutra as _gs

    prohibitions = [c for c in candidates if _gs(c).sutra_type is _STp.PRATISHEDHA]
    if prohibitions:
        return prohibitions[0]          # Art. 21 Ladder 1, step 3: prohibitions are settled before rules contend (core_loop.apply_pratishedhas)
    from engine.resolver import record_decision, resolve_with_reason

    decision = resolve_with_reason(candidates, state)
    record_decision(state, decision)
    return decision.winner


def _sid_key(sid: str) -> tuple[int, ...]:
    return tuple(int(x) for x in sid.split("."))


def _note_tripadi(state: State, sutra_id: str) -> None:
    from engine.core_loop import note_tripadi_progress

    note_tripadi_progress(state, sutra_id)


def run_subanta_post_4_1_2_scanner(s: State, *, max_steps: int = 500) -> State:
    from engine.resolver import resolver_decides

    with resolver_decides():
        return _run_subanta_post_4_1_2_scanner(s, max_steps=max_steps)


def _run_subanta_post_4_1_2_scanner(s: State, *, max_steps: int = 500) -> State:
    """
    Scan-driven execution for the post-4.1.2 region.

    This replaces the “macro list” style (linear iteration) with a repeated
    scan over the *same* rule pool:
    - enumerate applicable candidates on the current state
    - if several apply, take the earliest listed on ``SUBANTA_RULE_IDS_POST_4_1_2``
    - apply that id via ``apply_rule``
    - repeat until no candidates remain or ``max_steps`` is hit

    The candidate pool is intentionally limited to the subanta post-4.1.2
    spine (this module’s curated coverage set). It is **not** a global
    registry-wide autonomous derivation.
    """
    from engine.registry import get_sutra
    from engine.trace import TRACE_STATUSES_FIRED
    from engine.gates import asiddha_violates, is_blocked, is_frozen_by_nipatana

    # De-duplicate ids: unlike a linear recipe, a scanner does not need
    # repeated scheduling of the same sūtra id.
    all_ids: list[str] = list(dict.fromkeys(
        sid for sid in SUBANTA_RULE_IDS_POST_4_1_2 if sid != PADA_MERGE_STEP
    ))

    def _state_sig(st: State) -> tuple:
        # Signature for “did this rule actually do new work at a new site?”
        # Must be sensitive to term segmentation + tags, not just flat form.
        return (
            st.flat_slp1(),
            tuple(
                (
                    t.kind,
                    t.meta.get("upadesha_slp1"),
                    tuple(sorted(t.tags)),
                    len(t.varnas),
                    (t.varnas[0].slp1 if t.varnas else None),
                    (t.varnas[-1].slp1 if t.varnas else None),
                )
                for t in st.terms
            ),
            st.phase,
            st.tripadi_zone,
            frozenset(st.blocked_sutras),
        )

    def _scan_pool(ids: list[str]) -> None:
        nonlocal s
        remaining = list(ids)
        # Ledger: (sutra_id, state_signature_before) pairs that led to a fired
        # step without changing the signature (i.e., repeating the same “site”
        # would be an un-Pāṇinian infinite loop).
        no_progress_sites: set[tuple[str, tuple]] = set()
        steps = 0
        while remaining:
            if steps >= max_steps:
                raise RuntimeError(
                    f"subanta scanner exceeded max_steps={max_steps}; "
                    f"last form: {s.flat_slp1()!r}; remaining terms: {len(s.terms)}"
                )
            steps += 1

            candidates: list[str] = []
            for sid in remaining:
                rec = get_sutra(sid)
                if is_blocked(sid, s):
                    # Art. 15 glass box: a rule a pratiṣedha withholds says so in the trace (once), when it would otherwise have applied
                    if rec.cond is not None and not any(r.get("sutra_id") == sid and r.get("status") == "BLOCKED" for r in s.trace):
                        try:
                            if rec.cond(s):
                                s = apply_rule(sid, s)      # the dispatcher's pratiṣedha gate writes the BLOCKED row
                        except Exception:
                            pass
                    continue
                if asiddha_violates(sid, s):
                    continue
                if is_frozen_by_nipatana(rec.sutra_type, s):
                    continue
                if (sid, _state_sig(s)) in no_progress_sites:
                    continue
                cur = s.meta.get("tripadi_cursor")
                if cur and s.tripadi_zone and _sid_key(sid) < _sid_key(cur) and not sees_later_tripadi(sid, cur):
                    continue            # 8.2.1: an earlier tripāḍī rule never wakes on a later one's work
                if rec.cond is not None and rec.cond(s):
                    candidates.append(sid)

            # C2: a rule that would change nothing (a declined vibhāṣā, a gate-only record)
            # is not a candidate.
            from engine.scheduler import effective_candidates
            from engine.sutra_type import SutraType as _ST2

            # An adhikāra (6.4.1 अङ्गस्य, 8.2.1 पूर्वत्रासिद्धम्) changes no letter but opens the
            # scope every later rule reads; it is exempt from the vacuity test.
            scopes = [c for c in candidates if get_sutra(c).sutra_type in (_ST2.ADHIKARA, _ST2.PRATISHEDHA)]       # a निषेध changes no letter either
            rest = [c for c in candidates if c not in scopes]
            # One rule left needs no contest; the no-progress ledger below catches it if it is vacuous.
            # Probing every candidate on a clone is what makes this path slow, so only contested
            # steps pay for it.
            candidates = (effective_candidates(rest, s) if len(rest) > 1 else rest) + scopes
            if not candidates:
                return

            # An adhikāra opens its scope before the rules inside it contend (6.4.1 अङ्गस्य precedes 6.4.8 / 6.4.127).
            opening = [c for c in scopes if get_sutra(c).sutra_type is _ST2.ADHIKARA]
            winner = opening[0] if opening else _subanta_scanner_winner_by_spine_order(candidates, all_ids, s)
            sig_before = _state_sig(s)
            before_len = len(s.trace)
            s = apply_rule(winner, s)
            if (_state_sig(s) != sig_before or winner == "8.2.1") and get_sutra(winner).sutra_type is not _ST2.PRATISHEDHA:
                _note_tripadi(s, winner)       # (a niṣedha is no step of the order: it forbids, it does not run)       # 8.2.1: only a rule that did something puts the later ones out of reach (a declined vā rule does not)
            # Whatever the status (a declined vibhāṣā is not FIRED), a step that left the state
            # signature unchanged may not run again on that same signature.
            if _state_sig(s) == sig_before:
                no_progress_sites.add((winner, sig_before))

    # Phase-ordered pools (still glass-box, but no hardcoded linear macro pass):
    # - it-prakaraṇa first (so later rules see cleaned affix shapes)
    # - aṅgakārya next (6.4/7.* + bha/pada saṃjñā)
    # - sandhi next (6.1.*)
    # - structural merge into pada
    # - tripāḍī last (8.2.1+)
    it_ids      = [sid for sid in all_ids if sid.startswith("1.3.")]
    # The tripāḍī pool is the whole stratum (8.2.1–8.4.68), not a curated list: the loop
    # asks every rule there, 8.2.1 orders them, and the resolver settles contention.
    from engine.phase import is_tripadi_sutra
    from engine.registry import SUTRA_REGISTRY
    from engine.sutra_type import SutraType as _ST

    tripadi_ids = sorted(
        (sid for sid, rec in SUTRA_REGISTRY.items()
         if is_tripadi_sutra(sid) and (
             rec.sutra_type in (_ST.VIDHI, _ST.NIYAMA, _ST.VIBHASHA, _ST.NIPATANA, _ST.PRATISHEDHA)
             or rec.sutra_type is _ST.ADHIKARA)),      # 8.2.1 itself: it opens the stratum
        key=lambda sid: tuple(int(x) for x in sid.split(".")),
    )
    # The sandhi pool is 6.1.* plus the Adhyāya-1 rules the curated spine places *between* sandhi rules
    # (1.1.11 must see the harī that 6.1.102 has just made; 1.1.51 shapes the guṇa that precedes 6.1.77):
    # saṃjñā and paribhāṣā apply whenever their condition arises, not at a stage.
    first6 = next(i for i, sid in enumerate(all_ids) if sid.startswith("6.1."))
    last6 = max(i for i, sid in enumerate(all_ids) if sid.startswith("6.1."))
    sandhi_ids = [sid for i, sid in enumerate(all_ids)
                  if sid.startswith("6.1.") or (first6 <= i <= last6 and sid.startswith("1.") and not sid.startswith("1.3."))]
    angakarya_ids = [
        sid for sid in all_ids
        if sid not in set(it_ids) and (not sid.startswith("6.1.") or sid == "6.1.93") and not is_tripadi_sutra(sid)
    ]       # Adhyāya 1 stays in this pool too (see sandhi_ids); 6.1.93 competes with 7.2.115 here — the apavāda that takes away the vṛddhi of गो + अम् / शस्

    def _why_not(ids: list[str]) -> None:
        """Glass box: a rule of the pool that never came up still shows in the trace as SKIPPED
        (cond false here) — the learner sees what was *not* applied, as the recipe always showed."""
        nonlocal s
        seen = {row.get("sutra_id") for row in s.trace}
        for sid in ids:
            rec = get_sutra(sid)
            if sid in seen or rec.cond is None or is_blocked(sid, s):
                continue
            try:
                if rec.cond(s):
                    continue
            except Exception:
                pass
            s = apply_rule(sid, s)

    _scan_pool(it_ids)
    if any("stri_wAp" in u.tags and u.varnas for u in s.terms):
        # SHORTCUT S2: the ṭāp joins its stem (a + ā → ā, 6.1.101) inside the aṅga first, so that 7.3.105 / 106 / 113 and the ā-stem rules
        # see an ā-final aṅga, as for a lexicon stem like KawvA. Correct form: the scheduler orders 6.1.101 by the sūtra order.
        s.meta["ekadesha_scope"] = "tap"
        _scan_pool(["6.1.101"])
        s.meta.pop("ekadesha_scope", None)
    _scan_pool(angakarya_ids)
    _why_not(angakarya_ids)
    # Second it-prakaraṇa pass over substitutes created in aṅgakārya (śī 7.1.17/19,
    # śi 7.1.20: ś is it by 1.3.8).
    _scan_pool(list(IT_PRAKARANA_SEQUENCE))
    _scan_pool(sandhi_ids)
    # Pre-merge rutva: enter tripāḍī zone and convert stem-final s→r before HAL-initial sup
    # (8.2.66 _target_premerge requires len(terms)≥2, so must run before _pada_merge)
    _scan_pool(["8.2.1", "8.2.8", "8.2.7", "8.2.23", "8.2.72", "8.2.66", "8.2.68", "8.2.76"])
    s.meta.pop("tripadi_cursor", None)    # the stem as a pada (8.2.23 / 8.2.72 / 8.2.66 on its own end) is one site, the word's end another: 8.2.1 orders within a site
    _scan_pool(["6.1.113", "6.1.114", "6.1.87"])   # ru after a → u before a haś (manaru+bhyām), then a+u → o: manobhyām

    _pada_merge(s)          # always: a single term (su already lopa'd) still becomes the pada (8.2.7 reads it)

    _scan_pool(tripadi_ids)
    return s


def run_subanta_sup_attach_and_finish_scanner(s: State, *, max_steps: int = 500) -> State:
    """
    Preflight (P01) is still recipe-scheduled (includes ANUVADA and adhikāra openings).
    After 4.1.2 attaches sup, the rest is driven by the scanner loop.
    """
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    return run_subanta_post_4_1_2_scanner(s, max_steps=max_steps)


def run_subanta_pipeline(s: State) -> State:
    """
    Run the standard *subanta* ``apply_rule`` sequence on an already-built
    ``State`` (as returned by ``build_initial_state``).  Used by ``derive()``
    and by demos that attach a compound stem before *sup* (e.g. dik-samāsa).

    Implementation: ``core.canonical_pipelines`` — P01 (preflight) +
    *sup* + P13 (it → pada-merge) + P14–P15 (tripāḍī), all through ``apply_rule`` only.
    """
    s = run_subanta_preflight_through_1_4_7(s)
    return run_subanta_sup_attach_and_finish(s)


# (stem, liṅga) pairs whose forms the resolver-driven scanner does not yet reproduce, measured by
# tools/loop_vs_recipe on 2026-10-03. Two causes, both *missing rules*, not pipeline bugs:
#   • the strī of the tyadādi/kim/etad family needs ṭāp (4.1.4) as a rule — the recipe injects it structurally;
#   • idam's 7.2.102–113 ordering needs Kāśikā-sourced apavāda/nitya declarations (docs/GITA_GAP_PLAN.md).
# Quarantined, not hidden: they stay on the recipe until their rules exist; the set may only shrink
# (tests/constitutional/test_recipe_only_stems_ratchet.py). "*" = every liṅga.
_RECIPE_ONLY: frozenset[tuple[str, str]] = frozenset({
    ("idam", "*"), ("tyad", "strīliṅga"), ("tad", "strīliṅga"), ("yad", "strīliṅga"),
    ("etad", "strīliṅga"), ("kim", "strīliṅga"), ("kim", "napuṃsaka"),
})


def _recipe_only(stem_slp1: str, linga: str, anvadesha: bool) -> bool:
    # anvādeśa (2.4.32–34) is a caller-proposed input whose rules the scanner pool does not carry yet.
    return anvadesha or (stem_slp1, "*") in _RECIPE_ONLY or (stem_slp1, linga) in _RECIPE_ONLY


def _norm_root(x: str) -> str:
    """A stem's dhātu letters against the Dhātupāṭha's: 6.1.65 (ṇ-/ṣ-initial roots n-/s-) and 6.4.15 (a lengthened upadhā) leave the root itself."""
    x = x.translate(str.maketrans("AIUF", "aiuf"))
    return ("n" + x[1:] if x[:1] == "R" else "s" + x[1:] if x[:1] == "z" else x)


def derive(stem_slp1: str, vibhakti: int, vacana: int,
           linga: str = "pulliṅga",
           *,
           matra_prathama_2_3_46: bool = False,
           nAmadheya_vrddha_term_indices: tuple[int, ...] | frozenset[int] | None = None,
           autonomous_scanner: bool | None = None,
           anvadesha: bool = False,
           **vivaksha: str,
           ) -> State:
    """
    Aṣṭādhyāyī-kram pipeline.  Returns final state with complete trace.

    ``vivaksha`` — the speaker's intended meaning for this noun (engine/vivaksha.py: ``svaBeda``, ``antaraBeda``, ``kArakaArTa`` …),
    recorded on the tape by engine/tape_init; the sūtras that name the meaning read it, nothing sets a tag by hand.

    A stem's origin (made by matup / tṛc / kvip, from the dhātu han …) is **not** an argument: it comes from the Lexicon
    (``data/inputs/subanta_lexicon.json``, AMENDMENT 22). ``engine.lexicon.compose`` runs the entry's components through the
    real it-prakaraṇa and leaves a vyutpatti record on the stem (``engine/origin.py``); 7.1.70 (ugit), 6.4.11 (tṛc), 6.4.12/13
    (han) read that record. A stem with no entry is an avyutpanna prātipadika (1.2.45).

    ``anvadesha`` — the stem is in *anvādeśa* (2.4.32: a second mention, new predicate); tags the stem so
    **2.4.34** can give इदम् / एतद् → एन (एनम्, एनेन, एनयोः).  A fact about the sentence, so an input.

    ``matra_prathama_2_3_46`` — forwarded to ``build_initial_state``; when
    True, preflight runs **2.3.1** then **2.3.46** after **1.4.14**.

    ``nAmadheya_vrddha_term_indices`` — forwarded to ``build_initial_state``
    for **1.1.73** *vārttika* (*nāmadheya* optional *vṛddha*).

    NOTE (anti-patchwork): samāsa saṃjñās (bahuvrīhi / tṛtīyā-tatpuruṣa) must come
    from an upstream samāsa derivation. Use `derive_from_state(...)` instead of
    injecting them here.
    """
    if stem_slp1.strip() in {"tad", "yad", "etad", "idam", "adas"} and vibhakti == 8:
        raise ValueError("tyadādi pronouns do not take sambodhana cells")
    if linga == "strīliṅga" and stem_slp1.endswith("A"):
        # the feminine of a sarvādi word (sarvā, anyatarā, parā) is the a-stem + ṭāp (4.1.4): derive it from there, where the
        # sarvanāma rules (7.3.114 syāṭ, 7.1.52 suṭ) already run
        from sutras.adhyaya_1.pada_1.sutra_1_1_27 import _load_sarvadi
        if stem_slp1[:-1] + "a" in _load_sarvadi():
            stem_slp1 = stem_slp1[:-1] + "a"
    from engine import lexicon
    entry = lexicon.lookup(stem_slp1, linga)
    origin_record: set[str] = set()
    if entry is not None:
        _surface, origin_record = lexicon.compose(entry)       # LexiconGap if the analysis does not reproduce the stem (Art. 17/18)
    s = build_initial_state(
        stem_slp1, vibhakti, vacana, linga,
        matra_prathama_2_3_46=matra_prathama_2_3_46,
        nAmadheya_vrddha_term_indices=nAmadheya_vrddha_term_indices,
        derived_pratipadika=entry is not None,
    )
    s.terms[0].tags |= origin_record
    if entry is not None and entry.get("padas"):
        s.terms = _padas_tape(entry, s.terms[0])
    if vivaksha:
        from engine.tape_init.sanadi import with_vivaksha
        with_vivaksha(s, **vivaksha)
    if entry is not None:
        # the stem ends in the dhātu itself (kvip leaves nothing but it): its letters are the dhātu's own, for the tripāḍī rules that say
        # "dhātoḥ" (8.2.31–8.2.37) and name roots (8.2.36). The lexicon's record names the dhātu; the tape is only marked, not changed.
        from pipelines.dhatupatha import resolve_dhatu_identifier
        for tag in origin_record:
            if tag.startswith("origin_dhatu:"):
                try:
                    root = (resolve_dhatu_identifier(tag.split(":", 1)[1]).get("raw_dhatu_after_it_lopa_slp1") or "").replace("~", "")
                except KeyError:
                    continue
                vs = s.terms[0].varnas
                if root and _norm_root("".join(v.slp1 for v in vs)).endswith(_norm_root(root)):
                    for v in vs[len(vs) - len(root):]:
                        v.tags |= {"dhatu_v", "mula_dhatu_v"}
                    s.terms[0].meta["it_lopa_done"] = (tag.split(":", 1)[1], root)
    if anvadesha:
        s.terms[0].tags.add("anvadesha")
    if autonomous_scanner is None:
        autonomous_scanner = not _recipe_only(stem_slp1, linga, anvadesha)
    if autonomous_scanner:
        return run_subanta_sup_attach_and_finish_scanner(s)
    return run_subanta_pipeline(s)


def _padas_tape(entry: dict, stem) -> list:
    """A lexicon entry that keeps its parts apart (viśva + vah + kvip, pra + añc + kvin): the composed Terms replace the flat stem. The
    pūrvapada(s) are samāsa members; the last live Term is the stem proper and carries what the flat stem carried (saṃjñā, liṅga, record)."""
    from engine import lexicon
    live = [t for t in lexicon.stem_terms(entry) if t.varnas]
    for t in live[:-1]:
        t.tags.add("samasa_purvapada")
    live[-1].tags |= stem.tags | ({"samasa_uttarapada"} if len(live) > 1 else set())
    if "origin_pratyaya:kvin" in live[-1].tags:       # a kvin stem is a kṛdanta prātipadika (1.2.46), no longer the dhātu: 7.1.70 says adhātoḥ; its record names the dhātu. (kvip stems keep the dhātu Term: 8.2.36 rāj, 6.4.132 vāh read it)
        live[-1].tags -= {"upadesha", "dhatu"}
    for t in live if "origin_pratyaya:kvin" in live[-1].tags else ():     # ponytail: only añcu + kvin — rājf~ (kvip) must not get a nuṃ; the general ugit-of-a-kṛdanta rule is not written
        live[-1].tags |= {"origin_it:" + c for c in t.meta.get("it_markers", ()) if c in "uUfFxX"}
    live[-1].meta.update({k: v for k, v in stem.meta.items() if k not in live[-1].meta})
    return live


def derive_all_readings(*args, **kwargs) -> list:
    """Every legitimate surface this cell can produce, one per वा/विभाषा
    combination actually reached (``engine.vikalpa.explore``) — same
    arguments as ``derive()``. ``derive()`` itself still returns exactly one
    reading, so existing callers are unaffected; this is the opt-in for a
    caller that wants every branch (docs/FINAL_PLAN_2026-09.md item 6,
    "optional forms are still single-output").

    Returns a list of ``engine.vikalpa.Branch``; exactly one element when no
    वा rule was reached, matching ``derive()``'s own shape in that case.
    """
    from engine.vikalpa import explore
    return explore(lambda: derive(*args, **kwargs))


def _pada_merge(state: State) -> None:
    """Structural merge. Delegates to engine.phases.pada_merger.pada_merge."""
    from engine.phases.pada_merger import pada_merge
    pada_merge(state)
