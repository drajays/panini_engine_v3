# audit_cursor.md — Executable Audit Playbook for Cursor

> **Read `audit_claude.md` first.** That file explains *why*. This file
> is the *how* — file paths, exact greps, ordered tasks, and acceptance
> criteria. Cursor (or any human) executes these blocks **in order**;
> stop at the first failure and surface it.
>
> **Rule of the playbook:** every code change is rule-based — phonological,
> saṃjñā-registry, or Term-tag predicates. **No** `state.meta[..._arm]`
> writes added. **No** surface-string fingerprints in `cond()`. **No**
> reads of `data/reference/` from engine or sutras.

---

## 0. Authoritative reference sources (mandatory)

Use these for *every* `cond()` and `act()` change. When the engine
and a source disagree, the source wins; document the resolution
inline as a docstring comment. The **full** rationale lives in
`audit_claude.md` §A; this is the operational summary.

### 0.1 Tier 1 — sūtra pāṭha and direct vṛttis (primary)

| # | Source | Where | Use for |
|---|---|---|---|
| 1 | ashtadhyayi.com data repo | `github.com/ashtadhyayi-com/data` (`sutraani/data.txt`; key `i` = `1` + adhyāya + pāda + sūtra digits, e.g. `11012` = 1.1.12) | `text_dev`, `text_slp1` (field `e`), `padaccheda_dev` (`pc`), `anuvritti_from` (`an`), `sutra_type`, siddhārtha (`ss`). |
| 2 | Kāśikā Vṛtti (Vāmana + Jayāditya) | ashtadhyayi.com → "Kāśikā"; same data repo `kashika` nodes; Sharma's 6-vol edition | *Udāharaṇa* + *pratyudāharaṇa* — the justification quoted in every sūtra docstring. |
| 3 | Mahābhāṣya (Patañjali) + Pradīpa (Kaiyaṭa) + Uddyota (Nāgeśa) | ashtadhyayi.com → "Bhāṣya"; BORI edition | Deepest disambiguation. Required when Kāśikā is silent or paribhāṣā-interpretation is contested. |
| 4 | Siddhānta-Kaumudī + Tattva-bodhinī | ashtadhyayi.com → "SK" | Cross-check which sūtras tradition cites *together*. **Never drive engine ordering** (Const. Art. 3). |
| 5 | Laghu-Siddhānta-Kaumudī (Varadarāja) | sanskritdocuments.org; Chowkhamba print | Compact teaching prakriyās; paradigm sanity check. |
| 6 | Prakriyā-Kaumudī / Prakriyā-Sarvasva | print; partial GRETIL | Pre-SK alternatives for cross-validation. |

### 0.2 Tier 2 — paribhāṣā and meta-grammar

| # | Source | Where | Use for |
|---|---|---|---|
| 7 | Paribhāṣenduśekhara (Nāgeśa) | BORI / Chowkhamba; English: Kielhorn 1868 | Authoritative paribhāṣā corpus; mandatory for any *atideśa* / inherited *anuvṛtti*. |
| 8 | Vyāḍi-paribhāṣā, Śākaṭāyana-paribhāṣā | print | Older paribhāṣā traditions; tie-break when Nāgeśa is contested. |
| 9 | Liṅgānuśāsana | ashtadhyayi.com ancillaries | *Liṅga*-assignment rules. |
| 10 | Phiṭ-sūtras (Śāntanava) | ashtadhyayi.com ancillaries | Accent rules for prātipadika. |
| 11 | Uṇādi-sūtras | ashtadhyayi.com ancillaries | Uṇādi-pratyaya derivations. |

### 0.3 Tier 3 — kosha and dhātu

| # | Source | Where | Use for |
|---|---|---|---|
| 12 | Dhātupāṭha (Pāṇinīya) | `data/inputs/dhatupatha.json`; ashtadhyayi.com → "Dhātupāṭha" | Dhātu inventory: gaṇa, anubandha, artha. |
| 13 | Gaṇapāṭha | `data/inputs/ganapatha.json`; ashtadhyayi.com → "Gaṇapāṭha" | Named gaṇa-lists in module-level `frozenset`s. |
| 14 | Nighaṇṭu + Nirukta (Yāska) | gretil.sub.uni-goettingen.de | Pre-Pāṇinian semantic classes (rare). |
| 15 | Köln Sanskrit Lexicon (Monier-Williams) | sanskrit-lexicon.uni-koeln.de | Surface-form sanity check only — NOT a rule source. |

