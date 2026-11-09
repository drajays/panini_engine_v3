# Web UI plan — one site for learning vyākaraṇa (students and scholars)

Status: **draft, 2026-11-09** (cursor). Nothing below is built yet.
Owner decisions recorded in §2. Coordination note in §8 — read it before starting any phase.

## 1. Goal

One local site where:

- a **student** learns Pāṇinian grammar topic by topic, sees each word built one sūtra at a time, and practises with drills
  the engine checks;
- a **scholar** looks up any sūtra or any form and sees the full śāstrīya derivation: every rule checked, why the winning
  sūtra won, anuvṛtti, citations.

Old, duplicated and single-word demo pages are removed. The engine itself is not touched: this is display work only.

## 2. Owner decisions (2026-11-09)

| Question | Decision |
|---|---|
| Two servers (Flask :5050, FastAPI :8000) | **Flask serves every HTML page.** FastAPI stays a JSON API (Subhastini and other clients depend on `/v1/*`). |
| Engine `/reader` vs Subhastini | **Keep `/reader`** in the engine UI; it absorbs `/bhatti`, `/patha`, `/text`. |
| Explanation language | **Sanskrit terms, with switchable Hindi / English glosses.** |
| Demo pipelines behind `/devendra`, `/dik`, `/bhatti` | **Remove the pages only.** Retiring `pipelines/devendra.py`, `pipelines/dik_*.py`, `pipelines/bhattikavya_1_1.py` (and their tests) is a separate engine task. |
| First slice | **Phases 1–2** (route smoke tests, then removals and merges). |

## 3. What exists today

**Flask, `webui/` (port 5050, `run_web.sh`)** — 19 pages and 5 redirect stubs:

`/` home · `/shabdarupa` · `/dhaturupa` · `/reader` · `/derive` · `/matrix` · `/krdanta` · `/sarvanama` · `/devendra` ·
`/dik` · `/showcase` · `/patha` · `/text` · `/bhatti` · `/pipelines` · `/sutras` · `/sutra/<id>` · `/sig` · `/tests`.
Stubs that only redirect to `/dhaturupa`: `/tinanta`, `/tinanta/all`, `/dhatufilters`, `/prakriya/tinanta`, `/dhatupatha`.

**FastAPI, `api/` (port 8000, `make api`)** — 6 HTML pages beside the `/v1/*` JSON API:
`/` (`hub.html`) · `/practice` · `/lab` · `/shabda` · `/review` · `/coverage`; plus `docs/` mounted at `/pages`
(`docs/learn.html`, the step-by-step stepper with equation bar and predict-the-next-sūtra quiz).

**Problems**

1. **Duplication.** Noun forms appear on six pages (`/derive`, `/matrix`, `/showcase`, `/sarvanama`, `/shabdarupa`,
   `/shabda`, and partly `/lab`). Text analysis is split over `/patha`, `/text`, `/reader`.
2. **Two sites, hard-coded cross links.** `base.html` links to `http://127.0.0.1:8000/`; `api/hub.html` links to
   `http://127.0.0.1:5050/...` (including the stub `/tinanta`).
3. **Single-word demos presented as features.** `/devendra` (देवेन्द्रः, सूर्योदयः), `/dik` (two dik presets), `/bhatti`
   (eight fixed words), `/showcase` (fixed stems).
4. **Stale text.** `/shabdarupa` says "Our engine has no general taddhita derivation yet" — untrue since the taddhita loop
   (T1–T11, handover). `/krdanta` (May 2026) predates the kṛdanta spine behind `/v1/krdanta` (K1–K9).
5. **At least four separate trace renderers.** `webui/static/trace.js` (10 templates), inline step rendering in
   `shabdarupa.html` / `dhaturupa.html`, the `docs/learn.html` stepper, and per-page code in `api/*.html`.
   The same derivation looks different on every page.
6. **The best teaching page is hidden.** `docs/learn.html` is reachable only at `:8000/pages/learn.html`.
7. **Developer tools sit in the student menu** (`/pipelines`, `/sig`, `/tests`).
8. **Not offline.** `api/*.html` and `docs/learn.html` load Google Fonts, yet the launcher promises offline use.
9. **No UI tests.** No test under `tests/` requests a `webui` route, so a removal can break a page silently.

## 4. Target site

One Flask site, seven sections. Top menu in Devanāgarī with a small English/Hindi subtitle.

