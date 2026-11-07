# STATE (overwrite at each session end; ≤ 40 lines) — 2026-11-08

- Read next: this file, docs/SHORTCUT_LEDGER.md (next free id S143), docs/V4_CYCLE.md. Rules: glass-box (every change via apply_rule), no word recipes, strict xfail over fudge, shortcuts marked + ledgered, Vidyut/external corpora validators only.
- TOOLS: `.venv/bin/python -m pytest -n8 tests/` (system python3 has no xdist). A full run in a clean worktree (`git worktree add --detach <dir> HEAD`) = ~2.5 h; 13 failures there (tests/test_practice.py, test_notes_audit_general_match.py, test_upadesha_inputs.py) are untracked-data artefacts and pass in the main tree. `setsid` does not exist on macOS.
- THE KĀŚIKĀ IS READABLE: ~/data-master/ashtadhyayi-ai/db/ashtadhyayi.db, table texts(sutra_id, source='kashika', content). Read it for a sūtra's meaning and cite it; engine code must never read it (guard test). Several old "no source" ledger rows were wrong.
- Done 2026-11-07/08 (all on main, committed):
  1 ūṅ 4.1.66 (vivakṣā jAtiBeda=manuzyajAti) + ṅīn 4.1.73 (śārṅgaravādi only; S138) in chain.strI.
  2 loops open 3.1.1 ⊃ 4.1.1 ⊃ 4.1.76 (phase_adhikaras.json "nominal").
  3 real PRATISHEDHA/SAMJNA conds: 4.1.10 4.1.56 7.2.8 7.2.39 7.2.40 7.2.59 7.3.87 8.2.8 8.2.79 3.1.95; S114 S115 S120-S122 derived (vivakṣā svaBeda/antaraBeda/kArakaArTa, derive(..., **vivaksha); gaṇapāṭha for 1.1.37/1.4.57/58/61). Still gate-only (S131-S133): 3.1.94 4.1.163 4.1.174 5.4.69 7.3.3 8.2.3; hand-tag rows S116-S119 S123-S125 open.
  4 suDI→suDiyaH (lexicon su+DIN+kvip); 8.2.7 branch D (loop reaches paYcAnAm).
  5 (exercise audit 340 LK unexercised: 112 FAIL, 228 NO_EXAMPLE) fixed: ṣaṭ numerals from Kāśikā 1.1.24 (data/inputs/samkhya_patha.json, engine/samkhya.py): 7.1.22 luk, 7.2.84 vikalpa + 7.1.21 → pañca, aṣṭa/aṣṭau; 7.1.75 dadhnā/akṣṇā; 7.2.37 grahītā, 7.2.38 vṛto vā, 7.2.40; nenijāni (7.3.87).
  6 lakāras now shown as la~w, li~N … (engine/lakara_attach.py LAKARA_UPADESHA); 1.3.2/1.3.3/1.3.9 leave the l (user request).
- Item 6 (serial test_impact record + firing ledger) was started 2026-11-08 in a worktree at f7a8315a: `python -m tools.test_impact record -p tools.firing_coverage` → copy sig/test_impact.json (git-ignored), sig/firing_coverage.json, sig/suite_sig.json from the worktree into the repo, then run `python3 -m tools.sutra_class`, `tools.lk_plan`, `tools.deferred_register`, commit sig + docs. Use `quick --base f7a8315a` for later edits.
- Next: (a) finish step above; (b) 7.2.41-7.2.45 veṭ family and 7.2.5/7.2.6; (c) añ branch of 4.1.73 (needs jāti in the samagra) S138; (d) 3.1.94 vikalpa hook in the resolver; (e) 5.4.69 needs the samāsa machine; (f) 8.2.3 as an asiddha_strata exception; (g) harness gaps in tools/exercise_audit.py (kṛdanta/sanādi entry, label shapes).
- Known wrong still: ṣaṣ + nām gives zazRAm (ṣaṇṇām needs 8.4.45); yuṣmad/asmad go through pipelines/asmad_subanta, not derive().
- Uncommitted by design (the owner's): .gitignore, data/inputs/adhikara_scope_index.json, tools/build_scope_index.py, sig/loop_gauge.json, tests/constitutional/test_no_external_corpus_in_engine.py, scratch/, sig/exercise_audit.json (refreshed by the audit; commit it with the ledger refresh).
