# Resolution of the open items in `docs/CONFLICTS.md` §J (re-sweep 2026-10-06)

Read-only study. Nothing in the repo was changed; this file is the only output.

## Sources used

All quotations are verbatim from the **ashtadhyayi.com data repo**
(`github.com/ashtadhyayi-com/data`). The primary copy is your local checkout
`~/data-master/`. Every passage cited below was also checked against the current upstream
(`raw.githubusercontent.com/ashtadhyayi-com/data/master/…`, fetched 2026-10-06) and matches.

| tag | file | use |
|---|---|---|
| **data** | `sutraani/data.txt` (row key `i`) | sūtra text, anuvṛtti (`an`) — Art. 14 source #1 |
| **KV** | `sutraani/kashika.txt` | Kāśikā udāharaṇa / pratyudāharaṇa — Art. 14 source #2 |
| **SK** | `sutraani/kaumudi.txt` | Siddhānta-Kaumudī (cross-reference only, Art. 3) |
| **BM** | `sutraani/balamanorama.txt` | Bālamanoramā |
| **vārt.** | `sutraani/vartika.txt` | vārttikas |
| **PŚ** | `paribhashendushekhar/data.txt` | Paribhāṣenduśekhara (Art. 21) |
| **DP** | `dhatu/data.txt` | dhātupāṭha gaṇa / pada / seṭ-aniṭ |
| **prayoga** | `sutraani/sutra_prayogas.txt`, `dhatu/dhatuprayogas.txt` | kāvya attestations |

Forms are given in Devanāgarī with SLP1 in backticks. "recipe" and "loop" refer to the two engine
paths in `docs/RECHECK_2026-10-06.txt`.

---

## Summary

The quick answer for each item. Details, rule chains and evidence follow below.

| # | item | who is right (per KV/SK) | correct form(s) |
|---|---|---|---|
| 1 | pit uttama of abhyasta roots | **Vidyut** for laghūpadha roots (निज्, विज्, विष्, कित्); **engine recipe** for bhī/ki (ajanta) | नेनिजानि `nenijAni`, अनेनिजम् `anenijam`, चिकितानि `cikitAni`, but बिभयानि `biBayAni`, चिकयानि `cikayAni` |
| 2 | hi-lopa: घृणु…, स्कम्भु… | **Vidyut**, but the diagnosis in CONFLICTS.md is wrong (see §2) | घर्णुहि `GarRuhi` / घृणु `GfRu` (never घर्णु `GarRu`); स्कभान `skaBAna` |
| 3 | ṛ-final liṭ thal | **Vidyut + recipe**; the DP data agrees, so there is no data conflict | जहर्थ, जघर्थ, सस्मर्थ, तस्तर्थ, पपर्थ, पस्पर्थ, but ववरिथ |
| 4 | kūṅ / kuṅ / gurī ātmane | **engine loop** (kuṭādi ⇒ ṅit ⇒ no guṇa); Vidyut is wrong | कुविष्यते `kuvizyate`, कुष्यते `kuzyate`, गुरिष्यते `gurizyate`, गुरिता `guritA` |
| 5 | ātmane luṅ 1sg of ksa roots | **Vidyut**, via 7.3.72 क्सस्याचि (not "ārdhadhātuka") | अधुक्षि `aDukzi`, अधुक्षाताम् `aDukzAtAm` |
| 6 | kryādi ātmane | **Vidyut + recipe** | क्रीणीते `krIRIte`, क्रीणाते, क्रीणते |
| 7a | ad laṅ | **neither** (both engine and Vidyut wrong) | आदत् `Adat`, आदः `AdaH` |
| 7b | ad luṅ | **Vidyut + recipe** | अघसत् `aGasat` |
| 7c | su / stu luṅ (parasmai) | **Vidyut** | असावीत् `asAvIt`, अस्तावीत् `astAvIt` |
| 7d | bhas | **Vidyut** | बब्धः `babDaH`, बप्सति, अबभत् `abaBat`, अबब्धाम्, प्स्यात् `psyAt` |
| 7e | bhrasj | **Vidyut** | भ्रक्ष्यति / भर्क्ष्यति, बभ्रज्जे / बभर्जे, अभ्राक्षीत् / अभार्क्षीत् |
| 7f | rañj ātmane liṭ | **Vidyut + recipe** | ररञ्जे `raraYje` (रेजे belongs to राज्) |
| 7g | īṅ liṭ | **Vidyut** | अयाञ्चक्रे `ayAYcakre` |
| 7h | īś / īḍ laṅ dhvam | **Vidyut + recipe**; not an oracle mapping error | ऐड्ढ्वम् `EqQvam` (both roots) |
| 8a | ūrṇu liṭ | **Vidyut** | ऊर्णुनाव `UrRunAva`, ऊर्णुनुवतुः, ऊर्णुनुवे … |
| 8b | cakṣiṅ ātmane liṭ | **neither** | आचचक्षे `cacakze` (or चख्ये / चक्शे) |
| 8c | ās ātmane liṭ | **Vidyut** | आसाञ्चक्रे `AsAYcakre` |
| 8d | as(u) 4 luṅ | — | आस्थत् `AsTat` (attested, Raghuvaṃśa 12.23) |
| 8e | optional alternates | — | list of vibhāṣā sūtras and a branching rule (§8e) |

So 10 items go to Vidyut, 1 to the engine loop (item 4), 2 to the engine recipe (items 1, 6 partly),
and 2 are wrong on both sides (7a, 8b).

---

## 1. pit uttama endings of abhyasta roots — 7.3.87 नाभ्यस्तस्याचि पिति सार्वधातुके

**Sūtra (data `i=73087`):** नाभ्यस्तस्याचि पिति सार्वधातुके; anuvṛtti `गुणः$73082##पुगन्तलघूपधस्य$73086`.
So it blocks **only the laghūpadha guṇa of 7.3.86**. It does *not* block the ajanta guṇa of 7.3.84.

