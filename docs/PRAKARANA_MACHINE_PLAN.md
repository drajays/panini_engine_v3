# Prakaraṇa Machine — plan to mold v3 (not rebuild it), wired to the brain

*Written 2026-10-09 with the owner. Law: `CONSTITUTION.md` Art. 23 (AMENDMENT 23). Companion: `ROADMAP.md`, `docs/AMENDMENT_22.md` (lexicon).
Brain: `~/data-master/ashtadhyayi-ai` (read-only reference; never an input to `cond()`/`act()`).*

## 0. Should we start engine coding now?
**Yes for P0–P2 (measure, build the scope data, shadow-run it) — they change no behaviour. No for P3 onward until the cards they
depend on exist.** The brain is *not* finished: the transcripts are indexed and the first charts are encoded, but the concept
cards (key B of Art. 23) and the sūtra-level graph are not written. Each behaviour-changing phase below names the cards it needs.
The engine already works (≈17,000 constitutional tests, 19k+ in the suite, rāma 24/24, Vidyut agreement 81.1 % on the last
`make bench`); the rule is **mold it behind gates, never destroy it**.

## 1. Owner's decisions this plan implements
1. Mold v3; Vidyut stays the **minimum floor** (every sūtra Vidyut fires on a form must also fire here; Vidyut never gives order).
2. Goal: **all applicable sūtras are applied** — checkable, not asserted (P6).
3. The engine becomes **prakaraṇa-wise**: a block of sūtras is entered when its trigger is present (Pāṇini's own adhikāra blocks —
   Art. 23 §6); inside a block, sūtra order + the Art. 21 ladder still decide.
4. The machine of the *Pratyayabheda* slide: states **prātipadika · dhātu · nāmapada · kriyāpada**, edges **sanādi · kṛt · strī ·
   taddhita · sup · vikaraṇa+tiṅ** (loops allowed) → unlimited word generation, each word a glass-box derivation.
5. Authority (Art. 23): Aṣṭādhyāyī data **and** Pushpa Dixit/Neelesh Bodas must agree (concept card with video id + timestamp);
   granthas decide when objective and workable; in doubt Pushpa Dixit; she yields only to pāṭha text or an attested form.

## 2. What the audit found (details: brain `audits/engine_vs_pushpa_notes_1-9.md`)
| id | finding (all read in code) | fix lives in |
|---|---|---|
| W1 | `engine/scheduler.py::enumerate_candidates` scans all ~3,985 registry records every step, then dry-runs survivors | P1–P2 |
| W2 | numeric ranges stand in for blocks: `_MULTI_TERM_RANGES` calls 6.1.1–229 "saṃhitā" (saṃhitā starts 6.1.72); `_PHASE_RANGES`; `_skip_krt_window` | P2 |
| W3 | 6.1.1 dvitva fires on a hard-coded form (`pawat`), `san` only, or a `dvitva_recipe` flag — not one block with five nimittas (liṭ, san, yaṅ, caṅ, ślu) | P5 |
| W4 | 1.4.13 aṅga = one boolean tag, once (`("1.4.13_anga",0)` guard), taddhita cases switched on by pipeline flags; Pushpa: aṅga is **per pratyaya** | P5 |
| W5 | adhyāya 4–5 and 3.4.118+ are outside the loop (`_PHASE_RANGES`); taddhita only via hand pipelines | P3 |
| W6 | recipes (`pipelines/`) and the loop coexist; C4 plan turns recipes into fixtures = moves away from prakaraṇa order | P3–P4 |
| W7 | Art. 2/3 banned "prakaraṇa labels" without distinguishing Pāṇini's adhikāra blocks | **done** (Art. 23 §6) |

## 3. Target architecture
```
            ┌────────── L1 entity machine ───────────┐
 vivakṣā →  │ prātipadika ⇄ dhātu  (sanādi, kṛt)     │ → nāmapada | kriyāpada
            │ loops: strī, taddhita | sanādi          │
            └────────────────┬───────────────────────┘
                             │ each edge = "attach this pratyaya"
                  ┌──────────▼───────────┐
                  │ L2 process machine   │  13 stages (direct ādeśa → it-lopa → āgama → … → ac-sandhi → tripāḍī)
                  └──────────┬───────────┘
                             │ each stage = a scoped block of sūtras (adhikāra heads), never a numeric range
                  ┌──────────▼───────────┐
                  │ L3 block dispatcher  │  eligible = block entered ∧ cond(state); order = sūtra kram + Art. 21 ladder
                  └──────────────────────┘
```
* **L1** is data (`graph/machine_l0_l2.json` in the brain is the seed). A Lexicon entry's `vyutpatti` (AMENDMENT 22) is exactly a
  path through L1 — the two designs are the same design; do not build them twice.
