# Concepts from Puṣpā Dīkṣita's lectures the brain/engine does NOT already have

Scope, strictly: this file holds only what's genuinely new — a concept, a
classification, or a named gap — found by reading her transcripts
(`drajays/ashtadhyayi_brain`, `ashtadhyayi-ai/sources/transcripts/`).
Checked against `CONSTITUTION.md`, `AGENTS.md`, and the engine's own code
before including anything; left out everything that's already there (e.g.
3.4.114–116's sārvadhātuka/ārdhadhātuka test — the engine already implements
exactly that two-part logic: structural intervening-augment vs. direct
stipulation for liṭ/āśīrliṅ. Not repeated here).

## 1. लेट् lakāra does not exist in this engine at all — confirmed

Searched the whole codebase: `"leT"` appears in exactly one place
(`sutras/adhyaya_3/pada_4/tin_adesha_3_4_78.py`, a bare name in a lakāra
list), and nowhere else — no pipeline, no sūtra file, no test. Lesson 068
("पाठ-१५, आर्धधातुक लेट् लकार") and lesson 105 both treat it as a real,
addressable lakāra (Vedic, ārdhadhātuka). This is a flat-out missing
lakāra, not a partial/buggy one — the first engine has never touched.

## 2. "12 lakāras", not 10: leṭ and liṅ each split by śap-presence

Lesson 105: she counts **12** lakāras, not the usual 10, because two of
them are internally heterogeneous for her purposes:
- **लेट्**: when शप् (śap) is present in the middle, it behaves as
  ārdhadhātuka; when absent, as sārvadhātuka. So "sārvadhātuka-leṭ" and
  "ārdhadhātuka-leṭ" are treated as two different formation problems.
- **लिङ्**: विधिलिङ् (sārvadhātuka) and आशीर्लिङ् (ārdhadhātuka) are
  likewise two different problems, not one lakāra with two uses.

Net: लट्, लोट्, लङ्, विधिलिङ् (4) + sārvadhātuka-leṭ (5th) are one group;
लुट्, लृट्, लृङ्, लुङ्, लिट्, आशीर्लिङ्, ārdhadhātuka-leṭ are the other
(7 more = 12 total). This is a genuinely different count/grouping from
how the engine currently enumerates lakāras (`_LAKARA_TAG` in
`engine/tape_init/tinanta.py` has 11 entries, no leṭ split). Worth
knowing before anyone builds leṭ support: it isn't one lakāra, it's two
formation problems depending on śap.

## 3. "तिङ्-कृत् का भेद मिटाना" — group ārdhadhātuka affixes by phonetic+kit class, not by the tiṅ/kṛt label

This is the single most actionable new idea in the material. Lesson 105,
on लुट् (tāsi) specifically:

She explicitly erases the tiṅ-vs-kṛt distinction *as an organizing
category for derivation* ("तिङ्कृत प्रक्रिया अलग-अलग नहीं है" — tiṅ-formation
and kṛt-formation are not separate processes) and instead groups
ārdhadhātuka affixes by **phonetic-initial + kit-status class**:

