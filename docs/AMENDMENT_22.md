# AMENDMENT 22 — the Lexicon: stem origin is data, tags are derived (proposed)

**Status:** proposed 2026-10-06 at the owner's direction ("no shortcut; nouns tagged by Pāṇini's rules, not by flags").
Acceptance (Art. 10 §3) is the owner's; implementation proceeds on a branch-equivalent basis (every gate green per commit).

## Problem
A stem string carries no history. Today the engine is told what it cannot know through boolean arguments or hand-stamped tags
(`derive(..., ugit=True | tfc=True | han_dhatu=True)`, `t0.tags.add("ugit")` in `core/canonical_pipelines.py`, and the gold harness's
shape-guessing `_origin_flags`). Pāṇini has no such flags: *ugit* is "the aṅga has u/ṛ/ḷ as it-letter" (7.1.70), *tṛc-anta* is "the
pratyaya is tṛc/tṛn" (6.4.11), *dhātu* is "a root, or what ends in a kṛt of a root" (1.3.1 / 3.1.32 / 6.4.77), *saṃyoga* and *ṇatva*
depend on **where the term boundaries are** (8.4.1 "samānapade"). Each of these is a consequence of a derivation, so the
derivation (or its structural record) must be on the tape.

## Decision
1. **A Lexicon is an input** (Art. 6): `data/inputs/subanta_lexicon.json`. Each entry is a stem (SLP1) + liṅga and its
   **vyutpatti as an ordered list of components**, each a *lexical fact*:
   `{kind: prakriti|dhatu|upasarga|pratyaya, source: dhatupatha|ganapatha|krt|taddhita|sup, upadesha: "<SLP1 upadeśa>", artha: "<vivakṣā>"}`.
   A component names an upadeśa that already lives in an input table (dhātupāṭha id, `krit_pratyaya.json`, `taddhita_pratyaya.json`,
   gaṇapāṭha). **No derived property may appear in the lexicon** (no `ugit`, `nadī`, `kvip`, `iyaṅ`, `bha`, `pada`, `sarvanāma`-as-flag):
   `engine/lexicon.py::validate` rejects any key outside the schema. A stem with no entry is an *avyutpanna* prātipadika (1.2.45).
2. **Stem composition is a recorded structural stage** (like `__PADA_MERGE__`), not a sūtra: it puts the components on the tape as
   distinct `Term`s, lets the real it-prakaraṇa (1.3.2–1.3.9) run on each pratyaya, then merges into one prātipadika `Term` whose
   `meta["vyutpatti"]` is the list of `{kind, upadesha, it_letters, dhatu}` read **from the Terms after it-lopa** — nothing is stamped.
   The merge is refused (Art. 18 gap) when the concatenated surface differs from the entry's stem: a lexicon entry that the engine cannot
   reproduce is a gap, not a guess (Art. 17).
3. **Rules read the record.** 7.1.70 computes *ugit* from `vyutpatti[-1].it_letters ∩ {u, ṛ, ḷ}`; 6.4.11 / 6.1.66 / 1.1.43 read
   "last pratyaya ∈ {tṛc, tṛn}" (and the stems 6.4.11 itself lists); 6.4.8 / 6.4.13 read "a component is the dhātu *han*" and the
   dhātu-final of 6.4.77 (Phase 2). The tags `ugit`, `krt_tfc`, `han_dhatu` stop being inputs; they survive only as
   *derived* tags written by the composition stage from the same record (`engine/lexicon.py::derive_tags`), documented here.
4. **Flags are removed.** `derive(ugit=, tfc=, han_dhatu=)` and `bench._origin_flags` are deleted when their last caller migrates;
   tests that pinned "ugit is an input" are rewritten to "ugit is derived from the pratyaya's it-letters".
5. **Lexicon construction obeys Art. 17/19.** `tools/propose_vyutpatti.py` *proposes* analyses from stem shape and the dhātupāṭha;
   an entry is written only if the forward engine, run on the components, reproduces the stem string. Gold forms are never consulted
   to choose an analysis (we do not grade our own homework).
6. **Optional forms are forks, not biases.** Where Pāṇini gives vā/vibhāṣā (8.4.58 anusvāra/parasavarṇa on a stem-internal ṃ, 7.1.? …)
   the engine produces every branch (`engine/vikalpa.explore`); picking one for display is a presentation filter outside the engine.

## Phases (each ends green; numbers are gold-sweep agreement, harness `bench.ashtadhyayi_gold --kind subanta`)
| Phase | Scope | Needs (rules made real) |
|---|---|---|
| 1 | schema + validator + composition stage; ugit (matup/vatup, īyasun), tṛc/tṛn, han | 8.2.9 vatva; 5.3.57 īyasun attach; 3.1.133 tṛc check |
| 2 | kvip/kvin/root-final stems: iyaṅ/uvaṅ (6.4.77, 6.4.79–83), 8.2.36, 8.2.62, añc | 3.2.76/3.2.59, 6.1.67 vera aprktasya, 6.4.77–83 |
| 3 | śatṛ, kvasu, 7.1.22 numerals, vidvas samprasāraṇa | 3.2.124, 3.2.107, 6.4.131 |
| 4 | compounds & upasarga + kṛt: components stay distinct `Term`s through the ṇatva/ṣatva sūtras (8.4.1, 8.4.14, 8.3.x); samāsa saṃjñās by their own rules | 2.1–2.2 samāsa vidhis, 8.4 boundary reads |
| 5 | vikalpa forks for anusvāra/orthography; retire `ugit`/`tfc`/`han_dhatu` shims | — |

## Acceptance tests
`tests/constitutional/test_lexicon_schema.py` (no derived keys; every component upadeśa exists in an input table),
`tests/constitutional/test_no_origin_flags.py` (no `ugit=`/`tfc=`/`han_dhatu=`/`tags.add("ugit")` outside the derivation stage),
`tests/regression/test_lexicon_roundtrip.py` (every entry reproduces its stem).

## Acceptance
Pending (owner).
