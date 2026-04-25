"""
pipelines/subanta.py — subanta derivation driver.
──────────────────────────────────────────────────

Given:
  stem_slp1    : str, e.g. "rAma" (Velthuis / SLP1-style; अकारान्त = ends in hrasa ``a``)
  vibhakti     : 1..8
  vacana       : 1..3
  linga        : "pulliṅga" | "strīliṅga" | "napuṃsaka"

अकारान्त पुंलिङ्ग (a-stem masculine) helpers:
  • ``stem_slp1_looks_akarant_pullinga`` — shape check (pipeline/UI only).
  • ``derive_akarant_pullinga`` — same recipe as ``derive(..., linga="pulliṅga")``
    after validating stem shape (raises ``ValueError`` if not a-kāra-anta).

Returns:
  State  — with full trace in state.trace and rendered surface in
           state.flat_dev()  (reconcile with phonology.joiner for
           proper halanta/mātrā surface).

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
        1.1.100  *na mātrā samāse* ( *Kāśikā* *vṛtti*; not the Pāṇini *1.1.14* pāṭha)
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
from __future__ import annotations

from typing import List

from engine            import apply_rule
from engine.state      import State, Term
from phonology         import mk
from phonology.varna   import mk_inherent_a


def build_initial_state(stem_slp1: str, vibhakti: int, vacana: int,
                        linga: str = "pulliṅga",
                        *,
                        matra_prathama_2_3_46: bool = False,
                        nAmadheya_vrddha_term_indices: tuple[int, ...] | frozenset[int] | None = None,
                        ) -> State:
    """Build the initial state for a subanta derivation.

    ``matra_prathama_2_3_46`` — when True, sets
    ``state.meta['2_3_46_matra_prathama_eligible']`` so the subanta recipe
    may schedule **2.3.1** + **2.3.46** in preflight (caller opts into this
    *śāstra* slice; default subanta behaviour is unchanged).

    ``nAmadheya_vrddha_term_indices`` — optional indices for **1.1.73**
    *vārttika* (*vā nāmadheyasya vṛddha-saṃjñā*); stored as
    ``state.meta['1_1_73_nAmadheya_vrddha_term_indices']`` for **1.1.73**.
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
        if ch in AC_DEV:
            varnas.append(mk(ch))
            i += 1
            continue
        # Skip unknown.
        i += 1

    stem = Term(
        kind   = "prakriti",
        varnas = varnas,
        # The stem is NOT a pratyaya upadeśa; do not tag it 'upadesha'.
        # This prevents it-prakaraṇa rules like 1.3.3 from wrongly stripping
        # stem-final consonants (critical for consonant-ending stems like `tad`).
        tags   = {"prātipadika", "anga"},
        meta   = {"upadesha_slp1": stem_slp1},
    )
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


# Structural step in ``run_subanta_post_4_1_2`` (not a sūtra id).
PADA_MERGE_STEP = "__PADA_MERGE__"

# Canonical ``apply_rule`` ids from **1.3.2** through tripāḍī, in engine order,
# after **4.1.2** has attached *sup*.  Demos may iterate this tuple for verbose
# traces; keep in sync with ``run_subanta_post_4_1_2``.
SUBANTA_RULE_IDS_POST_4_1_2: tuple[str, ...] = (
    "1.3.2",
    "1.3.3",
    "1.3.4",
    "1.3.5",
    "1.3.6",
    "1.3.7",
    "1.3.8",
    "1.3.9",
    "1.3.10",
    "6.4.1",
    "7.1.2",
    "7.2.106",
    "7.2.102",
    "6.1.97",
    "6.1.69",
    "7.1.15",
    "7.1.12",
    "7.1.14",
    "7.3.113",
    "7.3.114",
    "7.1.13",
    "7.1.9",
    "7.1.17",
    "7.1.24",
    "7.1.19",
    "7.1.20",
    "1.1.42",
    "1.4.17",
    "1.4.16",
    "1.4.18",
    "7.1.54",
    "7.1.52",
    "1.3.5",
    "1.3.7",
    "1.3.9",
    "7.1.72",
    "6.4.8",
    "6.4.3",
    "7.3.103",
    "7.3.102",
    "6.4.129",
    "6.4.130",
    "6.4.134",
    "6.4.146",
    "6.4.148",
    "7.3.108",
    "7.3.109",
    "7.3.111",
    "7.3.119",
    "7.3.120",
    "6.1.102",
    "6.1.103",
    "6.1.78",
    "6.1.107",
    "6.1.77",
    "6.1.87",
    "6.1.88",
    "6.1.110",
    "6.1.101",
    PADA_MERGE_STEP,
    "8.2.1",
    "8.2.66",
    "8.3.15",
    "8.3.59",
    "8.4.1",
    "8.4.2",
)


