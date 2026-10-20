# Integration clients — Subhastini and sanskrit_learning

Plan of record (2026-10-20) for using this engine, with Vidyut as its oracle, from two
local applications. The engine stays a separate service; nothing here changes `engine/`,
`sutras/`, `phonology/` or `pipelines/`.

## Roles

| project | role | authority |
|---|---|---|
| `~/panini_engine_v3` — `make api`, :8000 | derivation, analysis (Art. 17), gaps (Art. 18), Vidyut oracle (Art. 19) | the only grammar authority |
| `~/subhastini` — `Start Subhastini.command` | **front door**: reading, writing, library, notes, translation | text provenance (its `RULES.md`) |
| `~/sanskrit_learning` | *Sanskrit Swayam Shikshak* — source of book lessons for sentence practice (AI tutor retired 2026-10-20) | the book, once proofread; local only (in copyright to 2029) |
| Ollama :11434 | shared by Subhastini translation and the tutor | — |

Dependencies point one way: clients call the engine; the engine imports neither client.
A client degrades gracefully when the engine is down.

## Constitutional boundaries

- **Art. 17.** A word is *analysed* only when the forward engine reproduces the surface
  exactly. Vidyut's kosha and Chedaka only propose candidates.
- **Art. 18.** A word the engine cannot derive is shown as a gap with the engine's reason —
  never hidden, never guessed.
- **Art. 19.** Engine ≠ Vidyut is a work item, not a verdict.
- **Art. 6.** Subhastini's `library/` (ODbL) never enters `data/inputs/`. Only `tools/` and
  `bench/` may read it, by path, read-only.
- The `/reader` in `webui/` (Prasthānatrayī bhāṣya) stays here and is exposed to
  Subhastini as a commentary source over the API; Subhastini does not grow a second reader.

## One place for the literature (2026-10-20, owner: "all Sanskrit literature in one place")

Subhastini is where everything is read. Texts stay where they live and are read live:

| source | lives in | reaches Subhastini through |
|---|---|---|
| Subhastini library (Gītā, itihāsa, purāṇa, Veda, kāvya, Manusmṛti, Arthaśāstra …) | `~/subhastini/library/` | itself |
| Advaita Sharada — 28 works with bhāṣya + ṭīkā (local reading copy, "All rights reserved") | engine `data/reference/advaita_sharada/raw/` | `/v1/library` (`as:`), loopback only |
| Saṃsādhanī e-readers (10, engine-verified words) | engine `data/reference/samsaadhanii/raw/` | `/v1/library` (`scl:`) + `/reader` links |
| ashtadhyayi.com granthas — Aṣṭādhyāyī with 16 vṛttis, Kaumudīs, Mahābhāṣya, Vākyapadīya, PŚ, Bhūṣaṇasāra, Mañjūṣā, Liṅgānuśāsana, Uṇādi, Śikṣā, Tarkasaṅgraha | `~/data-master` | `/v1/library` (`ac:`) |
| *Sanskrit Swayam Shikshak* | `~/sanskrit_learning` | (book lessons → sentence practice, phases S2–S5 below) |

## Sentence practice without AI (2026-10-20, owner: "the book with local AI is a bad idea")

Subhastini **वाक्याभ्यासः** (`#/abhyasa`). The text is the answer key; the engine checks every form; nothing is generated.

| phase | deliverable | check | status |
|---|---|---|---|
| S1 | drills on Saṃsādhanī "1000 Sentences": build from glosses, fill the form, kāraka, order, meaning; Leitner review | exact match; a blank only for an engine-derived word; kāraka from SCL tag + 1.4.x / 2.3.x | done |
| S2 | `~/sanskrit_learning/lessons/NN.json` per pāṭha: शब्द lists, वाक्य pairs, paradigm tables, page refs — rule-based extraction (`extract_lessons.py`): 91 lessons (60 drill, 31 reading passages not yet itemised) · 1,367 words · 1,314 sentences · 66 tables (raw lines) | every item points to its page | done 2026-10-20 |
| S3 | proofreading screen: sentence beside the page image; words neither the engine nor the koshas know are flagged | only proofread items are drilled | |
| S4 | the book's lessons in its order + vocabulary flashcards | as S1 | |
| S5 | transformation drills (tense / person / number, न, किम्) — the engine derives the target form | exact match to the engine's form | |

Book material stays local and out of git (Sātavalekar d. 1968 — in copyright in India until 2029).
API: `GET /v1/practice/sentences` (sets, quiz roles) · `/v1/practice/sentences/{set}` · `/v1/practice/sentences/{set}/{id}`
(each word: form, written-out tag, gloss, role → head with sūtras, engine verdict).

Nothing is copied between repos. A new source is a provider class in `tools/library_providers.py`
(`works / sections / section / item / search`) — Subhastini needs no change to list it.
`Start Subhastini.command` starts the engine API and the engine web UI when they are not running.

## API contract used by clients

