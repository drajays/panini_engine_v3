# Dhātu svara (udātta/anudātta/svarita), reconstructed in reverse

> **⚠ Circular with respect to `pada_label_dev`. Never a `cond()` input.**
> Every `reconstructed_svara` below was computed *from* `pada_label_dev`
> (plus structural ṅit/ñit). Wiring it into 1.3.12/1.3.72/1.3.78's
> `cond()`/`act()` to re-derive `pada` would not be a structural fix — it
> would be `pada_label_dev` re-deriving itself through one extra hop,
> indistinguishable from today's lookup except harder to audit (Article 0:
> "a classical scholar could audit line-by-line"). It becomes a legitimate
> `cond()` input only after `reconstructed_svara` is replaced by a svara
> read from the brain's real accented upadeśa, independently of
> `pada_label_dev` — see Caveat 1 below.

**Date:** 2026-10-07
**Scope:** `data/inputs/dhatu_svara_reconstructed.json`, built by
`scripts/derive_dhatu_svara_reconstructed.py` from
`data/inputs/dhatupatha_upadesha.json`. Additive only — neither file touches
the live engine (no sūtra `cond()`/`act()` changed, no pipeline/tape-init
changed). `pada_label_dev` stays the engine's load-bearing field; this is a
derived cross-check artifact sitting beside it.

## Why

Pāṇini's own dhātupāṭha marks every dhātu's vowel with one of three svaras:

- **udātta** — unmarked (the "elsewhere" case)
- **anudātta** — the underline mark
- **svarita** — the vertical stroke above

1.3.11 स्वरितेनाधिकारः opens the 1.3.12–1.3.93 kartari-pada block; 1.3.12
अनुदात्तङित आत्मनेपदम् reads **anudātta or ṅit** → आत्मनेपद; 1.3.72
स्वरितञितः... reads **svarita or ñit** (usage-conditioned on kartari-abhiprāya)
→ उभयपद; 1.3.78 शेषात् कर्तरि परस्मैपदम् gives **udātta/elsewhere** →
परस्मैपद. That is the forward direction: accent (plus the structural ṅit/ñit
anubandhas, which are a *different* axis — visible letters, not accent) →
pada.