**KV 7.3.87 (verbatim):**
> अभ्यस्तसंज्ञकस्याङ्गस्य लघूपधस्याजादौ पिति सार्वधातुके गुणो न भवति। **नेनिजानि। वेविजानि। परिवेविषाणि। अनेनिजम्। अवेविजम्। पर्यवेविषम्।** … अचीति किम्? नेनेक्ति। … सार्वधातुक इति किम्? निनेज। **लघूपधस्येत्येव — जुहवानि। अजुहवम्॥**

**SK:** "लघूपधगुणो न स्यात । नेनिजानि ।"

These are exactly the disputed cells (`nenijAni`, `anenijam`, `vevijAni`, `avevijam`, `vevizARi`,
`avevizam`), word for word. The pratyudāharaṇa जुहवानि proves that an **ajanta** abhyasta root keeps
its guṇa: so बिभयानि `biBayAni` (bhī) and चिकयानि `cikayAni` (ki) are correct. The "loop" output
`biByAni`, `cikyAni` is wrong.

**Correct cells**

| root | laṅ 1sg | loṭ 1sg/du/pl (P) | loṭ 1sg/du/pl (Ā) |
|---|---|---|---|
| णिजिँर् | अनेनिजम् | नेनिजानि, नेनिजाव, नेनिजाम | नेनिजै, नेनिजावहै, नेनिजामहै |
| विजिँर् | अवेविजम् | वेविजानि … | वेविजै … |
| विषॢँ | अवेविषम् | वेविषाणि … | वेविषै … |
| कितँ (3) | अचिकितम् | चिकितानि … | — |
| ञिभी | अबिभयम् | **बिभयानि** … (guṇa kept) | — |
| कि (3) | अचिकयम् | **चिकयानि** … (guṇa kept) | — |

**Implementation (cond in linguistic terms).** Make 7.3.87 a *pratiṣedha* scoped to 7.3.86's
laghūpadha branch. The cond reads: the aṅga has the abhyasta saṃjñā (6.1.5); the aṅga is laghūpadha
(its penultimate is a short ik); the following pratyaya is sārvadhātuka, **pit**, and ac-initial.
The pit-ness comes from 3.4.92 आडुत्तमस्य पिच्च (loṭ uttama) and from mip→am (3.4.101) staying pit
by sthānivadbhāva. 1.2.4 does not apply because the ending is pit. Do not let it touch 7.3.84 on an
ik-final aṅga.

There are two separate engine bugs:
- the **recipe** never fires 7.3.87 for ṇijir/vijir/viṣḷ/kit (and is inconsistent: `nenijAmahE`
  is right, `nenejE` wrong);
- the **loop** over-blocks: it removes 7.3.84 guṇa for bhī/ki.

Cross-validation: Vidyut agrees with KV on all laghūpadha cells and on बिभयानि.

---

## 2. hi-lopa (6.4.106) with घृणु / ऋणु / तृणु and स्तम्भु-type roots

The note in CONFLICTS.md says the guṇa and nasal rules "don't see the ṅit-ness of the deleted hi".
**That is not the cause.** In both groups the triggering pratyaya is not hi.

### 2a. घृणुँ, ऋणुँ, तृणुँ (tanādi, 8th gaṇa) — loṭ 2sg

1. **The vikaraṇa उ is ārdhadhātuka.** 3.1.79 तनादिकृञ्भ्य उः. The pratyaya उ is neither tiṅ nor
   śit, so 3.4.113 does not make it sārvadhātuka. By 3.4.114 आर्धधातुकं शेषः it is ārdhadhātuka, so
   1.2.4 (apit sārvadhātuka ⇒ ṅit) never reaches it. BM on करोति:
   "उप्रत्ययमाश्रित्य ऋकारस्य गुणः", and the same for कुरुतः: "तसो ङित्त्वादुकारस्य न गुणः".
2. **The laghūpadha guṇa before उ is optional.** SK under क्षिणु (tanādi):
   > उप्रत्ययनिमित्तो लघूपधगुणः । [(परिभाषा) **संज्ञापूर्वको विधिरनित्यः**] इति न भवतीत्यात्रेयादयः । भवत्येवेत्यन्ये । क्षिणोति । क्षेणोति ।
   > **ऋणु** गतौ ऋणोति । अर्णोति । … **तृणु** अदने । तृणोति । तर्णोति ।

   BM: "ऋणु गतौ । अत्रापि क्षिणुवन्मतभेदाल्लघूपधगुणतदभावौ".
3. **hi is ṅit**, because 3.4.87 सेर्ह्यपिच्च makes it apit and 1.2.4 then applies. This blocks guṇa
   of the **उ** (so घृणुहि, never घृणोहि). It has no bearing on the root vowel, whose guṇa is
   triggered by उ.
4. **6.4.106 उतश्च प्रत्ययादसंयोगपूर्वात्.** KV: "उकारो योऽसंयोगपूर्वस्तदन्तात् प्रत्ययादुत्तरस्य हेर्लुग् भवति … असंयोगपूर्वादिति किम्? प्राप्नुहि। राध्नुहि। तक्ष्णुहि॥"

The whole result follows from step 4's *asaṃyogapūrva* condition, checked on the aṅga **as it stands
after guṇa**:

| branch | aṅga | consonants before उ | 6.4.106 | form |
|---|---|---|---|---|
| no guṇa (Ātreya) | घृ-ण्-उ | ण् only (single) | applies | **घृणु** `GfRu` |
| guṇa (others) | घ-र्-ण्-उ | र्ण् (saṃyoga) | blocked | **घर्णुहि** `GarRuhi` |

This is exactly Vidyut's pair (`GarRuhi`, `GfRu`, plus tātaṅ). The engine's **घर्णु `GarRu`**
mixes the two branches: it takes the guṇa *and* the lopa. That is impossible under either view.

**Implementation.** 6.4.106's cond must test *asaṃyogapūrva* on the current varṇa string of the
aṅga (after 7.3.86 has or has not applied). It must not test the upadeśa or a cached pre-guṇa stem.
Order: 7.3.86 runs when उ is attached, which is before hi exists. 6.4.106 runs afterwards, so it sees
the guṇa'd aṅga automatically if it reads current state. If the engine gives one output per cell,
either branch is valid (SK lists ऋणोति first, then अर्णोति). The recipe's `GarRuhi` is the valid
guṇa branch, so keep it and only fix the loop.

