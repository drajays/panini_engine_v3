# Brain source: पुष्पा दीक्षित's "अष्टाध्यायी सहजबोध" lecture series (transcripts)

**Source:** 123 YouTube lecture transcripts (Hindi, ASR-generated), added to
`drajays/ashtadhyayi_brain` under `ashtadhyayi-ai/sources/transcripts/`
(commit `efa64ef`, "पुष्पा दीक्षित - अष्टाध्यायी सहजबोध playlist के 123
वीडियो के clean Hindi transcripts जोड़े"). Companion to the already-integrated
`sahajabodha` dhātupāṭha OCR (same author's printed book, wired into
`build_db.py`/`knowledge_api.py sahajabodha` — see `ashtadhyayi-ai/AI_AGENT_GUIDE.md`).

**User's framing:** these are auto-generated transcripts with pronunciation-driven
ASR errors, but conceptually authentic — to be read, cross-checked, and used to
resolve conflicts, with the usable concepts folded into the brain's own logic.

## 1. The curriculum (full index)

The 123 lectures are a complete, sequentially-numbered course — her own
systematic rebuild of tiṅanta formation, lakāra by lakāra, collecting the
scattered rules each lakāra needs from across all eight adhyāyas before
applying them (see §2). This is a navigable map, not available anywhere
else in the brain:

| # | प्रकरण | पाठ | topic |
|---|---|---|---|
| 001–002 | इत्संज्ञा | 1.1–1.2 | it-saṃjñā, pada-nirṇaya |
| 003–020 | सन्धि | 2.1–2.18 | ac-sandhi, hal-sandhi (18 lessons) |
| 021 | पञ्चोपाङ्ग | 3.1 | dhātvādeśa / pratyayādeśa |
| 022–029 | अङ्गकार्य | 4.1–4.8 | aṅga operations by final letter (a/ā/i,u/ṛ/ṝ/anidit/samprasāraṇī/anunāsika) |
| 030–032 | णिजन्त | 5.1–5.3 | causative formation |
| 033–034 | भावकर्म (sārvadhātuka lakāra) | 6.1–6.2 | bhāve/karmaṇi yak |
| 035–036 | कर्मकर्तृ | 7.1–7.2 | karmakartari |
| 037 | आशीर्लिङ् (parasmaipada) | 8 | yāsuṭ |
| 038–044 | यङ्लुक् | 9.1–9.7 | |
| 045–047 | यङन्त | 10.1–10.3 | |
| 048–051 | इडागम | 11.1–11.4 | seṭ/aniṭ |
| 052–059 | लुट् | 12.1–12.8 | incl. 2 sandhi-practice lessons |
| 060–066 | लृट् | 13.1–13.7 | incl. 2 sandhi-practice lessons |
| 067 | लृङ् | 14 | |
| 068 | लेट् (ārdhadhātuka) | 15 | — Vedic lakāra; not implemented in this engine at all currently |
| 069–070 | आशीर्लिङ् (ātmanepada) | 16.1–16.2 | sīyuṭ |
| 071 | भावकर्म of लृट्/लृङ्/लुट्/आशीर्लिङ् | 16.3 | |
| 072–082 | सन्नन्त (desiderative) | 17.1–17.11 | |
| 083–104 | लुङ् | 18.1–18.17, +4 untitled (100–103), +22 | sic/aṅ/caṅ, by far the largest section |
| 105–117 | लिट् | 19.1–19.13 | iḍāgama, ām, dvitva, abhyāsakārya, **ṣatva/ḍhatva/samprasāraṇa dhātus (19.6)**, by final letter, **kvasu/kānac (19.13)** |
| 118–122 | नामधातु | 20.1–20.5 | kyac/kyaṅ/kyaṣ, ṇic |
| 123 | च्वि/सति/त्रा/डाच् | 21 | |

**Directly relevant to open gaps** (both found this session, independently,
before this transcript set was read):
- **Lesson 110** (19.6, षत्व/ढत्व/सम्प्रसारणी धातुएँ in liṭ) is exactly
  `docs/PARKED_ISSUES.md`'s confirmed-real gap: 6.1.15–19/37–40 (vye/hve/ve/vay
  liṭ saṃprasāraṇa). **Could not be used this round** — see §3, the ASR lost
  every occurrence of the technical terms in this specific lesson.
- **Lesson 117** (19.13, क्वसु और कानच्) is exactly the kvasu/kānac kṛt-pratyaya
  pipeline gap found while checking 1.3.12 (`docs/BRAIN_1_3_12_CROSSCHECK.md`) —
  same caveat, not yet extracted.