### 0.4 Tier 4 — computational oracles (cross-validation only)

| # | Source | Where | Use for |
|---|---|---|---|
| 16 | **Vidyut** (Ambuda-org) | `github.com/ambuda-org/vidyut` | Rust prakriyā engine. Oracle for surface verification. **Never copy code logic** — independent verification only. |
| 17 | **Saṃsādhanī (IIIT-H Hyderabad)** | `sanskrit.uohyd.ac.in/scl/` (analyzer + sandhi + segmenter) | Subanta/tinanta/kṛdanta analyzer + morphological-tag taxonomy + gold paradigm corpora. |
| 18 | **Sanskrit Heritage Platform (INRIA)** | `sanskrit.inria.fr/` | Wide-coverage finite-state Sanskrit reader. Independent surface oracle. |
| 19 | JNU SCL group | scl-jnu.in | Subanta/tinanta tables. |
| 20 | DCS (Digital Corpus of Sanskrit) | `www.sanskrit-linguistics.org/dcs/` | Surface-form attestation in real texts. |
| 21 | GRETIL | `gretil.sub.uni-goettingen.de/` | Ancillary editions, hard-to-find texts. |
| 22 | SARIT | `sarit.indology.info/` | TEI-XML scholarly editions. |

### 0.5 Tier 5 — methodology references (engine design)

These justify *how* the engine is built, not *what* rules say.
Consulted when changing dispatcher / resolver / gate logic.

| # | Source | Why |
|---|---|---|
| 23 | Cardona, *Pāṇini: A Survey of Research* (1976) | Scholarly summary; tie-break between commentarial traditions. |
| 24 | Cardona, *Pāṇini: His Work and Its Traditions* (1988, 1997) | SutraType taxonomy must map onto Cardona's analysis. |
| 25 | Kiparsky, *Pāṇini as a Variationist* (1979); *Some Theoretical Problems* (1982) | Utsarga–apavāda, vipratiṣedha — drives resolver design. |
| 26 | Sharma, *The Aṣṭādhyāyī of Pāṇini* (6 vols.) | Bilingual modern edition. |
| 27 | Vasu, *The Aṣṭādhyāyī of Pāṇini* (1891 English trans.) | Free-text quick lookup. |
| 28 | Matilal, *The Word and the World* (1990) | Glass-box philosophy justification. |
| 29 | Joshi & Roodbergen, *The Aṣṭādhyāyī of Pāṇini* (multi-vol with Bhāṣya) | Bhāṣya-integrated translation. |
| 30 | Sanskrit Computational Linguistics proceedings (Kulkarni, Huet eds.) | Algorithmic background. |
| 31 | Deshpande, *Saṃskṛta-Subodhinī* + papers | Pedagogical rigor; user-facing explanations. |
| 32 | Kak, "The Paninian Approach to NLP" (1987) | Rewrite-system formalisation precedent. |

### 0.6 Forbidden as sources

- Unverified blog posts, YouTube transcripts.
- ChatGPT / any LLM output without independent verification.
- Wikipedia (use to locate primary, then cite primary).
- PDFs without edition lineage.
- Surface-form transliterators (Aksharamukha etc.) for **rule logic**.

### 0.7 Citation requirement (mandatory in every edited sūtra file)

Every sūtra file's module docstring **must** contain, by the time
this audit is complete, a "Sources consulted" section with at least
source #1 (ashtadhyayi.com row index) and source #2 (Kāśikā
udāharaṇa). Example:

```python
"""
6.4.3  नामि  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=64003
- Kāśikā: "अजन्तस्याङ्गस्य नामि परतो दीर्घो भवति" with udāharaṇa
  वृक्षाणाम्, प्लक्षाणाम्, अग्नीनाम्, वायूनाम्.
- Cross-validated against Vidyut (ambuda-org/vidyut) for रामाणाम्,
  वृक्षाणाम् surface output.

[v3 implementation paragraph below]
"""
```

---

## 0.7b Tiṅanta-only audit (parallel track)

For **full tiṅanta prakriyā** (10 lakāras × prayoga × paradigm), use the dedicated
playbook **`audit_tinanta_cursor.md`** (phases T0–T7). It extends this file’s P3/P4
logic but scopes files to `pipelines/tinanta.py`, corrected demos P008–P019, and
tiṅanta Web UI. Coordination: `audit/RUN_LOG.md` §F.

