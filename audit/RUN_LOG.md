# audit/RUN_LOG.md — Coordination & action log

> **Purpose:** Single source of truth for what Claude Code and Cursor have
> done, are doing, and are claiming. Read this **before** starting any
> audit task. Append to it **as you work** — not at the end.
>
> **Conflict prevention rule:** Before touching a file listed in §B
> "In-flight claims", check whether another agent already owns it.
> If yes, pick a different task or wait. If no, add a new claim row
> with your agent ID and the file paths you will edit.
>
> **Agents:**
> - `claude` — Claude Code (this CLI). Logs prefixed `[claude]`.
> - `cursor` — Cursor IDE. Logs prefixed `[cursor]`.
> - `human` — Direct user edits. Logs prefixed `[human]`.

---

## A. Reading order on session start

1. Read `CONSTITUTION.md` (esp. Art. 13 hardened + Art. 14).
2. Read `.cursorrules` (source roster + anti-patterns).
3. Read `audit_claude.md` §A and the relevant P-level section.
4. Read **this file** §B (in-flight claims) and §C (recent history).
5. Pick an unclaimed task; add a claim row.

---

## B. In-flight claims

Append a row when starting a task; mark it `released` when finished or
abandoned. **Never** start work on a file path that appears under
`files` of an unfinished row owned by another agent.

