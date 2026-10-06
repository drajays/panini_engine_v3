# Source conflicts

Disagreements between sources (or between a source and the engine) that the
engine must not resolve silently. Runtime conflict is Art. 21 (Paribhāṣenduśekhara).
Meaning disputes are Art. 22. Notable disagreements stay here until Ajay rules;
code is not changed meanwhile.

Paths: `data.txt` / `kashika.txt` = ashtadhyayi.com `sutraani/` (iCloud
`Panini_sanskrit/sanskrit/data-master/`); "adhikāra corpus" =
`~/ashtadhyayi/adhikara/pada-A.P/<id>.txt` (read by `scripts/adhikara_audit.py`).

---

## SC-T — sūtra pāṭha: workbook vs ashtadhyayi.com `data.txt` (AMENDMENT 20, 2026-10-06)

`scripts/build_sutra_context.py` now corrects workbook `text` to the T0 pāṭha (`data.txt` `s`) — 201 sūtras
(typos/truncations copied from an older site export: 1.1.5 क्क्ङिति, 1.1.34 truncated, 1.2.59 द्वायोः, 1.3.87 lacks च …).
Kept: 9 where the only difference is an added ँ (workbook marks pratijñā-anunāsika: क्विँप्, घिनुँण्). Owner overrides untouched.
Every case is in `data/inputs/sutra_context.conflicts.json` → `text` (`kind`: `corrected_to_T0` | `anunasika_marking_kept`).

---

## SC-001 — Is 4.1.92 तस्यापत्यम् an adhikāra over the apatya section? — RESOLVED 2026-10-01

**Ruling (Ajay):** It is an अर्थनिर्देश (Kāśikā) that connects with the earlier and
later affixes. Through svarita (1.3.11, per Nyāsa and Padamañjarī) it also acts as
the adhikāra of the apatya section. Implemented as AMENDMENT 16 / Constitution
Art. 20: the record stays `ADHIKARA` and gets `artha_nirdesha=ArthaNirdesha("apatya",
purva_from="4.1.83")`, with the frame covering 4.1.83–4.1.178 (scope end moved from
4.3.120). The handover's "Kāśikā reads it as adhikāra" was inaccurate. The
`data.txt` and workbook `AD … 43120` labels are a site taxonomy, not a source for
scope.

*Original record below.*

**Engine today:** `sutra_4_1_92` is `SutraType.ADHIKARA`, scope 4.1.92–4.3.120.
84 modules (4.1.93–4.1.178) gate on `adhikara_in_effect(sid, state, "4.1.92")`.

| Source | Says |
|---|---|
| `data.txt` row i=41092 | `type: AD$प्राग्दीव्यतीयः शेषाधिकारः$43120` — adhikāra, ends 4.3.120 (the engine follows this). The label names the प्राग्दीव्यतीय / शेष block, which doesn't fit 4.1.92 and may be a mis-attached row. |
| adhikāra corpus, 4.1.93–4.1.178 | Governing heads: 3.1.1, 3.1.2, 3.1.3, 4.1.1, 4.1.76, 4.1.82, 4.1.83. **4.1.92 isn't listed.** |
| workbook `sutra` row 41092 | `Sutra_type: अधिकारः`, `Influence: 41092-43120`. It agrees with `data.txt`. |
| Kāśikā 4.1.92 | "अर्थनिर्देशोऽयम्, पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते।" It's an artha-nirdeśa that attaches to the affixes before **and** after it, not an adhikāra that opens a forward scope. |

**Consequence:** If Kāśikā wins, 4.1.92 is a meaning-assignment over the
प्राग्दीव्यतीय affixes (on both sides). Gating 4.1.93+ on a forward 4.1.92 frame
would then be the wrong mechanism, though it fires on the same inputs in practice.
If `data.txt` wins, the current code stands, but the scope end (4.3.120 vs the
end of the apatya section, 4.1.178) still needs a ruling.

**Affected (84):** 4.1.93–4.1.178 except 4.1.105 and 4.1.162 (they have no
4.1.92 gate). Full list: `docs/ADHIKARA_AUDIT.md` § Mismatches.

