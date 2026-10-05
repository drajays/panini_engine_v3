# Conflict register — for the dedicated authority session

Rule of work (agreed 2026-10-05): the engine keeps being built; every point where the engine, Vidyut (the oracle of record), our older
recipe, or the dhātupāṭha data disagree, or where I made a modelling choice that Pāṇini/the commentaries should decide, is **recorded
here, not argued in code**. In the authority session you supply the source (Kāśikā, Bhāṣya, Siddhānta-Kaumudī, Padamañjarī …) or the
expert's view; I then change the engine, pin the result with a test, and close the entry.

Status: **OPEN** (needs your source) · **ENGINE-CHOICE** (I picked a reading; confirm or overrule) · **DATA** (dhātupāṭha/Vidyut data question).
Cell-level differences are generated into `docs/CONFLICT_CELLS.md` (`python3 -m tools.conflict_ledger`).
Commands to reproduce any entry: `.venv/bin/python -m tools.tri_compare ROOT --gana N --lakara L --pada P`.

---------------------------------------------------------------------------------------------------------------------------------
## A. Declared apavāda that is really something else (stand-ins) — ENGINE-CHOICE

The resolver models apavāda, para, pūrva, antaraṅga, but not **nitya** or **nimitta-vighāta**. Three declarations stand in for them.
Removing any of them breaks forms (verified), so they stay until the resolver models the real principle.

| id | declared | real principle (my reading) | what breaks if removed | question for the expert |
|---|---|---|---|---|
| A1 | 7.2.35 `apavada_of` 7.2.3 | iṭ is nitya; vṛddhi can be blocked by iṭ (7.2.4 neṭi), not conversely | `*avAnizam` for every seṭ root in luṅ | confirm iṭ-before-vṛddhi rests on nityatva, not apavāda |
| A2 | 7.3.96 `apavada_of` 6.1.68 | īṭ is para; once inserted the t/s no longer follows a hal (nimitta-vighāta) | `*AtiH`, `*acetiH` (2sg of seṭ roots) | same: is "ī-āgama then hal-lopa blocked" nitya or nimitta-vighāta? |
| A3 | 2.4.77 `apavada_of` 3.4.108 | no jus after a luk'd sic: 3.4.110 ātaḥ would be vyartha otherwise (jñāpaka) | `*aBUvuH` for bhū luṅ 3pl | the audit agent called it a "computational shortcut, not authentic" — what is the authentic account (pratyayalakṣaṇa + jñāpaka) and should the engine encode it as a `CONFLICT_OVERRIDES` jñāpaka entry? |
| A4 | 6.4.63 over 6.4.82/6.4.77; 6.1.96 over 6.1.87/6.1.101; 6.4.78 over 6.1.77; 7.2.1 over 7.3.84/7.3.86; 7.4.76/77 over 7.4.66; 2.4.85 and 3.4.81 over 3.4.79; 6.4.77 over 6.1.77; 7.1.4 over 7.1.3; 7.1.102 over 7.1.100 | specific over general (viśeṣa-sāmānya) | wrong forms (see the sweeps) | confirm each pair is truly utsarga–apavāda and not para/nitya |

## B. Scope decisions inside a sūtra — ENGINE-CHOICE

