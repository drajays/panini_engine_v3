# Panini Engine Audit Report

## Audit Scope
- **Component:** Rule Engine Infrastructure
- **Focus:** Glassbox Transparency, Rule-Based Execution, Conditions, Actions, Metadata
- **Sutra Audited:** [6.1.88 वृद्धिरेचि](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61088)

---

## Sutra 6.1.88 (वृद्धिरेचि) - Status: 🟢 Fully Supported

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **पूर्वम् (Preceding):** आत् (a, ā) - Drawn from 6.1.87
- **निमित्त (Trigger):** एचि (e, o, ai, au)
- **आदेश (Replacement):** वृद्धिः (ai, au)
- **अधिकार (Domain):** पूर्वपरयोः एकः (6.1.84) - Ekādeśa (Single replacement for both)

**Engine Verification:**
- The logic within `sutras/adhyaya_6/pada_1/sutra_6_1_88.py` correctly models the pairs in `_VRIDDHI_TARGET`. 
- SLP1 character mapping matches exactly: 
  - Preceding: `a`, `A` (अ, आ)
  - Trigger: `e`, `o`, `E` (ऐ), `O` (औ)
  - Result: `E` (ऐ), `O` (औ)

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- The `cond` function successfully performs pattern matching over a flattened stream of `varna` (phonemes) across terms.
- It robustly identifies occurrences where the preceding varna and the trigger varna appear adjacently.

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- The `act` function flawlessly performs an **एकादेश** (Ekādeśa).
- It applies the vṛddhi replacement to the preceding term (`ti1`, `vi1`) and safely deletes the trigger varna from the subsequent position (`ti2`, `vi2`).

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass** (with minor recommendations)
- **Traceability Hooks:** The `SutraRecord` maintains complete context. `apavada_of = ("6.1.87",)` correctly notes it as an exception to the Guṇa sandhi. `anuvritti_from = ("6.1.84",)` captures the Ekādeśa context.
- **Explainability (`__why_now_dev__`):** The `act` function explicitly injects runtime rationale into `state.meta["__why_now_dev__"]`.
  - Example output: `संधिः: a + E → E (वृद्धि-एकादेशः); (काशिका ६।१।८८)`

### Identified Gaps & Recommendations

1. **Varna Position Stability:**
   - In the `act` function, the operation `del state.terms[ti2].varnas[vi2]` shifts indices in real-time. Since the engine re-evaluates the state after an action, this is safe, but explicit logging of the term structure before/after the shift could enhance the UI/Traceability view.
2. **Standardization of `__why_now_dev__`:**
   - Ensure that the format used for `__why_now_dev__` here is strictly enforced via a schema across all Vidhi sutras so the web UI trace view parses it uniformly.

---
*End of Report for 6.1.88*

## Sutra 6.1.77 (इको यणचि) - Status: 🟢 Fully Supported (Gaps Resolved)

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **स्थानी (Target):** इकः (i, ī, u, ū, ṛ, ṝ, ḷ, ḹ)
- **निमित्त (Trigger):** अचि (All vowels a, ā, i, ī, u, ū, ṛ, ṝ, ḷ, ḹ, e, ai, o, au)
- **आदेश (Replacement):** यण् (y, v, r, l)
- **अधिकार (Domain):** संहितायाम् (Continuous utterance)

