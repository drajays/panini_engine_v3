# Integration clients — Subhastini and sanskrit_learning

Plan of record (2026-10-20) for using this engine, with Vidyut as its oracle, from two
local applications. The engine stays a separate service; nothing here changes `engine/`,
`sutras/`, `phonology/` or `pipelines/`.

## Roles

| project | role | authority |
|---|---|---|
| `~/panini_engine_v3` — `make api`, :8000 | derivation, analysis (Art. 17), gaps (Art. 18), Vidyut oracle (Art. 19) | the only grammar authority |
| `~/subhastini` — `Start Subhastini.command` | **front door**: reading, writing, library, notes, translation | text provenance (its `RULES.md`) |
| `~/sanskrit_learning` — tutor, :8100 (P4) | book-grounded concept answers (*Sanskrit Swayam Shikshak*) | machine output, labelled; never a source |
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
- The `/reader` in `webui/` (Prasthānatrayī bhāṣya) stays here and is later exposed to
  Subhastini as a commentary source over the API; Subhastini does not grow a second reader.

## API contract used by clients

| call | used for |
|---|---|
| `GET /v1/health` | launcher and client liveness |
| `POST /v1/subanta` `{stem, vibhakti 1–8, vacana 1–3, linga}` | verify a nominal reading |
| `POST /v1/tinanta` `{dhatu, lakara, prayoga, purusha, vacana}` | verify a verbal reading (`purusha` 3 = prathama) |
| `POST /v1/reviews` | "report wrong derivation" (P3) |
| `POST /v1/analyze` | word / text analysis (P2, not built yet) |

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
