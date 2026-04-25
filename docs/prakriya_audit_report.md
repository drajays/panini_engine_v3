# Prakriyā (derivation) pipeline audit

Generated as part of codebase standardization.  **Sūtra semantics** live only under `sutras/`; **recipes** under `pipelines/` only call `apply_rule` in a chosen order.

## 1. Duplicate sūtra *definitions*

- **Single registry rule:** `engine/registry.py::register_sutra` raises on duplicate `sutra_id`.  Every Pāṇinian rule is implemented in **exactly one** `sutras/**/sutra_*.py` with one `SutraRecord`.
- **Not duplicated:** *patchwork* redefinition of the same `sutra_id` in another file is **impossible** at import time.
- **Intentional repetition:** many pipelines repeat `apply_rule("1.1.60", s)` (etc.); that is *scheduling*, not a second *definition*.  The **1.1.60–1.1.63** preflight *śṛṅkhalā* is now centralized in `pipelines/preflight_lopa_samjna.py` (`PREFLIGHT_LOPA_LUK_1_1_6X` + `apply_preflight_luk_samjna_block`) and used from:
  - `pipelines/subanta.py` (when `sAlIya` continuation is not set),
  - `pipelines/krdanta.py` (two entry points),
  - `pipelines/subanta_trc.py`.
- **Taddhita glass-box** paths (e.g. `taddhita_salIya` after **2.4.71**) still call **1.1.60** / **1.1.61** in *derivation* order; they are not the same *slot* as subanta preflight and stay explicit in those recipes.

## 2. Canonical pathways (standard vs specialized)

| Path | Entry | Role |
|------|--------|------|
| **Subanta (general)** | `pipelines.subanta.derive` → `run_subanta_pipeline` | Aṣṭādhyāyī-ordered *subanta* after `build_initial_state`; preflight through **1.4.7**, **4.1.2** *sup*, then `SUBANTA_RULE_IDS_POST_4_1_2` + `__MERGE__`.  **This is the default** for a bare stem + *vibhakti*/*vacana*. |
| **A-kāra-anta puṃliṅga** | `derive_akarant_pullinga` | Thin wrapper: same as `derive(..., linga="pulliṅga")` + shape guard. |
| **Śālīya taddhita** | `pipelines.taddhita_salIya.derive_salIya` | Dedicated *samarthā* + *tatra-bhava* + *taddhita* spine; reuses the same *sūtra* modules, not a second engine. |
| **Śālīya + subanta** | `derive_salIyaH` | **Stage A** taddhita, then **Stage B** subanta with `META_SALIYA_TADDHITA_SUBANTA_CONTINUATION` to avoid a duplicate **1.1.60–1.1.63** preflight. |
| **Kṛdanta scaffold** | `pipelines.krdanta` (e.g. `build_krt_pratipadika_n`) | Dhātu + *kṛt*; shares preflight *luk* block via `apply_preflight_luk_samjna_block`. |
| **Tṛc nom. sg. slice** | `pipelines.subanta_trc.derive_trc_nom_sg` | Shorter *subanta* for *tṛc* stems + meta. |
| **Tinanta gold** | `tinanta_jayati_gold` etc. | *Fixed-step* replays; document ordering only; not a second registry. |
| **Dik / samāsa demo** | `dik_uttarapurva_demo` | Glass-box; still `apply_rule` only. |

**Principle:** similar base + *sup* should prefer **`derive` / `run_subanta_pipeline`** unless a *śāstrīya* reason forces a slimmer or meta-gated path (`subanta_trc`, gold).

## 3. Conflict resolution (not “last line wins”)

- **Utsarga–apavāda** is *not* implemented as “right-hand / later recipe step overrides” as a general mechanism.  Each *sūtra*’s `cond`/`act` and registry updates encode blocking and eligibility.
- **Structural gates (dispatcher `apply_rule` front matter):**  
  - Tripāḍī: `asiddha_violates` (`engine/gates.py` + `state.tripadi_zone`),  
  - *Nipātana* freeze,  
  - *pratiṣedha* `blocked_sutras`,  
  - *Vibhāṣā* choice.  
- **Apavāda-style blocks** in *sūtra* modules (e.g. **1.1.63** vs **1.1.62**, **1.1.65**) use `samjna_registry` / `paribhasha_gates` / `niyama_gates` as appropriate to CONSTITUTION Art. 2.
- **Recipe order** determines *which* *sūtra* is *tried* next; *whether* it fires is always `cond(state)`.

## 4. Gaps and follow-up (non-blocking)

- **Krdanta** vs **subanta** 1.1.1/1.1.73/… *blocks* are still spelled out in long form; a second helper could factor *identical* prefix *śrṅkhalā*s only where they truly match.
- **Tinanta** and **dik** demos are intentionally idiosyncratic; keep documented in this file when extended.

## 5. Invariants (machine-checked)

See `tests/unit/test_prakriya_audit.py`.
