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
        4.1.1   ngyāp anuvāda
        1.1.1   vṛddhi saṃjñā (definition {A,E,O}; prayoga in vidhi sūtras)
                [recipe schedules this early; vṛddhi *prayoga* not applied here—
                 no vidhi invokes operational vṛddhi at this step, only saṃjñā]
        1.1.2   guṇa saṃjñā   (available for later sandhi)

    STAGE 2: attach sup
        4.1.2   ADHIKARA + attaches the (v,v) pratyaya to state.terms

    STAGE 3: it-prakaraṇa on the pratyaya upadeśa
        1.3.3–1.3.8  it-saṃjñā (halantyam, tusma block, ñiṭuḍu, ṣaḥ, cuṭu, laśakvat)
        1.3.9   tasya lopaḥ (delete tagged it-varṇas)

    STAGE 4: aṅgakārya
        6.4.1   aṅgasya adhikāra
      (conditional) 7.1.54  nuṭ āgama for (6,3)
      (then)  1.3.9 again to lose the ṭ it-marker of nuṭ
        6.4.148 yasyeti ca (when aṅga-final a meets i-pratyaya)

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
                        linga: str = "pulliṅga") -> State:
    """Build the initial state for a subanta derivation."""
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


def derive(stem_slp1: str, vibhakti: int, vacana: int,
           linga: str = "pulliṅga") -> State:
    """
    Aṣṭādhyāyī-kram pipeline.  Returns final state with complete trace.
    """
    # Tyadādi pronouns like `tad` have no sambodhana (no vibhakti 8 forms).
    if vibhakti == 8 and stem_slp1.strip() in {"tad", "tyad", "yad", "etad", "idam", "adas", "kim"}:
        raise ValueError("त्यदादि-शब्देषु सम्बोधन-रूप (८-*) नास्ति।")

    s = build_initial_state(stem_slp1, vibhakti, vacana, linga)

    # STAGE 1 — saṃjñā preflight.
    s = apply_rule("1.4.14", s)
    s = apply_rule("4.1.1",  s)
    s = apply_rule("1.1.1",  s)  # saṃjñā only — prayoga awaits vidhi (e.g. 6.1.88)
    s = apply_rule("1.1.2",  s)
    # v3.7: tyadādi-gaṇa tagging (includes sarvanāma tag for these stems).
    s = apply_rule("1.2.72", s)
    # v3.5: sarvanāma-saṃjñā (sarvādi-gaṇa; rules self-gate).
    s = apply_rule("1.1.27", s)
    # v3.4: घि-संज्ञा for hari-like i/u stems (rules self-gate).
    s = apply_rule("1.4.7",  s)

    # STAGE 2 — sup attach.
    s = apply_rule("4.1.2",  s)

    # STAGE 3 — it prakaraṇa on the pratyaya.
    s = apply_rule("1.3.2",  s)      # v3.1: anunāsika-it for vowels (su → s)
    s = apply_rule("1.3.3",  s)
    s = apply_rule("1.3.4",  s)      # tusma antya — halantyam blocked (registry)
    s = apply_rule("1.3.5",  s)      # ādir ñiṭuḍavaḥ
    s = apply_rule("1.3.6",  s)      # ṣaḥ pratyayasya
    s = apply_rule("1.3.7",  s)      # cuṭu
    s = apply_rule("1.3.8",  s)      # v3.1: initial-ṅ it for sup pratyayas
    s = apply_rule("1.3.9",  s)

    # STAGE 4 — aṅgakārya.
    s = apply_rule("6.4.1",   s)
    # v3.7: tyadādi prep should occur before 7.1.* / sandhi steps so later
    # sandhi (e.g. 6.1.78 for -yoḥ) sees the a-ending aṅga.
    s = apply_rule("7.2.106", s)      # tad/tyad: t → s before su
    s = apply_rule("7.2.102", s)      # tyadādi final → a
    s = apply_rule("6.1.97",  s)      # collapse a+a in tyadādi aṅga
    # v3.1: sambuddhi su-lopa.  Fires only when pratyaya is tagged
    # 'sambuddhi' (cell 8-1) and aṅga ends in hrasva/eṅ.  Done EARLY
    # so later pratyaya-replacements don't re-materialize 's'.
    s = apply_rule("6.1.69",  s)
    # v3.1: ato-pratyaya replacements (ṭā→ina, ṅasi→āt, ṅas→sya).
    # v3.5: sarvanāma specials must run before general a-stem replacements.
    s = apply_rule("7.1.15",  s)      # ṅasi/ṅi → smAt/smin
    s = apply_rule("7.1.12",  s)
    # v3.1: ṅe → ya (dative-singular after a-stem).
    s = apply_rule("7.1.14",  s)      # sarvanāma: ṅe → smE
    s = apply_rule("7.1.13",  s)
    # v3.2: ato bhisa ais — Bis → Es (cell 3-3).  MUST run before
    # 7.3.103 so that the pratyaya's upadeśa is already 'Es' and
    # 7.3.103 (which keys off 'Bis') won't fire for this cell.
    s = apply_rule("7.1.9",   s)
    # v3.5: sarvanāma plural jas substitution (sarve).
    s = apply_rule("7.1.17",  s)
    # v3.6: napuṃsaka specials.
    s = apply_rule("7.1.24",  s)      # su/am → am (jnAnam)
    s = apply_rule("7.1.19",  s)      # au → SI (jnAne)
    s = apply_rule("7.1.20",  s)      # jas/Sas → Si (jnAnAni)
    # v3.6: śi → sarvanāmasthāna (must run AFTER 7.1.19/20 created Si).
    s = apply_rule("1.1.42",  s)
    s = apply_rule("7.1.54",  s)      # fires only when (6,3) & hrasva-final aṅga
    # v3.5: sarvanāma gen-pl: suṭ āgama before Am (sarveṣām).
    s = apply_rule("7.1.52",  s)
    # Re-fire relevant it-prakaraṇa after sarvanāma substitutions/āgamas.
    s = apply_rule("1.3.5",   s)
    s = apply_rule("1.3.7",   s)
    s = apply_rule("1.3.9",   s)      # re-fire: remove ṭ-it of nuṭ if inserted
    # v3.6: napuṃsaka plural: nuṃ + upadhā-dīrgha under sarvanāmasthāna.
    s = apply_rule("7.1.72",  s)
    s = apply_rule("6.4.8",   s)
    s = apply_rule("6.4.3",   s)      # v3.4: nāmi — lengthen i/u before nuṭ + Am (harīṇām)
    # v3.1: bahuvacane jhalyet — a → e before jhal-initial plural sup.
    # MUST run before 7.3.102 (which would otherwise make a → ā).
    s = apply_rule("7.3.103", s)
    # v3.1: supi ca — aṅga-final 'a' → 'ā' before consonant-initial sup.
    # Runs AFTER 7.1.12/13 replacements so the pratyaya's new first varṇa
    # (y, s, t, ...) is visible as the trigger.
    s = apply_rule("7.3.102", s)
    s = apply_rule("6.4.148", s)      # yasyeti ca
    # v3.4: hari-like (ghi) aṅgakārya (rules self-gate by upadeśa identity).
    s = apply_rule("7.3.108", s)      # sambuddhi: hari → hare
    s = apply_rule("7.3.109", s)      # jasi:       hari → hare
    s = apply_rule("7.3.111", s)      # ṅiti:       hari → hare
    s = apply_rule("7.3.119", s)      # ṅi:         harau
    s = apply_rule("7.3.120", s)      # ṭā:         hariṇā (via ṇatva later)

    # STAGE 5 — sandhi.
    # v3.2: jas/Sas pratyaya substitutions (cells 1-3, 2-3, 8-3).
    # Fire BEFORE other sandhi because they both delete the stem's
    # final 'a', so subsequent 6.1.x rules don't see stray 'a + X' pairs.
    s = apply_rule("6.1.102", s)      # jas → As (prathamā-pl pūrvasavarṇa)
    s = apply_rule("6.1.103", s)      # Sas → An (puṃsi acc-pl)
    s = apply_rule("6.1.78",  s)      # v3.1: ayādi — y-insertion before 'os'
    s = apply_rule("6.1.107", s)      # v3.1: ami pūrvaḥ — a+am → am (blocks 6.1.101)
    s = apply_rule("6.1.77",  s)      # v3.4: iko yanaci (hari+os → haryos)
    s = apply_rule("6.1.87",  s)
    s = apply_rule("6.1.88",  s)      # v3.1: vṛddhi — a+E/O → E/O
    s = apply_rule("6.1.110", s)      # v3.4: ṅasi/ṅas pūrvarūpa (hare + as(i) → hare + s(i))
    s = apply_rule("6.1.101", s)

    # STAGE 6 — pada merge.
    _pada_merge(s)

    # STAGE 7 — tripāḍī.
    s = apply_rule("8.2.1",  s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    s = apply_rule("8.3.59", s)       # v3.1: ṣatva after in-kuk vowels
    s = apply_rule("8.4.2",  s)       # v3.1: ṇatva

    return s


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