**Question for Ajay:** Should 4.1.92 be ADHIKARA (keep the gates, and fix the scope
end?) or an artha-nirdeśa (replace the 84 gates with a meaning tag read by the
affix sūtras)?

---

## SC-002 — 4.2.92 शेषे: adhikāra (Kāśikā) vs vidhi (`data.txt`) — OPEN

**Engine today:** `sutra_4_2_92` is `SutraType.ADHIKARA`, scope 4.2.92–4.3.134.
4.2.114 gates on it.

| Source | Says |
|---|---|
| Kāśikā 4.2.92 | "शेष इत्यधिकारोऽयम्। यानित ऊर्ध्वं प्रत्ययाननुक्रमिष्यामः, शेषेऽर्थे ते वेदितव्याः।" Adhikāra. |
| `data.txt` row i=42092 | `type: V$$`, i.e. vidhi. |
| adhikāra corpus, 4.2.114 | Lists 3.1.1–3.1.3, 4.1.1, 4.1.76, 4.1.82, 4.1.83. **4.2.92 isn't listed.** |

**Engine follows Kāśikā** (higher authority), so no change is proposed. This is
logged because the data sources disagree, and the audit counts 4.2.114 as a mismatch.

---

## SC-003 — sūtra-map workbook vs ashtadhyayi.com (T2 import) — OPEN

Produced by `scripts/build_sutra_context.py`. The full machine-readable list is in
`data/inputs/sutra_context.conflicts.json`. Nothing is auto-resolved: `sutra_context.json` keeps the workbook
(or override) value, and `provenance` says so. Neither source outranks Kāśikā; each row needs checking
against Kāśikā before the engine relies on that field.

| Field | Count | Rule |
|---|---|---|
| type | 13 | workbook `Sutra_type` ≠ `sutraBasics.json` `प्रकारः` (both non-empty) |
| adhikāra extent | 31 | workbook `Influence` range on a head ≠ first/last sūtra the adhikāra corpus says it governs (or only one side has it) |
| anuvṛtti | 325 | an `anuvritti/` source sūtra isn't among the workbook's anuvṛtti sources |

### type (all)

- 1.2.4: workbook ['अतिदेशः', 'संज्ञा'] · ashtadhyayi.com ['अतिदेशः']
- 1.2.18: workbook ['अतिदेशः', 'संज्ञा'] · ashtadhyayi.com ['अतिदेशः']
- 1.2.19: workbook ['अतिदेशः', 'संज्ञा'] · ashtadhyayi.com ['अतिदेशः']
- 1.2.22: workbook ['अतिदेशः', 'संज्ञा'] · ashtadhyayi.com ['अतिदेशः']
- 1.4.56: workbook ['संज्ञा', 'अधिकारः'] · ashtadhyayi.com ['अधिकारः']
- 1.4.83: workbook ['अधिकारः'] · ashtadhyayi.com ['संज्ञा', 'अधिकारः']
- 2.1.4: workbook ['संज्ञा'] · ashtadhyayi.com ['अधिकारः']
- 2.1.5: workbook ['अधिकारः'] · ashtadhyayi.com ['संज्ञा', 'अधिकारः']
- 2.2.23: workbook ['अधिकारः'] · ashtadhyayi.com ['संज्ञा']
- 3.1.22: workbook ['विधिः', 'अधिकारः'] · ashtadhyayi.com ['अधिकारः']
- 3.1.91: workbook ['संज्ञा', 'अधिकारः'] · ashtadhyayi.com ['अधिकारः']
- 3.3.94: workbook ['विधिः', 'अधिकारः'] · ashtadhyayi.com ['अधिकारः']
- 5.3.1: workbook ['संज्ञा', 'अधिकारः'] · ashtadhyayi.com ['संज्ञा']

### adhikāra extent (all)