This engine's own upadeśa strings (`upadesha_dev`/`upadesha_slp1`) never
carried the accent diacritic on import — only the anunāsika `~` survived
(e.g. `Asa~` for आस्, vs. the brain's accented आस्`\`). `pada_label_dev` was
instead scraped **pre-resolved** from ashtadhyayi.com (see
`scripts/build_dhatupatha_upadesha_v3.py`), via the lexical mechanism
documented in the 1.3.12 sūtra file (`sutras/adhyaya_1/pada_3/sutra_1_3_12.py`)
and wired in `engine/tape_init/tinanta.py` (`kartari_atmanepada_licensed`).
That mechanism is already verified (prior session: 99.18% agreement, 2164/2182
Bhvādi dhātus, against the brain's own structural `dhatupatha_svara.py`
checker) — see `docs/PARKED_ISSUES.md` history for that pass.

This pass runs the **implication backward**: given the already-classified
`pada_label_dev` and the structural ṅit/ñit facts (readable straight off
`upadesha_dev`'s final letter — ङ् or ञ् — with no accent needed), reconstruct
which svara the dhātu's vowel must have carried for 1.3.12/1.3.72/1.3.78 to
land on that pada by the default, lexical route.

## Rule table

| `pada_label_dev` | trailing it | reconstructed svara | governed by | basis |
|---|---|---|---|---|
| आत्मनेपदी | ends ङ् (ṅit) | *(none — ṅit alone suffices)* | 1.3.12 | `ngit` |
| आत्मनेपदी | no ṅit | **anudātta** | 1.3.12 | `accent` |
| उभयपदी | ends ञ् (ñit) | *(none — ñit alone suffices)* | 1.3.72 | `yit` |
| उभयपदी | no ñit | **svarita** | 1.3.72 | `accent` |
| परस्मैपदी | (never ṅit/ñit — शेष) | **udātta** | 1.3.78 | `default` |

## Verification on the current data (2240 rows)

```
आत्मनेपदी, ṅit:        55/55  — 100% (zero exceptions: every ṅit-final row is आत्मनेपदी)
आत्मनेपदी, anudātta:   461
उभयपदी, ñit:           46/50  — 92%  (3 missing pada_label_dev, 1 anomaly below)
उभयपदी, svarita:       538
परस्मैपदी, udātta:     1136   (+ 1 anomaly below)
no pada_label_dev:     3      (all trailing ञ् — see anomalies)
```

**Confidence:** 1698 `high`, 538 `medium` (the reconstructed-svarita bucket —
see caveat below), 4 `low` (flagged anomalies).

## Caveats (read before trusting a `reconstructed_svara` value)

1. **The brain is unavailable in this session.** `~/data-master/ashtadhyayi-ai`
   (AGENTS.md "Brain") carries the real accented upadeśa and would let this
   reconstruction be checked against source rather than re-derived from the
   same `pada_label_dev` it is supposed to explain. Until that cross-check
   runs, treat every `accent`-basis row (999 of them: 461 anudātta + 538
   svarita) as a **plausible, not confirmed**, reconstruction — it is
   logically forced by the rule table above, but the rule table itself is
   this session's reconstruction of the *default* route only.
2. **1.3.72 is usage-conditioned (vibhāṣā), not a pure lexical fact.** A root
   being ñit does not *guarantee* आत्मनेपद in a given sentence — only that it
   is *licensed* when the phala accrues to the agent (कर्तृ-अभिप्राय). The
   99.18%-verified lexical convention (ñit/svarita ⟺ उभयपदी-labeled in the
   dhātupāṭha) is a statement about the root's *capacity*, which is what
   `pada_label_dev` already records — not about which pada a specific finite
   form takes. This reconstruction inherits that same scope; it says nothing
   about per-sentence pada choice.
3. **Named exception sūtras (1.3.13–1.3.93) are usage/prefix-conditioned, not
   identity overrides of the lexical default.** E.g. 1.3.19 विपराभ्यां जेः
   (`sutras/adhyaya_1/pada_3/sutra_1_3_19.py`) only fires when जि carries a
   vi-/parā- prefix tag at derivation time — it does not mean जि's own
   dhātupāṭha accent differs from its bare-root pada. These sūtras ride on
   top of the reconstructed default and do not falsify it.
4. **Four flagged anomalies** (all `confidence: low`):
   - `BvAdi_nIY` (नीञ्) — labeled परस्मैपदी despite a trailing ञ्, which by the
     92%-consistent convention should mean उभयपदी. This is a 7-row
     `_CURATED_EXTENSIONS` entry in `scripts/build_dhatupatha_upadesha_v3.py`
     (test/demo convenience data, not gold-verified) — likely a pre-existing
     data error, not a real counter-example to 1.3.72. Needs a human check
     against the brain before `pada_label_dev` is "corrected" here.
   - `BvAdi_950`, `BvAdi_hfY`, `BvAdi_zwuY` (णीञ्/हृञ्/स्तुञ्) — same
     `_CURATED_EXTENSIONS` list, missing `pada_label_dev` entirely. All three
     are well-known उभयपदी roots (करोति/कुरुते-type), consistent with their
     trailing ञ्; `pada_label_dev` should be backfilled for them directly in
     `scripts/build_dhatupatha_upadesha_v3.py`, which this pass deliberately
     does not do (out of scope: that file feeds the live engine; this report
     only reads it).

## What this does *not* do

- It does **not** add accent diacritics to `upadesha_dev`/`upadesha_slp1`
  themselves, and does **not** rewire `sutra_1_3_12.py` / `sutra_1_3_72.py` /
  `kartari_pada_1_3_78.py` to consume the reconstructed svara instead of
  `pada_label_dev`. That swap — making the *live* mechanism structural — is
  the larger, previously-parked project (matching real brain-sourced accented
  upadeśa against engine rows, engine-wide blast radius); this pass is the
  narrower, purely-additive half of it: the data-side reconstruction, not the
  engine-side rewiring.
- It does not resolve the 4 flagged anomalies; they are surfaced for a human
  (or a future `make brain`-backed pass) to adjudicate.

## Reproducing

```
python3 scripts/derive_dhatu_svara_reconstructed.py
```

Pinned by `tests/unit/test_dhatu_svara_reconstructed.py`.
