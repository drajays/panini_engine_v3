# audit_claude.md — Pāṇini Engine v3 Glass-Box Audit

> **Authoritative source for every claim in this file:** Kāśikā Vṛtti
> (Vāmana–Jayāditya), in Aṣṭādhyāyī-kram, cross-validated against the
> source list in §A below. SK (Siddhānta-Kaumudī) is consulted only
> where the Kāśikā is silent and the engine still needs a rule order —
> never to override the kram.
>
> **Purpose:** Diagnose every place where the engine appears to deviate
> from "*Aṣṭādhyāyī-as-rewrite-system*" (Constitution Art. 0) — whether
> by patchwork in code, by display noise in the web UI, or by recipe
> shortcuts that bypass `apply_rule`. Each finding cites file:line and
> proposes a concrete fix that Cursor (using `audit_cursor.md`) can
> execute mechanically.
>
> **Scope realism:** Full remediation is a multi-week project. This
> document is the **plan and rationale**; `audit_cursor.md` is the
> step-by-step playbook. Neither file edits engine code.

---

## A. Authoritative source roster

The engine's *raison d'être* is to be a **glass-box mathematical
re-implementation of the Aṣṭādhyāyī as a rewrite system** (Art. 0).
For that, every rule must be defended by a quotable, citable,
versioned source. The list below is ordered by precedence: source #1
wins ties; #2 wins only when #1 is silent; and so on. Engine code
that does not cite at least one of these for any non-trivial
predicate is **suspect** and should be revisited.

### A.1 Tier 1 — sūtra pāṭha and direct vṛttis

| # | Source | Where | What it provides | Engine use |
|---|---|---|---|---|
| 1 | **ashtadhyayi.com data repo** | `github.com/ashtadhyayi-com/data`<br>(file `sutraani/data.txt`, key `i = 1·adhyāya·pāda·sūtra` e.g. `11012` = 1.1.12) | Sūtra pāṭha (`s`), SLP1 transliteration (`e`), structured padaccheda (`pc`), anuvṛtti links (`an`), siddhārtha gloss (`ss`), type label, vṛtti excerpts. | Canonical source for every `SutraRecord.text_dev`, `text_slp1`, `padaccheda_dev`, `anuvritti_from`. |
| 2 | **Kāśikā Vṛtti** (Vāmana + Jayāditya) | ashtadhyayi.com sūtra page → "Kāśikā" tab; same data repo `kashika` nodes; print: Sharma's Aṣṭādhyāyī of Pāṇini Vol. I-VI (Munshiram Manoharlal) | The *vṛtti* udāharaṇa that legitimizes each rule firing. The classical commentary in Aṣṭādhyāyī-kram — best aligned with engine philosophy. | Quoted in every sūtra docstring's "v3 implementation" paragraph as the justification for `cond()`'s predicate. |
| 3 | **Mahābhāṣya** (Patañjali) + **Pradīpa** (Kaiyaṭa) + **Uddyota** (Nāgeśa) | ashtadhyayi.com → "Bhāṣya" tab; print: Bhandarkar Oriental Research Institute (BORI) edition | Deepest disambiguation; paribhāṣā-source. Consult only when Kāśikā is silent or when a paribhāṣā-interpretation is contested. | Cite when resolving a conflict; document the resolution in `docs/AMENDMENT_*.md`. |
| 4 | **Siddhānta-Kaumudī** (Bhaṭṭojī Dīkṣita) + **Tattva-bodhinī** (Jñānendra Sarasvatī) | ashtadhyayi.com → "SK" tab | Reference for *which* sūtras tradition cites *together* in a prakriyā. **Never** used to drive engine ordering (Constitution Art. 3). | Used as cross-check for which rules a scholar would expect in a trace; not for kram. |
| 5 | **Laghu-Siddhānta-Kaumudī** (Varadarāja) | sanskritdocuments.org PDF / print: Chowkhamba | Compact teaching prakriyās; easier sanity check for paradigm cells. | Cross-validation oracle for paradigm tests. |
| 6 | **Prakriyā-Kaumudī** (Rāmacandra) + **Prakriyā-Sarvasva** (Nārāyaṇa Bhaṭṭa) | print editions; partial digitisation at GRETIL | Pre-SK prakriyā-order alternatives; valuable for cross-validation. | Same as #4. |

### A.2 Tier 2 — paribhāṣā and meta-grammatical literature

