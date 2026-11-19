# LK coordinator work (2026-11-19) — what the 8 workers could not do in a sūtra file

Source: scratch/lk_triage/a*_needs_coordinator.md (merged verbatim). Each needs coordinator files (pipelines/tinanta.py, krdanta.py, subanta.py, chain.py, pada_samhita.py, engine/{resolver,tape_init}, core/phases). One design piece at a time, then ONE full suite + ONE sig refreeze (S190 lesson: a table edit broke 14 tests).

## a1

- 1.3.91 | spec now written (fixture a1); cond needs d.meta ATMANE_LICENSE (1.3.78 key) + 'lug_derivation' tag + antarganas on dyut Term; tinanta bootstrap never sets them, so 1.3.91 SKIPPED | pipelines/tinanta.py, engine/tape_init/tinanta.py
- 1.3.14 / 1.3.15 | karmavyatihAra vivaksha (spec ok) never reaches the sūtras; 1.3.14 reads tag karmavyatihAra_usage nobody sets; not in _bootstrap sūtra list | pipelines/tinanta.py, engine/tape_init/tinanta.py
- 1.3.48 | saMpravadante: with upasargas sam+pra 3pl atmane engine gives sampravadaMte (8.3.23 sam-m→M absent + n→M) | sutras/8.3 (8.3.23 tripadi spine) core/phases/tripadi.py
- 1.3.28 | A+han atmane: engine Ahante for 3sg (should be Ahate; 6.4.37 anunasika-lopa not applied to han) | sutras 6.4.37 / tinanta adadi route
- 1.3.29 | only gam handled, uses arm-ish samo_recipe flag; svf etc. need pada_ctx rewrite (own file feasible but flag removal touches pipeline callers) | pipelines/tinanta.py
- 1.3.68 | BI+Nic atmane gives BIayate, needs ṣuk (6.1.55 BIzayate) ; atma_recipe flag | pipelines/tinanta.py, 6.1.55
- 1.2.13 | luG sic branch (samagata/samagaMsta) not handled; file only does ashir_liG; VIBHASHA branching on sic kit | pipelines/tinanta.py luG route
- 1.2.9 / 1.2.10 | san route gives ciicizate/BiBidizate (iT-agama, not 7.2.10 ekAca aniT), yaj san iT wrong | pipelines/tinanta.py san route, 7.2.10
- 1.2.7 / 1.2.8 | ktvA route: guna instead of kit-block (mfqitvA etc.); 1.2.7/1.2.8 need iT-ktvA kit tag before 7.3.84 | pipelines/krdanta.py, engine core_loop
- 1.2.6 / 1.2.18 / 1.1.5 / 1.1.47 / 1.1.57 / 1.1.59 / 1.4.8 / 1.4.22 / 1.4.108 | right form, sūtra never in route (not_fired); needs route/spine call | pipelines/tinanta.py, subanta pipeline, core/phases/*
- 1.1.28 / 1.1.32 | vibhāṣā sarvanāma for uttarapUrvA/katarakatama not produced; sarvādi lexicon + pipeline | lexicon, pipelines/subanta
- 1.4.5 / 1.4.6 | SrI/kfti strI nadI: 1.4.5/6 BLOCKED by other sūtra, engine gives SrIRAm (6.4.? ) | subanta pipeline / resolver
- 1.3.72 / 1.3.78 | not_fired (SKIPPED/VACUOUS) pada gate by other route | pipelines/tinanta.py
- other UNRUNNABLE (1.3.32 .. 1.4.107 etc.) | need Kāśikā-sourced expected forms + route support (no spec written) | tools-only, low priority

## a2

- 2.1.20,2.1.30,2.1.32,2.1.40,2.1.50,2.1.52,2.1.55,2.1.57,2.2.1,2.2.2,2.2.4,2.2.19,2.2.24,2.2.31-36 | samasa harness leaves the sup/sandhi residue (paYcannadIs, haryAtrAtas, kumBamkAras...): sup-lopa 2.4.71 / avyayībhāva 2.4.82-83 / sandhi not run at stem stage | pipelines/samasa*, harness stem-stage
- 2.1.6,2.1.14 | right form but sūtra not fired (made by another path in samasa pipeline) | pipelines/samasa*
- 2.1.13,2.1.36,2.1.51 | sup residue / pañcamī-ṣaṣṭhī members not lopped (AspAwaliputrAt, yUpEdArus, paYcankumArIs) | pipelines/samasa*
- 2.4.18 | 1.2.47 napuṃsaka-hrasva not applied after avyayībhāva (aDistrI vs aDistri) | pipelines/samasa*, 1.2.47 call
- 2.4.49 | tinanta liṭ path never calls 2.4.49 (iN→gAN): aDIye vs aDijage | pipelines/tinanta.py
- 2.4.78,2.4.79 | tinanta luṅ path does not schedule vibhāṣā sic-luk (only 2.4.77) | pipelines/tinanta.py, engine/resolver.py
- 2.4.64 | taddhita lug reading for plural not produced (gArgayaH vs gargAH) | pipelines/taddhita*, engine
- 2.3.36,2.3.50 | right form via subanta pipeline, vibhakti sūtra not fired (glass-box only) | pipelines/subanta.py
- 2.3.2,2.3.13,2.3.16,2.3.18,2.3.28,2.3.47,2.4.1,2.4.2,2.4.17,2.4.26,2.4.29,2.4.31,2.4.84,2.2.20 | UNRUNNABLE: no machine entry in tools.exercise_audit (kāraka/vibhakti/dvigu/dvandva constructions) | tools/exercise_audit.py (shared)

## a3

- 3.1.65 | fixture "atApi" (positive) is wrong: 3.1.65 FORBIDS ciN for tap in karmakartari (Kasika: anvatapta); engine has no karmakartari prayoga (tinanta accepts only kartari/karmani/bhave) | pipelines/tinanta.py, then recast fixture as negative
- 3.1.9,3.1.10,3.1.14,3.1.17,3.1.23,3.1.27 | no namadhatu/sanadi loop edge for kAmyac/kyac/kyaN/yaN/yak | pipelines/* (PRAKARANA_MACHINE_PLAN G1)
- 3.1.87 | no karmakartari entry point | pipelines/tinanta.py
- 3.1.4,3.1.62,3.4.68,3.4.69,3.2.112,3.3.103,3.4.70 | not_fired: form right via another path; sutra not in spine/route | core/phases/*, pipelines/*
- 3.1.41 | vid+Am+kf loT (vidANkurvantu): plain vid gives vidantu, Am/kf route absent | pipelines/tinanta.py
- 3.1.60 | ud+pad luG ta gives udapatta not udapAdi (cin with upasarga) | pipelines/tinanta.py (tinanta2 upasarga route)
- 3.2.177 | BrAj+kvip gives BrAg/BrAk, not BrAw (8.2.36 sa-adesa for BrAj missing/unrouted) | 8.2.36 + tripadi spine
- 3.3.97,3.3.101 | ktin/aN+TAp for av/iz give AvA/izA, not UtiH/icCA (vasamprasarana/6.1.108-class and 6.1.? icCA via 7.3.78 absent) | krdanta pipeline
- 3.3.156,3.2.112 | bucket A rival route | pipelines/*
- 3.4.67 | schema lacks krt values tfc/Rvul (spec cannot select them) | tools/build_vivaksha_schema.py
- 3.1.136,3.1.144,3.2.58,3.2.59,3.2.60,3.2.75(spec runs: gives pUH not grAvA),3.2.91,3.2.99,3.2.107(kala=parokza not in schema),3.2.182,3.2.185,3.3.14,3.3.41,3.3.46(no upasarga+lipsa),3.3.92,3.3.107,3.3.113,3.3.121,3.3.128,3.3.131,3.3.158,3.3.167,3.4.18,3.4.22,3.4.27,3.3.1 | no vivaksha key / upapada-krt entry / uNadi consumer; unrunnable | pipelines/krdanta*, schema builder, lexicon

## a4

- 4.1.17 | gArgya+ṣpha+ṅīṣ: engine gives gArgI (4.1.16/ṅīp route wins; ṣpha not selected for prāc gotra) | sutras/adhyaya_4/pada_1/sutra_4_1_16.py, pipelines/chain stri stage
- 4.1.39 | Sveta+ṅīp n-ādeśa: engine gives SvetA (ṭāp), varṇād anudāttāt toppadhāt to naḥ not selected | sutras 4.1.39 + stri-stage choice (pipelines)
- 4.1.58,4.1.93,4.1.94,4.1.168,4.2.7,4.2.38,4.2.107,4.4.41 | not_fired: form right by another route; taddhita pipeline does not route via the sūtra | pipelines/taddhita*, taddhita vidhāna dispatch
- 4.1.87 | strI/puṃs+ñ/snañ nipātana (strERam, pOMsnam) not produced; samūha sense only | taddhita pipeline + lexicon
- 4.1.114,4.1.115,4.1.116 | sūtra files are stubs (only set meta taddhita_kind); need aṇ attach + ṛṣyandhaka/mātur ut/kanīna ādeśa and rivalry with iñ (4.1.95) | pipelines/taddhita*, engine/resolver.py
- 4.1.175 | kamboja: añ (4.1.168) then luk; engine gives iñ kAmboji (4.1.169 route wins) | pipelines/taddhita*, resolver
- 4.2.36 | pitfvyaH/mAtulaH nipātana, sense svArTa unmodelled | lexicon nipātana facts + pipelines
- 4.2.61 | kramādibhyo vun (adhyetṛ/veditṛ sense aDyAyin not attached) | pipelines/taddhita*, schema sense
- 4.3.135 4.4.26 4.4.43 4.4.65 4.4.71 4.4.91 4.4.93 4.4.95 4.4.107 4.4.108 | taddhita not attached at all for these senses (stem returned) — sense keys absent from vivaksha schema/pipeline | data/inputs/vivaksha_schema.json builder, pipelines/taddhita*
- 4.2.81 | janapade lup (paYcAla nivAsa, plural) not applied; engine yields pAYcAlaH via aṇ | pipelines/taddhita*, resolver

## a5

- 5.1.5 | havizyam: s-stem + ya gives havisyam (8.3.59 za after i-final s-stem not applied) | tripadi spine / 8.3.59 file
- 5.1.38 | Satika (nimitta): 5.1.21 ṭhan not reachable in this frame, only SatyaH | sutra_5_1_21 + frame wiring
- 5.1.45, 5.1.52 | KArI -> KArIkam/KArIkaH (SK); engine drops ī (6.4.148 yasyeti ca) giving KArika | 6.4.148 file / vārttika
- 5.1.47, 5.1.56 | paYcakaH/saptakaH (SK) need 5.1.22 kan under these senses; ṭhañ gives pAYcikaH | sutra_5_1_22 and sense frames
- 5.1.79 | Ahnikam: ahan + ṭhañ gives Ahikam (ahnaH ṭilopa/ahna-ādeśa) | 6.4.145 / 7.3.? ahan file
- 5.1.96 | bhavavat names 4.3.11ff pratyayas (SHORTCUT S34), mAsikam etc. not produced | sutra_5_1_96 + 4.3.11 group real
- 5.1.115, 5.1.116 | vati pratyaya (vatiH) + avyaya sup-luk 2.4.82; no vati in lexicon | taddhita lexicon, pipelines/chain.py
- 5.1.119, 5.1.131 | tva/tal frame (5.1.119-120) and Suci -> SOcam never attach; engine gap | 5.1.120 + lexicon, chain.py
- 5.2.23, 5.3.9, 5.3.14, 5.3.16, 5.3.56, 5.3.60, 5.3.68, 5.3.77, 5.4.11, 5.4.42, 5.4.50 | stubs, no real cond/act; need sense frames + suffix lexicon (tasil/ha/etarhi/tarap/iyasun/kan/Sas/cvi) | taddhita lexicon, chain.py (avyaya luk)
- 5.4.74, 5.4.107, 5.4.138, 5.4.148, 5.4.150, 5.4.156, 5.4.157, 5.4.159 | samAsAnta stubs; need compound (samasa) state, chain has no samAsAnta stage | pipelines/chain.py, samasa core

## a6

- 6.4.107 | sunvaH (svādi su+Snu): pipelines/tinanta never calls 6.4.107 on the Snu path (terms merge to pada without an attempt); own-file change to also drop u of `nu` tried and reverted (no effect) | pipelines/tinanta.py
- 6.1.89 | upa+eti/edhate: upasarga+dhātu not joined (upaeti, upeDate); vṛddhi never attempted | pipelines/tinanta.py (upasarga sandhi)
- 6.1.94 | upozati/prozati: 6.1.94 SKIPPED, form made by another path | pipelines/tinanta.py / upasarga path
- 6.1.113, 6.1.125, 6.1.127 | vakya spec (join_tripadi) does not do vowel/ro-u sandhi between padas (vfkzaHatra, agnI iti, daDiatra) | pipelines/pada_samhita.py
- 6.1.15, 6.1.16, 6.1.85 | kta samprasāraṇa (uktaH, gfhItaH, juhAva) correct form but sūtra not fired, other route; izwaH/pfzwaH/BfzwaH/viddhaH/UQaH/SUnaH unreached | pipelines/krdanta.py, engine/resolver
- 6.1.32, 6.1.33 | hvā dvitva/samprasāraṇa in luṅ/sanādi gives ahvad / hehveizate | pipelines/tinanta.py (sanadi recipes)
- 6.3.2, 6.3.9 | samāsa stage: 6.3.2 alug not applied (stokAsimuktas); 6.3.9 forms araRyetilakAs/pUrvAhResPowakAs right but not fired by the sūtra, vane→vanakiMSukAs wrong (fixture expected fixed to stage form incl. -s, kept) | engine/tape_init/samasa.py, samāsa loop
- 6.4.80 | strI 2.1/2.3 striyam: 6.4.80 BLOCKED, form from other path | pipelines/subanta.py, resolver
- 6.4.163,6.4.164,6.4.167,6.4.168,6.4.169 | taddhita chain gives bare stem (sragvitamaH, sAmaH, AtmA, rAja): iSWan/Iyasun, svArTa, apatya/sADu/hita taddhita not produced | pipelines/chain.py, taddhita lexicon (new facts)
- 6.1.122, 6.2.184, 6.3.14, 6.3.42, 6.1.89 4th case | UNRUNNABLE: no harness spec for go'gram (pada-sandhi optional), nirudakam, stamBeramaH, pAcakavfndArikA, pra+UQaH | tools/exercise_audit.py harness / pipelines

## a7

- 7.4.49 | san route gives iadizate not jiGatsati (ghas->ghat, san route lacks 7.2.x/6.1.x steps); lRG case now passes after fixture typo fix | pipelines/tinanta.py (san route)
- 7.4.42 | stub cond/act; dhA+kta gives DItaH (6.4.66 fires) - needs hi substitution ordered before 6.4.66 | engine/scheduler.py or krdanta pipeline + sutra_7_4_42.py
- 7.4.43 | stub; hA+ktvA gives hIttvA (needs hi before 6.4.66 / ktvA-iT) | same as 7.4.42
- 7.1.95 | subanta kroSwu su gives kroSwuH: tRjvat atidesha (7.1.94/95) not wired in subanta route | pipelines/subanta*, sutra_7_1_94
- 7.1.71 | yuj nominative gives yujaH not yuYjaH (7.1.71 nuM for yuj missing in subanta route) | pipelines/subanta*, resolver
- 7.1.36 | vidvAn: Satf vid -> 'vid' not vidvAn (7.1.36 vasu adesha for liT-kvasu path) | pipelines/krdanta*
- 7.2.20/7.4.80/7.3.36/7.4.5/7.4.24/7.4.57/7.2.12/7.3.55/7.3.58/7.4.12 | san/nic/krdanta/AsIrliG route gaps (outputs wrong stem or iT/ac-vikaraNa steps) | pipelines/tinanta.py, krdanta pipeline
- 7.2.42-7.2.48/7.2.57/7.4.97/7.4.12 | vibhasha iT-nishedha: rules BLOCKED by rival (utsarga) so not_fired; needs resolver/vibhasha branching | engine/resolver.py
- 7.2.40 | engine_error 'list assignment index out of range' in executor for 7.2.1 (A+luG upasarga) | sutra_7_2_1.py (shared vrddhi path) or tinanta pipeline
- 7.2.56/7.2.63/7.2.66/7.2.70/7.1.91/7.3.69/7.1.74 | right form by other route (VACUOUS/SKIPPED/absent) | pipelines/tinanta.py / resolver
- 7.2.9/7.3.94/7.4.26/7.4.27/7.4.32/7.4.67/7.1.101 | UNRUNNABLE: no spec; needs a Kasika pratyudaharana source check + spec (not attempted, effort bound) | none yet

## a8

- 8.1.3, 8.1.6, 8.1.26, 8.1.72, 8.2.5, 8.2.63, 8.2.84, 8.3.33, 8.4.3, 8.4.66, 8.4.67 | UNRUNNABLE by nature: accent/pluta/chandas/sentence-level enclitic, no engine entry point or accent output | new entry points (pipelines/*, core/phases/*)
- 8.1.4, 8.2.2 | āmreḍita dvitva of a pada / asiddha-statement has no APPLIED trace or entry point | pipelines/*, core/phases/*
- 8.2.19 | stub (gate-only); not in core/phases/tripadi.py spine so r->l after upasarga before ay never runs (parAyate not palAyate) | core/phases/tripadi.py + real cond/act in sutra_8_2_19.py
- 8.2.21 | engine gives nigIrti (gR->girati/gilati route wrong upstream of 8.2.21) | pipelines/tinanta.py
- 8.2.24, 8.2.45, 8.3.38, 8.3.39, 8.3.48, 8.3.31, 8.3.32, 8.3.67, 8.3.76, 8.3.87, 8.4.61, 8.4.43, 8.4.49 | stub (gate-only act) and not in tripadi spine; form not produced / right form made by other route | core/phases/tripadi.py + real rules in own files
- 8.2.38 | no 8.2.37 bhaS before 8.2.38 in tinanta route (datse for Datse); dattse extra reading | pipelines/tinanta.py, core/phases/tripadi.py
- 8.2.45 | root Bujo~ odit not recognised (BuktaH); 8.2.45 absent from krdanta spine | core/phases/tripadi.py, it-lopa/odit lexicon fact
- 8.2.65 | engine has no kvasu route (kvasu spec yields gatavAn via ktavatu); jaganvAn unreachable | pipelines/krdanta, exercise_audit _KRT_VIV
- 8.3.4, 8.3.5, 8.3.6, 8.3.10, 8.3.12, 8.3.26, 8.3.27 | vakya route lacks 8.3.23 (mo'nusvara) and the 8.3.4-12 rules in the spine; 8.3.5 also needs sut-agama (6.1.137); 8.3.26/27 need anusvara/anunasika surface (Art. 4 s2) | core/phases/tripadi.py, sutra files stubs
- 8.3.56 | sah tumun/soQum and upasarga+tRc specs not buildable; turAzAw yields turAsAh route | pipelines/krdanta, subanta (turAsAh)
- 8.3.58 | sarpiHzu/yajuHzu (visarga stays before z per 8.3.36-style option inside sup) not produced; only sarpizzu | core/phases/tripadi.py (visarga option for s-final stem + su) 
- 8.4.12 | vftraGnA: samasa/krt route yields vftrahnA (hn->Gn by 7.3.54/6.4.? upstream) | pipelines/krdanta
- 8.4.16 | loT route short tripadi list lacks 8.4 natva (pariyARi) | pipelines/tinanta.py
- 8.4.60 | fixture expects BavAMllunAti (anusvara) but Kasika has anunasika; engine has no anunasika consonant surface | owner decision (HANDOVER 4.4)

