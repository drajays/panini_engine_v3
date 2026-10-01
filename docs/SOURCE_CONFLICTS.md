# Source conflicts

Disagreements between sources (or between a source and the engine) that the
engine must not resolve silently. Authority order: Jijñāsu > Kāśikā > Rajpopat >
data. Each entry stays **OPEN** until Ajay rules; code is not changed meanwhile.

Paths: `data.txt` / `kashika.txt` = ashtadhyayi.com `sutraani/` (iCloud
`Panini_sanskrit/sanskrit/data-master/`); "adhikāra corpus" =
`~/ashtadhyayi/adhikara/pada-A.P/<id>.txt` (read by `scripts/adhikara_audit.py`).

---

## SC-001 — Is 4.1.92 तस्यापत्यम् an adhikāra over the apatya section? — OPEN

**Engine today:** `sutra_4_1_92` is `SutraType.ADHIKARA`, scope 4.1.92–4.3.120.
84 modules (4.1.93–4.1.178) gate on `adhikara_in_effect(sid, state, "4.1.92")`.

| Source | Says |
|---|---|
| `data.txt` row i=41092 | `type: AD$प्राग्दीव्यतीयः शेषाधिकारः$43120` — adhikāra, ends 4.3.120 (the engine follows this). The label names the प्राग्दीव्यतीय / शेष block, which doesn't fit 4.1.92 and may be a mis-attached row. |
| adhikāra corpus, 4.1.93–4.1.178 | Governing heads: 3.1.1, 3.1.2, 3.1.3, 4.1.1, 4.1.76, 4.1.82, 4.1.83. **4.1.92 isn't listed.** |
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