def run_subanta_preflight_through_1_4_7(s: State) -> State:
    """
    STAGE 1 of ``run_subanta_pipeline``: saṃjñā preflight through **1.4.7**
    (everything before **4.1.2** *sup* attach).  Includes **1.2.45** *prātipadika*
    on *arthavad* non-dhātu stems.
    """
    s = apply_rule("1.4.14", s)
    if s.meta.get("2_3_46_matra_prathama_eligible"):
        s = apply_rule("2.3.1", s)
        s = apply_rule("2.3.46", s)
    s = apply_rule("4.1.1",  s)
    # Strī-pratyaya *ṭāp* (4.1.4) under *strī* adhikāra (4.1.3), before *sup* (4.1.2).
    if any("strīliṅga" in t.tags for t in s.terms):
        s = apply_rule("4.1.3", s)
        s = apply_rule("4.1.4", s)
    s = apply_rule("1.1.1",  s)  # saṃjñā only — prayoga awaits vidhi (e.g. 6.1.88)
    s = apply_rule("1.1.73", s)  # *vṛddha-pada* indices (1.1.1 *vṛddhi* + first *ac*)
    s = apply_rule("1.1.2",  s)
    s = apply_rule("1.1.3",  s)  # *ik* *sthāyin* gate for *guṇa* / *vṛddhi*
    s = apply_rule("1.1.7",  s)  # *saṃyoga* = adjacent *hal* (Tripāḍī / *hal* *vidhi* scope)
    s = apply_rule("1.1.60", s)  # *lopa* saṃjñā (*sthāne adarśanam*; anuv.* *sthāne* 1.1.50)
    s = apply_rule("1.1.61", s)  # *luk* / *ślu* / *lup* — *pratyaya-lopa* classes (needs 1.1.60)
    s = apply_rule("1.1.62", s)  # *pratyayalope pratyayalakṣaṇam* (paribhāṣā gate)
    s = apply_rule("1.1.63", s)  # *na lumatā … aṅgasya pratyayalakṣaṇam* (*apavāda* to 1.1.62)
    s = apply_rule("1.1.8",  s)  # *anunāsika* (anchor for ``anunasika`` / *M* in prakriyā)
    s = apply_rule("1.1.9",  s)  # *savarṇa* (6.1.101 / sandhi premiss)
    s = apply_rule("1.1.10", s)  # *nājjhalau* (*it* locus; before 1.3.2)
    s = apply_rule("1.1.11", s)  # *pragṛhya* (dual *ī*…*au* in *saṃjñā*)
    s = apply_rule("1.1.12", s)  # *adaso māt* (paribhāṣā for *a*ś / *etad*–*adas* *it*)
    s = apply_rule("1.1.13", s)  # *śe* ( *aś* / *ś* locus vs *pragṛhya* )
    s = apply_rule("1.1.14", s)  # *nipāta ekājanāṅ* ( 11014; *saṃjñā* for *ekāc* *nipāta* )
    s = apply_rule("1.1.100", s)  # *Kāśikā* *na mātrā samāse* ( *vṛtti*; *paribhāṣā* *gate* )
    s = apply_rule("1.1.15", s)  # *ot* ( 11015; *saṃjñā* )
    s = apply_rule("1.1.16", s)  # *sambuddhau śākalyasya*… ( 11016; *saṃjñā* )
    s = apply_rule("1.1.17", s)  # *uÞ* *aḥ* ( 11017 )
    s = apply_rule("1.1.18", s)  # *ū̐* ( 11018; ``U.N`` in SLP1)
    s = apply_rule("1.1.19", s)  # *IdU tau* *saptamī*-*artha* ( 11019; *saṃjñā* *extension* of 1.1.11)
    s = apply_rule("1.1.20", s)  # *dA-DhA* *ghu* *ad*+**āp** ( 11020; *ghu* *dhātu* *set* )
    s = apply_rule("1.1.21", s)  # *Adyantavad* *ekasmin* ( 11021; *paribhāṣā* )
    s = apply_rule("1.1.46", s)  # *AdyantO* *TakitO* — *ṭit* before / *kit* after *āgamin*
    s = apply_rule("1.1.22", s)  # *tarap-tamapO* *ghaH* ( 11022; *gha* *taddhita* *pratyaya* *set* )
    s = apply_rule("1.1.23", s)  # *bahuganavatuqati* *saMkhyA* ( 11023; *saṅkhyā* *prātipadika* *set* )
    s = apply_rule("1.1.24", s)  # *zRAntA* *zaW* ( 11024; *ṣaṭ* ending-set {'z','n'} )
    # v3.7: tyadādi-gaṇa tagging (includes sarvanāma tag for these stems).
    s = apply_rule("1.2.72", s)
    # *Avyutpanna* *prātipadika* (before **1.2.46** *kṛt-taddhita-samāsa* scope).
    s = apply_rule("1.2.45", s)
    # v3.5: sarvanāma-saṃjñā (sarvādi-gaṇa; rules self-gate).
    s = apply_rule("1.1.27", s)
    # v3.4: घि-संज्ञा for hari-like i/u stems (rules self-gate).
    s = apply_rule("1.4.7",  s)
    return s