**Engine Verification:**
- `_YAN_MAP` correctly maps all long and short `ik` varnas to their corresponding `yaṇ` consonants.
- `_AC_ALL` correctly enumerates all vowels that serve as triggers.

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- **Resolved:** The `_find_ik_ac_boundary` function now checks for **intra-term** *yaṇ* sandhi as well as across term boundaries. It iterates through the varnas within a term and replaces the `ik` if it is followed by an `ac`.
- It correctly respects exceptions such as Pragṛhya (`PRAGHYA_TERM_TAG`) and the complicated `1.1.58` *sthānivadbhāva* blocking logic (`_blocked_by_padadi_ac_lopa_padanta`) only across term boundaries.

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- Correctly replaces the `ik` varna with `yaṇ`.
- Tags the resulting varna with `IKO_YANACI_ADESHA_TAG` and `para_nimitta_yan_adesha` specifically when the transformation happens at the term boundary.

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass**
- **Resolved (`__why_now_dev__`):** The `act` function now injects a descriptive trace string into `state.meta["__why_now_dev__"]`, logging the exact phonetic transformation (e.g., `संधिः: i + अच् → y (यण्-आदेशः); (काशिका ६।१।७७)`). The UI/Traceability matrix will correctly reflect this glassbox behavior.

### Identified Gaps & Recommendations
- **All previous gaps resolved!** No further recommendations for this sutra.

## Sutra 6.1.78 (एचोऽयवायावः) - Status: 🟢 Fully Supported (Gaps Resolved)

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **स्थानी (Target):** एचः (e, ai, o, au)
- **निमित्त (Trigger):** अचि (All vowels a, ā, i, ī, u, ū, ṛ, ṝ, ḷ, ḹ, e, ai, o, au)
- **आदेश (Replacement):** अय्-अव्-आय्-आवः (ay, av, āy, āv)

**Engine Verification:**
- `_ECO_SPLIT` accurately handles the mapping of targets to their replacements: `e -> ay`, `ai (E) -> āy`, `o -> av`, `au (O) -> āv`.
- `_AC_ALL` is correctly constructed to include all trigger vowels.

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- **Resolved (Scope Restriction):** The rule no longer artificially restricts application to `anga/vikarana` boundaries. It correctly acts as a universal *saṃhitā* rule across term boundaries.
- **Resolved (Intra-Term):** The rule now correctly scans for intra-term `ec + ac` boundaries (`for k in range(len(vs) - 1)`), properly splitting targets inside a single term.
- **Resolved (Legacy Hack):** The non-Paninian `_find_target` shortcut for `os` suffixes was removed. The rule now correctly relies on the newly implemented `7.3.104` to convert `a -> e` beforehand, completing the derivation naturally.

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- Replaces the `ec` varna perfectly by rewriting `left.varnas[k]` to `a` and inserting `yv` at `k + 1`. This accurately simulates the splitting behavior regardless of whether it happens at a term boundary or internally.

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass**
- Explicitly documents the transformation in `state.meta["__why_now_dev__"]`. Traceability works smoothly.

### Identified Gaps & Recommendations
- **All previous gaps resolved!**

---
## Batch Audit: Sutras 6.1.109, 6.1.94, 6.1.89, 6.1.97, 6.1.127, 6.1.125, 6.1.107

### 🔴 Group 1: Stubs & Non-Phonetic Bypasses (6.1.109, 6.1.94, 6.1.89)
*   **[6.1.109 एङः पदान्तादति](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61109)** (Pūrvarūpa) - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** Now correctly scans for padānta `e/o` + `short a`, performs the `ekādeśa` (elision with `avagraha`), and implements `__why_now_dev__` traceability.
*   **[6.1.94 एङि पररूपम्](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61094)** (Pararūpa) - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** Now correctly scans for `a/ā`-ending upasargas before `e/o`-initial dhātus, properly executes pararūpa, and implements `__why_now_dev__` traceability.
*   **[6.1.89 एत्येधत्यूठ्सु](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61089)** (Vṛddhi) - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** Now correctly checks for `a/ā` followed by `iṇ`, `edha~` roots starting with `e`, or `vah` starting with `ūṭh`. Executes the proper vṛddhi `ekādeśa` and logs the UI trace. 6.1.94 accurately defers to it.