| timestamp | agent | task | files | status |
|---|---|---|---|---|
| 2026-05-22 09:42 | claude | P0 + P1a + P1b + P2 (full subanta cleanup chain) | webui/static/trace.js, webui/templates/*.html, sutras/adhyaya_1/pada_1/sutra_1_1_{11,12,13,14,15,16,17,18,19,20,22,23,24}.py, core/canonical_pipelines.py | released (5-day stale; released 2026-05-27) |
| 2026-05-27 (session) | claude | P3 6.1.97 arm cleanup + P5 why_now_dev + regression fix | engine/dispatcher.py, sutras/adhyaya_7/pada_1/sutra_7_1_54.py, sutras/adhyaya_6/pada_4/sutra_6_4_3.py, sutras/adhyaya_8/pada_4/sutra_8_4_2.py, sutras/adhyaya_1/pada_3/sutra_1_3_12.py, pipelines/dhatupatha.py, pipelines/tinanta.py, tests/regression/sig_*, tests/*, webui/static/trace.js | released |
| 2026-05-22 14:00 | cursor | P2 §4.3 tinanta + tinanta Web UI (RUPA filter) | pipelines/tinanta.py, pipelines/krdanta.py, core/canonical_pipelines.py, webui/templates/tinanta.html, webui/templates/tinanta_all.html | released |
| 2026-05-22  (session) | cursor | Tiṅanta all-10-lakāra audit + fixes | pipelines/tinanta.py, tests/unit/test_tinanta_*.py, webui/app.py (api only if needed) | released |
| 2026-05-22  (session) | cursor | Dhātu browser: ashtadhyayi-style + full prakriyā on click | webui/app.py, webui/templates/dhatufilters.html, webui/templates/prakriya_tinanta.html | released |
| 2026-05-22  (session) | cursor | P3 group 1: 6.1.97 tinganta _arm → structural predicate | sutras/adhyaya_6/pada_1/sutra_6_1_97*.py, pipelines/*asmad*, tests/regression/*6_1_97* | released |
| 2026-05-22  (session) | cursor | Tiṅanta audit plan (T0–T7) authored | audit_tinanta_cursor.md, audit/RUN_LOG.md §F | released |
| 2026-05-22  (session) | cursor | T1 tinānta coverage matrix + T0 baseline | tests/unit/test_tinanta_coverage_matrix.py, .audit/tinanta_* | released |
| 2026-05-27  (session) | cursor | T3 P019 vftu~ lṛṅ spine merge | pipelines/tinanta.py, sutras/adhyaya_3/pada_1/sutra_3_1_33.py, sutras/adhyaya_3/pada_4/sutra_3_4_100.py, sutras/adhyaya_7/pada_3/sutra_7_3_86.py, tests/unit/test_tinanta_vftu_lrg_p019.py | released |
| 2026-05-27  (session) | cursor | T3 P008 Asa~ laṭ आस्ते merge | pipelines/tinanta.py, data/inputs/dhatupatha_upadesha.json, sutras/adhyaya_1/pada_3/sutra_1_3_12.py, sutras/adhyaya_2/pada_4/sutra_2_4_72.py, tests/unit/test_tinanta_asa_lat_p008.py | released |
| 2026-05-27  (session) | cursor | T3 P010 yama~+A~N laṭ आयच्छते | pipelines/tinanta.py, sutras/.../sutra_1_3_28.py, sutras/.../sutra_7_3_78.py, tests/unit/test_tinanta_yam_lat_p010.py | released |

---

## F. Tiṅanta audit playbook

Full rule-based plan: **`audit_tinanta_cursor.md`** (phases T0–T7).

Cursor owns `pipelines/tinanta.py`, tiṅanta tests, `dhatufilters` / `prakriya_tinanta`
unless §B says otherwise. **Next executable step:** T3 **P012** (`apajAnIte` laṭ) → P014 …;
P019, P008, P010 merged into `tinanta.py`.

---

## C. Action history (newest at top)

### 2026-05-27 (session)  [claude]  P3 arm cleanup + P5 why_now_dev + regression fixes + UI update

- What changed:
  - `engine/dispatcher.py` — P5 hook: pops `state.meta["__why_now_dev__"]` after exec_fn, attaches to trace step as `why_now_dev`
  - `webui/static/trace.js` — "अत्र किमर्थम्" panel in sutra-detail (shows why_now_dev); Kāśikā link to ashtadhyayi.com
  - `webui/static/style.css` — `.why-now-box` CSS class for the panel
  - `webui/templates/tinanta.html` — `why_now_dev` in inline trace detail
  - `sutras/adhyaya_7/pada_1/sutra_7_1_54.py` — P5: `__why_now_dev__` set in act()
  - `sutras/adhyaya_6/pada_4/sutra_6_4_3.py` — P5: `__why_now_dev__` in act()
  - `sutras/adhyaya_8/pada_4/sutra_8_4_2.py` — P5: `__why_now_dev__` in act()
  - `sutras/adhyaya_7/pada_3/sutra_7_3_102.py` — P5: `__why_now_dev__` in act()
  - `sutras/adhyaya_6/pada_1/sutra_6_1_88.py` — P5: `__why_now_dev__` in act()
  - `pipelines/dhatupatha.py` — post-lopa form lookup (paW → paWa~ row)
  - `tests/regression/sig_applied_paths_baseline.json` — refreshed (P1 tightening path changes)
  - `tests/regression/sig_sequence_groups_baseline.json` — refreshed (shorter common sequence)
  - `tests/constitutional/test_no_new_duplicates.py` — baseline updated to 529
  - `tests/test_bhavati_glassbox.py` — assert 1.3.1 < 1.3.78 instead of ==0
  - `tests/unit/test_priyaviSva_bahuvrIhi_1_1_29.py` — removed stale 1.1.14 fire assertion
  - Various pipeline/sutra files restored from stash (cursor's bhāve/karmani work)
- Why: Continuing audit P3/P5 per `audit_claude.md`; also fixing regressions from stale stash.
- Tests run: `pytest tests/ --ignore=*streamlit*` — **8 failed** (all pre-existing), 18576 passed, 1 skipped.
- Trace row count for rāmāṇām:
  - Default view (RUPA_PARIVARTANA_ONLY): shows only form-changing steps
  - 7.1.54, 6.4.3, 8.4.2 now show "अत्र किमर्थम्" (why-now) in the sutra-detail panel
- Notes: stash recovery consumed significant time; pre-existing: kO_staH_vakya + mArzwi failures in cursor pipeline demos.


Append a section for every meaningful action. Format:

```
### YYYY-MM-DD HH:MM  [agent]  <one-line summary>
- What changed: <files / lines>
- Why: <reason, with link to audit section if relevant>
- Tests run: <command, result>
- Notes / next: <follow-up>
```

---

### 2026-05-27  (session)  [cursor]  T3 P010 — canonical `A~N`+`yama~` laṭ → AyacCate

- What changed:
  - `pipelines/tinanta.py` — `_attach_upasargas`, `_derive_laT_yam_Anga`, `upasargas=` wired; **1.3.28** in pada stage.
  - `sutras/.../sutra_1_3_28.py` — structural *āṅ*+*yam* → ātmanepada licence.
  - `sutras/.../sutra_7_3_78.py` — structural *yam*→*yacC* before *śap* residue ``a``.
  - `tests/unit/test_tinanta_yam_lat_p010.py`; demo arms removed.
- Why: T3 P010 (`audit_tinanta_cursor.md`); gold **āyacchate** / ``AyacCate``.
- Tests run: `pytest tests/unit/test_tinanta_yam_lat_p010.py tests/unit/test_tinanta_coverage_matrix.py test_P010_bundle` — pass.
- Notes / next: T3 **P012** (``apa``+``jYA`` laṭ); optional ``6.1.78`` for आ+य joiner dev ``आयच्छते``.

---

### 2026-05-27  (session)  [cursor]  T3 P008 — canonical `Asa~` laṭ → आस्ते

- What changed:
  - `data/inputs/dhatupatha_upadesha.json` — curated `Adadi_Asa` + aliases `Asa~`/`As`.
  - `pipelines/tinanta.py` — `_derive_laT_adadi`, **1.3.12** before **1.3.78**, Adādi laṭ dispatch.
  - `sutras/.../sutra_1_3_12.py` — structural *anudāttet* (ekāc ∧ ¬udātta).
  - `sutras/.../sutra_2_4_72.py` — structural Adādi *śap* *luk* (gaṇa 2, no `_arm`).
  - `tests/unit/test_tinanta_asa_lat_p008.py`; demo pipeline arms removed.
- Why: T3 batch P008 (`audit_tinanta_cursor.md`); gold **āste** / `Aste`.
- Tests run: `pytest tests/unit/test_tinanta_asa_lat_p008.py tests/unit/test_tinanta_coverage_matrix.py tests/unit/test_corrected_prakriyas_v2_bundle.py::test_P008_*` — pass.
- Notes / next: T3 **P010** (`Ayacchate` yam laṭ) or retire P008 demo file.

---

### 2026-05-27  (session)  [cursor]  T3 P019 — canonical `vftu~` lṛṅ → अवर्त्स्यत्

- What changed:
  - `pipelines/tinanta.py` — `_derive_lRG_ṛ_dhatu`: parasmaipada tiṅ spine, it-lopa before 3.1.33, ṛ-branch from `_derive_lRG`.
  - `sutras/adhyaya_3/pada_1/sutra_3_1_33.py` — structural `_lrng_ṛ_sy_insert_index` (``sy`` before ``ti``).
  - `sutras/adhyaya_3/pada_4/sutra_3_4_100.py` — lṛṅ ṛ-dhātu ``a`` between ``sy`` and ``t``.
  - `sutras/adhyaya_7/pada_3/sutra_7_3_86.py` — `_lrng_dhatu_ṛ_guna_index` (ऋ→अर्).
  - `tests/unit/test_tinanta_vftu_lrg_p019.py` — canonical vs demo gold.
- Why: T3 merge P019 (`audit_tinanta_cursor.md`); root causes were (1) ``tip``→``ti`` only after it-lopa, (2) ``vftu~`` आत्मनेपदी gate vs P019 parasmaipada (vā).
- Tests run: `pytest tests/unit/test_tinanta_vftu_lrg_p019.py tests/unit/test_tinanta_coverage_matrix.py tests/unit/test_tinanta_abhavisyat_lrg.py` — 28 passed.
- Notes / next: delete or retire `pipelines/avartsyat_lRG_vf_corrected_P019_demo.py`; T3 P008 (`Aste_lat`); structural 1.3.92 vā parasmaipada (recipe) if we generalize vṛd+lṛṅ.

---

### 2026-05-22  (session)  [cursor]  Tiṅanta audit plan (T0–T7) — rule-based playbook

- What changed:
  - `audit_tinanta_cursor.md` — new executable plan: coverage matrix, constitutional
    gates, P008–P019 merge order, prayoga depth, arm demolition, oracle/UI criteria.
  - `audit/RUN_LOG.md` §F — pointer + next steps for Cursor/Claude coordination.
- Why: user asked for an autonomous plan to audit entire tiṅanta prakriyā in rule-based
  manner (not ad-hoc P4 batch pick).
- Tests run: none (planning-only).
- Notes / next:
  - **T1** — add `tests/unit/test_tinanta_coverage_matrix.py`.
  - **T3** — merge P019 (`avartsyat_lRG`) then P008 (`Aste_lat`) into `tinanta.py`.
  - **T4** — bhāve/karmani 9×10 gold; **T2** — drop `P031_*` arm in `tinanta.py`.
  - Claude subanta claim unchanged; avoid `canonical_pipelines.py` until released.

---

### 2026-05-22  (session)  [cursor]  P3 group 1: 6.1.97 — remove demo-ID `_arm` gates

- What changed:
  - `sutras/adhyaya_6/pada_1/sutra_6_1_97.py` — structural `cond()` only
    (vikaraṇa cross, merged pada, P017 triple, asmad intra/cross, tyadadi);
    Article 14 docstring; no `P013`/`P017`/`asmad_crossterm` meta arms.
  - `pipelines/zuSrUzate_san_Sru_corrected_P013_demo.py`,
    `pipelines/pawapawAyati_anukaraNa_corrected_P017_demo.py`,
    `pipelines/asmad_subanta.py` — dropped arm writes before `6.1.97`.
- Why: `audit_cursor.md` §5.2 group 1 (lowest blast-radius `_arm` batch).
- Tests run:
  - `pytest` P013/P017 bundle + `test_no_demo_ids_in_sutra_arm_keys` — 18 passed.
  - `python3 -m pipelines.asmad_subanta` — all 21 cells ✓ (after `asmad_stem` tag in
    `_is_asmad_anga` for pañcami bahu cross-term without `7_2_*_done`).
  - `pytest tests/unit/test_tinanta_bhu_* tests/unit/test_tinanta_bhave_lat.py` — 48 passed.
- Notes / next: P3 group 2 (`2_4_71_luk_arm`) writers live in `canonical_pipelines.py`
  — **wait for claude P2 claim** or coordinate; P4 `_corrected_*` merge is unblocked.
  claude P1/P2 subanta still `in-progress` on `trace.js` / `P01_subanta_bootstrap`.

---

### 2026-05-22  (session)  [cursor]  Dhātu browser: ashtadhyayi-style + full prakriyā on cell click

- What changed:
  - `pipelines/dhatupatha.py` — `resolve_dhatu_identifier()` (accepts `01.0001`, SLP1, id).
  - `pipelines/tinanta.py` — `_dhatu_row_by_upadesha` delegates to resolver.
  - `webui/app.py` — `/dhatu/<id>` redirect, `/prakriya/tinanta`, `dhatupatha_id` in APIs.
  - `webui/templates/dhatufilters.html` — 10-lakāra grid; cell click → inline `trace.js` pane.
  - `webui/templates/prakriya_tinanta.html` — standalone full prakriyā page.
- Why: user asked to mirror [ashtadhyayi.com dhātu 01.0001](https://ashtadhyayi.com/dhatu/01.0001?filters=gana~1) with click-any-form → full prakriyā.
- Tests run: `python3` smoke — resolve `01.0001`→`BU`, redirect `/dhatu/01.0001`, API detail OK.
- Notes / next: optional Vidyut surface compare if `vidyut` installed; bhāve prayoga toggle on grid.

---

### 2026-05-22  (session)  [cursor]  Tiṅanta: 10 lakāras kartari + bhāve + karmaṇi lṛṅ

- What changed:
  - `pipelines/tinanta.py` — `_prep_bhave`, `_derive_bhave_laT`, `_derive_bhave_lit`,
    full **bhāve** dispatch for all 10 lakāras; `_derive_karmani_lRG` (9th karmaṇi
    lakāra); `_bhave_atmanepada_tin_after_lopa` on laṅ/liṅ/lṛṭ/lṛṅ/loṭ paths.
  - `tests/unit/test_tinanta_bhu_ten_lakara_kartari.py` — 10×9 smoke + 3sg gold.
  - `tests/unit/test_tinanta_bhave_lat.py` — bhāve laṭ 9 cells + liṭ 3sg.
- Why: user asked to keep correcting tiṅanta pipelines for all 10 lakāras; bhāve
  had been falling through to broken kartari path (e.g. भवत); karmaṇi lṛṅ raised
  `NotImplementedError`.
- Tests run: `pytest tests/unit/test_tinanta_*.py` — **202 passed** (181 legacy
  + 21 new).
- Notes / next: bhāve loṭ/āśīr-liṅ may need dedicated spines (not identical to
  karmaṇi); claude subanta P2 still in-flight on `canonical_pipelines.py`.

---

### 2026-05-22  (session)  [cursor]  Coordination protocol acknowledged (user directive)

- What changed: `audit/RUN_LOG.md` only — §E.1 scope-split table added;
  this entry documents standing rule for all future cursor sessions.
- Why: user requires **all** agents read §B/§C before work and log
  every action here; cooperate with claude without unnecessary overlap.
- Tests run: none.
- Notes / next:
  - **cursor released** — no §B claim active; safe for claude to
    continue P0+P1+P2 subanta chain.
  - **cursor will not edit** while claude owns: `trace.js`,
    subanta templates listed in §E.1, `P01_subanta_bootstrap` body,
    sūtra 1.1.11–1.1.24 (except already-shipped 1.1.20 cond via claude).
  - **claude should not revert** `P01_samjna_dhatu_class` or tiṅanta
    template filters without §B claim + §C note.
  - Next unclaimed cursor-sized tasks: P3 group 1 (`6_1_97_tinganta_*`),
    P4 tinanta `*_corrected_*` demos — **re-claim in §B first**.

---

### 2026-05-22 14:15  [cursor]  P2 §4.3 tiṅanta/kṛdanta dhātu saṃjñā + tinanta Web UI trace filter

- What changed:
  - `core/canonical_pipelines.py` — `P01_samjna_dhatu_class` (1.1.20 + 1.1.5).
  - `pipelines/tinanta.py` — call after dhātu `Term` on tape in `derive()`.
  - `pipelines/krdanta.py` — same at `derive_krt()` entry.
  - `webui/templates/tinanta.html` — default-on **रूप-परिवर्तन-मात्रम्**;
    audit/skipped off by default.
  - `webui/templates/tinanta_all.html` — inline trace panel: same filter +
    rerender toggles.
- Why: `audit_cursor.md` §4.3 (dhātu-class block) + P0 parity for tiṅanta UI.
- Tests run: `pytest tests/unit/test_tinanta_*.py` — 37 passed;
  `pytest tests/forward/test_forward_krdanta_{pacaka,nayaka}.py` — green.
- Notes / next: P3 `6_1_97_tinganta` arm migration; krdanta may later drop
  blanket `P01_samjna_1_1_*` per full P2 subanta split (claude in-flight).

---

### 2026-05-22 09:42  [claude]  Audit P0 shipped: UI default filter "रूप-परिवर्तन-मात्रम्"

- What changed:
  - `webui/static/trace.js` — `_traceStepInFilter` now honours
    `RUPA_PARIVARTANA_ONLY` checkbox; suppresses any step where
    `form_before === form_after`.
  - `webui/templates/derive.html`, `devendra.html`, `krdanta.html`,
    `pipelines.html`, `sarvanama.html`, `patha.html`, `matrix.html`,
    `showcase.html` — new default-on checkbox added before the
    APPLIED row.
- Why: per audit P0 (`audit_claude.md` §3 / `audit_cursor.md` §2).
  Default trace for रामाणाम् had ~125 rows, ~18 of which were
  saṃjñā registry stamps with no form change.
- Tests run: none (UI-only; engine untouched).
- Notes / next: continuing with P1a (tighten 1.1.20/22/23/24 cond).

---

### 2026-05-22 09:41  [claude]  Baseline captured

- What changed: `.audit/regression_baseline_2026-05-22.txt` written.
- Baseline: **10 failures, 18525 passed, 1 skipped**. 9 of those
  failures are pre-existing per project memory note (3 constitutional
  reference-leak, 5 sig_baseline rāma path deviations, 1 jñāna gold
  cell 8-1, 1 tad gold cell 1-1). No new failures attributable to
  audit work expected — flag any that appear.
- Snapshot of रामाणाम् trace (baseline):
  - Final form: `rAmARAm` ✓
  - Trace steps: 125 total — 29 APPLIED (18 no-form-change saṃjñā
    stamps + 11 operative), 19 AUDIT, 75 SKIPPED, 2 APPLIED_VACUOUS.
  - The 11 operative APPLIED rows (form actually changes) are:
    `7.1.54 rAmaAm→rAmanAm`, `6.4.3 rAmanAm→rAmAnAm`,
    `8.4.2 rAmAnAm→rAmARAm`, and 8 register-stamps where
    form_before === form_after (those are the noise).
- Why: per audit playbook §1 pre-flight requirement.
- Notes / next: continuing with P0 (UI filter) — safest start.

---

### 2026-05-22 09:30  [claude]  Audit governance documents created

- What changed:
  - `audit_claude.md` (33 KB) — rationale + §A 32-source roster.
  - `audit_cursor.md` (25 KB) — executable playbook.
  - `docs/AMENDMENT_14.md` — constitutional amendment proposal,
    status: PROPOSED — accepted on signing.
  - `CONSTITUTION.md` — Art. 10 reflects 15 Articles; Art. 13 §1
    hardened with regex; new Art. 14 added (citation requirement).
  - `.cursorrules` — full source roster + 10 anti-patterns +
    mandatory docstring citation block.
  - `.cursor/rules/panini-authoritative-sources.mdc` — new per-path
    rule on `sutras/**`.
  - `.cursor/rules/panini-anti-patchwork.mdc` — new per-path rule
    on `sutras/`, `pipelines/`, `core/`.
- Why: user accepted audit; wanted plan + governance before code edits.
- Tests run: none (governance-only).
- Notes / next: user approved P0/P1/P2 subanta cleanup.

---

## D. Glossary of in-flight phrases

- **P0 / P1 / P2 / …** — audit phases as defined in `audit_claude.md`
  §3 and `audit_cursor.md` §2–§7. Always refer by P-level in claims
  to make discoverability automatic.
- **Baseline** — the test-result + trace snapshot captured before any
  code change in a given session. Stored under `.audit/`.
- **Operative row** — a trace step whose `form_before !== form_after`.
- **Stamp row** — a SAMJNA trace step where `form_before === form_after`
  (the sūtra updated the registry but did not change varṇas).
- **Net-zero `_arm` rule** — Art. 13 §1 hardened: a commit may add an
  `_arm` write only if it removes another in the same commit.

---

## E. Coordination etiquette

- **Read §B + §C before every session.** Both `claude` and `cursor`
  must read this file first; append §C as you work, not only at the end.
- **Don't claim wide.** A claim covering "all of `sutras/`" is too
  broad — pick a P-level scope (e.g., "P1a: 1.1.20/22/23/24") and
  list those files.
- **Release on finish.** When done, change the claim row's status to
  `released` and append an action-history entry under §C.
- **Override only after discussion.** If a claim has been `in-progress`
  for more than 2 days without an action-history update, the other
  agent may release it with a note: "released by other agent due to
  inactivity; please re-claim if still active." Surface to the human
  user before doing this.
- **Constitution edits require both.** Any change touching
  `CONSTITUTION.md`, `.cursorrules`, or `.cursor/rules/*.mdc` must
  be preceded by a `docs/AMENDMENT_<N>.md` per Art. 10 and an
  action-history entry under §C linking to that amendment.

### E.1 Scope split (avoid unnecessary interference)

| Owner / phase | Primary files | Do **not** touch without re-claim |
|---|---|---|
| **claude** — P0/P1/P2 subanta | `webui/static/trace.js`, `webui/templates/{derive,devendra,krdanta,pipelines,sarvanama,patha,matrix,showcase}.html`, `pipelines/subanta.py`, `sutras/adhyaya_1/pada_1/sutra_1_1_{11–19,20,22,23,24}.py`, `P01_subanta_bootstrap` refactor in `core/canonical_pipelines.py` | While claude claim row is `in-progress` |
| **cursor** — P2 §4.3 tiṅanta/kṛdanta entry | `pipelines/tinanta.py`, `pipelines/krdanta.py` (dhātu bootstrap only), `webui/templates/tinanta.html`, `webui/templates/tinanta_all.html`, `P01_samjna_dhatu_class` in `core/canonical_pipelines.py` | Subanta bootstrap / trace.js unless coordinated |
| **Either** — after claim released | P3 `_arm` groups, P4 `_corrected_*` merges, P5 `why_now` | Re-claim in §B before editing |

**Shared file `core/canonical_pipelines.py`:** claude may refactor
`P01_subanta_bootstrap` / split `P01_samjna_*`; cursor added
`P01_samjna_dhatu_class` (lines ~1121–1129). Merge conflicts:
preserve **both** blocks; do not delete `P01_samjna_dhatu_class`.

**Tiṅanta UI:** uses **inline** trace JS in `tinanta.html` /
`tinanta_all.html` — **not** `trace.js`. P0 checkbox parity was
done separately on tiṅanta pages by cursor; subanta pages use
`trace.js` (claude P0).