- **तास्-वर्ग** ("t-initial, non-kit" class): तास् (लुट्'s own vikaraṇa),
  तृच्, तुमुन्, तव्य, तव्यत् — she states these five build identically
  (same iṭ-insertion behavior, same guṇa, same sandhi) because they share
  this one phonetic class, *not* because कृत्/तिङ् happen to agree. One
  procedure built for तास् automatically gives correct तृच्/तुमुन्/तव्य/
  तव्यत् forms (पात, पातृ, पातुम्, पातव्य — her own example, पा "to
  drink/protect").
- **स्या-वर्ग** ("s-initial, non-kit" class): स्य (लृट्) grouped the same
  way with its own kit-status peers.
- Textual evidence she cites for this grouping existing in the
  *Aṣṭādhyāyī itself*, not invented by her: the whole iṭ-āgama rule block
  (~7.2.8–7.2.78, she excludes the 3 purely sārvadhātuka sūtras in that
  span) is stated by Pāṇini in one place, deliberately separating
  sārvadhātuka-siddhi from ārdhadhātuka-siddhi — i.e. the *placement* of
  these sūtras in the text is itself evidence for a phonetic-class-based
  procedure, not a lakāra-by-lakāra one.

**Why this matters for this engine right now**: `pipelines/krdanta.py`'s
`derive_krt()` only supports Ṇvul/lyuṭ/lyap (confirmed missing: kvasu,
kānac, tṝc, tumun, tavya, tavyat — see `docs/BRAIN_1_3_12_CROSSCHECK.md`
and `docs/PARKED_ISSUES.md`'s kvasu note). Her classification says tṝc/
tumun/tavya/tavyat should NOT need a new derivation path built from
scratch — they belong to the *same* तास्-वर्ग the engine's existing लुट्
(tāsi) machinery in `pipelines/tinanta.py` already handles (7.2.35 iṭ
insertion, guṇa, sandhi). Building them as "तास्-वर्ग siblings" of लुट्,
rather than as independent new kṛt-pratyayas, is the concrete engineering
takeaway. (kvasu/kānac are a *different* class — ṅit/śit-marked,
liṭ-specific — her scheme doesn't claim they share तास्-वर्ग; that gap
stays open.)

## 4. The five-fold prakriyā classification, stated as a map

Lesson 001 opens the whole course with this, and it isn't written down
anywhere in the brain or in this repo as an explicit five-way split:

> प्रक्रिया (the actual derivation machinery, as opposed to saṃjñā/sandhi/
> paribhāṣā, which she treats as *prerequisite* background used by all
> five, not a sixth kind of प्रक्रिया) is of exactly five kinds:
> 1. धात्वधिकार — dhātu + pratyaya (tiṅanta + kṛt together, per §3 above)
> 2. सुबन्त — prātipadika + sup
> 3. तद्धित
> 4. समास
> 5. स्वर
>
> कारक/विभक्ति (semantic role assignment) is explicitly *excluded* from
> this list — her reasoning: kāraka-vibhakti belongs to अर्थ/वाक्य (meaning/
> sentence-construction), consulted when actually speaking, not to the
> word-formation machinery itself.

Useful as an explicit top-level map of what "100% sūtra coverage" (per
`docs/SUTRA_COVERAGE_100_PLAN.md`) is actually five sub-goals of, and
exactly how kāraka/vibhakti relates to (but sits outside) that map.

## 5. The explicit 13-step tiṅanta/kṛdanta procedure, as a checklist

Lesson 021 states the sequence as a flat, numbered list (she says "13
सोपान" — 13 steps). Reconstructed in order from her explanation:

1. धातु-संज्ञा (two sūtras: 1.3.1 भूवादयो धातवः for upadeśa-dhātus;
   3.1.32 सनाद्यन्ता धातवः for derived dhātus — san/ṇic/etc.)
2. इत्-संज्ञा (1.3.2–1.3.9)
3. "सत्वादि चार कार्य" — the four tasks that follow it-lopa for the raw
   dhātu (she references having covered these in Sahajabodha bhāga 1,
   पाठ 3; not independently re-derived here — flag for whoever has that
   book/lesson to confirm the exact four)
4. attach the desired pratyaya (kṛt or lakāra) to the now-clean dhātu
5. if a lakāra: इत्-संज्ञा on the lakāra's own anubandhas
6. keep only "ल" (ल-शेष) after that
7. तिङ्-आदेश in place of ल (तिप्-तस्-झि... , 3.4.78 family)
8. lakāra-specific substitution in place of *those* tiṅ-ādeśas
9–13. (the sārvadhātuka/ārdhadhātuka fork and what follows it — gaṇa+
   vikaraṇa if sārvadhātuka, nothing if ārdhadhātuka — per the already-
   known 3.4.113–116 logic, so not re-listed here)

This exact sequence, as an explicit numbered list, isn't written down
anywhere in `CONSTITUTION.md`/`AGENTS.md` — even though the *code*
(`engine/tape_init/tinanta.py`, `pipelines/tinanta.py`'s bootstrap) already
follows it. Worth adding as documentation (not a behavior change) so a
new reader can see the engine's bootstrap order is a direct implementation
of a named traditional procedure, not an engineering convention invented
for this project.

## 6. "अनुबन्ध must be remembered after it-lopa" — the meta-principle behind meta-tags

Lesson 001, via a fruit/vegetable-peeling metaphor: when it-lopa removes
an anubandha from the surface form, its *effect* must still be tracked —
"व्यर्थ होते तो पाणिनि लगाते ही क्यों" (if it were pointless, why would
Pāṇini have added it at all; every anubandha was added deliberately, so
even after it disappears phonetically, we must keep it "in the heart"
because its consequence (फल) will still be needed later in the
derivation).

Not a new rule — a stated *reason* for a pattern that's already pervasive
in the code (`ekac_dhatu`, `udatta_dhatu`, `mit`, `kngiti`, `is_apit`,
etc. — tags that persist on a `Term` after the phonetic it-letter itself
is long gone). Worth citing in `CONSTITUTION.md` if the architecture's
"tag survives lopa" convention is ever challenged as an engineering
shortcut — it's the traditional method, named and justified by a modern
teacher working strictly from the Aṣṭādhyāyī.

## Not included here (already known, or not yet verifiable)

- Sārvadhātuka/ārdhadhātuka classification mechanics (§ her lessons
  021/105) — matches `sutras/adhyaya_3/pada_4/sutra_3_4_{114,115,116}.py`
  already. Not repeated.
- The sārvadhātuka/ārdhadhātuka *ordering* principle (gather, then apply)
  from lesson 033/034 — already covered in
  `docs/BRAIN_TRANSCRIPTS_PUSHPA_DIKSHIT.md` §2, not repeated here.
- Lesson 110's ṣatva/ḍhatva/samprasāraṇa content and lesson 117's kvasu/
  kānac content — still not recoverable from the ASR text (confirmed
  zero keyword hits in 110; see `docs/BRAIN_TRANSCRIPTS_PUSHPA_DIKSHIT.md`
  §3). Flagged there, not re-flagged here.
- "सत्वादि चार कार्य" (step 3 above) — she references it rather than
  re-deriving it in these lessons; left unresolved rather than guessed.