| Section | For | Built from | Contents |
|---|---|---|---|
| **पाठः** (Learn) `/learn` | students | `docs/learn.html` | Lessons by prakaraṇa: saṃjñā → sandhi → subanta → tiṅanta → kṛt → taddhita → samāsa. Each lesson: short concept card, worked derivations in the stepper, predict-the-next-sūtra quiz. |
| **अभ्यासः** (Practice) `/practice` | students | `api/practice.html`, `/v1/practice/*` | Fill a paradigm cell · name the sūtra · Saṃsādhanī sentence drills. Every answer checked against an engine-derived form. |
| **रूपाणि** (Forms) `/forms/shabda`, `/forms/dhatu` | both | `/shabdarupa`, `/dhaturupa` | Full declension / conjugation tables; any cell opens its derivation. Kṛdanta and taddhita tabs. |
| **प्रक्रिया** (Derive) `/derive` | both | `/derive`, `/v1/analyze` | One box: type a word (analysis → every reading re-derived) or choose stem + features. |
| **सूत्राणि** (Sūtras) `/sutras`, `/sutra/<id>` | scholars | `/sutras`, `docs/data/sutras.json` | Pāṭha, padaccheda, anuvṛtti, adhikāra scope, Kāśikā udāharaṇa, forms where the engine applies it, implementation status (real / placeholder). |
| **ग्रन्थाः** (Reader) `/reader` | both | `/reader` | Unchanged core; absorbs `/bhatti`, `/patha`, `/text`. |
| **यन्त्रशाला** (Workshop) `/dev/...` | developers | `/pipelines`, `/sig`, `/tests`, `/coverage`, `/review` | Separate link in the footer, not in the student menu. |

### 4.1 One derivation view

A single component (`webui/static/trace.js`, extended) used on every page:

- **Student / Scholar switch** (remembered in `localStorage`).
  - Student: only form-changing steps (`APPLIED`), the equation bar (भव् + अ + ति with upadeśa under each part), a one-line
    explanation in the chosen gloss language.
  - Scholar: also `AUDIT`, `APPLIED_VACUOUS`, `BLOCKED` rows (Art. 8 §2: hidden by default is not missing); the rival
    sūtras and why this one won (para / nitya / antaraṅga / apavāda, from the resolver's trace data); anuvṛtti expanded;
    source citations.
- **Lipi**: Devanāgarī / SLP1 / IAST everywhere (`lipi.js` already does this for traces).
- **Permalinks** per derivation and per step (`#step-N`), so a teacher can cite "step 7".
- **Print / export** of a derivation as a clean page.

### 4.2 Gloss languages

Sanskrit technical terms are never translated away. Hindi and English glosses are added beside them, switchable.
Glosses live in one data file under `webui/static/` (display data), not in templates.

## 5. Phases

Each phase ends green on `make full-check` and its own tests, and is released in `audit/RUN_LOG.md` + `handover.md`.

### Phase 1 — safety net

- `tests/unit/test_webui_routes.py`: every kept page returns 200 through Flask's test client; every removed URL returns a
  301/302 to its replacement; every `/api/*` route a kept page calls still answers.
- Screenshot the current pages once (for before/after comparison; not committed).

**Done when:** the test passes on the current UI before anything is removed.

### Phase 2 — removals and merges (pages only)

| Remove | Replacement (redirect target) |
|---|---|
| `/matrix`, `/showcase`, `/sarvanama` | `/shabdarupa` (same stem/liṅga query args) |
| `/krdanta` | `/dhaturupa` kṛdanta tab (uses `/v1/krdanta`) |
| `/devendra`, `/dik` | `/derive` (and a note that samāsa returns when the engine derives compounds generally) |
| `/bhatti`, `/patha`, `/text` | `/reader` |
| `/tinanta`, `/tinanta/all`, `/dhatufilters`, `/prakriya/tinanta`, `/dhatupatha` | one legacy-redirect table in `webui/app.py` instead of five functions |
| `api/lab.html`, `api/shabda.html` | `/shabdarupa` |

- Before deleting a page, check whether it does anything the replacement lacks; if so, port it first (likely candidates:
  `/matrix`'s per-cell rule view, `/sarvanama`'s sarvanāma stems in the stem picker).
- Delete the templates and their `/api/...` handlers that nothing else calls (`/api/devendra`, `/api/dik/glass`,
  `/api/sarvanama*`, `/api/matrix*`, `/api/paradigm-presets`, `/api/krdanta`) — only after a grep shows no other caller.
- Fix the stale texts listed in §3.
- Menu: four featured links (Forms ×2, Reader, Sūtras) until the new menu lands in Phase 4.

**Done when:** route test updated and green; no template or handler left without a link to it.

### Phase 3 — one site

- Move `api/practice.html`, `api/review.html`, `api/coverage.html` and `docs/learn.html` into `webui/templates/`
  (extending `base.html`); they keep calling the FastAPI JSON endpoints, or Flask proxies them — decide by checking how
  `/reader` already proxies `/api/subhastini/`.
- `api/main.py`: the HTML routes redirect to the Flask URLs; `/v1/*` unchanged. `api/hub.html` removed.
- `Panini Engine.command`, `run_web.sh`, README: one URL to open.
- Bundle the Devanāgarī/Latin fonts under `webui/static/fonts/`; no external requests.

**Done when:** every page is reachable from one origin; Subhastini's calls to `/v1/*` still pass (`tests/` for the API).

### Phase 4 — home page, menu, one derivation view

- New `home.html`: two entry doors ("I am learning" → पाठः / अभ्यासः; "I am looking something up" → रूपाणि / प्रक्रिया /
  सूत्राणि), plus search box (word or sūtra number).
- New menu in `base.html` (the seven sections of §4).
- Shared derivation view (§4.1) replaces the inline renderers in `shabdarupa.html`, `dhaturupa.html`, `reader.html`
  and the API pages.

### Phase 5 — Learn

- Lesson index by prakaraṇa; each lesson = concept card + 3–6 worked derivations + quiz.
- Lesson order follows the teaching sequence of Pushpa Dixit / Neelesh Bodas (Art. 23); concept cards cite video id +
  timestamp or the Aṣṭādhyāyī text. Lesson order is pedagogy only; engine order stays Aṣṭādhyāyī krama (Art. 3).
- Lesson content in data files (one JSON per lesson), not in templates.

### Phase 6 — Practice

- Paradigm-cell drill (pick stem/dhātu, hide cells, check against the engine).
- Name-the-sūtra drill (decoys = the rules the engine rejected at that step, as `learn.html` already does).
- Sentence drills from `/v1/practice/sentences` (existing).
- Progress kept in `localStorage`; no accounts.

### Phase 7 — Sūtra explorer

- `/sutra/<id>`: pāṭha, padaccheda, samāsa-free reading, anuvṛtti chain (links), adhikāra scope, Kāśikā udāharaṇa and
  pratyudāharaṇa, engine status (real / placeholder / deferred, from `docs/DEFERRED_SUTRAS.md` data), "derivations
  where this sūtra applies" (from recorded traces), neighbouring sūtras.
- `/sutras`: filter by adhyāya/pāda, type (saṃjñā, paribhāṣā, vidhi, niyama, atideśa, adhikāra), status, prakaraṇa.

### Phase 8 — polish

Mobile layout, keyboard navigation, contrast and font sizes for long Devanāgarī reading, print styles, a short
"how to read a derivation" help page.

## 6. Rules this work must keep

- **UI only.** No change to `sutras/`, `engine/`, `phonology/`, `pipelines/`; no change to gold or baselines.
- **Nothing the UI shows feeds a `cond()`** (Art. 2, Art. 6). Display data (glosses, lessons, Kāśikā text from
  `docs/data/sutras.json`) stays under `webui/` or `docs/`.
- **The UI never computes a form itself.** Every form shown is engine output; Vidyut appears only as a labelled
  cross-check (Art. 19).
- **Engine truth stays visible.** Default views may hide `AUDIT` / vacuous rows, but the Scholar switch always reveals
  them (Art. 8 §2).
- Hotspots untouched (`engine/{scheduler,resolver,core_loop,dispatcher}.py`, `pipelines/tinanta.py`, `CONSTITUTION.md`).

## 7. Risks

| Risk | Mitigation |
|---|---|
| A removed page had a feature the replacement lacks | Phase 2 compares each page with its replacement before deletion. |
| External clients bookmark old URLs | Redirect table kept permanently. |
| Subhastini depends on an `api/*.html` page | Grep `~/subhastini` for `:8000/` page URLs before Phase 3. |
| Unifying four trace renderers changes what users see | Phase 4 ships behind the Student/Scholar switch; screenshots from Phase 1 for comparison. |

## 8. Coordination

At the time of writing, claim **`ui-p1-cleanup`** (cursor, in-progress since 2026-11-09 09:46) holds `webui/app.py`,
`docs/UI_PLAN.md`, `README.md`, `run_web.sh`, `Panini Engine.command`, and the working tree has its uncommitted edits to
`webui/templates/base.html` (grouped menu), `webui/static/style.css`, `webui/templates/sutras.html`,
`webui/templates/sig_graph.html`, `api/hub.html`, `api/review.html`, `api/shabda.html`.

This plan does not touch those files until that claim is released or merged with this one. Phases 2–4 overlap it
directly; the grouped menu it adds is a reasonable interim step and Phase 4 replaces it.
