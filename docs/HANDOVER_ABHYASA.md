# Handover for Claude — अभ्यास tab, search, व्युत्पत्ति (cursor, 2026-11-13)

Read this before touching `/practice` or any `abhyasa` file. Full plan, parity table and gap list: `docs/ABHYASA_PLAN.md`.

## What the owner asked
1. Make **sanskritabhyas.in** (main reference) + the RKMVU abhyāsa available in our **अभ्यास** tab, beginner → grammarian,
   backed by our engine + Vidyut + our other data.
2. A **search box**: shabdarūpa of *any* word (even outside the lists, e.g. गार्गी) and **how it is made**, back to the
   dhātu, using the kośa base in `~/subhastini` — "kośas propose, rules verify".
3. Launch from **`Panini Engine.command`** (double-click opens http://127.0.0.1:5050/practice).

## Source order (owner, 2026-11-13 21:16)
**Our engine first, Vidyut second, kośa (printed ashtadhyayi.com paradigm / Subhastini kośas) third.** Every form shows
its source badges in that order (यन्त्रम् · विद्युत् · कोशः); anything without यन्त्रम् carries "यन्त्रं न्यूनम्".

## Pages (hash routes on /practice — mirror sanskritabhyas.in)
`#abhyasa/<family>` drills · `#list/{noun,verb,krdanta,taddhita,pronoun,number}` · `#word/<stem>/<liṅga>` ·
`#dhatu/<pāṭha id>[/<prayoga>/<pada>/<lakāra>]` · `#krdanta/<id>` · `#taddhita/<pratyaya>` · `#namadhatu/<stem>/<pratyaya>` ·
`#search/<word>[/<liṅga>]` · `#fav` · `#requested` · `#compare` · `#pratyaya/{sup,tin,krt,taddhita}` · `#lipi`.
New API: `/api/abhyasa/{dhatu/<id>, krdanta_view, krt_table/<k>, taddhita_page/<p>, taddhita_names, taddhita_view,
pronoun_list, number_list, tin_page, similar, namadhatu_view}`; data `data/practice/sankhya.json`.

## Prakriyā visuals (owner, 2026-11-14) — `webui/static/prakriya.js` (+ `style.css` `.pk-r-*`, `.pk-v`, `.pk-del/.pk-ins`)
Every derivation view (prakriyā page, शब्दरूप / धातुरूप tabs, अभ्यास explanations) now shows, per step:
parts coloured by role from the trace's `parts` (धातुः, प्रकृतिः, अभ्यासः, विकरणम्, आगमः, प्रत्ययः/सुप्/तिङ्, उपसर्गः), the changed part
bold-underlined; **click a form** (or the "वर्णाः" switch) to toggle संहितम् राम ↔ विभक्तम् र् आ म् अ, where the स्थानी is struck
(red dashed) and new varṇas boxed (green), with a note "अ ⇒ आ स्थानी → आदेशः / + न् आगमः / + भ् ऊ द्वित्वम् (अभ्यासः) / … ⇒ ∅ लोपः";
saṃjñā steps get a chip "संज्ञा: अङ्गम् ⇐ राम" (map `SAMJNA` in prakriya.js, display only). The varṇa diff is an LCS whose
ties put insertions first. Display only — the engine's trace is not changed. Not yet: `docs/learn.html` has its own stepper.

## Rule for every answer (do not break)
The answer is **our engine's form**, accepted when Vidyut and/or the printed ashtadhyayi.com paradigm agree. Where the
engine cannot derive yet (yaṅ/yaṅluk/sanādi stacks, nāmadhātu, unbanked kṛts) the drill shows Vidyut's form **badged
"यन्त्रं न्यूनम्"**. Disagreements are never taught; they go to `data/practice/abhyasa_gaps.json`. No engine file was
changed; nothing here may be imported by `engine/ sutras/ phonology/ pipelines/` (test enforces it).

## Files (all new unless noted)
| File | Role |
|---|---|
| `core/abhyasa.py` | Question engine: 12 families (noun, pronoun, number, verb, kṛdanta, taddhita, nāmadhātu, sandhi, varṇa/lipi, pratyāhāra, it, vākya) × drills (mcq, recall, match, tf, odd, table, sutra, compose, kāraka); levels आसान/मध्यम/कठिन/वैयाकरण; filters as sanskritabhyas; `search()`, `guess_linga()`, `lists()`, `grade_compose()`. Live paradigms are cached; verbs read verified tables first (`verified_tin`) and give live derivation a 10 s budget. |
| `core/vyutpatti.py` | व्युत्पत्ति: parse kośa entries (sūtra numbers, quoted sūtra texts, `base+pratyaya` formulas, dhātu+artha) from `$PANINI_LEXDB` (default `~/subhastini/lexicon/lex.db`, read-only); verify with Vidyut, Kāśikā udāharaṇas (`docs/data/sutras.json`), uṇādi examples; show engine status per sūtra (`sig/sutra_class.json`); `engine_check()` re-derives with our engine; recurse to the dhātu. |
| `tools/abhyasa_vidyut.py` | Vidyut worker (runs under `.venv`): grids with sanādi/upasarga, kṛt, taddhita, nāmadhātu, steps, sandhi split-back, lipi, `names`, `taddhita_reverse`, `krt_reverse`. |
| `tools/build_abhyasa_bank.py` | Builds `data/practice/abhyasa_bank.json` (slow families: kṛdanta, taddhita, sandhi, vākya…) + gap queue. `.venv/bin/python -m tools.build_abhyasa_bank [--only fam,…]`, ~2 h. |
| `data/practice/vakya_lexicon.json` | Our own lexicon (29 nouns, 18 verbs, 9 sentence lessons, kāraka→vibhakti teaching table with sūtras). |
| `webui/abhyasa.py` | Flask blueprint `/api/abhyasa/*`: catalog, question, paradigm, list, grade, explain, search, vyutpatti, vyutpatti/engine, lipi, gaps. Registered by 2 lines in `webui/app.py` (after `/practice`). |
| `webui/templates/practice.html` (rewritten), `webui/static/abhyasa.js` | The tab: search bar, family tabs, views अभ्यास · सूचियाँ · तुलना · पसंदीदा · प्रत्यय, options panel, source badges, "प्रक्रिया" (shared `prakriya.js`), font size, hi/en/sa labels. |
| `Panini Engine.command` (edited) | Double-click → अभ्यास; `home` arg → old hub; menu `p` open अभ्यास, `b` rebuild bank. |
| `tests/unit/test_abhyasa.py`, `tests/unit/test_vyutpatti.py` | Parity, answer-key rule, engine-contract (entry-point signatures), firewall, bank invariants, kośa parsing. |

## Engine contract the drills rely on (rename → `test_abhyasa.py` fails)
`pipelines.subanta.derive`, `pipelines.tinanta.derive(…, upasargas, pada, san_recipe, nic_recipe)`,
`pipelines.krdanta.derive_krdanta / build_dhatu_state`, `pipelines.taddhita_loop.derive_taddhita`,
`pipelines.pada_samhita.join`, `pipelines.it_prakarana.run_it_prakarana`, `phonology.pratyahara.build_pratyahara`,
`pipelines.asmad_subanta.derive_asmad/derive_yuzmad`, term tag `origin_pratyaya:<upadeśa>`.

## Engine gaps found for you (details: ABHYASA_PLAN §6, §8; queue: `data/practice/abhyasa_gaps.json`, 602 cells)
- **4.1.16 यञश्च unexercised** → गार्गी comes out *गार्ग्या* (Kāśikā: गार्गी via 4.1.105 → 4.1.16 → 6.4.150).
- `subanta.derive("asmad"/"yuzmad")` wrong beyond 1/1 (the tab uses `pipelines.asmad_subanta` instead).
- mahA + fzi → *mahazi* (1.1.51 raparatva across padas); hase~ lṛṭ *hatizyati*; qudAY vidhiliṅ *dadAyAt*.
- kṛt avyayas declined (*gatvAH*: 1.1.40 + 2.4.82); Śatṛ/tṛc vivakṣā gives the bare root; matup / ḍhak senses.
- Speed: adādi `tinanta.derive` ~5 s/cell (ada~ laṭ 47 s). Homograph upadeśas resolve to the first row.

## State of git
All of it is on `main` (33e42236 + merge d390c2b0, then the sanskritabhyas-pages commit of 2026-11-13 night).

## How to check quickly
`python3 -m pytest tests/unit/test_abhyasa.py tests/unit/test_vyutpatti.py tests/unit/test_webui_routes.py -q`
then open `/practice`, search **गार्गी**: table (engine ✓ Vidyut ✓) and the tree गॄ + ग → गर्ग + यञ् + ङीप् → गार्गी.

## Next (open)
Multiple upasargas/gati; all-lakāra comparison page; more UI languages; vākya lessons 10–12 (ktvā/tumun, participles,
kta) after the kṛt gaps close; re-run the bank after engine fixes so fixed cells leave the gap queue.
