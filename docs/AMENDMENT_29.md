# AMENDMENT 29 — vārttikas, Bhāṣya rulings and paribhāṣās live inside the sūtra (accepted by the owner 2026-10-31)

**Status:** accepted: *"fully agree go ahead"* (owner, 2026-10-31), after the design put to him in the session of that date. Adds Article 25; Article 10's count becomes twenty-six (0 through 25). Touches nothing in Arts. 1 – 23 except by reference (Arts. 2, 7, 12, 13, 14, 16, 21, 22).

## Problem
Kātyāyana's vārttikas and Patañjali's rulings extend, restrict or displace sūtras (4.2.43 + *parśvā ṇas vaktavyaḥ*; 1.3.2 + *ira it-saṃjñā vācyā*). The engine met them only as ad-hoc code and docstrings inside unrelated files (backlog below): no id, no source, no tier, invisible to coverage, and not under Art. 21. A rule the pāṭha does not contain cannot be a fifth kind of unit that fires beside the sūtras.

## Rule (Art. 25)
1. **The sūtra is the only unit that fires.** A vārttika or Bhāṣya ruling is an entry of the `vartikas` tuple of the sūtra it modifies, in that sūtra's own file (Art. 7: one sūtra, one file). The sūtra derives its power from them; nothing else fires.
2. **Entry** (`engine.vartika.Vartika`): `id` = host + `.v<n>` (n = the vārttika's number in the host's Bhāṣya; `4.2.43.v4`); `source` (Kātyāyana vā. n / Patañjali, with the Bhāṣya number); `tier` (Art. 22: `T1` Kātyāyana, `T2` Patañjali); `relation` to the host: `apavada` (displaces the host's own act where both hold), `extension` (adds a site the host does not reach), `restriction` (withholds the host's own act where it holds); its own `cond`/`act` (Art. 2: the tape only, never the surface form; the vivakṣā it asks must occur in the host's samagra, Amendment 25); `text_dev`, verbatim from the database (`ashtadhyayi.db`, `texts`, source `vartika`, or the Bhāṣya's own quotation) — cited, never invented (Art. 14).
3. **Trace and coverage.** The vārttika is folded into the host's cond/act when the record is built, so scheduler, resolver and dispatcher see one id. The applied step carries `sutra_id` = host (Art. 16 credits the host) plus `vartika`, `vartika_label` (`4.2.43 + vā. 4`), `vartika_source`, `vartika_tier`, `paribhasha`.
4. **No private priority.** A vārttika contends exactly as its host (Art. 21): the relation is the only thing it declares; the host's `apavada_of`, ladder rungs and resolver treat the merged record as one candidate.
5. **Paribhāṣās stay one shared data layer** (`data/inputs/paribhasha_shekhara.json`, Art. 12): an entry names them by id (`PS<num>`), never copies the text; the trace names the paribhāṣā when it decides. Unknown ids are refused.
6. **Switch-off per tier** for audit: `engine.vartika.disabled_tiers("T1")` runs the derivation with the entries of that tier off and clears the effectiveness memo.
7. **Validation at construction:** id shape and uniqueness, tier ∈ {T1, T2}, relation ∈ the three, source and text present, cond/act callable, paribhāṣā ids exist. Test: `tests/constitutional/test_amendment_29_vartikas.py` (also checks the words against the database).

## Engine support (small)
`engine/vartika.py` (entry, `compose`, validation, switch); `SutraRecord.vartikas` (folds in `__post_init__`); one pop-and-annotate in `engine/dispatcher.py`. Scheduler and resolver unchanged.

## Worked example — 4.2.43 + vā. 4: parśu + ṇas → pārśva
Bhāṣya 4.2.43 (5368): *parśvāḥ saṇ vaktavyaḥ … yadi saṇ kriyate, itsaṃjñā na prāpnoti; evaṃ tarhi ṇas vaktavyaḥ* — *parśūnāṃ samūhaḥ pārśvam*. Kāśikā 4.2.42: *parśvā ṇas vaktavyaḥ … padasaṃjñakatvād guṇo na bhavati*. Relation `extension` (stem `parśu`, sense `samūha`, pratyaya `ṇas`). The loop: ṇ it by 1.3.7, s it by 1.3.3, ṇit vṛddhi 7.2.117, **1.4.16 siti ca** gives *pada* (so 1.4.18 bha and the guṇa 6.4.146 never come), 6.1.77 yaṇ: **pārśva**. Strict xfail in `tests/regression/test_taddhita_basics.py` flipped to a passing test. To carry it, 1.4.16 (`engine/samjna_sup_prakriti.is_siti_pada_context`) now also accepts a taddhita pratyaya whose *it* the loop tagged `it:sit` (svādi includes the taddhitas, as 1.4.17 already says).

**Host placement, flagged for the owner.** The database's `vartika` table and the Bhāṣya put this vārttika under 4.2.43 (tal-prakaraṇa, vā. 4); the Kāśikā prints it under 4.2.42 (after *ahnaḥ khaḥ krato*). Built under 4.2.43 on the T1/T2-over-T7 rule (Art. 22). Moving it to 4.2.42 is a one-line change of host if the owner prefers the Kāśikā's position.

## Migration backlog — existing ad-hoc vārttika spots (not migrated here; grep `vartika|vārttika|वार्त`)
engine: `engine/it_samjna.py` (1.3.2 *ira it*).
sūtras (22): 1.1.9, 1.1.28, 1.1.73 (vā. 1, 2), 1.2.48 (*īyaso bahuvrīhi-pratiṣedha*), 1.3.2, 1.3.3, 1.3.9 (*iñr*), 2.1.26, 2.2.18, 2.2.26 (*sarvanāmno vṛtti-mātre puṃvat*; meta key `vartika_sarvanAma_puMvat_vrtti`), 3.1.57, 4.1.4, 6.1.1, 6.1.17, 6.1.64, 6.4.143, 7.1.59, 7.2.114, 8.4.1, 8.4.41, 8.4.45, 8.4.47 (`_find_vartika_dvitva`). Total 23 files. Migration order: those that read meta keys instead of the tape first (2.2.26, 1.1.73), then those whose vārttika is already a separate branch (8.4.47, 1.3.2/1.3.9).

## Not changed
Every sūtra other than 4.2.43 (and the 1.4.16 helper widening); Art. 21's ladder; the paribhāṣā data file; the closed vivakṣā vocabulary.
