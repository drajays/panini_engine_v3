# PARKED_ISSUES_RESOLVED — AI-drafted resolutions, re-verified against the brain (2026-10-06)

**Verification status** (brain = `~/data-master/ashtadhyayi-ai`: sūtra table, dhātu table, SK/Kāśikā/Bhāṣya texts)

| Item | Status | What the brain says |
|---|---|---|
| (a) caha~ | **VERIFIED — engine right** (reason corrected) | dhātu rows: curādi `10.0120 caha~` sits inside the jñapādi mit run (jYapa~ 0118, yama~ 0119, caha~ 0120, capa~ 0121, raha~ 0122, bala~ 0123, ciY 0124); a second non-mit kathādi `10.0405 caha` exists; bhvādi `1.0830 caha~` too. SK 6.4.92: "caha parikalkane. cahayati. acIcahat. kaTAdO … acacahat". Mit ⇒ 6.4.92 blocks the vṛddhi of 7.2.116 ⇒ cahayati. Vidyut's cAhayati for `caha~` treats the mit row as non-mit. The draft's phrase "kathādi-style vṛddhi" is muddled; the SK text is what decides. |
| (b) fRu~ loṭ 2sg | **VERIFIED as a real engine bug; fix not yet written** | SK 2.4.79 has the paradigm "ऋणोति। अर्णोति। अर्णुतः। अर्ण्वन्ति"; 6.4.106 (Kāśikā/SK) needs asaṃyogapūrva. Engine/Vidyut agree on all cells except 2sg: engine luk's the hi of the guṇa stem (arRu); the guṇa stem has saṃyoga rR so luk is barred ⇒ arRuhi, the aguṇa stem gives fRu. Fix needs (1) guṇa before the 6.4.106 test and (2) the vibhāṣā fork of (e). |
| (c) gurI~ | **VERIFIED — engine right** | dhātu row `6.0131 gurI~\` (tudādi, ātmane) lies between kruqa~/huqa~ and ku\N 6.0136 = inside the kuṭādi run ⇒ 1.2.1 ṅidvat ⇒ no guṇa (1.1.5). Separate rows gUrI~ (4.0049) and gUra~ (10.0217) exist, so there is no ātmane/gura mix-up in the engine's tag. Vidyut's gorizIzwa is the non-kuṭādi treatment. |
| (d) sf luṅ / Divi~ | **VERIFIED — engine right** | SK 3.1.56 "tena bhvādyor nāṅ" (bhvādi sf takes sic: asArzIt); Kāśikā 3.1.80 "hivi Divi jivi prINanArTAH … upratyayo Bavati, akArascāntādeśaH" ⇒ Dinvati. |
| (e) vibhāṣā cells | **VERIFIED, with one correction** | 1.2.3 vibhāṣorṇoḥ (SK: UrRunuviTa/UrRunaviTa, UrRuvitA/UrRavitA) ✔; 3.1.44 vārttika "spṛśamṛśakṛṣatṛpadṛpāṃ ca…" with Kāśikā forms asprākṣīt/aspārkṣīt/aspṛkṣat, akārkṣīt/akṛkṣat ✔; 6.1.39 ✔. **Correction:** the draft cites 8.3.117 for nyaṣīdat/nyasīdat — that is **8.3.119** (nivyabhibhyo'ḍvyavāye vā *chandasi*): Vedic only, laukika has one form. |
| (f) 6.1.8 loss / hang | Engine defect, not grammar (agrees with our finding) | — |
| (g) 40 "gate-only" sūtras | **VERIFIED in substance, sūtra numbers wrong in the draft** | Brain numbering: 8.3.115 soḍhaḥ · 8.3.116 stambhusivusahāṃ caṅi · **8.3.117 sunoteḥ syasanoḥ** · **8.3.118 sadeḥ parasya liṭi** (sad/svañj: abhiṣasāda, pariṣasvaje) · 8.3.119 nivyabhibhyo'ḍvyavāye vā chandasi · 8.4.14 upasargād asamāse'pi ṇopadeśasya ✔ · 6.1.15/16/17/19/37/38/39/40 ✔ (texts match). The draft shifted 8.3.115–117 by two. |
| (h) stale recipe | closed | — |

Use these verdicts; where the table says "corrected", the corrected form below the line is authoritative.

---

# PARKED_ISSUES — resolved against primary/commentarial sources

Scope: the eight tiṅanta items in `uploads/PARKED_ISSUES.md`. For each item: **verdict**
(engine / Vidyut / neither), the **sūtra-gaṇasūtra basis** (with number), and the
**commentary authority** (Kāśikā, Bālamanoramā, Siddhāntakaumudī, Dhātupāṭha + its readings).
When the tradition or the editions genuinely split, that is stated explicitly.

## Sources used (all local, reproducible)

| Source | Local file | Note |
|---|---|---|
| Kāśikā, Bālamanoramā, Laghu-Śabdenduśekhara, Tattvabodhinī, Vasu (per sūtra) | `research/avg/<n-n-n>.html` (via `strip.py`) | fetches from avg-sanskrit.org/sutras/ |
| Siddhāntakaumudī (sa.wikisource, प्रकरण 41–50 / 51–60 / 61–71) | `research/sk41_50.txt`, `sk51_60.txt`, `sk61_71.txt` | SK's own vṛttis and examples |
| Dhātupāṭha, sa.wikisource edition | `research/ws_dhatupatha.txt` | gaṇa headings + numbering; cites sūtras in headings (e.g. "कुटादयः (1.2.1)") |
| Dhātupāṭha (digital, Vidyut) + gaṇasūtras | `research/vidyut_dhatupatha.tsv`, `vidyut_ganasutras.tsv` | SLP1; used as the second pāṭha witness |

Method: the sūtra text is quoted from the Kāśikā/Prathamāvṛtti tradition, the pāṭha from an
independent edition and from Vidyut's transcription, and the *forms* from the SK and the
commentaries' own examples. Engine and Vidyut outputs are treated as claims to be tested, never
as evidence.

---

## (a) `caha~` curādi — **engine right; Vidyut's `cAhayati` wrong**

The engine generates **चहयति**; Vidyut **चाहयति** (i.e. Vidyut applies the non-mit, kathādi-style
treatment).

Evidence:

1. **Mit status.** The curādi portion of the Dhātupāṭha carries the gaṇasūtra **ज्ञपादयो मितः**
   (Vidyut `10.0493 jYapAdayo mitaH`; the parallel bhvādi gaṇasūtra is `01.0933 GawAdayo mitaH`,
   i.e. *घटादयो मितः*). The Siddhāntakaumudī prints the mark in the pāṭha itself — SK चुरादि:
   **"ज्ञप मिच्च"** (root 1625) — and the Bālamanoramā states the range for **चह** explicitly:
   *"चह परिकल्पने इति। इत आरभ्य 'चिञ् चयने' इत्येतत्पर्यन्तं चेत्यनुवर्तते। अतस्तेषां मित्त्वण्णिचि
   ह्रस्वः। तदाह — चहयतीति"* (Bālamanoramā 395, on *मितां ह्रस्वः*). The mit members are ज्ञप्,
   यम् (चान्मित्), **चह**, रह, बल, चिञ्.
2. **The sūtra.** **6.4.92 मितां ह्रस्वः** — Kāśikā: *"मितो धातवः 'घटादयो मितः' इत्येवम् आदयो ये
   प्रतिपादिताः, तेषाम् उपधाया ह्रस्वो भवति णौ परतः। घटयति। व्यथयति। जनयति। रजयति। शमयति।
   ज्ञपयति।"* (Note that it is the **jñapādi** list inside curādi, not the bhvādi ghaṭādi list,
   that covers चह.)
3. **SK's own paradigm.** SK चुरादि: **"चह परिकल्कने। चहयति। अचीचहत्"**, with the note that चह
   is *also* repeated in the kathādi group (अचचहत् for the non-mit treatment; चप इत्येके).

⇒ **चहयति** is the form the tradition derives; Vidyut's `cAhayati` reflects the *kathādi*
(वृद्धि) treatment and is incorrect for the mit reading. **Engine correct.**

---

## (b) `fRu~` (√ऋणु, तनादि) loṭ 2sg — **neither as posed; engine's `arRu` wrong, Vidyut's set right**

The engine produced bare **अर्णु**; Vidyut produced **{अर्णुहि, अर्णुतात्, ऋणु, …}**.

Evidence:

1. **Vikaraṇa.** **3.1.79 तनादिकृञ्भ्यः उः** (u-vikaraṇa; Kāśikā: *"तनु विस्तारे इत्येवम् आदिभ्यो
   धातुभ्यः कृञश्च उप्रत्ययो भवति। शपोऽपवादः। तनोति। सनोति। क्षणोति।"*).
2. **The paradigm (SK, तनादि, "अथ सप्त स्वरितेतः").** *"ऋणु गतौ। ऋणोति। अर्णोति। अर्णुतः।
   अर्ण्वन्ति। आनर्ण। आनृणे। अर्णितासे। आर्णीत्। आर्त। आर्णिष्ट। आर्थाः। आर्णिष्ठाः"* — the
   tradition's own paradigm keeps **both** an aguṇa stem (ऋणोति, आनृणे) and a guṇa stem
   (अर्णोति, अर्णुतः, आनर्ण, आर्णीत्). (Matches independent lexica: कविकल्पद्रुम/वाचस्पत्यम्
   "अर्णोति ऋणोति, ऋणुते".)
3. **The rule that actually decides the 2sg.** **6.4.106 उतश्च प्रत्ययादसंयोगपूर्वात्** — Kāśikā:
   *"उकारो योऽसंयोगपूर्वः तदन्तात्प्रत्ययादुत्तरस्य हेर्लुक् भवति। चिनु। सुनु। कुरु। उतः इति किम्?
   लुनीहि। पुनीहि। प्रत्ययातिति किम्? युहि। रुहि। असंयोगपूर्वातिति किम्? **प्राप्नुहि। राध्नुहि।
   तक्ष्णुहि।**"* plus the chandas vikalpa vacana *"उतश्च प्रत्ययाच् छन्दोवावचनम् … आतनुहि
   यातुधानान्। धिनुहि यज्ञपतिम्। तेन मा भगिनं कृणु।"*
   That is: the हि-luk happens only when the pratyaya-final *u* is **not** preceded by a saṃyoga.
4. Hence, from the two legitimate stems:
   * aguṇa stem ऋण् + उ + हि → *u* preceded by a single consonant ⇒ **ऋणु** ✔
   * guṇa stem अर्ण् + उ + हि → *u* preceded by the saṃyoga र्ण् ⇒ **no luk** ⇒ **अर्णुहि** ✔
   (and, with तातङ्, अर्णुतात्). A **bare अर्णु** is precisely what the *pratyudāharaṇa*
   प्राप्नुहि/तक्ष्णुहि excludes; in laukika it is not derivable (the chandas-vā vacana is a
   Vedic licence only).

⇒ The issue's framing "6.4.106 luk vs 7.3.84 guṇa on ऋ" is a false opposition: **7.3.84** supplies
the guṇa (present in the guṇa half of the paradigm, as in अर्णोति/अर्णुतः), and **6.4.106** then
governs *hi*-luk by the *asaṃyogapūrva* condition. **Engine wrong (single bare अर्णु); Vidyut
right (it keeps both stems and blocks luk in the guṇa stem).**

*Note (not the cause):* 2.4.79 **तनादिभ्यस्तथासोः** (SK: *"तनादेः सिचो वा लुक् स्यात्तथासोः
परतः"*) concerns sič-luk before *thās*, not *hi*; it does not govern this cell.

---

## (c) `gurI~` (कुटादि) āśīrliṅ/luṅ/lṛṭ — **engine right; Vidyut's `gori-` forms wrong**

The engine gives **गुरीषीष्ट**-type (no guṇa); Vidyut **गोरीषीष्ट**-type (guṇa of the upadhā).

Evidence:

1. **The root is inside the कुटादि range.** **1.2.1 गाङ्कुटादिभ्योऽञ्णिन्ङित्** — Kāśikā:
   *"गाङिति इङादेशो गृह्यते … **कुटादयोऽपि 'कुट कौटिल्ये' इत्येतदारभ्य यावत् 'कुङ् शब्दे' इति।**
   एभ्यो गाङ्कुटादिभ्यः परे अञ्णितः प्रत्यया ङितो भवन्ति, ङिद्वद् भवन्ति … कुटादिभ्यः कुटिता।
   कुटितुम्। कुटितव्यम्। उत्पुटिता … अञ्णिति किम्? उत्कोटयति। उच्चुकोट। उत्कोटकः।"*
   The pāṭha confirms the extent: the section is headed **"कुटादयः (1.2.1)"** and runs
   *76 कुट कौटिल्ये … **106 गुरी उद्यमने** … 110 ध्रु*, i.e. √गुरी lies between कुट and कुङ्.
2. **Consequence.** A pratyaya following a कुटादि root that is not ञित्/णित् counts as **ṅit**;
   by **1.1.5 क्क्ङिति च** (Kāśikā: *"क्ङिन्निमित्ते ये गुणवृद्धी प्राप्नुतः, ते न भवतः। चितः,
   चितवान् … ङिति खल्वपि चिनुतः, चिन्वन्ति"*) guṇa and vṛddhi are therefore **prohibited**.
   āśīrliṅ (सीयुट्/यासुट्; **3.4.104 किदाशिषि** — Kāśikā: *"…यासुडागमो भवति, स च उदात्तः किद्वद्
   भवति … **गुणवृद्धिप्रतिषेधः तुल्यः**, सम्प्रसारणम्…"*; cf. **3.4.103** with its *jñāpaka* about
   the lākāra's ṅittva) and luṅ are ṅit/kit environments in any case, so **no guṇa** is expected.
3. **Direct commentary support for कुटादि ⇒ no vṛddhi.** Kāśikā on **7.2.1 सिचि वृद्धिः
   परस्मैपदेषु**: *"अन्तरङ्गम् अपि गुणम् एषां वृद्धिर्वचनाद् बाधते। **न्यनुवीत्, न्यधुवीत्
   इत्यत्र कुटादित्वात् ङित्त्वे सति प्रतिषिद्धायां वृद्धौ उवङादेशः क्रियते।**"* — an explicit
   statement that कुटादि-ṅittva *prohibits* the otherwise due vṛddhi before सिच्.
4. **Why Vidyut differs.** Vidyut's pāṭha places `gurI~` in **तुदादि** (`06.0131 gurI~ udyamane`),
   where 1.2.1 does not apply and the pratyaya is not ṅit-by-kutādi, so guṇa surfaces. The pāṭha
   witness disagrees with that placement; the Kāśikā's कुटादि span (कुट → कुङ्) settles it in
   favour of कुटादि.

⇒ **Engine correct; Vidyut's गोरी* are the forms of the same root treated as a non-कुटादि root.**

Editorial caveats (genuine data-level split, does not change the verdict):

* The pāṭha contains **two** entries: **गुरी उद्यमने** in कुटादि (above) and, separately,
  **गूर उद्यमने** in the curādi ātmanepada block *आ कुस्मादात्मनेपदिनः* — SK prints it as
  **"गूर उद्यमने"** (root 1695, in *"आ कुस्मादात्मनेपदिनः … गूर उद्यमने। शम। लक्ष आलोचने।
  नान्ये मित इति मित्त्वनिषेधः। शामयते"*), and the sa.wikisource pāṭha at *157 गूर उद्यमने*
  (matching the same numbering offset as SK). The engine's tag "kuṭādi · ātmane" mixes the
  ātmanepada property of the **गूर** entry with the **गुरी** entry — worth aligning the dataset,
  but for the guṇa question both readings are covered by 1.2.1 (गुरी) or by the general
  kit/ṅit blocking of āśīrliṅ and luṅ.
* Vidyut's gaṇasūtra set gives the ātmanepada block as "आ कुस्माद्" (`10.0496 A kusmAdAtmanepadinaH`);
  the pāṭha/SK reading is "आ कुस्माद्" with *कुस्म नाम्नो वा* — same block.

---

## (d) √सृ luṅ (`asArzIt`) and √दिवि (`Dinvati`) — **engine right (SK confirms both)**

1. **√सृ (bhvādi, सेट्/अनिट् treatment).** SK भ्वादि: *"सृ गतौ। क्रादित्वान्नेट्। ससर्थ। ससृव।
   रिङ्। … असार्षीत्। असार्ष्टाम्"* — the SK itself prints **असार्षीत्** (with अकार्षीत्-सिच् :
   **3.1.44 च्लेः सिच्**, vṛddhi by **7.2.1 सिचि वृद्धिः परस्मैपदेषु**, non-iṭ by **7.2.10
   एकाच उपदेशेऽनुदात्तात्**, whose Kāśikā notes *अवधिष्ट* etc.).
2. **√दिवि.** SK: *"हिवि। दिवि। धिवि। जिवि प्राणनार्थाः। हिन्वति। दिन्वति"* and, under
   **3.1.80 धिन्विकृण्व्योरच्**, *"अनयोरकारोऽन्तादेशः स्यादुप्रत्ययश्च शब्विषये … धिनोति।
   धिनुतः। धिन्वति"*, with **6.4.107 लोपश्चास्यान्यतरस्यां म्वोः** (*"धिन्वः धिनुवः। धिन्मः
   धिनुमः"*) and **6.4.106** (*"धिनु। … धिनवाव"*). SK's own outputs **दिन्वति** are exactly the
   engine's form.

⇒ Engine's `asArzIt` and `Dinvati` are the SK-attested forms; Vidyut's differing outputs are a
tool-side divergence, not a correction of the engine.

---

## (e) Missing vibhāṣā alternates (ऊर्णु liṭ; कृष्-type sič fork) — **engine gap: both forms required**

These are genuine **vikalpa** cells; a single form per cell is under-generation.

1. **√ऊर्णु, iṭ-ādi pratyayas.** **1.2.3 विभाषोर्णोः** — Kāśikā: *"ऊर्णुञ् आच्छादने, अस्मात् परः
   इडादिः प्रत्ययो विभाषा ङिद्वद् भवति। **प्रोर्णुविता। प्रोर्णविता।**"* Bālamanoramā 278 makes
   the two liṭ forms explicit: *"ङित्त्वपक्षे गुणाऽभावादुवङ् (**ऊर्णुनुविथ**); ङित्त्वाऽभावपक्षे गुणः
   (**ऊर्णुनविथ**)"*, and adds लुट्/लृट् pairs (ऊर्णविता/ऊर्णुविता; ऊर्णविष्यति/ऊर्णुविष्यति) — matching
   SK's *"ऊर्णुनाव। ऊर्णुनुवतुः। ऊर्णुनुवुः"*, *"ऊर्णुनुविथ। ऊर्णुनविथ। ऊर्णुविता। ऊर्णविता"*,
   *"ऊर्णौति। ऊर्णोति"* (vṛddhi-vikalpa) and *"ऊर्णोतेराम्नेति वाच्यम्"*, plus 7.2.10's Kāśikā
   (*"वाच्य ऊर्णोर्णुवद्भावो यङ्प्रसिद्धिः प्रयोजनम्"*).
2. **√कृष् aorist fork.** **3.1.44 च्लेः सिच्** with the vārttika **"स्पृश-मृश-कृष-तृप-दृपां च्लेः
   सिज्वा वाच्यः"** (Kāśikā ad 3.1.44: *"अस्प्राक्षीत्, अस्पार्क्षीत्, अस्पृक्षत् … अकार्षीत्,
   अक्राक्षीत्, अकृक्षत्"* — the last with *kṣa* instead of सिच्). SK prints the same pair
   (*"अक्राक्षीत् … अकार्क्षीत् … पक्षे क्सः। अकृक्षत्"*; तुदादि ātmanepada: *"अकृष्ट"*).
3. **Other live vikalpa cells already in the corpus** (useful controls when fixing the generator):
   6.1.39 **वश्चास्यान्यतरस्याम्** (*ऊवतुः/ऊवुः* vs *ऊयतुः/ऊयुः*), 6.4.107 **लोपश्चास्यान्यतरस्यां
   म्वोः** (*सुन्वः/सुनुवः; धिन्वः/धिनुवः*), 8.3.117 (न्यषीदत्/न्यसीदत्; व्यष्टौत्/व्यस्तौत्).

⇒ Verdict: the engine must emit **both** alternatives for 1.2.3, the 3.1.44 vārttika fork, 6.1.39,
6.4.107 (and the 8.3.117 vā) — the tradition is not split here; it is explicitly *vā*.

---

## (f) Intermittent loss of 6.1.8 in liṭ (ह्रगे / ऋधु); one laG hang — **engine defect, not a grammatical question**

1. **Rule.** **6.1.8 लिटि धातोरनभ्यासस्य** — Kāśikā: *"लिटि परतोऽनभ्यासस्य धातोरवयवस्य प्रथमस्य
   एकाचो द्वितीयस्य वा यथायोगं द्वे भवतः। पपाच। पपाठ। **प्रोर्णुनाव।** … लिटि इति किम्? कर्ता।
   हर्ता। … द्विर्वचनप्रकरणे छन्दसि वेति वक्तव्यम्।"* In laukika liṭ the reduplication is नित्य
   (the छन्दस् option aside).
2. **Controls from SK for the very roots/classes in the report.** √ऋधु (दिवादि/स्वादि): *"ऋधु वृद्धौ।
   **आनर्ध**। आर्धत्"* — abhyāsa **आनर्ध** in liṭ, no abhyāsa in luṅ (**आर्धत्**). Curādi-फणादि
   roots: *"ज्वरति। **जज्वार**"*, *"गडति। **जगाड**"*, *"हेडति। **जिहेड**"* — i.e. ह्रगे's class
   reduplicates in liṭ (प्रोर्णुनाव-type), so a liṭ cell in which 6.1.8 has "dropped out" is
   simply a wrong derivation.
3. **Reproducibility.** 12 reruns across hash seeds did not reproduce either the 6.1.8 loss or the
   hang at *bhū* laG-2-2; that points to engine-internal nondeterminism/performance, not to a
   grammar dispute. Recommended handling: keep as an engine bug with logging (rule id + cell), and
   do not cite it as a sūtra-interpretation question.

---

## (g) "40 gate-only sūtras" (prefix-dependent ṣatva/ṇatva; liṭ samprasāraṇa of vye/hve) — **not gate-only; each is determinate and quotable**

The two families named in the parked note are fully rule-governed; the following are read and
verified (sūtra text + commentary examples):

**Prefix-conditioned ṣatva / pratiṣedha / ṇatva**

* **8.3.115 सनोतेः स्यसनोः** — Kāśikā: *"सुनोतेः सकारस्य मूर्धन्यदेशो न भवति स्ये सनि च परतः।
  अभिसोष्यति। परिसोष्यति। अभ्यसोष्यत्। पर्यसोष्यत्। … स्यसनोः इति किम्? सुषाव।"*
* **8.3.116** — Kāśikā on सद्/ष्वञ्ज् in liṭ (*अभिषसाद, परिषस्वजे*); Bālamanoramā 408 states the
  controlling maxim **उपसर्गनिमित्तस्य प्रतिषेध** with the counter-forms **पर्यसीषिवत्, न्यसीषहत्**
  (स्तम्भु/सिवु/सह).
* **8.3.117** — नि/वि/अभि with aḍ-vyavāya, *chandas*, **वा**: **न्यषीदत्/न्यसीदत्**, **व्यष्टौत्/व्यस्तौत्**.
* **8.4.14 उपसर्गादसमासेऽपि णौपदेशस्य** — Kāśikā: *"… तस्य उपसर्गस्थान् निमित्तादुत्तरस्य णकारादेशो
  भवति असमासेऽपि समासेऽपि। **प्रणमति। परिणमति।** … उपसर्गातिति किम्? प्रगता नायकाः …।
  णोपदेशस्य इति किम्? **प्रनर्दति।**"*

**Liṭ samprasāraṇa of √व्ये / √ह्वे / √वे / √वय्**

* **6.1.15 वचिस्वपियजादीनां किति** — *उक्तः, सुप्तः, इष्टः, ऊढः, उषितः*; the jayādi list covers
  **वेञ् (उतः)**, **व्येञ् (संवीतः)**, **ह्वेञ् (आहूतवान्)**.
* **6.1.17 लिट्यभ्यासस्य उभयेषाम्** — *उवाच, सुष्वाप, इयाज* (jayādi) / *जग्राह, **विव्याध*** (others).
* **6.1.19 स्वपिस्यमिव्येञां यङि** — *सोषुप्यते, सेसिम्यते, **वेवीयते*** (√व्ये reduplicates with
  samprasāraṇa in yaṅ).
* **6.1.37 न संप्रसारणे संप्रसारणम्**, **6.1.38 लिटि वयो यः** (उवाय, ऊयतुः), **6.1.39 वश्चास्यान्यतरस्याम्**
  (**ऊवतुः/ऊयतुः**), **6.1.40 वेञः** (ववौ, ववतुः, ववुः) — i.e. √वे/√वय् have *no* liṭ
  samprasāraṇa (or only optionally), while √व्ये/√ह्वे do.
* **6.1.16 ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च** completes the ङit-side
  (*गृहीतः, जीनः, विद्धः, उचितः, विचितः, वृक्णः*).

⇒ Verdict: the "gate" should be replaced by these sūtra-conditioned implementations; no tradition
split, but three of them are **vā/vibhāṣā** (8.3.117, 6.1.39, and the chandas-vā vārttika under
8.3.116) and must produce alternatives.

---

## (h) Stale ajādi caṅ recipe — **no verdict needed**

The recipe is being retired and the looping pipeline is the accepted one; recorded here so the item
is closed and not re-opened.

---

## Summary table

| Item | Verdict | Key authority |
|---|---|---|
| (a) चह | **engine right** | gaṇasūtra ज्ञपादयो मितः; 6.4.92 मितां ह्रस्वः (Kāśikā, Bālamanoramā 395, SK *चहयति*) |
| (b) √ऋणु loṭ 2sg | **engine wrong; Vidyut right** | 3.1.79; 6.4.106 (+chandas-vā vacana); SK तनादि paradigm |
| (c) √गुरी āśīrliṅ/luṅ/lṛṭ | **engine right** | 1.2.1 गाङ्कुटादिभ्योऽञ्णिन्ङित् (+1.1.5; 3.4.104; Kāśikā on 7.2.1) |
| (d) √सृ luṅ / √दिवि | **engine right** | SK (असार्षीत्; 3.1.80 with दिन्वति; 3.1.44+7.2.1/7.2.10) |
| (e) vibhāṣā cells | **engine gap — emit both** | 1.2.3 विभाषोर्णोः; 3.1.44 vārttika (स्पृश-मृश-कृष-…); 6.1.39; 6.4.107; 8.3.117 |
| (f) 6.1.8 loss / hang | **engine defect, not grammar** | 6.1.8 (Kāśikā; SK आनर्ध, जज्वार, जगाड) |
| (g) "gate-only" 40 sūtras | **implementable, not indeterminate** | 8.3.115–117, 8.4.14, 6.1.15–19, 6.1.37–40 |
| (h) stale recipe | closed, no verdict | — |

Two places where the *sources themselves* differ (flagged, not silently resolved): the gaṇa
placement of `gurI~` (कुटादि in the pāṭha and Kāśikā vs तुदादि in Vidyut's data) in item (c), and
the spelling of the ātmanepada curādi root (गूर in SK/pāṭha vs Vidyut's separate `gUra~` entry).
