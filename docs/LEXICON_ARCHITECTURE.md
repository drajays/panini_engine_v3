# Lexicon architecture — replacing ad-hoc per-stem flags with declared origin facts

**Status: a first, verified slice landed 2026-10-07. Not the full vision.**

## The original ask

An earlier design note (not committed as a doc, but the basis for this work)
argued against passing a finished stem string with "cheat-code" flags —
`ugit=True`, `tfc=True`, `han_dhatu=True` — because those flags are the
*consequence* of a derivation (a stem came from matup/śatṛ/tṛc/a kvip
compound), fed back in as if they were primitive input. It asked for a
structured **Lexicon** that declares a stem's morphological origin (root +
pratyaya, or compound structure) instead, mirroring how the dhātupāṭha
itself is already consulted as input data (gaṇa, antargaṇa membership,
it-markers — never re-derived from scratch inside a sūtra's `cond()`).

## Why the flags exist at all

`pipelines/subanta.py`'s `derive()` takes a **bare stem string** (`"Bavat"`,
`"kartf"`), not a `Term` carrying derivation history. That's deliberate — it
lets subanta be tested in isolation from whatever kṛt/samāsa pipeline would
normally produce the stem — but it means `derive()` has no way to know
*why* a stem ends the way it does. `sutra_7_1_70.py` (7.1.70 उगिदचां...)
needs to know a stem is **ugit** (matup/vatup/īyasun/kvasu/vidvas-derived);
`sutra_6_4_11.py` (6.4.11) needs **tfc** (tṛc/tṛn-derived); `han_dhatu`
flags a kvip हन्-compound (3.2.87). Before this change, two things supplied
these facts, both shortcuts:

1. A caller-supplied boolean (`derive("Bavat", 1, 1, ugit=True)`) — the
   caller had to already know the fact and pass it every time.
2. `bench/ashtadhyayi_gold.py`'s `_origin_flags()`, run over the ~9,005-stem
   gold sweep: a **spelling-suffix guess** (`stem.endswith(("mat", "vat", …))`)
   — not a declared fact at all, just a heuristic with known exceptions
   patched in by hand (`_NOT_TFC` for पितृ/मातृ/भ्रातृ/... — kinship nouns
   that end in "-tṛ" but aren't tṛc agent nouns).

## What changed

`data/inputs/subanta_krt_origin_lexicon.json` is a small, hand-curated
lexicon: for each stem it lists, it declares **where the stem came from**
(root + kṛt-pratyaya, e.g. `{"root": "BU", "krt": "SatfL"}` for `Bavat`) and
what flags that implies — not a guess from the string's tail.
`engine/registries/subanta_origin_lookup.py` reads it (read-only, same
pattern as `engine/registries/lexicon_lookup.py`). `pipelines/subanta.py`'s
`derive()` now consults it **before** falling back to the caller's explicit
flag or the gold harness's suffix guess — a declared fact (including a
declared `False`, as for पितृ) wins over both.

Net effect: `derive("Bavat", 1, 1)` now gives भवान् **without** the caller
passing `ugit=True` — the fact comes from the lexicon. The flag still works
for any stem the lexicon doesn't cover yet (most of the ~9,005-stem gold
sweep), so nothing regresses for unlisted stems; `bench/ashtadhyayi_gold.py`
now prefers the lexicon when a stem is listed, and only guesses from
spelling otherwise.

Two existing unit tests (`test_idam_strI_sarvanama_paradigms.py`,
`test_gita_gap_fixes.py`) asserted the *old* behavior — that `Bavat`/
`Bavitf` *without* a flag were "ordinary" non-origin-tagged stems — as a
demonstration that the flag, not a hardcoded rule, controlled the result.
Updated both to assert the new default (lexicon-supplied) result for the
listed stems, and added an unlisted-stem case to each so the "flag still
required when there's no lexicon entry" behavior stays covered.

## What this is not

- **Not** a general Term-level origin/provenance system. A real kṛt
  pipeline (building `Bavat` from `BU` + `śatṛ`, `kartf` from `kṛ` + `tṛc`)
  would produce these facts structurally, with no lexicon file needed —
  this JSON file is a stand-in for that, honest about being hand-curated
  (see each entry's `"note"`).
- **Not** upasarga/samāsa boundary tracking as distinct `Term`s (the other
  half of the original design note — needed for ṇatva/ṣatva across a
  compound member boundary, `docs/PARKED_ISSUES.md`'s subanta note,
  ~1,000 cells). Not attempted this round.
- **Not** a fix for 6.4.77–83 (iyaṅ/uvaṅ of dhī/śrī/bhū/bhrū/strī) reading
  kvip-origin from a lexicon. `docs/PARKED_ISSUES.md` already notes 6.4.77
  *is* implemented for the tiṅanta (verb-medial) case; whether the subanta
  (prātipadika-final) case needs origin-lexicon input the way `ugit`/`tfc`
  do is a real next question, not yet investigated.
- **Not** an anusvāra-orthography vibhāṣā fork for 8.4.58 (the other
  PARKED_ISSUES.md subanta item, ~700 cells). Not attempted this round.
- **Only 15 stems** are in the lexicon today (the ones already exercised by
  unit tests, plus the kinship-noun exceptions). Expanding it to the
  gold sweep's ~250 śatṛ/-vat/-tṛ cells is real, bounded, follow-on work —
  each entry needs its root+pratyaya verified, not guessed.

## Where to pick this up

- Add more stems to `data/inputs/subanta_krt_origin_lexicon.json` as their
  origin is verified (brain `dhatupatha`/`dossier` lookups, or a real kṛt
  derivation once one exists for that pratyaya).
- Investigate whether 6.4.77–83 need the same origin-lexicon treatment for
  subanta kvip/kvin finals, or whether the existing tiṅanta implementation
  already covers what's needed once the stem's dhātu is known.
- Build the upasarga/samāsa-boundary half separately — it's a bigger,
  riskier change (Term-level, not a lookup file) and deserves its own pass.