| id | sūtra | decision | ours / Vidyut | question |
|---|---|---|---|---|
| B1 | 7.2.4 neṭi | blocks only 7.2.3 (hal-anta vṛddhi), not 7.2.1 (ac-final): `ayAvIt`, `aBEzIt` keep vṛddhi with iṭ | Vidyut agrees | what is the authentic scope of neṭi (Kāśikā on 7.2.4)? |
| B2 | 6.4.107 | made a **vibhāṣā** (default: no lopa) for non-kṛ roots: `tanuvaH` / `tanvaH`; kṛ nitya via 6.4.108 | recipe `tanuvaH`; Vidyut returned nothing for tanu~ | is 6.4.107 optional, and what is the anuvṛtti that makes it so? |
| B3 | 8.3.78 | applied to dhvam after iṇ in **liṭ and luṅ**; **not** to āśīr-liṅ ṣīdhvam | `eDizIDvam` = Vidyut = recipe; text says ṣīdhvam | does 8.3.78/79 give `eDiṣīḍhvam` (and vibhāṣā 8.3.79) in āśīr-liṅ? Vidyut and recipe disagree with the text as I read it |
| B4 | 7.4.28 riṅ | only before **āśīr**-liṅ's yāsuṭ/sīyuṭ (`kriyAt`), not vidhi-liṅ (`kuryAt`, `jaGfyAt`) | Vidyut agrees | confirm "śayaglinkṣu" glin = āśīrliṅ only |
| B5 | 7.1.100 ṛta id dhātoḥ / 7.1.102 | only before a weak (kṅit) ending; not before sic (7.2.1 vṛddhi instead: `apArizma`) | Vidyut agrees | confirm kṅiti is required by the sūtra or only by 1.1.5 |
| B6 | 6.4.87 hu-śnuvoḥ | yaṇ only before a **weak** vowel-initial ending; pit endings take guṇa first (`cinavAni`, `acinavam`); extended to hu itself (`juhvati`) | Vidyut agrees | confirm 6.4.87 vs 7.3.84 ordering principle (guṇa antaraṅga to yaṇ?) |
| B7 | 6.4.77 | iyaṅ/uvaṅ suppressed when a pit sārvadhātuka follows (guṇa first: `biBayAni`); uvaṅ for śnu after a conjunct only before kṅit (`Apnuvanti`/`ApnavAni`) | Vidyut agrees | same question as B6 |
| B8 | 7.1.4 ad abhyastāt | applied to jhi→ati **and loṭ ju→atu**, and to ślu roots before dvitva has happened (`slu_replaced_sap`) | Vidyut agrees | is ślu-root abhyasta-hood to be read at 7.1.4 time or after 6.1.10? (engine phases force the former) |
| B9 | 3.4.109 | applied in laṅ for abhyasta (and ślu-roots) and after luk'd sic via 3.4.110; **vid** not yet | Vidyut agrees except where listed | same timing question as B8 |
| B10 | 1.2.4 | an ātmanepada loṭ **uttama** tiṅ (iṭ, vahi, mahiṅ and their ādeśas) is not kṅit (3.4.92 pic ca) | Vidyut agrees | confirm āṭ's pit-ness passes to the whole uttama ādeśa in ātmanepada |
| B11 | 1.2.2 vija iṭ | the iṭ of o~vijI~ makes its affix kit (no guṇa: `vijitA`); implemented as tag at 7.2.35 plus a block in 7.3.84/86 | Vidyut agrees | confirm kit-ness is of the iṭ only |
| B12 | 6.4.120, 6.4.98 | `SaSaratuH` (no e) for ṛ-roots: the a is guṇa-born, so 6.4.120 does not apply; 6.4.98 matches `Gan` (han after 7.3.55) | Vidyut gives `SaSaratuH, SaSratuH` | is `SaSratuH` (a-lopa) also licensed? by which sūtra? |
| B13 | 7.2.116 | `N` counts as ñ on kṛt/taddhita affixes, as ṅ on vikaraṇa/tiṅ (the engine spells ñ as `N` in `GaN`) | — | data hygiene: do we respell kṛt/taddhita ñ-it as `Y` engine-wide? (large change) |
| B14 | 7.4.60 vs 7.4.66 | in liṭ the abhyāsa's ṛ is handled by 7.4.66 **before** 7.4.60 trims its rapara r (`cakarta`, `Anarza`) | Vidyut agrees | confirm the order is vipratiṣedha-para, not antaraṅga |
| B15 | 6.1.10 / aṭ | the aṭ augment stands as its own Term before the abhyāsa (`abiBet`) | Vidyut agrees | confirm āgama placement before an abhyasta aṅga (6.4.71 + 1.1.46) |
| B16 | vikaraṇas (3.1.73–3.1.81) | stand only before a sārvadhātuka **lakāra** (laṭ, loṭ, laṅ, vidhi-liṅ); none before liṭ, luṭ, lṛṭ, luṅ, lṛṅ, āśīr-liṅ | Vidyut agrees | confirm: tiṅ of luṭ/lṛṭ is sārvadhātuka by 3.4.113 yet takes no śap — what is the stated reason (3.1.33 for lṛṭ/luṭ; 3.1.43–44 for luṅ; 3.4.114–116)? |

## C. Disagreements with Vidyut where I believe the engine is right — OPEN (need a text)

| id | cell | ours | Vidyut | sūtra | note |
|---|---|---|---|---|---|
| C1 | `pf`, gaṇa 3, any lakāra | `piparti` | `paparti` | 7.4.77 artipipartyośca | Siddhānta-Kaumudī reads pipartti; Vidyut seems not to apply 7.4.77 to `pf` |
| C2 | `manTa~` āśīr-liṅ | (loop) `maTyAsam` | `maTyAsam` | 6.4.24 | our **recipe** says `manTyAsam`; recipe is wrong, loop = Vidyut. Close when confirmed |
| C3 | `cakziN`, `liha~`, `hana~`, `hA`, `ṛ` (many) | loop = Vidyut | recipe differs | — | recipe is the wrong side; listed so the recipes can be retired |

## D. Real gaps (rule not written or not modelled) — OPEN, need the rule's authentic statement