The same applies to ऋणु (अर्णुहि / ऋणु) and तृणु (तर्णुहि / तृणु).

### 2b. स्तन्भुँ, स्तुन्भुँ, स्कन्भुँ, स्कुन्भुँ — loṭ 2sg

1. 3.1.82 स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च gives śnā (and optionally śnu).
2. **3.1.83 हलः श्नः शानज्झौ**: after a consonant, śnā becomes **śānac** before hi. KV: "मुषाण। पुषाण।"
   SK: "**स्तभान । स्तुभान । स्कभान । स्कुभान ।** पक्षे स्तभ्नुहीत्यादि ।"
3. **The nasal-lopa trigger is śānac itself, not hi.** śānac is **śit**, so it is sārvadhātuka by
   3.4.113, and it is **apit**, so 1.2.4 makes it ṅit. 6.4.24 अनिदितां हल उपधायाः क्ङिति then deletes
   the upadhā न. The roots are *udit* (उँ), not *idit*, so the *anidit* condition holds.
   KV 6.4.24: "क्ङितीति किम्? स्रंसिता।"
4. 6.4.105 अतो हेः: after the a-final śāna, hi is deleted (BM: "शानजादेसे कृते 'अतो हे' रिति लुक्").

So the result is स्कभान `skaBAna`. The engine's `skamBAna` means 6.4.24 is not reading the ṅit-ness
of **śānac**. Fix 6.4.24's cond to accept any following kit/ṅit pratyaya, including an ādeśa that is
itself śit+apit. Nothing about hi needs pratyayalakṣaṇa (1.1.62) here.

---

## 3. ṛ-final liṭ thal — 7.2.13, 7.2.61, 7.2.63, 7.2.64

### The data does not conflict

The repo's `data/inputs/dhatupatha_upadesha.json` and ashtadhyayi.com `dhatu/data.txt` agree:

| root | DP id | seṭ/aniṭ |
|---|---|---|
| हृ (3) | 03.0016 | aniṭ |
| घृ (3) | 03.0015 | aniṭ |
| स्मृ (5) | 05.0015 | aniṭ |
| स्तृञ् (5) | 05.0006 | aniṭ |
| पृ (5) | 05.0013 | aniṭ |
| स्पृ (5) | 05.0014 | aniṭ |
| **वृञ् (5)** | **05.0008** | **seṭ** |

The difference is in the rule chain, not the data.

### Rule chain

- **7.2.13** कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि is a **niyama** (KV: "क्रादय एव लिट्यनिटस्ततोऽन्ये सेट इति").
  Every other root, aniṭ or not, gets iṭ in liṭ (बिभिदिव, लुलुविम).
- **7.2.61** अचस्तास्वत् थल्यनिटो नित्यम्: an ajanta root that is **nitya-aniṭ in tās** gets no iṭ in
  thal. KV: "याता — ययाथ … नित्यग्रहणं किम्? विधोता, विधविता — विदुधविथ".
- **7.2.63** ऋतो भारद्वाजस्य is a niyama. The thal prohibition is **nitya only for ṛ-final roots**
  and optional for other ajantas. KV verbatim:
  > ऋकारान्ताद् धातोर्भारद्वाजस्याचार्यस्य मतेन तासाविव नित्यानिटस्थलीडागमो न भवति। **स्मर्ता — सस्मर्थ। ध्वर्ता — दध्वर्थ।** … ऋत एव भारद्वाजस्य, नान्येषां धातूनाम्। ययिथ। वविथ।

  SK's saṅgraha: "ऋदन्त ईदृङ् नित्यानिट्" (and the scope note uses PŚ 62 अनन्तरस्य विधिर्वा भवति प्रतिषेधो वा).
- **7.2.64** बभूथाततन्थजगृम्भववर्थेति निगमे. KV: "ववर्थ — … **ववरिथेति भाषायाम्।** क्रादिसूत्रादेवास्य प्रतिषेधे सिद्धे नियमार्थं वचनम् — निगम एव न भाषायामिति॥".
  KV on 7.2.13 says the same: "वृञो हि थलि ववर्थ इति निपातनाद् व्यवस्था". SK 7.2.64: "तेन भाषायां थलीट् । ववरिथ । ववृव । ववृवहे ।"

### Correct 2sg thal forms

| root | form | reason |
|---|---|---|
| हृ | जहर्थ `jaharTa` | 7.2.61 + 7.2.63 (ṛ-final, nitya-aniṭ) |
| घृ | जघर्थ `jaGarTa` | same |
| स्मृ | सस्मर्थ `sasmarTa` | same; KV example verbatim |
| स्तृञ् | तस्तर्थ `tastarTa` | same |
| पृ (5) | पपर्थ `paparTa` | same |
| स्पृ | पस्पर्थ `pasparTa` | same |
| वृञ् | ववरिथ `vavariTa` | 7.2.64: no-iṭ thal only in nigama |

### Two engine bugs

1. **Loop gives iṭ** (`jahariTa`, `jaGariTa`, `sasmariTa`, `tastariTa`, `papariTa`). Either 7.2.61
   does not fire, or krādi-niyama iṭ is applied after it. Fix:
   - 7.2.61's cond: the dhātu is ac-final in upadeśa, and it is aniṭ in tās with **no** optional-iṭ
     rule for tās (7.2.10 anudātta-upadeśa ekāc; not covered by 7.2.44 svaratisūti…, 7.2.38, etc.).
   - 7.2.63 then keeps the prohibition nitya for ṛ-final roots and turns it into an option for the
     rest (ययाथ / ययिथ).
   - Also, a root like स्वृ (ṛ-final but vā-iṭ in tās by 7.2.44) must still get iṭ: सस्वरिथ.
     That is the KV "नित्यग्रहणं किम्" point.
2. **Recipe abhyāsa is wrong** (`smasmarTa`, `spasparTa`, `stastarTa`). 7.4.60 हलादिः शेषः with
   7.4.61 शर्पूर्वाः खयः: with st- and sp- the **khay** survives (त-, प-), giving तस्तर्थ and पस्पर्थ.
   With sm- the म is not khay, so the first hal survives, giving **स**स्मर्थ.