- 1.4.56: workbook ['1.4.56', '1.4.98'] · corpus extent ['1.4.56', '1.4.97']
- 2.1.4: workbook None · corpus extent ['2.1.4', '2.2.38']
- 2.1.11: workbook None · corpus extent ['2.1.11', '2.2.38']
- 2.2.23: workbook ['2.2.23', '2.2.28'] · corpus extent None
- 2.3.1: workbook ['2.3.1', '2.3.73'] · corpus extent ['2.3.1', '2.3.72']
- 3.1.3: workbook None · corpus extent ['3.1.3', '5.4.160']
- 3.1.97: workbook None · corpus extent ['3.1.97', '3.1.132']
- 3.2.123: workbook ['3.2.123', '3.2.331'] · corpus extent ['3.2.123', '3.3.1']
- 4.1.82: workbook ['4.1.82', '5.2.140'] · corpus extent ['4.1.82', '5.4.160']
- 4.1.83: workbook ['4.1.83', '4.4.1'] · corpus extent ['4.1.83', '4.3.168']
- 4.1.92: workbook ['4.1.92', '4.3.120'] · corpus extent None
- 4.2.92: workbook None · corpus extent ['4.3.23', '4.3.23']
- 4.4.75: workbook ['4.4.75', '5.1.136'] · corpus extent ['4.4.75', '4.4.144']
- 5.1.78: workbook ['5.1.78', '5.1.98'] · corpus extent ['5.1.78', '5.1.96']
- 6.1.1: workbook None · corpus extent ['6.1.1', '6.1.12']
- 6.1.46: workbook None · corpus extent ['6.4.46', '6.4.70']
- 6.1.71: workbook ['6.1.71', '6.1.154'] · corpus extent ['6.1.72', '6.1.157']
- 6.1.83: workbook ['6.1.83', '6.1.109'] · corpus extent None
- 6.1.84: workbook None · corpus extent ['6.1.84', '6.1.111']
- 6.1.133: workbook ['6.1.133', '6.1.154'] · corpus extent None
- 6.1.135: workbook None · corpus extent ['6.1.135', '6.1.157']
- 6.2.64: workbook ['6.2.64', '6.2.91'] · corpus extent ['6.2.6', '6.2.91']
- 6.3.1: workbook None · corpus extent ['6.3.1', '6.3.139']
- 6.4.46: workbook ['6.4.46', '6.4.70'] · corpus extent None
- 7.2.19: workbook ['7.2.19', '7.2.98'] · corpus extent None
- 7.2.91: workbook None · corpus extent ['7.2.91', '7.2.98']
- 7.3.10: workbook ['7.3.10', '7.3.32'] · corpus extent ['7.3.10', '7.3.31']
- 7.4.58: workbook None · corpus extent ['7.4.58', '7.4.97']
- 8.1.16: workbook ['8.1.16', '8.3.55'] · corpus extent ['8.1.16', '8.3.54']
- 8.2.82: workbook ['8.2.82', '8.2.108'] · corpus extent ['8.2.82', '8.2.107']
- 8.3.2: workbook None · corpus extent ['8.3.2', '8.3.12']

### anuvṛtti (first 50 of 325)