- **Lesson 068** (लेट्) — लेट् lakāra does not appear anywhere else in this
  brain or in `panini_engine_v3`; flagging its existence as a Vedic lakāra
  this engine has never addressed.

## 2. What's usable today: the method itself (lessons 001, 033–034)

Lesson 033/034 (भावकर्म प्रकरण, सार्वधातुक लकार) states a principle explicitly,
and demonstrates it with भावकर्म यक् (त्वया अहम् आहूये — "I am called by you",
कर्म के पुरुष से मध्यम/उत्तम-पुरुष प्रत्यय का चयन):

> एक लकार के रूप बनाने के लिए जो नियम अष्टाध्यायी में बिखरे (adhyāyas 2, 3, 6,
> 7 अलग-अलग अधिकारों में) हैं, उन सबका संकलन पहले करना चाहिए, फिर एक साथ लागू
> करना चाहिए — धातु से परे जब भी सार्वधातुक (यहाँ "साधा") प्रत्यय/विकरण लगता
> है, तो कोई आर्धधातुक ("आधा") तत्व बीच में नहीं आता; भावकर्म यक् हो या
> कर्तरि-गणानुसार विकरण, दोनों में यही सिद्धान्त एक-सा लागू होता है।

("ASR-cleaned" rendering — the raw transcript has this consistently as
"साधा"/सार्वधातुक and "आधा"/आर्धधातुक; both substitutions are stable across
the lesson and were legible from context, not guessed.)

**Why this matters to this engine specifically**: this is a direct,
independent, traditionally-sourced statement of the exact architectural
principle `core/phases/tripadi.py`, `pipelines/tinanta.py`'s "no vikaraṇa
after the sārvadhātuka gate", and the project's whole pipeline-over-adhyāya
design already assume. It doesn't change any code — it's confirmation from
a named traditional source (not Vidyut, not ashtadhyayi.com) that the
engine's core sequencing philosophy (gather every adhyāya's rule for one
lakāra, apply as one pass) is itself an authentic Pāṇinian method, not an
engineering convenience. Worth citing in `AGENTS.md`/`CONSTITUTION.md` if
a reader ever asks why the pipeline is structured this way.

## 3. ASR quality: real, and term-dependent — don't cite rule text from this corpus yet

Spot-checked lesson 110 (19.6, षत्व ढत्व सम्प्रसारणी धातुएँ) specifically
because it matches an open engine gap. Result: **zero** occurrences of
षत्व, ढत्व, or सम्प्रसारण anywhere in the 79 KB transcript — despite being
the lesson's own title topic. The ASR evidently cannot render these
specific rare technical nouns at all (not even as a near-miss), while in
lesson 033 the two-term pair सार्वधातुक/आर्धधातुक degraded to a *stable,
decodable* substitution (साधा/आधा) throughout. The difference seems to be
frequency: सार्वधातुक/आर्धधातुक recur constantly across the whole 123-lesson
course and the ASR settled on a consistent (if wrong) rendering; rarer
terms specific to one lesson did not.

**Conclusion — do not use this corpus for rule-level citations** (that's
Kāśikā/SK/Bhāṣya's job, per Art. 14) **until a human or an audio-aware
transcription pass fixes it.** It is safe and valuable right now for:
the curriculum map (§1), and passages where the terms you need are common
enough to have a stable, context-decodable substitution (as in §2) — verify
by grep for the literal term first, the way lesson 110 was ruled out here.

## 4. Not done this round (scope)

- **Did not fix the 3 filenames that exceed ext4's 255-byte limit**
  (033/034's 6.1/6.2 and 062's 13.3 — Devanagari + brackets run long in
  UTF-8 bytes even though they fit under macOS's UTF-16-code-unit limit,
  which is presumably why they were created successfully there). Content
  is still readable via `git show "<ref>:<long path>"` in the
  `ashtadhyayi_brain` repo; a rename-only commit to fix checkout on Linux
  was attempted and blocked by this session's own permission policy for
  shared-resource writes — left for the user or a future session with
  that permission.
- **Did not transcribe-correct the other 121 lessons**, or re-derive
  lesson 110/117's intended rule content from audio. Flagged as exactly
  what's needed (§3) rather than guessed at.
- **Did not wire a `transcripts` table into `build_db.py`/`knowledge_api.py`**
  the way `sahajabodha` already is — the OCR'd book is structured tabular
  data (serial → row); these are free-text lecture transcripts with poor
  technical-term ASR, so the right ingestion shape (per-lesson free text?
  per-topic excerpts? only after cleanup?) needs a decision, not just an
  importer. Recommend deciding that only after a cleanup pass makes the
  content trustworthy enough to cite.