### 🔴 Group 2: Hardcoded Hacks (6.1.127)
*   **[6.1.127 इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61127)** - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** The hardcoded `P023` (`div -> diu`) test bypass was completely eradicated and properly relocated to its linguistically correct sutra (`6.1.131 दिव उत्`).
    *   This rule is now authentically implemented as a `VIBHASHA` (optional rule). It properly detects a padānta `ik` followed by an asavarṇa `ac`, makes it short (hrasva), and blocks sandhi (prakṛtibhāva) while setting the `__why_now_dev__` UI trace.

### 🟡 Group 3: Functional but Structurally Flawed (6.1.97, 6.1.107, 6.1.125)
*   **[6.1.97 अतो गुणे](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61097)** - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** The condition was beautifully refactored to dynamically scan for apadānta short `a` followed by a `guṇa` vowel (`a/e/o`), gracefully handling both intra-term and cross-term boundaries (with 1.4.2 *vipratiṣedha* competitor detection). `__why_now_dev__` was also added.
*   **[6.1.107 अमि पूर्वः](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61107)** - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** The incorrect `AC_DEV` condition was fixed to use the correct `_AK` set (a, i, u, ṛ, ḷ, and long). The `__why_now_dev__` string was also added.
*   **[6.1.125 प्लुतप्रगृह्या अचि नित्यम्](https://cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/read.html?s=61125)** - 🟢 **Fully Supported (Gaps Resolved)**
    *   **Resolved:** The `_AC_ALL` set was fixed to encompass long vowels as well. UI traceability `__why_now_dev__` was added to explain the *prakṛtibhāva* firewall.

## Sutra 8.2.39 (झलां जशोऽन्ते) - Status: 🟢 Fully Supported (Gaps Resolved)

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **स्थानी (Target):** झलाम् (jhal - all stops and fricatives)
- **निमित्त (Trigger):** अन्ते (at the end of a pada)
- **आदेश (Replacement):** जशः (jaś - j, b, g, ḍ, d)

**Engine Verification:** 🟢 **Pass**
- **Resolved:** The `_JHAL_TO_JAS` mapping is now correctly expanded to cover sibilants and `h` (`ṣ->ḍ`, `s->d`, `ś->j`, `h->g`). While competing rules (like 8.2.30 `coḥ kuḥ` or 8.2.31 `ho ḍhaḥ`) intercept some of these earlier in the tripāḍī, the grammatical fallback matrix here is now sound.

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- The rule accurately triggers when a term is tagged as a `pada`, ending in a letter present in the `_JHAL_TO_JAS` map, and lacks the idempotency tag.

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- **Resolved:** The action accurately replaces the varna and now creates a dynamic samjna registry key (`8_2_39_{old}_to_{new}`) rather than hardcoding `t_to_d`.

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass**
- **Resolved:** `state.meta["__why_now_dev__"]` is now correctly populated, providing human-readable explanations on the UI for *jhal -> jaś* transformations at a padānta.

---

## Sutra 8.4.55 (खरि च) - Status: 🟢 Fully Supported (Gaps Resolved)

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **स्थानी (Target):** झलाम् (jhal)
- **निमित्त (Trigger):** खरि (khar)
- **आदेश (Replacement):** चर् (car - voiceless unaspirated stops)

**Engine Verification:** 🟢 **Pass**
- **Resolved:** The `_hits` function now dynamically flattens the *varṇa* stream (`flat = [(ti, vi)...]`), allowing this rule to authentically function as a *saṃhitā* sandhi operating across word boundaries (`dad+ta -> datta`).

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- **Resolved:** All four non-phonetic hardcoded test bypasses (`P031-P034`) were completely eradicated. The engine now relies entirely on the legitimate phonetic `_hits` calculation. (Tests requiring missing grammatical steps were properly marked as `xfail` instead of being faked here).

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- Beautifully handles executing the substitutions for all recorded hits across the sequence.

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass**
- **Resolved:** Now generates a rich `__why_now_dev__` string summarizing the precise phonetic changes made (`{old}→{new}`).

## Sutra 8.4.40 (स्तोः श्चुना श्चुः) - Status: 🟢 Fully Supported (Gaps Resolved)

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **स्थानी (Target):** स्तोः (s, t, th, d, dh, n)
- **निमित्त (Trigger):** श्चुना (in contact with ś, c, ch, j, jh, ñ)
- **आदेश (Replacement):** श्चुः (ś, c, ch, j, jh, ñ)

**Engine Verification:** 🟢 **Pass / Excellent Logic**
- The target map `_STU_TO_SCU` precisely covers the mapping from `stu` to `ścu` classes.
- The `_SCU` trigger set is perfectly configured.
- **Resolved:** The logic for **8.4.44 (शात्)** was refactored into a crystal-clear guard (`if prev == "S" and c in _TAVARGA: continue`). It correctly ensures that `tu`-varga letters are protected from `ścutva` when they directly follow `ś` (e.g., preserving `praśna`), while still allowing `s` to become `ś`.
- The rule flattens the entire saṃhitā stream (`flat = [(t, i) for t in state.terms for i in range(len(t.varnas))]`), granting it flawless cross-term and intra-term capabilities.
- **Resolved:** The phantom non-tripāḍī backdoor `8_4_40_pre_tripadi_arm` was deleted, restoring Paninian Tripāḍī integrity.

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- Accurately checks for occurrences using the dynamic `_find_stu` phonetic function. It natively handles idempotency because once a `stu` varna transforms, it is no longer in the `_STU_TO_SCU` map.

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- The action uses a `while (hit := _find_stu(state)) is not None:` loop to correctly transform all instances. 
- **Resolved:** The unreferenced `_find_zt` dead code was deleted, reducing technical debt.

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass**
- **Resolved:** A dynamic trace string is now generated during the `while` loop, accumulating all the `{old}→{new}` changes and injecting them into `state.meta["__why_now_dev__"]`.


## Sutra 8.4.45 (यरोऽनुनासिकेऽनुनासिको वा) - Status: 🟢 Fully Supported (Gaps Resolved)

### 1. Linguistic Representation (Rule-Based Definition)
**Sutra Details:**
- **स्थानी (Target):** यरः (yar - all consonants except `h`)
- **निमित्त (Trigger):** अनुनासिके (when followed by an `anunāsika` nasal)
- **आदेश (Replacement):** अनुनासिकः (anunāsika - the nasal of the target's varga)
- **प्रकार (Type):** वा (Vibhāṣā / Optional)

**Engine Verification:** 🟢 **Pass / Excellent Logic**
- **Resolved:** The empty stub has been completely rewritten into an authentic phonological rule!
- The mapping `_NASAL_OF` correctly handles all sparśa (stop) consonants, while a separate path correctly adds the `anunasika` tag to the semivowels (`y, v, l`), demonstrating deep understanding of Paninian phonetics.
- The boundary check strictly enforces the `padānta` context by ensuring the target is the final varṇa of a `pada`-tagged term and correctly ignoring `bha` terms.

### 2. Glassbox Condition (`cond`) 
**Engine Verification:** 🟢 **Pass**
- **Resolved (Authentic Phonetics):** The blind `tripadi_gate_eligible` backdoor was completely deleted. The engine now honestly scans the term boundaries to detect a padānta `yar` followed by an `anunāsika`.
- **Resolved (Vibhāṣā):** The rule was correctly re-cast as a `VIBHASHA` type with `vibhasha_default=False`. It now correctly surfaces both the `vāg+mukham` and `vāṅmukham` pakṣas via the `vikalpa` engine!

### 3. Glassbox Action (`act`)
**Engine Verification:** 🟢 **Pass**
- Beautifully handles the distinct substitutions for vargīya consonants (literal character replacement) versus antastha semivowels (tag injection).

### 4. Glassbox Metadata and Traceability
**Engine Verification:** 🟢 **Pass**
- **Resolved:** The `act` function now generates a perfect `__why_now_dev__` string summarizing the precise phonetic change (e.g., `{old}` becoming `{new}` optionally).