The vavarTa / vavariTa direction: the recipe's `vavarTa` is wrong, and the loop and Vidyut's
`vavariTa` is right.

---

## 4. कूङ् / कुङ् / गुरीँ (tudādi) — no guṇa, because they are kuṭādi

**1.2.1 गाङ्कुटादिभ्योऽञ्णिन्ङित्.** KV defines the range:
> कुटादयोऽपि **<<कुट कौटिल्ये>> इत्येतदारभ्य यावत् <<कुङ् शब्दे>> इति।** एभ्यो गाङ्कुटादिभ्यः परेऽञ्णितः प्रत्यया ङितो भवन्ति … उत्कुटिता। उत्कुटितुम्।

SK in the tudādi list closes the gaṇa on exactly these roots:
> {गुरी} उद्यमने । अनुदात्तेत् । गुरते । जुगुरे । **गुरिता** । …
> {कुङ्} शब्दे । दीर्घान्त इति कैयटादयः । **कुविता । अकुविष्ट ।** ह्रस्वान्त इति न्यासकारः । **कुता । अकुत ।** वृत् । **कुटादयो वृत्ताः ।**

Every non-ñit, non-ṇit pratyaya after these roots (sya, tās, iṭ, sīyuṭ, sic) is therefore ṅit, and
1.1.5 क्ङिति च blocks guṇa. Vidyut's कविष्यते, कोष्यते, गोरिष्यते, कोता, अकोष्ट are wrong. The engine
loop is right. The repo already tags these roots through `antarganas`, so the data supports this.

**DP note.** `06.0136 kuN` (aniṭ) and `06.0137 kUN` (seṭ) are the two readings of one root that SK
reports (Nyāsa: hrasvānta, aniṭ; Kaiyaṭa: dīrghānta, seṭ). Keep both entries. Both are inside
kuṭādi. Do **not** apply this to bhvādi `01.1103 kuN` (कवते, चुकुवे; SK under 6.4.87), which is
outside kuṭādi.

**Correct forms (ātmane)**

| root | luṭ | lṛṭ | luṅ 3sg | luṅ 2pl | āśīr 2pl |
|---|---|---|---|---|---|
| कूङ् | कुविता | कुविष्यते | अकुविष्ट | अकुविढ्वम् / अकुविध्वम् | कुविषीढ्वम् / कुविषीध्वम् |
| कुङ् (6) | कुता | कुष्यते | अकुत | अकुढ्वम् | कुषीढ्वम् |
| गुरीँ | गुरिता | गुरिष्यते | अगुरिष्ट | अगुरिढ्वम् / अगुरिध्वम् | गुरिषीढ्वम् / गुरिषीध्वम् |

**Remaining engine bugs**
- **Recipe for कूङ्: no uvaṅ.** It gives `kUizyate` and `akvizwa`. 6.4.77 अचि श्नुधातुभ्रुवां य्वोरियङुवङौ
  turns dhātu-final ऊ before an ac into उव्. KV: "लुलुवतुः, लुलुवुः". It is the apavāda of 6.1.77
  (yaṇ), and PŚ 55 वार्णादाङ्गं बलीयो भवति also favours the aṅga rule. Correct: कुविष्यते, अकुविष्ट.
- **कुङ् luṅ 2pl: loop is right.** The loop gives `akuQvam`, the recipe `akuDvam`. sic is deleted:
  by 8.2.27 ह्रस्वादङ्गात् before त (अकुत, SK), and by 8.2.25 धि च before ध्वम्. Then 8.3.78 इणः षीध्वंलुङ्लिटां धोऽङ्गात् applies: उ is in iṇ, and
  the dhvam belongs to luṅ, so ध becomes ढ: **अकुढ्वम्**. The same reasoning gives āśīr **कुषीढ्वम्**
  (loop `kuzIQvam` is right).
- **गुरी / कूङ् after iṭ: two forms.** 8.3.79 विभाषेटः makes the ढ optional, so both forms are
  correct. See §8e.

---

## 5. Ātmane luṅ 1sg of ksa roots: अधुक्षि — 7.3.72 क्सस्याचि

The rule is **7.3.72 क्सस्याचि** (data `i=73072`). It has nothing to do with ārdhadhātuka.
KV verbatim:
> क्सस्याजादौ प्रत्यये लोपो भवति। **अधुक्षाताम्। अधुक्षाथाम्। अधुक्षि।** अचीति किम्? अधुक्षत्। अधुक्षताम्।

SK under विष्लृ: "तङि क्सः । अजादौ क्सस्याचि इति अल्लोपः । **अविक्षत । अविक्षाताम् । अविक्षन्त** ॥"