def run_subanta_post_4_1_2(s: State) -> State:
    """
    Run **1.3.2** … tripāḍī on ``s`` after **4.1.2** has attached *sup*.
    Inserts ``_pada_merge`` at the same point as the historical monolithic recipe.
    """
    for rid in SUBANTA_RULE_IDS_POST_4_1_2:
        if rid == PADA_MERGE_STEP:
            _pada_merge(s)
        else:
            s = apply_rule(rid, s)
    return s


def run_subanta_pipeline(s: State) -> State:
    """
    Run the standard *subanta* ``apply_rule`` sequence on an already-built
    ``State`` (as returned by ``build_initial_state``).  Used by ``derive()``
    and by demos that attach a compound stem before *sup* (e.g. dik-samāsa).
    """
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2",  s)
    return run_subanta_post_4_1_2(s)


def derive(stem_slp1: str, vibhakti: int, vacana: int,
           linga: str = "pulliṅga",
           *,
           matra_prathama_2_3_46: bool = False,
           nAmadheya_vrddha_term_indices: tuple[int, ...] | frozenset[int] | None = None,
           ) -> State:
    """
    Aṣṭādhyāyī-kram pipeline.  Returns final state with complete trace.

    ``matra_prathama_2_3_46`` — forwarded to ``build_initial_state``; when
    True, preflight runs **2.3.1** then **2.3.46** after **1.4.14**.

    ``nAmadheya_vrddha_term_indices`` — forwarded to ``build_initial_state``
    for **1.1.73** *vārttika* (*nāmadheya* optional *vṛddha*).
    """
    # Tyadādi pronouns like `tad` have no sambodhana (no vibhakti 8 forms).
    if vibhakti == 8 and stem_slp1.strip() in {"tad", "tyad", "yad", "etad", "idam", "adas", "kim"}:
        raise ValueError("त्यदादि-शब्देषु सम्बोधन-रूप (८-*) नास्ति।")

    s = build_initial_state(
        stem_slp1, vibhakti, vacana, linga,
        matra_prathama_2_3_46=matra_prathama_2_3_46,
        nAmadheya_vrddha_term_indices=nAmadheya_vrddha_term_indices,
    )
    return run_subanta_pipeline(s)


def _pada_merge(state: State) -> None:
    """Structural: merge all Terms into a single pada-tagged Term.
    This is NOT a sūtra; it is tagged '__MERGE__' in the trace."""
    if not state.terms:
        return
    all_varnas: List = []
    for t in state.terms:
        all_varnas.extend(t.varnas)
    pada = Term(kind="pada", varnas=all_varnas, tags={"pada"}, meta={})
    state.terms = [pada]
    state.trace.append({
        "sutra_id"    : "__MERGE__",
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : "पद-मेलनम्",
        "form_before" : state.flat_slp1(),  # already merged, but same
        "form_after"  : state.flat_slp1(),
        "why_dev"     : "पद-रचना — सुबन्त-संयोजनम् (संरचनात्मकं, न सूत्रम्)।",
        "status"      : "APPLIED",
    })
