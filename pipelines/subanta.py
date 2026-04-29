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
                        ) -> State:
    """Build the initial state for a subanta derivation.

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
    "7.1.94",
    "6.4.11",
    "6.1.66",
    "7.1.2",
    "7.2.106",
    "7.2.102",
    "6.1.97",
    "7.2.113",
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
    "1.1.11",
    "6.1.103",
    "6.1.78",
    "6.1.107",
    "6.1.125",
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


def _subanta_scanner_winner_by_spine_order(candidates: list[str], spine_ids: list[str]) -> str:
    """
    When several post-4.1.2 sūtras *cond* true together, pick the one listed
    earliest on ``SUBANTA_RULE_IDS_POST_4_1_2`` (fixed Aṣṭādhyāyī-kram; CONSTITUTION
    Art. 3 — no autonomous ``engine.resolver`` tie-break in this pipeline).
    """
    if not candidates:
        raise ValueError("subanta scanner needs at least one candidate")
    if len(candidates) == 1:
        return candidates[0]
    order = {sid: i for i, sid in enumerate(spine_ids)}
    return min(candidates, key=lambda sid: order.get(sid, 1_000_000))


def run_subanta_post_4_1_2_scanner(s: State, *, max_steps: int = 500) -> State:
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
                    continue
                if asiddha_violates(sid, s):
                    continue
                if is_frozen_by_nipatana(rec.sutra_type, s):
                    continue
                if (sid, _state_sig(s)) in no_progress_sites:
                    continue
                if rec.cond is not None and rec.cond(s):
                    candidates.append(sid)

            if not candidates:
                return

            winner = _subanta_scanner_winner_by_spine_order(candidates, all_ids)
            sig_before = _state_sig(s)
            before_len = len(s.trace)
            s = apply_rule(winner, s)
            if len(s.trace) > before_len:
                last = s.trace[-1]
                if last.get("sutra_id") == winner and last.get("status") in TRACE_STATUSES_FIRED:
                    sig_after = _state_sig(s)
                    # If this firing did not change anything observable in the
                    # state signature, do not allow it to re-fire on the exact
                    # same signature again.  But the rule remains available for
                    # other sites or after other rules change the tape.
                    if sig_after == sig_before:
                        no_progress_sites.add((winner, sig_before))

    # Phase-ordered pools (still glass-box, but no hardcoded linear macro pass):
    # - it-prakaraṇa first (so later rules see cleaned affix shapes)
    # - aṅgakārya next (6.4/7.* + bha/pada saṃjñā)
    # - sandhi next (6.1.*)
    # - structural merge into pada
    # - tripāḍī last (8.2.1+)
    it_ids      = [sid for sid in all_ids if sid.startswith("1.3.")]
    tripadi_ids = [sid for sid in all_ids if sid.startswith("8.")]
    sandhi_ids  = [sid for sid in all_ids if sid.startswith("6.1.")]
    angakarya_ids = [
        sid for sid in all_ids
        if sid not in set(it_ids) | set(sandhi_ids) | set(tripadi_ids)
    ]

    _scan_pool(it_ids)
    _scan_pool(angakarya_ids)
    _scan_pool(sandhi_ids)

    if len(s.terms) > 1:
        _pada_merge(s)

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


def derive(stem_slp1: str, vibhakti: int, vacana: int,
           linga: str = "pulliṅga",
           *,
           matra_prathama_2_3_46: bool = False,
           nAmadheya_vrddha_term_indices: tuple[int, ...] | frozenset[int] | None = None,
           autonomous_scanner: bool = False,
           ) -> State:
    """
    Aṣṭādhyāyī-kram pipeline.  Returns final state with complete trace.

    ``matra_prathama_2_3_46`` — forwarded to ``build_initial_state``; when
    True, preflight runs **2.3.1** then **2.3.46** after **1.4.14**.

    ``nAmadheya_vrddha_term_indices`` — forwarded to ``build_initial_state``
    for **1.1.73** *vārttika* (*nāmadheya* optional *vṛddha*).

    NOTE (anti-patchwork): samāsa saṃjñās (bahuvrīhi / tṛtīyā-tatpuruṣa) must come
    from an upstream samāsa derivation. Use `derive_from_state(...)` instead of
    injecting them here.
    """
    s = build_initial_state(
        stem_slp1, vibhakti, vacana, linga,
        matra_prathama_2_3_46=matra_prathama_2_3_46,
        nAmadheya_vrddha_term_indices=nAmadheya_vrddha_term_indices,
    )
    if autonomous_scanner:
        return run_subanta_sup_attach_and_finish_scanner(s)
    return run_subanta_pipeline(s)


def _pada_merge(state: State) -> None:
    """Structural: merge all Terms into a single pada-tagged Term.
    This is NOT a sūtra; it is tagged '__MERGE__' in the trace."""
    if not state.terms:
        return
    # Preserve pragṛhya across structural merge so sentence-level sandhi rules
    # (6.1.125 / 6.1.101 / 6.1.77) can see it on the pada term.
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

    keep_pragrahya = any(PRAGHYA_TERM_TAG in t.tags for t in state.terms)
    # Preserve index-based saṃjñās that are semantically "on the whole stem"
    # across structural merges, so they don't re-fire vacuously later.
    keep_bha = any("bha" in t.tags for t in state.terms)
    keep_pratipadika = any("prātipadika" in t.tags for t in state.terms)
    keep_anga = any("anga" in t.tags for t in state.terms)
    keep_linga = (
        "strīliṅga" if any("strīliṅga" in t.tags for t in state.terms)
        else "napuṃsaka" if any("napuṃsaka" in t.tags for t in state.terms)
        else "pulliṅga" if any("pulliṅga" in t.tags for t in state.terms)
        else None
    )
    all_varnas: List = []
    for t in state.terms:
        all_varnas.extend(t.varnas)
    tags = {"pada"}
    if keep_pragrahya:
        tags.add(PRAGHYA_TERM_TAG)
    if keep_bha:
        tags.add("bha")
    if keep_pratipadika:
        tags.add("prātipadika")
    if keep_anga:
        tags.add("anga")
    if keep_linga:
        tags.add(keep_linga)
    if any("krt_tfc" in t.tags for t in state.terms):
        tags.add("krt_tfc")
    pada = Term(kind="pada", varnas=all_varnas, tags=tags, meta={})
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
