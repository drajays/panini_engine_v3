# Shortcut ledger (owner policy, 2026-10-27)

Rule: no shortcut by default. A temporary shortcut is allowed only when it keeps the engine fast to build, is **marked in code** (`# SHORTCUT <id>:` naming the ceiling) and **listed here**, and is corrected before the Laghukaumudī track is called finished. The track is not finished while any row is open.

| id | where | what is simplified | the correct form | status |
|----|-------|--------------------|------------------|--------|
| S1 | sutra_7_1_78 / 7_1_79 | stubs; the abhyasta exclusion is read as the `origin_abhyasta` tag inside 7.1.80/81 | 7.1.78 as a real pratiṣedha; 7.1.79 neuter vā | open |
| S2 | 4.1.4 / 6.1.101 | ṭāp stays a separate Term; 6.1.101 joins a+ā after the aṅgakārya pool, so 7.3.105/106 never see ā-final aṅga (`aja` vocative → ajAH) | merge ṭāp at 4.1.4 time for non-sarvanāma stems; rerun 4.1.4 / taddhita tests | closed 2026-10-27 (see S2b) |
| S3 | 7.3.44 | stub; ṇvul/ka feminine gives pAWakA | real rule (pratyayasthāt kāt pūrvasyāta idāpy asupaḥ) | closed 2026-10-27 (see S2b) |
| S4 | 4.1.6 | vārttikas `dhātor ugitaḥ pratiṣedhaḥ`, `añcateś copasaṃkhyānam` not modelled | model both | open |
| S5 | 7.1.80 | luk dhātus ending in ā (yā, bhā) get no optional nuṃ | record the aṅga's final through luk | open |
| S6 | 8.4.47 / 8.4.56 | duplicate doubled readings (paWantyyO, kurvvatI) | resolve the optional doubling | open |
| S7 | 4.1.3 / 4.1.5 / 4.1.6 | the new NIp Term carries `prātipadika` + `anga` tags so existing nadī rules read it | a pratyayānta-prātipadika merge (4.1.1) done once, not per sūtra | open |
| S8 | sutra_4_1_5 | ṅīp only for derived (vyutpanna) ṛ-/n-final stems; avyutpanna masculine stems (rājan → rājñī) get none | Lexicon fact: which avyutpanna stems are strī-less words vs nitya-strī (svasṛ, mātṛ) | open |
| S2b | pipelines/subanta.py + 6.1.101 | the ṭāp ekādeśa runs as a scoped pre-pass (meta ekadesha_scope=tap) before the aṅgakārya pool | scheduler orders 6.1.101 by sūtra order across pools | open |
| S9 | 3.2.130 | iṅ / dhāri: only the bare dhātu iN is wired (no adhi- upasarga, no ṇijanta dhāri); its form comes out `yan` | upasarga + ṇic through the loop, then 6.4.77 iyaṅ (adhīyan, dhārayan) | open |
| S10 | sutra_3_2_127 | sat-saṃjñā is a tag on the participle's pratyaya Term; it is not carried to the merged stem's origin record, so 2.2.11 cannot read it yet | add `origin_sat` to engine/origin.py when 2.2.11 is made real | open |
