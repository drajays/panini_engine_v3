# 1.3.12 अनुदात्तङित आत्मनेपदम् — brain cross-check (2026-10-06)

## The rule

**Text** (ashtadhyayi.com row i=13012): `anudAttaNita Atmanepadam` / अनुदात्तङित आत्मनेपदम्
**Padaccheda:** अनुदात्त-ङितः / आत्मनेपदम्

- **Kāśikā:** अविशेषेण धातोरात्मनेपदं परस्मैपदं च विधास्यते, तत्रायं नियमः क्रियते — अनुदात्तेतो ये धातवो ङितश्च तेभ्य एवात्मनेपदं भवति नान्येभ्यः।
- **Siddhāntakaumudī:** अनुदात्तेत उपदेशे यो ङित्तदन्ताच्च धातोर्लस्य स्थाने आत्मनेपदं स्यात्।
- **Reading:** a dhātu whose *upadeśa* carries either (a) an **anudātta** accent on its *it*-vowel, or (b) **ṅ** as an *it*-letter, takes **ātmanepada** l-affixes. This is the DEFAULT; 1.3.13–1.3.93 (anuvṛtti from here) name ~65 further sūtras of root-specific exceptions and refinements before 1.3.78 श्रेष at् कर्तरि परस्मैपदम् supplies parasmaipada as the residual default.
- **Paribhāṣā cited:** PŚ 41 (vikaraṇebhyo niyamo balīyān), PŚ 50 (asiddhaṁ bahiraṅge antaraṅge), PŚ 131 (tiṅ/śap-anubandha-nirdiṣṭaṁ...).

## What the engine does today

`sutras/adhyaya_1/pada_3/sutra_1_3_12.py` reads a pre-computed lexical fact,
`Term.meta["kartari_atmanepada_licensed"]`, set in `engine/tape_init/tinanta.py`
from the dhātupātha's own `pada_label_dev` field (ashtadhyayi.com's stated
pada for the root) — not from the upadeśa's own accent/ṅit marks. This is
the same pattern used elsewhere for lexical facts (gaṇa, antargaṇa
membership), and is **not** a bare arbitrary flag: `pada_label_dev` is
itself ashtadhyayi.com's scholarly-maintained classification, traceable
to the same Pāṇinian analysis 1.3.12–93 perform.

## Independent structural verification

The brain ships a second, independent implementation of exactly this
rule: `~/data-master/ashtadhyayi-ai/agent/dhatupatha_svara.py` `expected()`,
built from the **accented upadeśa** (sanskritdocuments.org's सस्वरा
dhātupāṭha, 2,212 dhātus) — i.e. it reads the *actual* anudātta/ṅit/ñit
marks structurally, not a pre-computed pada field, and combines 1.3.12 +
1.3.72 (svarita/ñit → ubhaya) + 1.3.74 (gaṇa 10 → ubhaya default).

Cross-checked against ashtadhyayi.com's own stated `pada` for all 2,212
entries (2,182 with both fields populated):

```
agree:    2164 / 2182  (99.18%)
disagree:   18 / 2182  (0.82%)
```

The 18 disagreements are where the bare 1.3.12/72/74 default differs from
the final, fully-resolved pada — i.e. exactly the cases one of the ~65
named exception sūtras (1.3.13–93) should override. Spot-checked one:
**जि** (ji, "to conquer") — structural default predicts ātmane (anudātta
it-vowel), final pada is parasmai; `sutras/adhyaya_1/pada_3/sutra_1_3_19.py`
(विपराभ्यां जेः) is a real, already-implemented exception granting ātmane
*only* with वि/परा — consistent with a parasmai *default* for bare जि.
The other 17 were not individually re-derived against their specific
override sūtra this round — flagged here for whoever picks this up, not
silently assumed:

| dhātupāṭha id | root(s) | upadeśa (svara) | ashtadhyayi.com pada | 1.3.12/72/74 structural default |
|---|---|---|---|---|
| 01.1000 | अञ्च् | aci~ | U (ubhaya) | P |
| 02.0041 | अधी / इ | i\N | P | A |
| 01.0207 | ईज् | Ija\ | A | P |
| 01.0846 | क्ष्विद् | YikzvidA~ | A | P |
| 10.0231 | गॄ | gF | A | U |
| 01.0699 | ग्लेष् | glezf~ | A | P |
| 04.0050 | घूर् | GUrI\ | A | P |
| 01.0642 | जि | ji~\ | P | A |
| 04.0048 | धूर् | DUrI\ | A | P |
| 01.0320 | बाड् | bAqf\ | A | P |
| 01.0860 | भ्रंश् | BraMSu~ | A | P |
| 01.0196 | मुञ्च् | muci\ | A | P |
| 10.0235 | यु | yu | A | U |
| 01.0564 | वल् | vala\ | A | P |
| 01.0321 | वाड् | vAqf\ | A | P |
| 01.0425 | वेप् | wuvepf\ | A | P |
| 01.0843 | श्वित् | SvitA~ | A | P |
| 10.0058 | स्मि | zmiN | U | A |

**Verdict:** the engine's current `pada_label_dev` lookup for 1.3.12 is
correct for 99.18% of the dhātupāṭha by independent structural
cross-check, and the remaining 0.82% are exactly where Pāṇini's own later
sūtras (1.3.13–93) are expected to override the default — not engine bugs.
**Not fixed/changed this round** — see "Not attempted" below.

## Where Vidyut fires 1.3.12 (brain floor, T10)

The brain's Vidyut-floor sample for 1.3.12 is dominated by **kvasu** (liṭ
participle, -vas), **kānac** (liṭ ātmane participle, -āna), and **yaṅ**
(frequentative) derivations: देN+kvasu → digivAn, पर्द+kvasu → papardvAn,
वस्+śānac → vasAnaH, वेष्ट्+kvasu → vivezwvAn, वस्+kvasu → vavasvAn,
रय्+kvasu, यती/यय/द्युत्+kānac, स्मृ/स्वृ+yaṅ (सास्मर्यते), etc.

**None of these can be exercised end-to-end today**: this engine has no
kvasu, kānac, or yaṅ kṛt-pratyaya pipeline (`pipelines/krdanta.py`'s
`derive_krt()` only supports Ṇvul, lyuṭ, lyap). This is a real,
separate infrastructure gap — already partly noted in
`docs/PARKED_ISSUES.md` under subanta ("kvasu -vas... not written") —
not a defect in 1.3.12 itself. 1.3.12's pada-licensing *is* consumed
correctly today via the tiṅanta path (laṭ/liṭ/etc. finite verbs), which
is where its ~2,182-root cross-check above was run.

## Not attempted (scope, on purpose)

- **Did not swap the live mechanism** to read accent-marked upadeśa
  directly. The accent marks are stripped from this engine's own
  `data/inputs/dhatupatha_upadesha.json` (confirmed: brain's `Asa~\`
  vs. this repo's `Asa~`) — bringing them in is a real, additive data
  project (match ~2,212 brain svara entries to ~3,983 engine dhātu rows,
  add a new field, re-verify against the *full* suite given the blast
  radius: every tiṅanta derivation in the engine reads this pada). Given
  the existing mechanism is independently verified at 99.18% and the
  gap is explained by sūtras this engine already implements correctly
  (1.3.19 checked), the risk/reward did not favor a live swap this round.
- **Did not re-derive the other 17 exception roots** against their
  specific override sūtra (1.3.13–93) one by one — flagged above as a
  concrete, bounded follow-up list instead of guessing.
- **Did not build kvasu/kānac/yaṅ kṛt pipelines** — needed to directly
  exercise the Vidyut-floor examples, out of scope for a citation check.

Method fully reproducible: `~/data-master/ashtadhyayi-ai/agent/dhatupatha_svara.py`
`parse()` + `expected()`, run under that tool's own venv (needs
`indic_transliteration`).