| id | cell | ours | Vidyut | sūtra needed |
|---|---|---|---|---|
| D1 | `duha~`/`diha~` 2sg laṭ | `dokzi` | `Dokzi` | 8.2.37 ekāco baśo bhaṣ jhaṣantasya sdhvoḥ (bhaṣ before s) + 8.2.31/32 |
| D2 | `liha~` | `leqQi` | `leQi` | 8.3.13 ḍho ḍhe lopaḥ + 6.3.111 ḍhralope dīrgha |
| D3 | `quDAY` (dhā) 3du/2du/2pl laṅ-type | `dadDaH` | `DattaH` | 8.2.38 dadhas tathoś ca (+ 8.2.37, 8.4.53/55) |
| D4 | `Basa~` 3du/2du/2pl | `bapstaH` | `babDaH` | 8.2.? (bhas→bhs+ta, jhal-saṃyoga rule giving bdh) — rule unidentified |
| D5 | `Dana~` 3pl | `daDati` | `daDanti` | 7.1.4 ad abhyastāt exception for … ? |
| D6 | `sranBu~` liṭ | `sasraBe` | `sasramBe` | 6.4.24 aniditāṃ: which condition keeps the m? |
| D7 | `vyaca~` liṭ | `vavyAca` | `vivyAca` | 6.1.17 liṭy abhyāsasyobhayeṣām (samprasāraṇa of the abhyāsa of vyac) |
| D8 | `dIN` luṭ/lṛṭ | `detA` | `dAtA` | which sūtra makes dīṅ's ī → ā before ārdhadhātuka? |
| D9 | `hi` (hinoti) liṭ 1du | (fixed) | `jiGyiva` | 6.4.82 yaṇ after the abhyāsa — done; listed for the record |
| D10 | `tfha~` laṅ/liṅ | `atfRaw` | `atfReq, atfRew` | 7.2.? iṭ + 8.2.? for tṛh (ṭ/ḍ options) |
| D11 | `o~hAk` luṅ | `ahAstAm` | `ahAsizwAm` | data: is o~hAk seṭ or aniṭ? (see E1) |
| D12 | `cakziN` liṭ | `cacakziye` | `cakzayAYcakre …` | cakṣiṅ→khyā/ṇic? why Vidyut gives āṃ forms |
| D13 | `mAN`,`o~hAN` liṅ (fixed) | — | — | 7.4.76 + 6.4.113; listed for the record |
| D14 | gaṇa 7 liṅ `vfjI~`, `undI~`, `tancU~` | `kfRatyAt`-type | `kfntyAt` | 6.4.24/6.4.25 + śnam n-lopa before yāsuṭ: scope of "kṅiti" for liṅ yāsuṭ |
| D15 | gaṇa 10 ātmane liṭ (`sPuqi~`) | `pusPuRqiye` | `sPuRqayAYcakre`, also `pusPuRqe` | 3.1.35 kāspratyayād āmamantre liṭi for ṇijanta: obligatory or optional? |
| D16 | `IzWa`-type `ISa~` luṅ | — | — | 7.2.77/7.2.78 done; vibhāṣā 8.3.79 for ḍhvam: Vidyut gives `EDiDvam` only |
| D17 | `vyuza~`, `pluza~` luṅ | `avyozIt` | `avyuzat` | 3.1.55 puṣādi-dyutādi-ḷdit parasmaipadeṣu aṅ — the aṅ list (puṣādi, dyutādi, ḷdit) must be encoded |
| D18 | `tF` gaṇa 4 | — | (Vidyut: no forms) | gaṇapāṭha / dhātu: does Vidyut drop it for a reason? |
| D19 | `ciY` (ubhaya), some `hu` ātmane | — | (Vidyut: no forms) | pada of these roots (parasmaipadī or ubhaya?) |

## E. Data questions (dhātupāṭha) — DATA

| id | item | question |
|---|---|---|
| E1 | `o~hAk` (jahāti): our data aniṭ, Vidyut seṭ | which is right for luṅ (`ahAsIt`/`ahAsizwAm`)? |
| E2 | `hf`, `Gf`, `f` ātmane/ubhaya flags | pada labels (`उभयपदी`) vs Vidyut's output |
| E3 | `vana~`, `yama~`, `rama~` … rows that repeat across gaṇas | row ids are used now; confirm no duplicates are lost |
| E4 | roots with `anudatta` flag false for all (`flags.udatta`) | the flag seems to mean "udātta svara", not "anudāttopadeśa"; 6.4.37 uses `ekac and not udatta` as a proxy |

## F. Harness / architecture limits (not Pāṇinian questions)