| # | Source | Where | What it provides |
|---|---|---|---|
| 7 | **Paribhāṣenduśekhara** (Nāgeśa) | print: BORI / Chowkhamba; English: Kielhorn 1868 | Authoritative paribhāṣā corpus; needed when interpreting any sūtra under an inherited *anuvṛtti* / *atideśa*. |
| 8 | **Vyāḍi-paribhāṣā** + **Śākaṭāyana-paribhāṣā** | print editions | Older paribhāṣā traditions; consulted when Nāgeśa's reading is contested. |
| 9 | **Liṅgānuśāsana** (attributed to Pāṇini) | ashtadhyayi.com → ancillary | *Liṅga*-assignment rules; needed for any *liṅga*-sensitive vidhi. |
| 10 | **Phiṭ-sūtras** (Śāntanava) | ashtadhyayi.com → ancillary | Accent rules for prātipadikas; relevant for *svara*-sūtras. |
| 11 | **Uṇādi-sūtras** | ashtadhyayi.com → ancillary | Unādi-pratyaya derivations; relevant when a Term is uṇādi-formed. |

### A.3 Tier 3 — kosha and dhātu sources

| # | Source | Where | What it provides |
|---|---|---|---|
| 12 | **Dhātupāṭha** (Pāṇinīya) | `data/inputs/dhatupatha.json` (local); ashtadhyayi.com → "Dhātupāṭha" | Dhātu inventory with gaṇa, anubandha, artha. Single source of truth for `dhatu_gana`, `dhatu_upadesha_slp1`. |
| 13 | **Gaṇapāṭha** | `data/inputs/ganapatha.json` (local); ashtadhyayi.com → "Gaṇapāṭha" | The *gaṇa*-lists named in sūtras (sarvādi, bahvādi, ākṛti-gaṇas etc.) Single source for `SARVADI`, `BAHVADI`, etc. frozensets. |
| 14 | **Nighaṇṭu + Nirukta** (Yāska) | gretil.sub.uni-goettingen.de | Pre-Pāṇinian semantic-class evidence; cited rarely, mostly for Vedic. |
| 15 | **Köln Sanskrit Lexicon (Monier-Williams)** | sanskrit-lexicon.uni-koeln.de | Surface-form sanity check (NOT a source of rule logic). |

### A.4 Tier 4 — modern computational corpora and oracles

| # | Source | Where | What it provides | Engine use |
|---|---|---|---|---|
| 16 | **Vidyut** (Ambuda-org) | `github.com/ambuda-org/vidyut` | Reference Rust prakriyā engine: dhātu, sup, kṛt, taddhita inflection with high coverage. | Oracle for cross-validating final surface forms. **Never** copy code logic — Vidyut and v3 differ in architecture; we want independent verification. |
| 17 | **Saṃsādhanī suite (IIIT-H / Hyderabad)** | `sanskrit.uohyd.ac.in/scl/` (analyser: `sanskrit.uohyd.ac.in/scl/SHMT/sandhi.html` and subanta/tinanta analyzers) | Subanta, tinanta, kṛdanta analyzers with morphological tags; sandhi engine; segmenter; gold paradigm corpora. | Cross-validate `(stem, vibhakti, vacana)` → surface. Tag taxonomy informs `term.tags`. |
| 18 | **Sanskrit Heritage Platform** (Gérard Huet, INRIA) | `sanskrit.inria.fr/` | Wide-coverage Sanskrit reader / morphological analyser using a finite-state architecture. | Independent surface-form oracle. Useful for sandhi sanity. |
| 19 | **JNU Sanskrit Computational Linguistics group** | scl-jnu.in (when reachable) | Academic prakriyā-generation tools; subanta/tinanta tables. | Cross-validation. |
| 20 | **DCS (Digital Corpus of Sanskrit)** | `www.sanskrit-linguistics.org/dcs/` | Annotated text corpus; useful for surface-form attestation. | Surface-attestation only; not rule-source. |
| 21 | **GRETIL** | `gretil.sub.uni-goettingen.de/` | E-texts of Aṣṭādhyāyī ancillaries, commentaries, etc. | Source for hard-to-find textual editions. |
| 22 | **SARIT** | `sarit.indology.info/` | TEI-XML scholarly editions of Sanskrit grammatical texts. | Authoritative when print editions are unavailable. |

### A.5 Tier 5 — scholarly works on Pāṇinian engineering

These are **methodology references** — they justify how the engine
should be built, not what the rules are.

