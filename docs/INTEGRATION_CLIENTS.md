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
| S2 | `~/sanskrit_learning/lessons/NN.json` per pāṭha: शब्द lists, वाक्य pairs, paradigm tables, page refs — rule-based extraction | every item points to its page | |
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
| `POST /v1/tinanta` `{dhatu, lakara, prayoga, purusha, vacana}` | verify a verbal reading (`purusha` 3 = prathama) |
| `POST /v1/reviews` | "report wrong derivation" (P3) |
| `POST /v1/analyze` | word / text analysis (P2, not built yet) |
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
| P2 | `POST /v1/analyze` in `core/analyze.py`: candidates from `forms.db` + Vidyut, forward-verified; statuses *engine-verified* / *oracle-only* / *unknown*. Subhastini's colour padaccheda calls it; Vidyut then lives only in the engine `.venv` | next |
| P3 | `tools/corpus_gaps.py` / `make corpus-gaps`: frequency-ranked gaps over Subhastini's library; "report wrong" → `/v1/reviews`; coverage over a fixed text set (Gītā first) | |
| P4 | tutor `/ask` with page citations; paradigm questions routed to the engine; every Devanāgarī word in an answer checked by `/v1/analyze`; stronger local model; Subhastini "Ask the book" panel | |
| P5 | sandhi splits accepted only when the engine re-joins them; until then labelled oracle-only | |