---

## 0.8 Coordination log (MANDATORY before every task)

Both Claude Code and Cursor share **one** repo. To avoid double-work
and merge conflicts, every task **must** be claimed in
`audit/RUN_LOG.md` before you start.

Procedure:

1. Open `audit/RUN_LOG.md`. Read §B (in-flight claims) and §C
   (recent action history).
2. If your intended files appear in another agent's `in-progress`
   claim row, **pick a different task** or wait.
3. Add a new row to §B with timestamp, agent (`cursor` or
   `claude`), the P-level (e.g., `P3 group 1`), the file paths
   you'll edit, and `status: in-progress`.
4. Work the task.
5. When done, change the row's status to `released` and append a
   §C entry (what changed / why / tests run / next).

Refusal: if the log says another agent is editing a file you need
and your task cannot proceed without it, surface that to the human
user — do not silently override the claim.

---

## 1. Pre-flight (do once, before any P-level work)

```bash
# Confirm working tree
git status
# Save a baseline of all known traces
python -m tools.replay_trace --all > .audit/trace_baseline_$(date +%F).txt
# Snapshot the regression test status
pytest tests/regression -q > .audit/regression_baseline_$(date +%F).txt || true
pytest tests/constitutional -q > .audit/constitutional_baseline_$(date +%F).txt || true
```

Create the `.audit/` directory if missing. Commit `.audit/.gitkeep`
so the path exists in source control. **Do not commit the baseline
files** themselves; they are local snapshots.

Acceptance: both baseline files exist; their content is the reference
for every "form must not change" check below.

---

## 2. P0 — Web UI: default-hide registry-stamp noise

Cost: ~30 min. Risk: low (UI-only). Engine unchanged.

### 2.1 Add a default-on filter in `webui/static/trace.js`

**File:** `webui/static/trace.js`
**Anchor:** `function applyTraceFilter()` (around line 96)

Add a third state to the existing checkbox row: a default-on
"रूप-परिवर्तन-मात्रम्" (form-changing only) checkbox that, when
checked, hides AUDIT and APPLIED_VACUOUS rows.

Implementation hint:
```js
function _traceStepInFilter(step, active) {
  if (step._is_structural) return active.has("STRUCTURAL");
  const st = step.status || "APPLIED";
  if (active.has("RUPA_PARIVARTANA_ONLY")) {
    return st === "APPLIED";  // hide AUDIT, APPLIED_VACUOUS, etc.
  }
  if (st === "APPLIED_VACUOUS") return active.has("APPLIED");
  return active.has(st);
}
```

### 2.2 Add the checkbox to every template that has the filter row

**Files (grep all at once):**
```bash
grep -ln 'value="APPLIED"' webui/templates/
```
Expected hits: `derive.html`, `pipelines.html`, `showcase.html`,
`patha.html`, `matrix.html`, `sarvanama.html`, `devendra.html`,
`krdanta.html`.

For each: insert before the `value="APPLIED"` label:
```html
<label>
  <input type="checkbox" value="RUPA_PARIVARTANA_ONLY" checked>
  रूप-परिवर्तन-मात्रम्
</label>
```

### 2.3 Acceptance

```bash
# Manual: open /derive in browser, generate रामाणाम्.
# Expected: trace shows ≤ 13 rows by default.
# Untick the new checkbox → all rows reappear.
```

No code change to `engine/`, `sutras/`, or `core/`. No new tests
required at this step (UI-only).

---

## 3. P1 — Tighten registry-stamp saṃjñā cond()

Cost: ~2 hours per sūtra × 12 sūtras = ~1.5 days. Risk: medium
(must preserve `samjna_registry` semantics for downstream cond reads).

### 3.1 Target list (priority order)

For each, the new `cond()` returns False unless a Term in the current
state could plausibly need the saṃjñā:

| Sūtra | Current cond | New cond (predicate) |
|---|---|---|
| 1.1.20 ghu | registry not stamped | `any(t.kind == 'dhatu' and t.meta.get('upadesha_slp1') in GHU_DHATU_UPADESHA_SLP1 for t in state.terms)` AND registry not stamped |
| 1.1.23 saṅkhyā | registry not stamped | `any('prātipadika' in t.tags and (t.meta.get('upadesha_slp1') or '').rstrip('~') in SANKHYA_1_1_23_PRATIPADIKA_SLP1 for t in state.terms)` |
| 1.1.24 ṣaṭ | registry not stamped | `any('prātipadika' in t.tags and _shashanta(t.meta.get('upadesha_slp1') or '') for t in state.terms)` |
| 1.1.22 gha (tarap-tamap) | registry not stamped | `any('taddhita' in t.tags and (t.meta.get('upadesha_slp1') or '') in {'tarap','tamap'} for t in state.terms)` |
| 1.1.11 pragṛhya (dvivacana) | reads arm flag | keep the structural arm (post-6.1.102 etc.) BUT also gate the registry stamp behind `_is_dvivacana(state)` derived from the sup-attached Term's `tags ∩ {'sup_dvi'}` (NOT from `state.meta['vibhakti_vacana']`) |
| 1.1.14 nipāta | registry not stamped | `any('nipāta' in t.tags for t in state.terms)` |
| 1.1.15–1.1.19 | registry not stamped | only fire when an aṅga/pada Term ends in the trigger vowel + vibhakti context matches structurally (no meta read) |
| 1.1.43 sarvanāmasthāna | (already conditional) | audit only — no change expected |
| 1.1.27 sarvanāma | registry not stamped | `any('prātipadika' in t.tags and (t.meta.get('upadesha_slp1') or '') in SARVADI for t in state.terms)` |
| 1.1.29 / 1.1.30 | (already conditional via samāsa context) | audit only — no change expected |
| 1.1.62 / 1.1.63 (luk-saṃjñā) | (already conditional) | audit only |
| 1.1.73 vṛddha-pada | (already conditional on first-ac vṛddhi) | audit only |

### 3.2 Per-sūtra procedure

For each row above:

1. Open the sūtra file.
2. Add the helper predicate as a private module-level function
   (so `cond()` stays one-liner-readable).
3. Update `cond()` to AND the new predicate with the existing check.
4. **Do not touch `act()`.** The registry write must still happen on
   the rare occasion the cond is True.
5. Update the docstring's "v3 implementation" paragraph to cite the
   Kāśikā udāharaṇa that justifies the predicate, with source link
   to ashtadhyayi.com (§ 0).
6. Run the per-sūtra regression slice:
   ```bash
   pytest tests/ -k "sutra_1_1_20" -v
   ```
7. Run the full subanta cell regression:
   ```bash
   pytest tests/regression/ -k "subanta or rama" -v
   ```
8. **Acceptance:** all formerly-passing tests still pass; trace row
   count for the 24 राम cells decreases.

### 3.3 Idempotency

Each sūtra's `act()` already pops its arm or refuses to re-write the
registry. If a re-fire is observed in a trace (two APPLIED rows for
the same sutra-id), that is an engine bug — file a `tests/regression/`
case rather than patching the sūtra.

---

## 4. P2 — Split the preflight blocks in `core/canonical_pipelines.py`

Cost: ~3 hours. Risk: medium (touches the canonical recipe spine).

### 4.1 Block split

**File:** `core/canonical_pipelines.py`
**Replace:** the current `P01_samjna_1_1_3_to_1_1_100` and
`P01_samjna_1_1_15_to_1_1_24` (lines ~1100–1138).

**With three new blocks (each calls only what the use-class needs):**

```python
def P01_samjna_subanta_minimum(s: State) -> State:
    """Subanta-only spine: prātipadika + sup-pratyaya + pada + aṅga.

    Kāśikā: 1.2.45 (prātipadika), 1.4.13/14 (aṅga, pada), 1.4.17
    (pada-saṃjñā non-sarvanāmasthāna).
    """
    for sid in ("1.2.45", "1.4.13", "1.4.14"):
        s = apply_rule(sid, s)
    return s


def P01_samjna_pragriya_cluster(s: State) -> State:
    """1.1.11–1.1.19 — pragṛhya cluster, only when dvivacana/nipāta
    context is structurally detectable on the tape."""
    for sid in ("1.1.11", "1.1.12", "1.1.13", "1.1.14", "1.1.15",
                "1.1.16", "1.1.17", "1.1.18", "1.1.19", "1.1.100"):
        s = apply_rule(sid, s)  # each sūtra's cond decides
    return s


def P01_samjna_dhatu_class(s: State) -> State:
    """Dhātu-only: ghu (1.1.20), kṅiti (1.1.5), etc. Called from
    tinanta/kṛdanta pipelines, NOT from subanta."""
    for sid in ("1.1.20", "1.1.5"):
        s = apply_rule(sid, s)
    return s
```