- Ordering that depends on engine phases: ślu roots count as abhyasta at 3.4.108/109, 7.1.4 before dvitva (B8, B9).
- The loop never tags `atmanepada` (1.4.100 does not fire); rules read "not parasmaipada" (3.4.102, 3.4.107, 1.2.11, 2.4.85).
- Candidates conflict resolution (`engine/resolver.py` purva/para): "same Term and different results by order ⇒ para" introduced this
  session; confirm against the intended vipratiṣedha reading (Art. 21).

---------------------------------------------------------------------------------------------------------------------------------
## G. Checked against ashtadhyayi.com data (`data/reference/ashtadhyayi_com/sutraani__data.txt`, `sutraani__sutra_prayogas.txt`)

Those files give, per sūtra: text, padaccheda (`pc`), anuvṛtti (`an`), adhikāra (`ad`), and example words with the cited sūtra. They carry no Kāśikā prose, so
they settle only what the anuvṛtti/examples show. Reading-only; the engine never imports them (Art. 6).

| id | finding from the data | effect on the register |
|---|---|---|
| A3 | 2.4.77 examples `श्रदधुः`: "gāti-sthā… sico luk", and 3.4.110 `आतः` cites the same word `श्रदधुः` for jus. So jus after a luk'd sic is the sūtra's own intended use | A3 supported: jus after luk'd sic is authentic; keep, upgrade the stand-in to a proper override entry when the resolver can model it |
| B1 | 7.2.4 `नेटि` anuvṛtti = 7.2.1 (vṛddhiḥ, sici) + 7.2.3 (vadavraja-halantasya, acaḥ); examples are all hal-anta (`पर्याणंसीत्`, `उदनंसिषुः`, `मच्योष्ट`) | consistent with blocking the 7.2.3 case; no example for the ac-final 7.2.1 case |
| B3 | 8.3.78 `पc` = `इणः षीध्वम्-लुङ्-लिटाम्`; examples `कृषीढ्वं`, `नाध्यगीढ्वं` (ṣīdhvam of āśīr-liṅ is named in the sūtra); 8.3.79 `विभाषेटः` anuvṛtti = 8.3.78 | the sūtra itself names ṣīḍhvam, so āśīr-liṅ is in scope (engine, Vidyut and recipe all omit it); `eDiṣīḍhvam` ~ `eDizIDvam` question stays but the direction is: ṣ is correct and 8.3.79 is optional. Engine change pending (D16/B3) |
| B4 | 7.4.28 anuvṛtti = `यि`, `अकृत्सार्वधातुकयोः` (7.4.25), `ऋतः`; examples `ध्रियते` (yak), `क्रियताम्` (yak) | confirms riṅ is for ārdhadhātuka/yi contexts; āśīr-liṅ fits, vidhi-liṅ (sārvadhātuka) excluded |
| B2 | 6.4.107 `लोपश्चास्यान्यतरस्यां म्वोः`; anuvṛtti = 6.4.98 kṅiti, 6.4.106 (asaṃyogapūrvāt, uta, ca, pratyayāt) ; adhikāra: asiddhavat | `anyatarasyām` is in the sūtra ⇒ vibhāṣā confirmed; engine choice B2 is correct |
| C1 | 7.4.77 `अर्तिपिपर्त्योश्च` anuvṛtti = abhyāsasya, ślau (7.4.75), it (7.4.76); no examples | ittva in ślau for `pf`: engine's `piparti` follows the sūtra; Vidyut's `paparti` is the outlier → mark closed in favour of engine |
| D1/D3 | 8.2.37 examples `विजिघृक्षु`, `अधाक्षीद्`; 8.2.38 examples `अन्तर्धत्स्व`, `पिधध्वं`, `अभिधत्त` (bhaṣ for the abhyāsa and the root's dh before t/th) | confirms the missing rules and the target forms (`Datta`, `dattaH`→`DattaH`) |
| D15 | 3.1.35 anuvṛtti empty; examples `संत्रासयांचकार`, `कासांचक्रे` | āṃ for ṇijanta in liṭ is in use, supports Vidyut's āṃ forms for gaṇa 10; engine to follow |
| D17 | 3.1.55 14 examples (`पुषः`, `प्रापत्`, `समासदत्`) | confirms aṅ for puṣādi/dyutādi/ḷdit; list to be implemented from the gaṇapāṭha |
| D7 | 6.1.17 example `संविव्ययुः` (vye) | the sūtra covers the abhyāsa samprasāraṇa in liṭ; `vyaca~` as 6.1.16 member to be checked |

Net: 4 items (A3, B2, B4, C1) are now closed by the data, 5 more (B3, D1/D3, D15, D17, D7) have a clear direction and become engine work; the
rest still need your Kāśikā/Bhāṣya or expert view.