* **L2** stage order is a *hypothesis from the charts* until each box has a card (Aṣṭādhyāyī data + Pushpa/Neelesh).
* **L3** replaces the global scan: `eligible(state) = ⋃ blocks entered by the current stage and tape`. `cond()` stays the final
  judge, so a wrong block can only *hide* a rule — which the shadow run (P1) and the completeness invariant (P6) catch.
* **Glass box:** every step records stage, block, candidate set, winner, losers and the named reason (existing `record_decision`).
* **Vidyut floor:** `knowledge_api.py floor …` gives the minimum set; `check_trace` already compares. Floor ⊆ our fired set.

## 4. Phases (each ends green; no phase starts before its gate)
| P | what | behaviour change? | needs cards | gate (measured, regenerate with one command) |
|---|---|---|---|---|
| P0 | **Baselines + counters.** Record: constitutional/suite pass counts, `make bench` agreement, `tools.loop_vs_recipe subanta|tinanta` totals, SIG baseline; add per-step counters (registry records scanned, `cond` calls, probes). Ratchet file under `docs/ratchet_*`. | no | – | numbers committed; counters visible in `make coverage` |
| P1 | **Scope index from the brain.** *(Step 0 done 2026-10-09: `engine/prakarana.py` + `data/inputs/prakarana_map.json` — all 3,983 sūtras are members of ≥1 of 34 prakaraṇa modules, enforced by `tests/constitutional/test_prakarana_complete.py`; 10 modules are `hyp`, 1 `pending` until their cards exist. Not yet used by the scheduler.)* Generate `data/inputs/adhikara_scope_index.json`: for every sūtra, its governing adhikāra chain (brain `edges rel='adhikara'`, 14,271 edges; `sutras.adhikara`). Test: every sūtra belongs to ≥1 block; head's `adhikara_scope` end matches. **Shadow mode:** scheduler also computes the scoped candidate set and asserts `fired ⊆ scoped`; diffs are logged as Art. 18 gaps. | no | – | 0 firings outside scoped set across the paradigm + gaṇa-1 sweeps (else the index/block is wrong → fix data, not engine) |
| P2 | **Replace range heuristics** (`_MULTI_TERM_RANGES`, `_PRATIPADIKA_REQUIRED_RANGES`, `_skip_krt_window`, `_PHASE_RANGES`) by the scope index, one at a time. | no (parity) | – | every sweep identical to P0 baselines; scanned-per-step drops (target ≥10×) |
| P3 | **L1 driver.** `derive_path([...edge labels...])` over the entity machine; wire existing subanta/tiṅanta/kṛdanta first, then sanādi, strī, taddhita (W5), samāsa, upasarga+dhātu. Generation mode: walk L1 under a depth/size budget. | additive | C-L1 (Pratyayabheda), C-sanadi | each new edge: Kāśikā/attested forms reproduce (Art. 19); no recipe flag read |
| P4 | **L2 stages as scoped blocks**; decision boxes = "is any eligible sūtra of this block applicable?". Pipelines become fixtures (ROADMAP C4). | yes, gated | C-L2-1…13 (one per box) | loop == recipe on the 364 shipped derivations |
| P5 | **Concept fixes**, one card each, failing test first (expected from Kāśikā/attested): W3 dvitva as one prakaraṇa with five nimittas; W4 aṅga per pratyaya; pada/apada; saṃjñā lookup-when-named. Amendment if it touches Art. 2/3/13. | yes | per fix | new test red→green; sweeps ≥ baseline |
| P6 | **Completeness invariant.** At each step compute *all applicable* sūtras; each must be `fired`, `blocked-by <named rule>`, `lost-to <named rule>` (Art. 21 ladder) or an Art. 18 gap. Add the Vidyut-floor test. | no | – | gap list ranked; zero unexplained applicable sūtras on the sweeps |
| P7 | **Breadth** (ROADMAP Phase F) driven by the P6 gap list, prakaraṇa by prakaraṇa, 10–30 sūtras per batch. | yes | as needed | coverage ledger (Art. 16) |

**Rules that bite (unchanged):** one file per sūtra (Art. 7); no `_arm` keys / utsarga narrowing (13/15); no reading of forms, vibhakti,
reference data in `cond` (Art. 2/6); expected forms from Kāśikā/attested/oracle, never model-written (Art. 19); work in a git worktree —
another session commits to `main` (see `handover.md`).