### 4.2 Rewire `P01_subanta_bootstrap`

**File:** `core/canonical_pipelines.py`
**Anchor:** `def P01_subanta_bootstrap` (around line 1074).

Replace the body of the function. Drop calls to:
- 1.1.1 (vṛddhi-saṃjñā) — taddhita-only, schedule from
  `P05_vrddha_pada_bootstrap` already.
- 1.1.2 (guṇa-saṃjñā) — guṇa rules are vidhi, the saṃjñā needs to be
  visible only when a guṇa-vidhi is about to fire; handle via the
  guṇa-vidhi's own preflight (`P00_guna_prayoga_readiness`).
- The blanket `P01_samjna_1_1_3_to_1_1_100` and `_15_to_1_1_24`.

Use:
```python
def P01_subanta_bootstrap(s: State) -> State:
    if s.meta.get("2_3_46_matra_prathama_eligible"):
        s = apply_rule("2.3.1", s); s = apply_rule("2.3.46", s)
    if s.meta.get("2_3_50_sheSa_shashthi_eligible"):
        s = P00_anabhihite_shashthi_shese_2_3_50(s)
    s = apply_rule("4.1.1", s)  # ṅyāp-prātipadikāt adhikāra
    if any("strīliṅga" in t.tags for t in s.terms):
        s = apply_rule("4.1.3", s); s = apply_rule("4.1.4", s)
    s = P01_samjna_subanta_minimum(s)         # 1.2.45 + 1.4.13/14
    s = P01_samjna_pragriya_cluster(s)        # tightened cond — most skip on bahuvacana
    s = apply_rule("1.1.73", s)               # nāmadheya vṛddha (only fires when names given)
    s = apply_rule("1.2.72", s)
    s = apply_rule("1.1.27", s)               # sarvānāma (now tightened in P1)
    s = apply_rule("1.1.29", s); s = apply_rule("1.1.30", s)
    return s
```

### 4.3 Wire dhātu-class block into tinanta/krdanta entry points

**Files:**
- `pipelines/tinanta.py` — find the bootstrap (search for
  `def derive` and the first `apply_rule` block); insert
  `P01_samjna_dhatu_class(s)` right after the dhātu Term is
  established.
- `pipelines/krdanta.py` — same procedure.

### 4.4 Acceptance

```bash
pytest tests/regression -v 2>&1 | tee .audit/regression_after_P2.txt
diff .audit/regression_baseline_*.txt .audit/regression_after_P2.txt
# Expected diff: no NEW failures. May have FEWER failures if a known
# pre-existing failure was caused by the noise.
```

Also: run `make sig-snapshot` (if it exists) and review the new SIG.
Expected: fewer edges through 1.1.x saṃjñā nodes.

---

## 5. P3 — Demolish `_arm` flags incrementally

Cost: ~1 day per sūtra group, in priority order. Risk: medium-high
(rule firing semantics change). Always covered by regression tests.

### 5.1 Discovery commands

```bash
# Which sūtras still gate on _arm?
grep -rln 'state\.meta\.get([^)]*_arm' sutras/ | sort > .audit/arm_sutras.txt
wc -l .audit/arm_sutras.txt
# Which arms are written?
grep -rn 'state\.meta\["[^"]*_arm"\]' pipelines/ core/ engine/ \
  | awk -F'"' '{print $2}' | sort -u > .audit/arm_keys.txt
wc -l .audit/arm_keys.txt
```

### 5.2 Migration order

Take groups in this order (lowest blast radius first):

1. **`6.1.97_pararupa_*` (3 keys with demo IDs)** — pre-existing
   technical debt called out in memory. Replace with phonological
   predicate `a + a/e at cross-term boundary, not pragṛhya, not
   tinganta-vikaraṇa-context`. Run the asmad / P013 / P017 demos
   after, expect identical surfaces.

2. **`2_4_71_luk_arm`, `2_4_74_yang_luk_arm`** — only 2 keys, used by
   the luk preflight block. Replace with: the luk sūtra fires when a
   *lupyate*-eligible pratyaya is on the tape with the right adhikāra.
   The arm becomes redundant.

3. **`2.2.x samāsa block`** (~38 keys) — replace with a `samasa_pending`
   Term tag set by the recipe; each 2.2.x sūtra's `cond()` checks the
   tag plus the structural shape (anekapadī, dvandva-arthe, etc.) from
   its own definition. **Largest batch — do last.**

