# V4 cycle — prātipadika ↔ dhātu as composable stages (2026-10-31)

Target (user's diagrams): prātipadika —sup→ nāmapada; prātipadika —taddhita/strī→ prātipadika; prātipadika —sanādi→ dhātu; dhātu —kṛt→ prātipadika; dhātu —sanādi→ dhātu; dhātu —vikaraṇa+tiṅ→ kriyāpada. Aṣṭādhyāyī shape: 1–2 prakṛti, 3–5 pratyaya, 6–8 operations → pada.

Done: `pipelines/chain.py` (`Stem`, `krt`, `taddhita`, `sup`), tests/unit/test_chain.py: kṛt → taddhita → taddhita → sup compose on the existing loop entry points.

Open, ranked:
1. strī stem stage — only ṭāp (4.1.4) runs, and only in the subanta preflight; ṅīp/ṅīṣ/ṅīn (4.1.5 ff.) are not on that path (gaura/brāhmaṇa get ṭāp, Bavat gets nothing). Needs those sūtras in the loop first.
2. sanādi / nāmadhātu stages: result must be a dhātu `build_dhatu_state` accepts (san/ṇic/yaṅ today = recipe flags, laṭ only; kyac hard-coded in tinanta.py:2630).
3. Adhikāra nesting: the taddhita loop never opens the frames 3.1.1 ⊃ 4.1.1 ⊃ 4.1.3 ⊃ 4.1.76 (data/inputs/adhikara_scope_index.json has them); rules fire on phase window + vivakṣā. Open the frames from the index when a sūtra of a scope fires, then let conds read them.
4. Recipe spines (tinanta.py, subanta.py) hard-sequence 6–8 steps and open tripāḍī by hand; phase 6.1.72 sandhi runs after 6.4–7.4 in the loop.
5. Vākya = padasamūha, pada = suptiṅanta = prakṛti + pratyaya (1.4.14). The engine has the pada (Term kind="pada" from engine/phases/pada_merger.py; 1.4.14 in the subanta preflight) but no vākya object: sentences are demo recipes (pipelines/kO_staH_vakya.py, grAmas_tava_svam_vakya.py). Plan: a `Pada` record (kind subanta|tiṅanta, prakṛti kind prātipadika|dhātu, the ordered pratyaya chain from the origin record) returned by every entry point, and `Vakya = tuple[Pada]`, so analysis (reader→engine gap loop) and derivation share one type; sentence-level sandhi/kāraka relations only after that.