Before any ac-initial ending (इ, आताम्, आथाम्, and अन्त from झ via 7.1.3), the final a of ksa is
deleted. So you get अधुक्षि (not अधुक्षे), अधुक्षाताम् (not अधुक्षेताम्), and अविक्षन्त (not the
recipe's `avikzAnta`).

**The earlier "fix" has the wrong basis.** CONFLICTS.md records "7.2.81 not in luṅ (अधुक्षाताम्)".
That basis is unsound:
- luṅ tiṅ endings are sārvadhātuka (3.4.113).
- 7.2.81's text has no lakāra restriction. KV gives पचेते, पचेताम्.

The real reason is a vipratiṣedha. Both 7.2.81 (ā of a ṅit ending after an a-final aṅga becomes iy)
and 7.3.72 (lopa of ksa's a) apply at the same moment. **1.4.2 विप्रतिषेधे परं कार्यम्** picks
7.3.72, the later sūtra. Once ksa has lost its a, the aṅga is no longer a-final, so 7.2.81 has
nothing to apply to.

So: put 7.2.81 back for luṅ, gated only by its own cond (a-final aṅga + ṅit sārvadhātuka ā), and let
the resolver choose 7.3.72 by paratva. Otherwise aṅ/caṅ luṅ ātmane duals, where the aṅga does end in
the a of aṅ/caṅ, will lose their -एताम्/-एथाम्.

**Cells:** duh, dih, lih, dviṣ, diś, viṣ (luṅ Ā): 1sg -क्षि, 3du -क्षाताम्, 2du -क्षाथाम्,
3pl -क्षन्त. Note 7.3.73 लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये gives optional अदुग्ध / अधुक्षत etc.
before dental-initial endings (an alternate; see §8e).

---

## 6. Kryādi ātmane: क्रीणीते (not क्रियिणाते)

Derivation of क्री + श्ना + ते:
1. श्ना (3.1.81) is śit, so it is sārvadhātuka, and apit, so it is ṅit (1.2.4). That blocks guṇa of
   क्री (1.1.5).
2. **No iyaṅ.** 6.4.77 requires an **ac**-initial pratyaya ("अचीति किम्? आप्नुयात्", KV). श्ना begins
   with न्.
3. ṇatva by 8.4.2 gives क्रीणा.
4. ते is apit sārvadhātuka, so it is ṅit. **6.4.113 ई हल्यघोः** turns the ā of śnā into ī before a
   hal-initial kṅit sārvadhātuka. KV: "लुनीते। पुनीते।". Result: **क्रीणीते**.
5. Before ac-initial endings, **6.4.112 श्नाऽभ्यस्तयोरातः** applies (ā-lopa; KV: "लुनते। लुनताम्।
   अलुनत।"). Dual: क्रीण्+आते gives **क्रीणाते**. Plural: झ→अत by 7.1.5 आत्मनेपदेष्वनतः
   (KV: "पुनते। लुनते।"), giving **क्रीणते**.

SK 3.1.81: "क्रीणाति । ई हल्यघः क्रीणीतः । … क्रीणन्ति । **क्रीणीते । क्रीणाते ।**"

The loop's `kriyiRAte` has an iyaṅ that 6.4.77 forbids, and it skips 6.4.113. Correct cells:
लट् क्रीणीते, लङ् अक्रीणीत, लोट् क्रीणीताम्.

---

## 7. Smaller items

### 7a. अद् laṅ: आदत्, आदः — both engine and Vidyut are wrong

**7.3.100 अदः सर्वेषाम्.** KV: "अद भक्षणे अस्मादुत्तरस्यापृक्तस्य सार्वधातुकस्याडागमो भवति
**सर्वेषामाचार्याणां मतेन। आदत्। आदः।**"
SK: "आदत् । आत्ताम् । आदन् । आदः । आत्तम् । आत्त । आदम् …".

The augment अट् is added to the apṛkta त्/स्. Because of सर्वेषाम् it is **nitya**. Vidyut's
`Ad/At` and the engine's `Adt` both miss it. The 7.3.100 cond: the aṅga is the dhātu अद्, and the
following pratyaya is an apṛkta (single-consonant) hal-initial sārvadhātuka.

### 7b. अद् luṅ: अघसत् — the loop's `akzat` is wrong

2.4.37 लुङ्सनोर्घसॢ, then ḷdit, so 3.1.55 gives aṅ: अघसत्. The upadhā-lopa of
**6.4.98 गमहनजनखनघसां लोपः क्ङित्यनङि** is excluded **before aṅ**. KV: "**अनङीति किम्? अगमत्।
अघसत्।**" The loop ignores *anaṅi*. Prayoga: अघसन् (Bhaṭṭikāvya 5.66, cited under 2.4.37 in
`sutra_prayogas`).

### 7c. षुञ् / ष्टुञ् luṅ parasmai: असावीत्, अस्तावीत्

**7.2.72 स्तुसुधूञ्भ्यः परस्मैपदेषु** adds iṭ to sic. KV: "**अस्तावीत्। असावीत्। अधावीत्।**
परस्मैपदेष्विति किम्? अस्तोष्ट। असोष्ट।" With iṭ present, 7.2.1 vṛddhi of the ajanta aṅga gives
सौ→साव्. Then 7.3.96 adds īṭ and 8.2.28 deletes sic, giving असावीत्.

SK adds: "पूर्वोत्तराभ्यां ञिद्भ्यां साहचर्यात्सुनोतेरेव ग्रहणम् इति पक्षे असौषीत्". So 7.2.72's
"सु" is **svādi सुञ्** (05.0001). For bhvādi/adādi षु (01.1091, 02.0036) the regular aniṭ असौषीत् is
allowed on that view. The engine's `asOzIt` for 5 षुञ् is wrong.

### 7d. भसँ (3, chāndasa): बब्धः, बप्सति, अबभत्, अबब्धाम्, प्स्यात्

- **6.4.100 घसिभसोर्हलि च** deletes the upadhā before hal- and ac-initial kṅit pratyayas. Its
  anuvṛtti carries छन्दसि, but DP and SK class भस् as a chāndasa root ("अथ आगणान्ताः परस्मैपदिनश्छान्दसाश्च"),
  so the rule applies to it.
- SK: "{भस} भर्त्सनदीप्त्योः । बभस्ति । घसिभसोर्हलिच इत्युपधालोपः । झलो झलि इति सलोपः । **बब्धः ।
  बप्सति ।**"
- KV 6.4.100: "बब्धामिति भसेर्लोटि तामि … उपधालोपसलोपधत्वजश्त्वानि".

Chain for बब्भ्-तस्: 6.4.100 upadhā-lopa gives बभ्स्तस्; 8.2.26 deletes स; 8.2.40 झषस्तथोर्धोऽधः
turns त into ध; 8.4.53 jaśtva turns भ into ब. Result: **बब्धः**. The loop's `bapstaH` skips 8.2.26
and 8.2.40.

- **laṅ 3sg:** halṅyādi-lopa of त् gives अबभस्. Then **8.2.73 तिप्यनस्तेः** (स→द् before tip, except
  for अस्; KV: "अचकाद् भवान्") gives अबभद्, and 8.4.56 gives **अबभत् / अबभद्**. The engine's
  `abaBaH` is wrong.
- **āśīr:** yāsuṭ is kit (3.4.104), so 6.4.100 applies: भ्स्यात्. 8.4.55 then gives **प्स्यात्**.

### 7e. भ्रस्जँ (6): भ्रक्ष्यति / भर्क्ष्यति etc.

- **6.4.47 भ्रस्जो रोपधयोः रमन्यतरस्याम्** applies before ārdhadhātuka: र and the upadhā स् are
  optionally replaced by रम्, which gives भर्ज्.
  KV: "भ्रष्टा, भर्ष्टा … भ्रज्जनम्, भर्जनम्". SK: "बभर्ज … बभर्जे । रमभावे । बभ्रज्ज … बभ्रज्जे ।
  **भ्रष्टा । भर्ष्टा । भ्रक्ष्यति । भर्क्ष्यति ।** … भर्क्षीष्ट । भ्रक्षीष्ट । **अभार्क्षीत् । अभ्राक्षीत् ।
  अभर्ष्ट । अभ्रष्ट ।**"
- **vārt.:** "क्ङिति रमागमं बाधित्वा संप्रसारणं पूर्वविप्रतिषेधेन". Before kṅit there is
  samprasāraṇa only (भृज्ज्यात्).
- The consonant cluster before jhal: **8.2.29 स्कोः संयोगाद्योरन्ते च** deletes स, and **8.2.36
  व्रश्चभ्रस्ज…** turns ज into ष. KV 8.2.36: "भ्रस्ज — भ्रष्टा". Before स, 8.2.41 षढोः कः सि gives
  क्ष. So भ्रक्ष्यति and भ्रष्टा. The engine's `Bradkzyati` / `BradktA` applies jaśtva to स instead of
  8.2.29 + 8.2.36.
- **liṭ ātmane:** भ्रस्ज् ends in a saṃyoga, so liṭ is **not kit** (1.2.5, see 7f). There is no
  samprasāraṇa. The forms are **बभर्जे / बभ्रज्जे**: स→श→ज by 8.4.40 + 8.4.53, and abhyāsa ब by
  7.4.60 + 8.4.54. The loop's `baBfjje` wrongly applies samprasāraṇa. The recipe's `badgBrajje` has a
  broken abhyāsa.
- **āśīr ātmane:** 1.2.11 needs an ik before the final hal, and bhrasj has none. So sīyuṭ is not kit:
  भर्क्षीष्ट / भ्रक्षीष्ट.

### 7f. रञ्ज् ātmane liṭ: ररञ्जे — रेजे belongs to राज्

**1.2.5 असंयोगाल्लिट् कित्.** KV: "**असंयोगादिति किम्? सस्रंसे। दध्वंसे।**" A root ending in a
nasal + consonant cluster keeps its nasal in liṭ, because there is no kit to trigger 6.4.24. The
other nasal-loss rule for this root, 6.4.26 रञ्जेश्च, applies only before **शप्**. Without nasal
loss there is no "ekahalmadhya" a, so 6.4.120 एत्व cannot apply. Result: **ररञ्जे**, ररञ्जाते …

The kāvya रेजे (Śiśupālavadha 3.17, 18.41; Raghuvaṃśa 14.86) is listed in `dhatuprayogas` under
**01.0956 राजृँ** and justified there by **6.4.125 फणां च सप्तानाम्** (optional ettva for rāj etc.).
It is not a form of रञ्ज्. The loop's `reje` for 4 रञ्ज् is wrong.

### 7g. ईङ् (4) liṭ: अयाञ्चक्रे

ई is ijādi (ई ∈ ic) and gurumat (1.4.12), so **3.1.36 इजादेश्च गुरुमतोऽनृच्छः** adds ām. ām is
ārdhadhātuka, so 7.3.84 gives guṇa: ई→ए→अय् (6.1.78). Then 3.1.40 adds the कृञ् anuprayoga.
SK: "{ईङ्} गतौ । ईयते । **अयांचक्रे** ।"

The engine has two bugs:
- recipe `IAYcakre`: missing guṇa before ām;
- loop `yAYcakre`: it applied yaṇ to ई. 6.1.77 cannot apply, because guṇa (7.3.84) runs first: ām is
  the very ārdhadhātuka that triggers it.

Expected forms: अयाञ्चक्रे / अयामास / अयाम्बभूव.

### 7h. ईश् / ईड् laṅ dhvam: ऐड्ढ्वम् — Vidyut is right, not a mapping error

KV 7.2.78 ईडजनोर्ध्वे च:
> … ध्वेशब्द ईशेरपि इडागम इष्यते — ईशिध्वे, ईशिध्वमिति। … **ध्व इति कृतटेरेत्वस्य ग्रहणात् लङि ध्वमि न भवितव्यमिटा। लोटि पुनरेकदेशविकृतस्यानन्यत्वाद् भवितव्यमिटा॥**

SK: "ईशीड्जनां से ध्वे शब्दयोः सार्वधातुकयोरिट् स्यात् … ईडिध्वे … [एकदेशविकृतस्यानन्यत्वात्]
ईडिष्व । ईडिध्वम् । विकृतिग्रहणेन प्रकृतेरग्रहणात् । **ऐड्ढ्वम्** ।"

The iṭ goes only to **ध्वे**, the form that has gone through ṭi→e (3.4.79):
- **laṭ** ध्वे gets iṭ: ईडिध्वे, ईशिध्वे.
- **loṭ** ध्वम् (from ध्वे, by 3.4.91) gets iṭ through PŚ 37 एकदेशविकृतमनन्यवत्: ईडिध्वम्, ईशिध्वम्.
- **laṅ** ध्वम् is the original ending, never ध्वे, so it gets **no** iṭ.

Chain for laṅ: ऐश्/ऐड्+ध्वम्. 8.2.36 turns श into ष, 8.2.39 turns ष/ड into ड, and 8.4.41 ṣṭutva
turns ध्व into ढ्व. Result: **ऐड्ढ्वम्** `EqQvam` for **both** roots. The loop's `ESiDvam` and
`EqiDvam` over-apply 7.2.77/7.2.78.

**Implementation.** The cond of 7.2.78 (and 7.2.77's se) must check that the ending is the
**ṭi→e product** ध्वे / से, or its loṭ continuation सव / ध्वम् by एकदेशविकृत. It must not match a
laṅ ध्वम्.

---

## 8. Earlier open items

### 8a. ऊर्णुञ् liṭ: ऊर्णुनाव (no ām)

Under 3.1.36, KV gives the vārttika:
> ऊर्णोतेश्च प्रतिषेधो वक्तव्यः॥ **प्रोर्णुनाव।** अथवा — वाच्य ऊर्णोर्णुवद्भावो यङ्प्रसिद्धिः प्रयोजनम्। आमश्च प्रतिषेधार्थम् एकाचश्चेडुपग्रहात्॥

So ūrṇu is exempted from 3.1.36. This comes either from the direct pratiṣedha vārttika or from the
**nuvadbhāva** vārttika, whose stated purposes include "आमश्च प्रतिषेधार्थम्". The vārttika is
present in your data, so the CONFLICTS.md note "no sūtra in the data covers nuvat" is answered by KV
on 3.1.36.

Reduplication: 6.1.2 अजादेर्द्वितीयस्य, with **6.1.3 न न्द्राः संयोगादयः** (the र is not doubled).
SK: "नुशब्दस्य द्वित्वम् । णत्वस्यासिद्धत्वात् … **ऊर्णुनाव । ऊर्णुनुवतुः । ऊर्णुनुवुः ॥**"
Prayoga: ऊर्णुनाव, Śiśupālavadha 19.21 (`sutra_prayogas` under 6.1.2).

Other forms:
- thal: 1.2.3 विभाषोर्णोः makes iṭ optionally ṅit, giving ऊर्णुनविथ / ऊर्णुनुविथ.
- uttama 1sg: 7.1.91 णलुत्तमो वा gives ऊर्णुनाव / ऊर्णुनव.
- ātmane: ऊर्णुनुवे …; 2pl ऊर्णुनुविध्वे / -ढ्वे by 8.3.79.

All of this matches Vidyut.

**Implementation.** Encode the vārttika as an exception inside 3.1.36's cond: dhātu ≠ ऊर्णु. Cite
"KV 3.1.36 vārt. ऊर्णोतेश्च प्रतिषेधो वक्तव्यः" (Art. 14). It is not a new `_arm`.

### 8b. चक्षिँङ् ātmane liṭ — Vidyut and engine are both wrong

- **2.4.54 चक्षिङः ख्याञ्** applies before ārdhadhātuka. KV adds "क्शादिरप्ययमादेश इष्यते".
- **2.4.55 वा लिटि**: in liṭ the substitution is optional. KV: "**आचख्यौ, आचख्यतुः, आचख्युः। न च भवति — आचचक्षे, आचचक्षाते, आचचक्षिरे॥**"
- SK 2.4.55: "ञित्त्वात्पदद्वयम् । **चख्यौ-चख्ये-चक्शौ-चक्शे** … **चचक्षे** ।"

So for ātmane 3sg the valid forms are **चचक्षे** (no substitution), **चख्ये**, and **चक्शे**. There
is **no ām**: चक्ष् is not ijādi, and nothing in 3.1.35–39 covers it. Vidyut's `cakzayAYcakre` is a
ṇijanta form and does not belong in the shuddha cell. The engine's `cacakziye` keeps the इ of चक्षिँङ्.
SK says "इकारोऽनुदात्तो युजर्थः", so that इ is an **it**: it marks the root anudātta-it for ātmanepada
and is deleted by 1.3.2.

Unsubstituted paradigm: चचक्षे, चचक्षाते, चचक्षिरे, चचक्षिषे, चचक्षाथे, चचक्षिध्वे (क्ष is not iṇ,
so 8.3.79 does not apply), चचक्षे, चचक्षिवहे, चचक्षिमहे.

### 8c. आसँ ātmane liṭ: आसाञ्चक्रे

आ is not in ic, so 3.1.36 does not apply. The rule is **3.1.37 दयायासश्च**. KV: "दयाञ्चक्रे।
पलायाञ्चक्रे। **आसाञ्चक्रे॥**". SK under आस: "दयायासश्च । आसांचक्रे ।"

The engine's `Ase` misses 3.1.37. The cond: dhātu ∈ {दय्, अय्, आस्} in liṭ. Forms: आसाञ्चक्रे /
आसामास / आसाम्बभूव, with 1.3.63 आम्प्रत्ययवत् कृञोऽनुप्रयोगस्य making कृ ātmane.

### 8d. असुँ (4, क्षेपणे) luṅ: आस्थत्

**3.1.52 अस्यतिवक्तिख्यातिभ्योऽङ्** (aṅ in both padas; SK notes that puṣādi 3.1.55 already covers
parasmai, so 3.1.52 is needed "तङर्थम्"), then **7.4.17 अस्यतेस्थुक्**. KV: "**आस्थत्, आस्थताम्,
आस्थन्।**" Then 6.4.72 adds āṭ and 6.1.90 gives vṛddhi.

Prayoga: Raghuvaṃśa 12.23 "तस्मिन्नास्थदिषिकास्त्रम्" (`dhatuprayogas` 04.0106, `plung_1_1`), and
Śiśupālavadha 18.30 (`sutra_prayogas` under 3.1.52 and 7.4.17). Ātmane: पर्यास्थत (SK 7.4.17).

### 8e. Optional alternates (vibhāṣā) — what to generate

Each of these sūtras carries वा / विभाषा / अन्यतरस्याम् / a vārttika "वा" in data or KV. The
glass-box way to cover them is for the dispatcher to **fork the state** when a sūtra whose record is
marked `optional` (from its own text) is applicable. Run both continuations and return the set.
This needs no surface lists and no new `_arm`.

| sūtra | effect | example pair |
|---|---|---|
| 7.3.90 ऊर्णोतेर्विभाषा | vṛddhi before hal pit sārvadhātuka | और्णोत् / और्णौत् |
| 8.3.79 विभाषेटः | ढ after iṇ + iṭ | अकुविढ्वम् / अकुविध्वम्, गुरिषीढ्वम् / -ध्वम् |
| 3.1.38 उषविदजागृभ्योऽन्यतरस्याम्, 3.1.39 भीह्रीभृहुवां श्लुवच्च | ām in liṭ | बिभयाञ्चकार / बिभाय |
| 6.4.68 वाऽन्यस्य संयोगादेः | ए in āśīr | ग्लेयात् / ग्लायात् |
| 7.2.63 (by niyama, for non-ṛ ajanta) | thal iṭ | ययाथ / ययिथ |
| 7.3.86 + संज्ञापूर्वको विधिरनित्यः (tanādi) | laghūpadha guṇa before उ | घर्णुहि / घृणु, अर्णोति / ऋणोति |
| 3.1.82 श्नुश्च | śnu beside śnā | स्कभान / स्कभ्नुहि |
| 7.3.73 लुग्वा दुहदिहलिहगुहाम् | ksa-luk before dentals | अदुग्ध / अधुक्षत |
| 6.4.47 भ्रस्जो रोपधयो रमन्यतरस्याम् | ram | भर्क्ष्यति / भ्रक्ष्यति |
| 2.4.55 वा लिटि | ख्याञ्/क्शाञ् in liṭ | चख्ये / चक्शे / चचक्षे |
| 1.2.3 विभाषोर्णोः | iṭ ṅit | ऊर्णुनविथ / ऊर्णुनुविथ |
| 7.1.91 णलुत्तमो वा | ṇal-uttama ṇit | ऊर्णुनाव / ऊर्णुनव |
| 8.4.56 वाऽवसाने | final car | अबभत् / अबभद् |
| 6.4.125 फणां च सप्तानाम् | ettva / abhyāsa-lopa | रेजे / रराजे |
| 7.2.72 (SK sāhacarya view) | iṭ only for svādi su | असौषीत् (bhvādi/adādi षु) |

---

## Paribhāṣās relied on (Art. 21)

| PŚ # / source | text | used in |
|---|---|---|
| 1.4.2 (sūtra) | विप्रतिषेधे परं कार्यम् | §5: 7.3.72 over 7.2.81 |
| PŚ 37 | एकदेशविकृतमनन्यवत् | §7h: loṭ ध्वम् keeps 7.2.78 iṭ |
| PŚ 50 | असिद्धं बहिरङ्गमन्तरङ्गे | §2a ordering: 7.3.86 on उ comes before 6.4.106 on hi |
| PŚ 55 | वार्णादाङ्गं बलीयो भवति | §4: uvaṅ (6.4.77) over yaṇ |
| PŚ 62 | अनन्तरस्य विधिर्वा भवति प्रतिषेधो वा | §3: scope of the 7.2.63 niyama (SK) |
| (Vyāḍi/SK) | संज्ञापूर्वको विधिरनित्यः | §2a: optional laghūpadha guṇa for tanādi |
| 1.1.62 / 1.1.63 | प्रत्ययलोपे प्रत्ययलक्षणम् / न लुमताङ्गस्य | §2: *not* needed; the triggers are उ and शानच्, not the lost hi |
| KV 7.3.73 (MBh 1.154) | पूर्वत्रासिद्धे न स्थानिवत् | §5: ksa a-lopa is not sthānivat for 8.2.26 |

---

## Regression cells to pin (suggested tests, gold from KV/SK)

```text
3 Riji~r laG P 1-1  anenijam        # KV 7.3.87
3 Riji~r loT P 1-1  nenijAni        # KV 7.3.87
3 viji~r loT P 1-1  vevijAni        # KV 7.3.87
3 vizx~  loT P 1-1  vevizARi        # KV 7.3.87 (परिवेविषाणि)
3 YiBI   loT P 1-1  biBayAni        # KV 7.3.87 pratyudāharaṇa जुहवानि
8 tfRu~  loT P 2-1  {tarRuhi, tfRu} # SK tanādi + KV 6.4.106; never tarRu
9 stanBu~ loT P 2-1 staBAna         # SK 3.1.83
1 smf / 5 smf liT P 2-1  sasmarTa   # KV 7.2.63
5 vfY    liT P 2-1  vavariTa        # KV 7.2.64
6 gurI~  luT A 3-1  guritA          # SK (kuṭādi)
6 kUN    lRT A 3-1  kuvizyate       # SK कुविता + 6.4.77
2 duha~  luG A 1-1  aDukzi          # KV 7.3.72
2 duha~  luG A 3-2  aDukzAtAm       # KV 7.3.72
9 qukrIY laT A 3-1  krIRIte         # SK 3.1.81, KV 6.4.113
2 ada~   laG P 3-1  Adat            # KV/SK 7.3.100
2 ada~   luG P 3-1  aGasat          # KV 6.4.98 anaṅi
2 zwuY   luG P 3-1  astAvIt         # KV 7.2.72
3 Basa~  laT P 3-2  babDaH          # SK
6 Brasja~ lRT P 3-1 {Brakzyati, Barkzyati}   # SK 6.4.47
4 ranja~ liT A 3-1  raraYje         # KV 1.2.5
4 IN     liT A 3-1  ayAYcakre       # SK
2 Iqa~   laG A 2-3  EqQvam          # KV 7.2.78, SK ऐड्ढ्वम्
2 UrRuY  liT P 3-1  UrRunAva        # KV 3.1.36 vārt., SK 6.1.3
2 cakziN liT A 3-1  {cacakze, caKye, cakSe}  # KV/SK 2.4.55
2 Asa~   liT A 3-1  AsAYcakre       # KV 3.1.37
4 asu~   luG P 3-1  AsTat           # KV 7.4.17
```

## Not covered here

These cells are in `RECHECK_2026-10-06.txt` but were not in your list, so I did not resolve them:
dyuta~, sranBu~, mAN/qudAY/quDAY āśīr, f, pf (3), SFY, qumiY/mIY, rADa~, vyuza~, pluza~, Raha~,
Saka~, lupx~/mucx~/vidx~, tfha~, anjU~, undI~, hisi~, kfza~, o~hAk, mila~, dIN. Two pointers from the
same sources:
- ऋ (3): SK 7.3.87 gives इयर्ति, इयृतः, इय्रति, आर, ऐयः, ऐयृताम्, ऐयरुः, इयृयात्, अर्यात्, आरत्, which
  match Vidyut.
- पृ (3, ह्रस्व): SK says "ह्रस्वान्तोऽयमिति केचित् । पिपर्ति । पिपृतः । पिप्रति । पिपृयात्", so the
  engine's पिपर्ति follows an accepted view (7.4.77), not Vidyut's पपर्ति.