| # | Source | Why this matters for the engine |
|---|---|---|
| 23 | **George Cardona**, *Pāṇini: A Survey of Research* (1976; rev. 1980) | Definitive scholarly summary of Pāṇinian studies. Cited when adjudicating between commentarial traditions. |
| 24 | **George Cardona**, *Pāṇini: His Work and Its Traditions* (Vol I, 1988; Vol II, 1997) | Detailed analysis of sūtra-types, anuvṛtti, atideśa, vibhāṣā. Engine taxonomy (`SutraType`) should map cleanly onto Cardona's typology. |
| 25 | **Paul Kiparsky**, *Pāṇini as a Variationist* (1979); *Some Theoretical Problems in Pāṇini's Grammar* (1982) | On *utsarga*–*apavāda*, *vipratiṣedha*, and Pāṇini's ordering principles. Cited when designing the resolver (`engine/resolver.py`). |
| 26 | **Rama Nath Sharma**, *The Aṣṭādhyāyī of Pāṇini* (6 vols., Munshiram Manoharlal) | Modern academic edition with Devanāgarī, transliteration, translation, and Kāśikā-aligned commentary in English. The most accessible bilingual reference. |
| 27 | **S. C. Vasu**, *The Aṣṭādhyāyī of Pāṇini* (English translation, 1891) | Older but freely available English translation. Useful for quick lookup. |
| 28 | **Bimal K. Matilal**, *The Word and the World* (1990) | Pāṇinian philosophy of language; useful when justifying meta-design (e.g., glass-box vs. lookup). |
| 29 | **S. D. Joshi & J. A. F. Roodbergen**, *The Aṣṭādhyāyī of Pāṇini* (translation + Mahābhāṣya commentary, multi-volume) | Cross-referenced English translation with Mahābhāṣya commentary integration. |
| 30 | **Amba Kulkarni & Gérard Huet** (eds.), *Sanskrit Computational Linguistics* proceedings | Modern computational treatment of Pāṇinian rules; algorithmic considerations. |
| 31 | **Madhav M. Deshpande**, *Saṃskṛta-Subodhinī* and various papers on Pāṇinian analysis | Pedagogical rigor; relevant when explaining the engine to users. |
| 32 | **Subhash Kak**, "The Paninian Approach to Natural Language Processing" (1987) | Early formalisation of Pāṇinian rule application as a rewrite system. |

### A.6 Forbidden as sources

- Unverified blog posts or YouTube transcripts.
- ChatGPT / LLM-generated prakriyās without independent verification.
- Wikipedia (use to find the canonical source, then cite that).
- PDFs without a clear edition lineage.
- Surface-form-only tools (Aksharamukha etc.) as a source of rule
  logic — they are transliterators, not grammars.

### A.7 Procurement protocol for new sūtras

When implementing or modifying a sūtra:

1. Open the sūtra at ashtadhyayi.com (source #1) for `text_dev`,
   `padaccheda_dev`, `sutra_type`, `anuvritti_from`.
2. Open the **Kāśikā** tab (source #2). Identify the *udāharaṇa* and
   the *pratyudāharaṇa*. Both go into the docstring.
3. If Kāśikā is ambiguous, open the **Bhāṣya** tab (source #3).
4. If still ambiguous, open Cardona Vol I/II (source #24) for
   scholarly disambiguation.
5. Cross-validate the resulting surface against **Vidyut** (#16) and
   **Saṃsādhanī** (#17). If they disagree with the engine output,
   the engine is suspect — investigate before merging.
6. Cite all consulted sources in the sūtra file's docstring.

---

---

## 0. The motivating example — `रामाणाम्` (ṣaṣṭhī bahuvacana of राम)

The user's screenshot of the current trace shows ~35 trace rows for
this single cell. Of those, only ~10 are actual *vidhi*/*ādeśa*
operations; the rest are **paribhāṣā/saṃjñā registrations** (✓ and ⟡
rows) that fire unconditionally at the start of every subanta
derivation regardless of whether their definitions are ever used by
this cell.

### 0.1 The canonical Kāśikā prakriyā for `रामाणाम्`

| # | Sūtra | Operation | Why fires here |
|---|---|---|---|
| 1 | **1.2.45** अर्थवदधातुरप्रत्ययः प्रातिपदिकम् | राम → *prātipadika* saṃjñā | राम is *arthavat*, neither *dhātu* nor *pratyaya* (Kāśikā 1.2.45: *arthavat aprātipadikam yat śabdasvarūpaṃ tat prātipadikasaṃjñakaṃ bhavati*) |
| 2 | **4.1.1** ङ्याप्प्रातिपदिकात् | open adhikāra for sup-attachment | We are entering the chapter where sup is added after prātipadika |
| 3 | **4.1.2** स्वौजस…आम्…सुप् | राम → राम + आम् | *ṣaṣṭhī bahuvacana* = आम् from the 21-sup inventory (Kāśikā 4.1.2 *yathāsaṅkhyam* with 4.1.2 list) |
| 4 | **1.3.4** न विभक्तौ तुस्माः | प्रतिषेधः: blocks म् of आम् from being *it* | *vibhakti* context (आम् is a sup-vibhakti), म् ∈ tu-varga-s-mā set, so 1.3.3 *halantyam* is prohibited |
| 5 | **1.4.103** सुपः | sup-saṃjñā for आम् | Sets the sup vibhakti-saṃjñā |
| 6 | **1.4.17** स्वादिष्वसर्वनामस्थाने | pada-saṃjñā for the stem before non-sarvanāmasthāna sup | आम् is not in *suṭ* (1.1.43), so the stem is *pada* before आम्. (Required for 8.2.1+ tripādi visarga later; not relevant for *nuṭ* insertion since नुट् is *aṅga* op, but the saṃjñā is part of the spine) |
| 7 | **7.1.54** ह्रस्वनद्यापो नुट् | राम् + आम् → राम् + न् + आम् (= रामनाम्) | *Hrasva* stem + *āmi* (sup सं starting with vowel ā). The नुट् *āgama* is inserted (न् with *u* indicating sthāna, ट् marking *aṅga-anta*); *Kāśikā* 7.1.54 *hrasva-nadyā-pa-ḥ ām-i nuṭ-āgamo bhavati* |
| 8 | **6.4.3** नामि | अङ्ग-final hrasva *a* → dīrgha ā before *nāmi* | राम् + न् + आम् → राम-ा + न् + आम् = रामानाम् (the *नाम्* trigger is the post-नुट् *नाम्* form, Kāśikā 6.4.3 *aco nāmi padasya dīrgho bhavati*) |
| 9 | **8.4.2** अट्कुप्वाङ्नुम्व्यवायेऽपि | *ṇatva*: न् → ण् after रा (र् + अ) | The intervening *aṭ* (a-varga) does not block *ṇatva*; Kāśikā 8.4.2 *aṭ-ku-pu-āṅ-num vyavāye 'pi* |
| ⋆ | 8.2.1 पूर्वत्रासिद्धम् | tripādī gate-open | AUDIT row, required for *asiddhatva* of 8.2–8.4 |
| ⋆ | 1.4.110 विरामोऽवसानम् | avasāna-saṃjñā | AUDIT, required for the final form to be a *pada-anta* |

**Total: 9 operative sūtras + 2 AUDIT gates = 11 rows.** Anything
beyond this on the trace is either patchwork or unrelated saṃjñā
noise.

### 0.2 What the current trace actually contains (annotated)

From the user's screenshot, the rows are (status icons preserved):

| Row | Sūtra | Status | Should be in trace for रामाणाम्? |
|---|---|---|---|
| 4.1.1 | ङ्याप्प्रातिपदिकात् | ⟡ | YES |
| 1.1.1 | वृद्धिरादैच् | ✓ | **NO** — vṛddhi-saṃjñā is never invoked for रामाणाम् (no guṇa/vṛddhi vidhi fires) |
| 1.1.73 | यस्य अचामादिः वृद्धिः | ✓ | **NO** — vṛddha-pada saṃjñā only relevant to taddhita 4.1.83+ |
| 1.1.2 | अदेङ् गुणः | ⟡ | **NO** — no guṇa here |
| 1.1.3 | इको गुणवृद्धी | ⟡ | **NO** — no *ik* sthānin here |
| 1.1.7 | हलोऽनन्तराः संयोगः | ✓ | **NO** — no saṃyoga arises |
| 1.1.60 | स्थाने अदर्शनं लोपः | ✓ | NO — *lopa-saṃjñā* not invoked (no lopa here) |
| 1.1.61 | प्रत्ययस्य अदर्शनं लुक्श्लुलुपः | ✓ | **NO** — luk/ślu/lup not invoked |
| 1.1.62 | प्रत्ययलोपे प्रत्ययलक्षणम् | ⟡ | NO — no pratyaya-lopa here |
| 1.1.63 | लुमता प्रत्ययलोपे | ⟡ | NO |
| 1.1.8 | मुखनासिकावचनोऽनुनासिकः | ✓ | NO — anunāsika saṃjñā not invoked by 7.1.54 / 6.4.3 / 8.4.2 |
| 1.1.9 | तुल्यास्यप्रयत्नं सवर्णम् | ✓ | NO — savarṇa not invoked here |
| 1.1.10 | नाज्झलौ | ⟡ | NO |
| 1.1.11 | ईदूदेद्द्विवचनं प्रगृह्यम् | ✓ | **NO** — pragṛhya is *dvivacana*-only; this is bahuvacana |
| 1.1.12 | अदसो मात् | ⟡ | NO |
| 1.1.13 | शे | ⟡ | NO |
| 1.1.14 | एकाच् अनाङ् निपातः प्रगृह्यम् | ✓ | NO — no nipāta in stem |
| 1.1.100 | न मात्रासमासे | ⟡ | NO |
| 1.1.15 | ओत् | ✓ | NO |
| 1.1.16 | सम्बुद्धौ शाकल्यस्य | ✓ | NO — not sambuddhi |
| 1.1.17 | उञः | ⟡ | NO |
| 1.1.18 | ऊँ | ✓ | NO |
| 1.1.19 | ईदूतौ च सप्तम्यर्थे | ✓ | NO — saptamy-artha, but pragṛhya again |
| 1.1.20 | दाधा घ्वदाप् | ✓ | **NO** — ghu-saṃjñā is for dhātu dā/dhā; no dhātu present |
| 1.1.21 | आद्यन्तवदेकस्मिन् | ⟡ | NO |
| 1.1.46 | आद्यन्तौ टकितौ | ⟡ | NO |
| 1.1.22 | तरप्तमपौ घः | ✓ | **NO** — taddhita tarap/tamap; not relevant |
| 1.1.23 | बहुगणवतुडति संख्या | ✓ | **NO** — saṅkhyā-saṃjñā for bahu/gaṇa/vatu/ḍati |
| 1.1.24 | ष्णान्ता षट् | ✓ | **NO** — ṣaṭ-saṃjñā for ṣṇ-anta numerals |
| 1.2.45 | अर्थवदधातुरप्रत्ययः | ✓ | YES |
| 4.1.2 | (sup attach) | ⟡ → रामआम् | YES |
| 3.1.1, 3.1.2 | प्रत्ययः, परश्च | ⟡ | NO — these are *kṛt/taddhita* paribhāṣās, not sup |
| 1.4.102 | tāni trīṇi… | ✓ | OK (pratyaya-vibhakti saṃjñā) but display-redundant |
| 1.4.103 | सुपः | ⟡ | YES |
| 1.4.13 | यस्मात्प्रत्ययविधिः | ✓ | YES (aṅga-saṃjñā) |
| 1.4.14 | सुप्तिङन्तं पदम् | ✓ | YES (will be needed for pada-saṃjñā at 1.4.17) |
| 1.3.4 | न विभक्तौ तुस्माः | ✓ | YES |
| 1.3.9 | उपदेशे इतस्य लोपः | ○ | YES (vacuous, no it to lopa) |
| 1.3.10 | समानामनुदेशः | ⟡ | YES |
| 6.4.1 | अङ्गस्य | ⟡ | YES (adhikāra) |
| 1.4.17 | स्वादिष्वसर्वनामस्थाने | ✓ | YES |
| 7.1.54 | ह्रस्वनद्यापो नुट् | ✓ → रामनाम् | **YES** (operative) |
| 1.3.9 | (it-lopa of नुट् ut) | ○ | YES |
| 6.4.3 | नामि | ✓ → रामानाम् | **YES** (operative) |
| 6.4.129 | भस्य | ⟡ | NO (bha-adhikāra; not needed here) |
| ◈ | पद-मेलनम् | ◈ | structural OK |
| 1.4.110 | विरामोऽवसानम् | ✓ | YES |
| 8.2.1 | पूर्वत्रासिद्धम् | ⟡ | YES (gate) |
| 8.4.2 | अट्कुप्वाङ्नुम्व्यवायेऽपि | ✓ → रामाणाम् | **YES** (operative) |

**Diagnosis:** ~20 of the rows are paribhāṣā/saṃjñā stamps whose
target term-class is not present in this state at all. They are not
"wrong" in the sense of producing incorrect output — but they are
*śāstrīya* noise and create the impression of an undisciplined engine.

---

## 1. Root causes (architectural)

### 1.1 Blind preflight blocks in `core/canonical_pipelines.py`

Two helpers schedule a fixed list of saṃjñā/paribhāṣā sūtras
**before** any condition check on the actual stem:

- `P01_samjna_1_1_3_to_1_1_100` (lines **1100–1118**): unconditionally
  fires 1.1.3, 1.1.7, 1.1.8, 1.1.9, 1.1.10, 1.1.11, 1.1.12, 1.1.13,
  1.1.14, 1.1.100 (plus optional luk-block 1.1.60–1.1.63).
- `P01_samjna_1_1_15_to_1_1_24` (lines **1121–1138**): unconditionally
  fires 1.1.15 through 1.1.24 + 1.1.46.
- `P01_subanta_bootstrap` (lines **1074–1097**): calls both, plus
  unconditionally fires 1.1.1, 1.1.73, 1.1.2, 1.2.72, 1.1.27, 1.1.29,
  1.1.30.

This is the single largest source of trace noise. The Kāśikā never
cites 1.1.20 (ghu) when explaining रामाणाम्; it cites it only when
working through a dhātu form involving दा/धा.

### 1.2 Saṃjñā sūtras implemented as global registry stamps

Files like `sutras/adhyaya_1/pada_1/sutra_1_1_20.py` (ghu),
`sutra_1_1_23.py` (saṅkhyā), `sutra_1_1_11.py` (pragṛhya) implement
`cond()` as:

```python
def cond(state):
    return state.samjna_registry.get(KEY) != EXPECTED
```

That is: "have I already stamped the registry? if not, do so." This
is constitutionally permitted under Article 13 §3 (saṃjñās *may* be
module-level frozensets), but it produces an AUDIT trace row for
every subanta/tinanta derivation, regardless of whether any term in
the state would ever be looked up under that saṃjñā.

**This is not a code bug** — it is a *display-layer* concern combined
with a recipe-scheduling concern.

### 1.3 Endemic `_arm` flag patchwork (Article 13 violation, scale-wise)

Survey numbers (current repo):

| Metric | Count |
|---|---|
| Sūtra files reading `state.meta[..._arm]` inside `cond()` | **3,398 / 4,042** (84%) |
| Pipeline/core files writing `_arm` flags | **~130** |
| `_arm` writes in `core/canonical_pipelines.py` alone | **~20** |
| Sūtra files outwardly clean (no `_arm` read in cond) | **~644** |

The constitution (Art. 13) treats `_arm` flags as technical debt
"to be removed when that file is next refactored." In practice the
codebase is **structured around arm-gated sūtras**, not the other way
around. Recent cleanup (memory notes: 1.3.69, 1.3.77, 7.1.3, 8.2.39,
8.4.56, 6.4.88, 8.2.23, 3.4.99, 3.4.108, 6.1.66, 6.1.97, 3.3.173,
3.4.116) shows the migration is real but covers <0.5% of the surface.

### 1.4 Recipe duplication (Article 12 violation)

| File class | Count |
|---|---|
| `pipelines/*_demo.py` | **149** |
| `pipelines/*_corrected_P0NN_*.py` | **31** |
| `pipelines/*_P0NN_*.py` (P-numbered) | **75** |

Many `*_corrected_*.py` files exist because the original (uncorrected)
recipe was kept "for trace stability." This duplicates the spine and
spreads `_arm` writes across files. Article 12 §3 requires *one*
canonical pipeline per *prayoga* class.

### 1.5 Demo-id leakage into sūtra `cond()` (Article 13 §1 violation)

Sūtras gating on `state.meta["P036_3_4_82_lit_Nal_arm"]`,
`state.meta["6_1_97_pararupa_P013_arm"]`,
`state.meta["6_1_97_pararupa_P017_arm"]`, etc. embed demo-prakriyā
identifiers (P036, P013, P017) inside the rule predicate. The arm
*itself* is acceptable transitional debt; the **demo-id** is not.

Memory note already lists these as "remaining known technical debt":
- `2_2_X_arm` (all samāsa 2.2.x)
- `6_1_97_pararupa_P013_arm`, `_P017_arm`
- `6_1_97_asmad_crossterm_arm`
- (Resolved already: `P022_8_2_23` → `8_2_23_dyauH_v_lopa_arm`)

---

## 2. Web UI: what works, what to fix

### 2.1 Status taxonomy (engine/trace.py)

Working as designed:

| Status | Icon | Meaning |
|---|---|---|
| `APPLIED` | ✓ | sūtra fired, *varṇa* changed |
| `APPLIED_VACUOUS` | ○ | cond=True, no varṇa change (e.g. 1.3.9 with no *it*) |
| `AUDIT` | ⟡ | adhikāra/paribhāṣā/anuvāda — cond=True, no varṇa change *and* no expected change |
| `BLOCKED` | ✗ | gate forbade execution (pratiṣedha, asiddha, vibhāṣā) |
| `SKIPPED` | · | cond=False |
| `STRUCTURAL` | ◈ | non-sūtra step (pada-merging etc.) |

### 2.2 Existing filter (webui/templates/derive.html L62-66, trace.js L82-105)

A checkbox row exists with toggles for APPLIED / AUDIT / SKIPPED /
BLOCKED. APPLIED is checked by default; AUDIT is *also visible* by
default (it's bucketed under APPLIED for the purposes of the filter
— see trace.js L92 `if (st === "APPLIED_VACUOUS") return active.has("APPLIED")`,
but AUDIT is its own bucket and shows whenever AUDIT is in `active`).

**Finding:** AUDIT and APPLIED_VACUOUS rows are visible by default
even when the user only wants "the real prakriyā." There is no
single-click "show only what actually changed the form" filter.

### 2.3 Missing display features (per user requirement)

1. **"Why this sūtra fires NOW"** panel — `renderSutraDetail` already
   shows `why_dev` (the static Kāśikā gloss) but does **not** show a
   per-state explanation like "fires because *aṅga-anta* is hrasva
   *a* and following sup is आम्." That field doesn't exist in the
   trace schema yet.
2. **Trigger-term highlight** — when 7.1.54 fires, the UI does not
   point at the term in `form_before` that caused the cond to be
   satisfied. (The data exists in `step.term_kind`; not surfaced
   visually.)
3. **Kāśikā citation link** — `why_dev` is engine-authored, not a
   Kāśikā quote. A `kashika_text_dev` field would let the UI display
   the actual Kāśikā vṛtti gloss alongside the engine's `why_dev`.

---

## 3. Audit findings, ranked

### P0 — Display: cut the saṃjñā-stamp noise (lowest cost, biggest perceived win)

**Decision:** add a default-on filter "show only रूप-परिवर्तन-कारी सूत्राणि"
(only form-changing rules) that hides AUDIT and APPLIED_VACUOUS rows,
plus add a toggle "विस्तरः" that reveals them.

This does *not* change engine behaviour. It changes only what the
user sees by default. The full trace remains available for
sūtra-by-sūtra audit when wanted.

### P1 — Recipe: stop calling registry-stamp sūtras when no term needs them

Make `P01_samjna_*` blocks **state-aware**:

- 1.1.20 (ghu) — only fire if `state.terms` contains a dhātu whose
  upadeśa-SLP1 is in `GHU_DHATU_UPADESHA_SLP1`.
- 1.1.23 (saṅkhyā), 1.1.24 (ṣaṭ) — only fire if a prātipadika term's
  upadeśa-SLP1 is in the respective set.
- 1.1.11, 1.1.14, 1.1.15–1.1.19 (pragṛhya cluster) — only fire if the
  state's `vibhakti_vacana` requires *dvivacana* OR a *nipāta* is on
  the tape.
- 1.1.22 (tarap-tamap-gha) — only fire if a taddhita pratyaya is on
  the tape.

Done by tightening each sūtra's `cond()` (NOT by removing the
preflight call — the engine is still allowed to schedule; the sūtra
just declines). This preserves Constitution Art. 3 (no recipe-order
shortcuts) and Art. 12 (fullest valid path: the sūtra still gets
considered, it just correctly says "not now").

### P2 — Recipe: split `P01_samjna_*` by use-class

Keep three preflight blocks, scheduled from the appropriate recipe:

- `P01_samjna_subanta_minimum` — only 1.2.45, 1.4.13, 1.4.14, 1.4.17
  (the saṃjñās needed for *every* subanta).
- `P01_samjna_pragriya_block` — 1.1.11/13/14/15/16/17/18/19 only when
  `dvivacana` / vocative / nipāta context exists.
- `P01_samjna_dhatu_class` — 1.1.20 (ghu), 1.1.5 (kṅiti), etc., only
  when a dhātu term is on the tape (tinanta + krdanta pipelines).

### P3 — Architecture: incremental demolition of `_arm` flags

Per Constitution Art. 13, replace `_arm`-gated `cond()` with
structural predicates (Term tags, registry presence, phonological
shape). The memory file lists what's already been migrated. Continue
in priority order:

1. **`2.2.x` samāsa block** (~38 sūtras with `2_2_X_arm`) — replace
   with `samasa_pending` tag + samāsa-class enumeration.
2. **`6.1.97_pararupa_*P013/P017_arm`** — replace with phonological
   condition `a + a/e at term boundary in non-pragṛhya context`.
3. **`6.1.97_asmad_crossterm_arm`** — fold into the same predicate.

### P4 — Pipeline cleanup: merge `_corrected_*` duplicates

Each `*_corrected_P0NN_demo.py` should either:
1. Be deleted, with its trace baseline updated to the canonical
   pipeline output, OR
2. Be merged into the canonical recipe with a vibhāṣā fork (Art.
   12 §3), OR
3. Be renamed to remove `_corrected` (which implies the other is
   wrong; one of them must die).

### P5 — Documentation: per-sūtra "WHY this fires NOW" field

Add `step.why_now_dev: str` to the trace schema (engine/trace.py).
Populated by each sūtra's `act()` based on the actual state at
trigger time. Example for 7.1.54:

```python
step["why_now_dev"] = (
    f"अङ्गस्य {anga_anta_slp1} ह्रस्व, परं सुप् {sup_slp1} (आम्); "
    f"अतो नुट्-आगमः। (कशिका ७।१।५४)"
)
```

UI displays this in the sutra-detail panel alongside the static
`why_dev` (which remains the universal Kāśikā gloss).

---

## 4. Verification methodology

For each fix, the audit playbook (`audit_cursor.md`) requires:

1. **Before:** snapshot the trace row count and the firing-sūtra list
   for the 24 राम cells + 7 भू cells (existing regression set in
   `tests/regression/`).
2. **After:** re-snapshot. Acceptable deltas:
   - AUDIT/APPLIED_VACUOUS rows: may decrease (target).
   - APPLIED rows: must NOT decrease (we did not delete operative
     rules).
   - Final form (`form_after`): must NOT change.
3. **Kāśikā cross-check:** for any cell whose APPLIED list changed,
   manually open the Kāśikā at the most-specific operative sūtra
   (e.g. 7.1.54 for रामाणाम्) and confirm the new list matches the
   *vṛtti* example.

The audit playbook codifies these checks into `make audit-cells`.

---

## 5. What the user will see when this audit is complete

### 5.1 Default `रामाणाम्` trace (target)

```
✓ 1.2.45  अर्थवदधातुरप्रत्ययः प्रातिपदिकम्   राम
⟡ 4.1.1  ङ्याप्प्रातिपदिकात्                राम  (adhikāra opens)
✓ 4.1.2  स्वौजसमौट्…आम्…                  राम → रामआम्
✓ 1.3.4  न विभक्तौ तुस्माः                  रामआम् (म्=इत् blocked)
⟡ 1.4.103 सुपः                             रामआम्
⟡ 6.4.1  अङ्गस्य                            रामआम्  (aṅga adhikāra)
✓ 1.4.17 स्वादिष्वसर्वनामस्थाने               रामआम्  (pada-saṃjñā)
✓ 7.1.54 ह्रस्वनद्यापो नुट्                  रामआम् → रामनाम्
○ 1.3.9  उपदेशे इतस्य लोपः                  रामनाम्
✓ 6.4.3  नामि                              रामनाम् → रामानाम्
◈ पद-मेलनम्                                रामानाम्
✓ 1.4.110 विरामोऽवसानम्                    रामानाम्
⟡ 8.2.1  पूर्वत्रासिद्धम् (tripadi gate)     रामानाम्
✓ 8.4.2  अट्कुप्वाङ्नुम्व्यवायेऽपि           रामानाम् → रामाणाम्
```

**13 rows instead of ~35.** Every row earns its place; the user can
toggle "विस्तरः" to see the saṃjñā-registration rows that are skipped
in the default view.

### 5.2 What the per-step panel shows when user clicks on 7.1.54

```
सूत्रम्: 7.1.54  ह्रस्वनद्यापो नुट्
पदच्छेदः: ह्रस्व-नदी-आपः / आमि / नुट्
स्थितिः: प्रयुक्तम्

अनुवृत्तिः: अङ्गस्य (6.4.1), आम् (anuvṛtti from 4.1.2 inventory)

विधिः (काशिका):
  ह्रस्व-नद्या-आपः परस्य आम् नित्यम् नुट्-आगमो भवति।
  ह्रस्वान्त-नदी-आबन्त-अङ्गेभ्यः परस्य आमो नुट्-आगमः।

अत्र किमर्थम् (why now):
  अङ्गम् = राम् (ह्रस्व अ-कारान्तम्);
  परः सुप् = आम् (षष्ठी बहुवचनम्);
  अतः नुट्-आगमः → राम् + न् + आम् = रामनाम्।

पूर्वरूपम्: रामआम्
उत्तररूपम्: रामनाम्
```

---

## 6. Out-of-scope

This audit does **not** propose changing:
- The constitution itself (Articles 0–13).
- The dispatcher / resolver / gates / executors / `apply_rule`.
- The sūtra-record schema's required fields (only adds optional fields).
- Pre-existing test failures listed in `[[project_engine_constitution]]`
  (9 known failures as of 2026-05-21) — those are tracked separately.

If any of these need to change, that is an **Amendment** under
Constitution Art. 10, not an audit fix.

---

## 7. How to use this document

- **Read this top to bottom** before starting any cleanup work.
- For each P-level item (P0–P5), open the corresponding section of
  `audit_cursor.md` for the exact file/line/command sequence.
- Always re-read `CONSTITUTION.md` Art. 7 and Art. 11 before
  modifying any file under `engine/` — these are off-limits.
- When in doubt about the Kāśikā reading, prefer Kāśikā over SK;
  prefer Mahābhāṣya over Kāśikā **only** for resolving an explicit
  disagreement, and document the resolution in `docs/AMENDMENT_*.md`.