### 5.3 Per-sūtra migration template

For sūtra `X.Y.Z` currently `cond: state.meta.get("X_Y_Z_arm")`:

1. Find every writer of `X_Y_Z_arm`:
   ```bash
   grep -rln "X_Y_Z_arm" pipelines/ core/
   ```
2. For each writer, identify *what state condition* the arm was
   standing in for. Usually it's "the recipe just set up a context
   the sūtra needs to recognize." Write that condition as a Term tag
   or phonological predicate.
3. Replace the sūtra's `cond()`:
   ```python
   def cond(state):
       # was: state.meta.get("X_Y_Z_arm")
       return _the_structural_predicate(state)
   ```
4. Replace each writer's `state.meta["X_Y_Z_arm"] = True` with
   the corresponding Term-tag write (e.g., `term.tags.add("samasa_pending")`)
   OR delete the writer if the predicate is already true at that
   point in the recipe.
5. Run the affected pipeline's regression:
   ```bash
   pytest tests/regression -k "X_Y_Z or relevant_keyword" -v
   ```
6. Run constitutional tests:
   ```bash
   pytest tests/constitutional -v
   ```
7. If green, commit:
   ```
   sutra X.Y.Z: replace _arm gate with structural predicate
   ```

### 5.4 What "done" looks like

For each migrated sūtra, both of the following must be true:
- `grep "X_Y_Z_arm" sutras/ pipelines/ core/` returns **zero lines**.
- The regression baseline is unchanged (no new failures, no surface
  changes).

When all groups are done, `.audit/arm_sutras.txt` should drop from
~3,398 lines to a small residue of *legitimate* coordination keys
(e.g., `ashir_liG`, `3_1_68_kartari_recipe`, `pratipadika_avayava_ready`)
that are not patchwork per Constitution Art. 13 §2.

---

## 6. P4 — Merge `_corrected_*` demo pipelines into canonical

Cost: ~30 min per file × 31 files = ~2 days. Risk: low (test
coverage already exists; we just consolidate).

### 6.1 Discovery

```bash
ls pipelines/*_corrected_P0*_demo.py | tee .audit/corrected_pipelines.txt
```

### 6.2 Per-file procedure

For each `*_corrected_P0NN_*demo.py`:

1. Find the original (non-corrected) sibling:
   ```bash
   base=$(basename "$f" | sed 's/_corrected_P0[0-9]*_demo/_demo/' \
                        | sed 's/_corrected_P0[0-9]*/.py/')
   ```
2. `diff` the two. The corrected version should differ in:
   - One or more `apply_rule` calls (usually adding a sūtra the
     original missed, or fixing an order).
   - Possibly an `_arm` write that the original lacked.
3. **Merge plan:**
   - If the difference is a missing `apply_rule`: the original is
     the bug; replace it with the corrected version's spine, run all
     its regression tests, delete the corrected version, rename any
     test imports.
   - If the difference is an `_arm` write: the corrected version is
     itself patchwork; fix the **sūtra** to not need the arm (per
     P3), then both files converge to the same spine and one of them
     can be deleted.
4. Update `streamlit_app/pages/*.py` and `webui/app.py` to drop the
   deleted pipeline from any selector / dropdown.

### 6.3 Acceptance

```bash
ls pipelines/*_corrected_*demo.py | wc -l  # must drop to 0
pytest tests/regression -v                  # no new failures
```

---

## 7. P5 — Per-step "why now" trace enrichment

Cost: ~1 hour per sūtra family, target ~30 families. Risk: low
(additive field).

### 7.1 Engine schema extension

**File:** `engine/trace.py`
**Change:** add optional field `why_now_dev: Optional[str] = None` to
the `TraceStep` schema. Backward-compatible (existing rows omit it,
UI handles missing).

### 7.2 UI surface

**File:** `webui/static/trace.js`
**Anchor:** `function renderSutraDetail(step)` (around line 172).

Insert below the existing `why` block:

```js
${step.why_now_dev
  ? `<div class="kv"><strong>अत्र किमर्थम्</strong>
       <span class="dev">${escapeHtml(step.why_now_dev)}</span>
     </div>`
  : ""}
```

### 7.3 Sūtra-side population (incremental)

For each priority sūtra family, edit the `act()` to append the
`why_now` field on the trace step the dispatcher records. The
dispatcher's hook for this lives in `engine/dispatcher.py` —
`notify_apply_rule_end`. Each sūtra adds:

```python
def act(state: State) -> State:
    ...
    # populate why_now after the operation
    state.trace[-1]["why_now_dev"] = (
        f"अङ्गम् {anga_anta_slp1} ह्रस्व; परं सुप् {sup_slp1}; "
        f"अतः नुट्-आगमः। (काशिका ७।१।५४)"
    )
    return state
```

**Priority families:**

1. 7.1.x (sup-related vidhis) — fires on most subanta cells.
2. 6.4.x (aṅga-kārya) — fires on every dīrgha / nuṭ / vuk insertion.
3. 8.x (tripādī sandhi) — fires at end of every form.
4. 3.x (kṛt / sanādi / pratyaya-vidhāna) — for tinanta/krdanta.
5. Eventually all VIDHI/NIYAMA sūtras.

### 7.4 Kāśikā quote enrichment

Each sūtra file may optionally add a `kashika_dev: str` constant that
stores the exact Kāśikā vṛtti opening line (transliterated to
Devanāgarī). The UI displays it inside the sutra-detail panel under
"विधिः (काशिका)". Source: ashtadhyayi.com Kāśikā JSON (§ 0 row 2).

---

## 8. Verification gate (run after each P-level)

```bash
# 1. Constitutional tests must remain green
pytest tests/constitutional -v

# 2. Regression tests: no NEW failures
pytest tests/regression -v > .audit/regression_after_P${LEVEL}.txt
diff .audit/regression_baseline_*.txt .audit/regression_after_P${LEVEL}.txt | \
  grep -E '^>.*FAIL' || echo "OK: no new failures"

# 3. SIG snapshot diff (if make sig-snapshot exists)
make sig-snapshot 2>/dev/null && \
  diff sig/baselines/last.json sig/baselines/current.json | head -100

# 4. Manual UI check
python -m webui.app &
# Open http://localhost:5000/derive, generate रामाणाम्
# Expected:
#   - default trace ≤ 13 rows
#   - "विस्तरः" reveals the saṃjñā stamps
#   - each row's sutra-detail panel shows kāśikā-quoted why and
#     state-specific "why now"
```

---

## 9. Anti-patterns to refuse

While executing this audit, **refuse** to add any of the following.
If a task seems to require one, stop and surface it as a question:

- A new `state.meta[..._arm]` key.
- A `cond()` that reads `state.meta["lakara"]`, `vibhakti_vacana`,
  `puruṣa`, `vacana`, or any surface Devanāgarī string.
- A `cond()` that reads from `data/reference/`.
- A new `pipelines/*_corrected_*_demo.py` file.
- A `sutras/.../sutra_X_Y_Z.py` whose `cond()` mentions a demo or
  prakriya ID (`P0NN`, `corrected_v2`).
- An import of `requests` or any network library inside `sutras/` or
  `engine/`.
- A monkey-patch of any class in `engine/`.

---

## 10. Schedule (suggested)

| Week | Tasks |
|---|---|
| 1 | P0 (UI filter) + P1 (sūtra 1.1.20, 1.1.23, 1.1.24, 1.1.22) |
| 2 | P1 finish + P2 (preflight split) |
| 3 | P3 group 1 (6.1.97_pararupa_*) + P5 priority family 1 (7.1.x) |
| 4 | P3 group 2 (2.4.71 luk) + P4 (merge `_corrected_*` batch 1) |
| 5+ | P3 group 3 (2.2.x samāsa, the big one) + P4 finish + P5 expand |

Each week ends with a clean `git log --oneline` of the form
`audit Pn: <what>` commits, each independently revertible.

---

## 11. Reporting back

At the end of every working session, append to `audit/RUN_LOG.md`
(create if missing):

```
## 2026-MM-DD HH:MM
- P-level worked on: P1 (sūtra 1.1.20, 1.1.23)
- Files changed: sutras/adhyaya_1/pada_1/sutra_1_1_20.py, _1_1_23.py
- Tests run: pytest tests/regression -k 'rama' (24 cells, all pass)
- Trace row deltas: rāma cell 6-3 dropped from 35 → 27 rows
- Notes: pragṛhya cluster requires Term-tag detection of dvivacana sup;
  paused on 1.1.11 until 4.1.2 act() tags sup terms with sup_dvi.
```

This gives the user (and the next Cursor session) a continuous record
of what was done, what was left, and where to resume.