| call | used for |
|---|---|
| `GET /v1/health` | launcher and client liveness |
| `POST /v1/subanta` `{stem, vibhakti 1–8, vacana 1–3, linga}` | verify a nominal reading |
| `POST /v1/tinanta` `{dhatu, lakara, prayoga, purusha, vacana}` | verify a verbal reading (`purusha` 3 = prathama). A bare upadeśa shared by several dhātus derives the first in pāṭha order and returns `homographs` (each with its form); pass a pāṭha id (`02.0070`) to choose |
| `POST /v1/reviews` | "Report wrong derivation" from Subhastini's derivation panel |
| `POST /v1/analyze` `{text, steps?}` | word / line / verse → per word `verified` · `split` · `avyaya` · `oracle_only` · `unknown`, readings with verdicts; `steps` attaches the forward derivations (core/analyze) |
| `GET /v1/library` · `/v1/library/search?q=` | catalogue of every work the engine holds · search across them |
| `GET /v1/library/works/{work}[/{section}[/{item}]]` | sections · items (text + commentary titles) · one item with passages and commentaries; `as:` works answer loopback clients only (403 otherwise) |

Vidyut → engine mapping: dhātu `aupadeshika` with svara marks (`\`, `^`) removed is the
engine upadeśa (`ga\mx~` → `gamx~`); `la~w`→`laT`, `viDili~N`→`liG`, `ASIrli~N`→`AsIrliG`
…; `puM/strI/napuMsaka` → `pulliṅga/strīliṅga/napuṃsaka`; `samboDanam` → vibhakti 8.

## Phases

| phase | deliverable | status |
|---|---|---|
| P0 | `git init` sanskrit_learning; Subhastini launcher starts the engine API; this contract | done 2026-10-20 |
| P1 | Subhastini "how is this derived?" — Vidyut proposes, engine verifies via existing endpoints | done 2026-10-20 |
| P2 | `POST /v1/analyze` (`core/analyze.py`): form index + Vidyut kosha (`bench/oracle_kosha`, engine `.venv/vidyut-data`) propose, every reading re-derived (any vibhāṣā branch); homograph dhātus resolved by gaṇa + artha; written ं for final म् accepted by name (8.3.23). Subhastini's colour padaccheda and "How is it derived?" call it | done 2026-10-20 |
| P3 | `make corpus-gaps` (`tools/corpus_gaps.py` → `.audit/corpus_gaps.json`): token-weighted statuses + gap clusters over Subhastini's classical texts (epics stay with DCS); "Report wrong derivation" → `/v1/reviews` | done 2026-10-20 |
| P4 | ~~AI tutor~~ — retired by the owner; replaced by **S2** (`~/sanskrit_learning/extract_lessons.py`, see the sentence-practice table) | S2 done 2026-10-20 |
| P5 | `pipelines/pada_samhita.join`: two padas, 6.1.72, the resolver picks among the 6.1 ac-sandhi sūtras. Chedaka (`bench/oracle_cheda`) proposes splits of unread words; status `split` only when every part is engine-derived and the engine re-joins them. Visarga / consonant seams are named gaps | vowel seams done 2026-10-20 |

**Measured (2026-10-20, `make corpus-gaps`, 2,000 most frequent words = 77,792 of 206,345 tokens of Gītā, Bhāgavata,
Manusmṛti, Arthaśāstra and the kāvya/nīti works):** verified 82.3 % · avyaya 7.3 % · oracle-only 4.1 % · unknown 6.3 %
(before P5 splits). Top clusters: kṛt absolutives (दृष्ट्वा, निशम्य: 1,501 tokens), ṇic in liṅ (कारयेत्), स्त्रियः / पुंसः, नृणाम्,
liṭ abhyāsa (ददर्श) — the same clusters the DCS benchmark ranks.

## Engine findings from real use (work items, Art. 19)

1. **Homograph dhātus.** `dhatupatha_upadesha.json` drops svara, so 319 upadeśa spellings name 717 of 2,240 rows
   (98 within one gaṇa, e.g. कदिँ 01.0073 P / 01.0878 Ā; शासुँ 02.0012 Ā / 02.0070 P). Fixed at the edges: `/v1/tinanta`
   lists `homographs`, `core/analyze` resolves by gaṇa + artha. Not fixed: `pipelines/tinanta._dhatu_row_by_upadesha`
   still takes the first row for a bare upadeśa (hotspot — coordinator); the real fix is svara-marked upadeśas.
2. **ādhṛṣīya optional ṇic (gaṇasūtra आ धृषाद्वा).** ashtadhyayi.com dhātu data tags 183 curādi rows `णिज्विकल्पः`
   (50 in the आधृषीयः antargaṇa); e.g. 10.0382 भू प्राप्तौ, pada A — Deva (dhāturūpanandinī note): "प्राप्तौ णिचि भावयते
   तङि । भवते शपि". The engine derives only the ṇic branch (अभावयत); the śap branch (अभवत) is missing (curādi spine in
   `pipelines/tinanta.py` — coordinator). Vidyut's अभवत् for this row is parasmaipada for an ātmanepadī root — its own
   work item.
3. **Neuter sambuddhi (हे वारे / हे वारि).** Kāśikā 7.1.73 (brain card C-650): the ac-grahaṇa is a jñāpaka that 1.1.63 na
   lumatāṅgasya is anitya, so after 7.1.23 luk the sambuddhi guṇa (7.3.108) is optional. The engine applies 7.3.108
   unconditionally (never consults 1.1.63 there), so only हे वारे-type forms are derived. Needs an owner ruling on how an
   anitya paribhāṣā is represented (Art. 22) before any sūtra changes.
