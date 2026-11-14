# Ṣopadeśa audit — Kāśikā 6.1.64 lakṣaṇa against `data/inputs/dhatupatha_upadesha.json` (2026-11-15)

**Status: findings for the owner; no engine or data change made.** The engine reads the dhātu's upadeśa from the pāṭha data;
the Kāśikā itself says the primary criterion is "ये तथा पठ्यन्ते" (as read in the pāṭha) and gives the lakṣaṇa only as an
alternative ("अथवा लक्षणं क्रियते").

## What the Kāśikā (DB `kashika`, 6.1.64) actually says
- Vidhi: धातोरादेः षकारस्य स्थाने सकारादेशः (षह → सहते; षिच → सिञ्चति).
- Lakṣaṇa: **अज्दन्त्यपराः सादयः षोपदेशाः स्मिस्विदिस्वदिस्वञ्जिस्वपितयश्च । सृपिसृजिस्तृस्त्यासेक्सृवर्जम् ।**
  (an s followed by an ac or a dantya, plus smi, svidi, svadi, svañji, svapi; excluding sṛp, sṛj, stṛ, styā, sek, sṛ).
- Vārttika: **सुब्धातुष्ठिवुष्वष्कतीनां प्रतिषेधो वक्तव्यः** — ṣoḍīyati, ṣaṇḍīyati (subdhātu), ṣṭhīvati, ṣvaṣkate.

## Where the pasted account (2026-11-15) differs, and what the engine does
| pasted | Kāśikā / engine |
|---|---|
| the lakṣaṇa is for *monosyllabic (ekāc)* roots | the Kāśikā says nothing of ekāc: "सादयः" with ac/dantya after the s. Not adopted. |
| exceptions are 7 roots incl. *stu* | the exceptions are sṛp, sṛj, stṛ, styā, sek, sṛ. *stu* is **not** excepted (ṣṭu is ṣopadeśa: अभिष्टौति, 8.3.65). Not adopted. |
| ṣvaṣk listed as an always-ṣopadeśa root | it is a vārttika **exception** to 6.1.64 (it keeps ṣ). Engine: `_PRATISHEDHA = {zWivu~, zvazka~}`. |
| ṇ → n and ṭavarga → tavarga both "by 6.1.64" | ṇ → n is 6.1.65 णो नः (own sūtra, own file); the ṭavarga reversion is निमित्तापाये नैमित्तिकस्याप्यपायः, done inside the engine's 6.1.64 act. |
| vārttika wording "सत्वप्रतिषेधो … ष्वष्कादीनाम्", example षण्ढीयते | Kāśikā wording "सुब्धातुष्ठिवुष्वष्कतीनां प्रतिषेधः", examples षोडीयति, षण्डीयति. |

The engine's 6.1.64 already carries the vārttika's two dhātu exceptions and the ṭavarga reversion. The subdhātu half of the vārttika
(a nāmadhātu in क्यच्, e.g. षण्डीयति) is the nāmadhātu entry-point gap (plan G1), not a 6.1.64 gap.

## Literal-lakṣaṇa check of the data (for the owner's pāṭha check; not auto-fixed)
Roots the data reads with **s** that satisfy the lakṣaṇa literally and are not in its exception list:
sAD (5), sIk (1), sUrkz/sUrkzy (1), sam (4), smiw (10), stanB/stunB (9), stfh/stfnh (6), stim (4), stu (1), sTuq (6), and the gaṇa‑10 stems
sAma, sAnb, sAntv, sAra, sTUla, sUca, sUtra, saBAja, sangrAma, sanketa, satra, stana, stena, stoma, suKa.
Data reads **ṣ** but the lakṣaṇa does not cover: zvakk, zvazk, zwyE (the vārttika/exception cases).
## Result of the check (owner asked 2026-11-15)
Each flagged root was compared with the brain's Dhātupāṭha table (`dhatus`, ashtadhyayi.com) and with the Kāśikā 8.3.65 examples.
- **28 of the 29 are read with s in the pāṭha itself** (sūrkṣ, sūrkṣy, samī, stima, stṛhū, stṛnhū, sthuḍ, stanbhu, stunbhu, stṛñ, sānb, smiṭ, the gaṇa‑10
  stems …). Our data equals the pāṭha: **no change**. The lakṣaṇa is a Kāśikā alternative ("अथवा"), not a second source of truth, and
  the gaṇa‑10 stems are ṇic-stems of nouns, not pāṭha roots in the ṣopadeśa sense. sānt​va is read both as षान्त्व (our `curAdi_10_0051 zAntva~`) and सान्त्व.
- **One real data fault, `BvAdi_zwuY` (tier `curated_extension`, gaṇa 1, `upadesha_slp1 = stuY`).** The pāṭha root is **ष्टुञ्** (adādi 2.38,
  `Adadi_02_0038 zwuY`, already in the data); the curated duplicate keeps the post‑6.1.64 spelling with s, so 8.3.65 (अभिष्टौति) can never see an
  ādeśa-s on it. Its own note says so ("full ``zwuY`` ṭhu-it pending"). Users: `pipelines/stutavAn_prathamA_stuY.py`, `pipelines/dhatupatha.py`,
  `core/canonical_pipelines.py`, `tests/forward/test_forward_krdanta_trc.py`, `tests/unit/test_ktavatu_vAnt_chatushtaya_pipelines.py`.
  **Not fixed now:** switching the upadeśa to `zwuY` needs the general 6.1.64 + ṭu‑it handling and a re-pin of those derivations; it is the
  coordinated job "6.1.64 general scope" after the commit sequence, not a data edit.

## ṇopadeśa lakṣaṇa vs the data (2026-11-15) — CLOSED: table kept as is
n-initial roots outside the Kāśikā's 8-root exception list that the data reads with n: narba (1.170), nizka (10.209), nala (10.333), nivAsa
(10.427); `Rala~` (1.972) is a separate ṇ entry and stays. Decision: **no data change** — the pāṭha table reads n for all four and the
reading of the pāṭha takes precedence over the lakṣaṇa. **Source caveat:** a justification from Kṣīrasvāmin / standard commentary was
offered but is not in the local brain (no Kṣīrataraṅgiṇī / Mādhavīya dhātuvṛtti) and has not been checked; this entry rests on the pāṭha
reading, not on that citation. Reopen only if an edition is found that prints ṇarba, ṇiṣka, ṇala or ṇivāsa.
Deferred with the later "general 6.1.64 / 6.1.65" job: `BvAdi_nIY` (should be `RIY`) and `BvAdi_zwuY` (`stuY`, should be `zwuY`).