- 1.1.18: workbook ['1.1.11', '1.1.16', '1.1.17'] · ashtadhyayi.com ['1.1.7', '1.1.11', '1.1.16']
- 1.1.63: workbook ['1.1.62'] · ashtadhyayi.com ['1.1.63']
- 1.1.72: workbook ['1.1.68'] · ashtadhyayi.com ['1.1.68', '1.1.168']
- 1.3.9: workbook [] · ashtadhyayi.com ['1.3.2']
- 1.3.13: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.14: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.15: workbook ['1.3.12', '1.3.14'] · ashtadhyayi.com ['1.3.13', '1.3.14']
- 1.3.16: workbook ['1.3.12', '1.3.14', '1.3.15'] · ashtadhyayi.com ['1.3.13', '1.3.14', '1.3.15']
- 1.3.17: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.18: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.19: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.20: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.21: workbook ['1.3.12', '1.3.20'] · ashtadhyayi.com ['1.3.13', '1.3.20']
- 1.3.22: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.23: workbook ['1.3.12', '1.3.22'] · ashtadhyayi.com ['1.3.13', '1.3.22']
- 1.3.24: workbook ['1.3.12', '1.3.22'] · ashtadhyayi.com ['1.3.13', '1.3.22']
- 1.3.25: workbook ['1.3.12', '1.3.22'] · ashtadhyayi.com ['1.3.13', '1.3.22']
- 1.3.26: workbook ['1.3.12', '1.3.22', '1.3.25'] · ashtadhyayi.com ['1.3.13', '1.3.22', '1.3.25']
- 1.3.27: workbook ['1.3.12', '1.3.26'] · ashtadhyayi.com ['1.3.13', '1.3.26']
- 1.3.28: workbook ['1.3.12', '1.3.26'] · ashtadhyayi.com ['1.3.13', '1.3.26']
- 1.3.29: workbook ['1.3.12', '1.3.26'] · ashtadhyayi.com ['1.3.13', '1.3.26']
- 1.3.30: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.31: workbook ['1.3.12', '1.3.30'] · ashtadhyayi.com ['1.3.13', '1.3.30']
- 1.3.32: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.33: workbook ['1.3.12', '1.3.32'] · ashtadhyayi.com ['1.3.13', '1.3.33']
- 1.3.34: workbook ['1.3.12', '1.3.32'] · ashtadhyayi.com ['1.3.13', '1.3.33']
- 1.3.35: workbook ['1.3.12', '1.3.32', '1.3.34'] · ashtadhyayi.com ['1.3.13', '1.3.33', '1.3.34']
- 1.3.36: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.37: workbook ['1.3.12', '1.3.36'] · ashtadhyayi.com ['1.3.13', '1.3.36']
- 1.3.38: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.13']
- 1.3.63: workbook ['1.3.12'] · ashtadhyayi.com ['1.3.62']
- 1.4.7: workbook ['1.4.6'] · ashtadhyayi.com ['1.4.3', '1.4.6']
- 1.4.20: workbook [] · ashtadhyayi.com ['1.4.14', '1.4.18']
- 1.4.80: workbook [] · ashtadhyayi.com ['1.4.59', '1.4.60']
- 1.4.100: workbook [] · ashtadhyayi.com ['1.4.99']
- 1.4.108: workbook [] · ashtadhyayi.com ['1.4.105']
- 2.3.49: workbook ['2.3.48'] · ashtadhyayi.com ['2.3.46', '2.3.47']
- 3.1.4: workbook ['3.1.1'] · ashtadhyayi.com ['3.1.3']
- 3.1.54: workbook ['3.1.22', '3.1.43', '3.1.44', '3.1.48', '3.1.52', '3.1.53'] · ashtadhyayi.com ['3.1.4', '3.1.52', '3.1.53']
- 3.1.74: workbook ['3.1.1', '3.1.2', '3.1.22', '3.1.67', '3.1.68', '3.1.73'] · ashtadhyayi.com ['3.1.67', '3.1.68', '3.1.75']
- 3.1.75: workbook ['3.1.1', '3.1.2', '3.1.22', '3.1.67', '3.1.68', '3.1.73'] · ashtadhyayi.com ['3.1.67', '3.1.68', '3.1.75']
- 3.1.80: workbook ['3.1.1', '3.1.2', '3.1.22', '3.1.67', '3.1.68', '3.1.79'] · ashtadhyayi.com ['3.1.67', '3.1.68', '3.1.80']
- 3.1.85: workbook ['3.1.84'] · ashtadhyayi.com ['3.1.67', '3.1.68', '3.1.84']
- 3.1.86: workbook ['3.1.1', '3.1.2', '3.1.22', '3.1.84'] · ashtadhyayi.com ['3.1.67', '3.1.68', '3.1.84']
- 3.4.81: workbook [] · ashtadhyayi.com ['3.4.79']
- 3.4.110: workbook ['3.4.108', '3.4.109'] · ashtadhyayi.com ['3.4.99', '3.4.108', '3.4.109']
- 3.4.114: workbook ['3.1.1', '3.1.2', '3.1.91'] · ashtadhyayi.com ['3.4.113']
- 3.4.115: workbook ['3.4.114'] · ashtadhyayi.com ['3.4.113', '3.4.114']
- 3.4.116: workbook ['3.4.114'] · ashtadhyayi.com ['3.4.113', '3.4.114']
- 4.1.10: workbook ['3.1.1', '3.1.2', '4.1.1', '4.1.3'] · ashtadhyayi.com ['4.1.5']