## 5. The brain, and how each phase uses it
| need | where | command |
|---|---|---|
| everything about a sūtra (rule, meaning, ±examples, prakriyā, conflicts) | brain DB | `make brain S=6.1.77` |
| adhikāra scope, anuvṛtti, governing heads | tables `sutras`, `edges` (`adhikara` 14,271 · `anuvrtti` 6,947 · `prakriya_next` 2,808 · `badhya_badhaka_pair` 111 · `v3_apavada_of` 119 · `uses_term`/`defines` saṃjñā links) | `knowledge_api.py graph <id> adhikara 2`, `path A B` |
| conflict evidence per Art. 22/23 | brain | `make resolve S=…` |
| Vidyut minimum floor for a form | brain | `knowledge_api.py floor tinanta BU 1 Lat Kartari Prathama Eka` |
| machine seed (L0–L3 from the owner's charts) | `graph/machine_l0_l2.json` | read; every node is `chart`, not verified |
| what Pushpa Dixit / Neelesh Bodas say, with source quality | `agent/transcripts.py` → `exports/transcript_index.tsv`, `db/transcripts.db` | `python3 agent/transcripts.py build · stats · search "<text>"` |
| Neelesh's slide text (citation-grade after OCR check) | `sources/slides_neelesh/series_NN/NNN - <id>.md` | grep; frames: `agent/frames.py <video> <sec>` |
| corrected Pushpa lecture notes 1.1–1.9 (grade A) | `sources/notes_pushpa_bhag1/` | `transcripts.py search` |
| audit of engine vs notes | `audits/engine_vs_pushpa_notes_1-9.md` | read |

Transcript grades: **A** corrected notes (citation grade) · **D** Devanagari ASR · **W** Whisper · **L** English ASR · **T** English in
Devanagari — D/W/L/T are gist-only (Art. 23 §5). Teacher rank: Pushpa Dixit 1, Neelesh Bodas 2, NCT Acharya 3 (modelling only).
Pushpa Dixit's videos show a blank board — no slide extraction for her; her transcripts/notes are the text.

## 6. Concept cards (key B) — format and first list
`ashtadhyayi-ai/cards/C-NNN.md` (not yet created). Fields: `claim` · `sūtras` (each must resolve in the brain) · `key A` (pāṭha/data
evidence) · `key B` (teacher, video id, timestamp, grade) · `status` (`open | accepted | overruled | conflict`) · `engine impact`.
First cards, in this order: C-L1 Pratyayabheda · C-13 the 13 sopāna (Pushpa series_09 video 1 `u67LzdIOrrE`, hypothesis: = L2) · C-dvitva
(6.1.1–12, five nimittas) · C-anga (per-pratyaya) · C-pada/apada · C-asiddha-same-stage (Neelesh Class 29: when two tripāḍī sūtras
apply at one stage, the earlier operates) · C-vipratiṣedha (Neelesh Class 30; series 14 Classes 33–41) · C-utsarga-apavāda (Class 20).

## 7. Open decisions for the owner
1. P4 reorders work by stage; confirm the 13-box order against Pushpa (series_09 video 1) before any code (cards C-13).
2. Where the cards live: brain (`cards/`, proposed) vs engine `docs/`. Proposed: brain, engine cites card ids in docstrings (Art. 14).
3. Neelesh's English-ASR series (11, 14, 17 …) need the Whisper re-run with a Sanskrit-term prompt, or his slides, before use.

## 8. Handover — jobs and state left running (2026-10-09 ~07:00 IST)
* `transcript_repo/` (`~/transcript_repo`): `whisper_pass.py --only 21 20 12 16 13 11 17` (log `whisper2.log`) fills uncaptioned
  videos; resume: `cd ~/transcript_repo && python3 -u whisper_pass.py --only 21 20 12 16 13 11 17`. Series 10 (NCT Acharya) still pending.
* `slides_pass.py` (log `slides_prio.log`) writes Neelesh slide OCR into the brain; priority list is in its command line (series 11 framework/
  conflict classes first, series 14 Classes 33–41, series 17 Classes 1–7, series 15 Class 3); resume: rerun the same command, it skips done files.
* Not yet committed in the brain: new transcript files from those jobs, slide OCR files, series 01/10 additions. After they finish:
  `python3 agent/transcripts.py build`, then commit and push `ashtadhyayi-ai/`.
* Uncommitted in this repo (other session, untouched): 23 modified files (6.4.8/11/13, 7.1.70, 8.2.9/10, matup/subanta pipelines — AMENDMENT 22 phase 1).
* Known OCR limit: long paragraph slides come out noisy; look at the frame for any card that rests on one.
