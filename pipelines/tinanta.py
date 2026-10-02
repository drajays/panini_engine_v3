"""
pipelines/tinanta.py — tiṅanta glass-box derivation driver.
─────────────────────────────────────────────────────────────

Full automatic Pāṇini-sūtra prakriyā for tiṅanta forms.
Every phonological step calls apply_rule(); zero patchwork, zero gold shortcuts.

CONSTITUTION compliance (Arts. 2, 6, 7, 8):
  • All cond() calls are phonemic/saṃjñā-blind to vibhakti/vacana.
  • puruṣa + vacana enter ONLY as recipe parameters to select the tiṅ ādeśa
    from data/inputs/tin_upadesha.json (recipe layer, NOT engine layer).
  • pada (parasmaipada/ātmanepada) is derived via sūtra 1.3.78 — NOT passed externally.
  • dhātu comes from data/inputs/dhatupatha_upadesha.json — NOT hardcoded.
  • vikaraṇa is selected by gaṇa per the relevant sūtras (3.1.68, 3.1.69, etc.).

Recipe order for bhvādi laṭ kartari (e.g. भू → भवति):
  STAGE 1 — dhātu-prakaraṇa (upadeśa it-lopa)
    1.3.1   bhūvādayo dhātavaḥ  (dhātu saṃjñā)
    1.3.2   upadeśe'janunāsika it  (anunāsika vowel → it)
    1.3.3   halantyam  (final hal → it)
    1.3.9   tasya lopaḥ  (lopa of it-varṇas)

  STAGE 2 — pada-nirṇaya
    1.3.78  śeṣāt kartari parasmaipada  (sets parasmaipada gate)

  STAGE 3 — lakāra attachment + tiṅ selection
    3.1.91  dhātoḥ  (adhikāra: pratyayas come from dhātu)
    3.1.1   pratyayaḥ  (general pratyaya adhikāra)
    3.1.2   paraś ca
    3.1.3   ādyudāttaś ca
    3.2.123 vartamāne laṭ  (adhikāra for laṭ)
    [structural: attach laT Term]
    3.4.77  lasya  (l-adhikāra for tiṅ substitution)
    3.4.78  tiptasjhi…  (recipe arms tin_adesha_form; laT → tiṅ ādeśa)
    1.4.99  parasmaipade  (marks ādeśa as parasmaipada saṃjñā)
    1.3.3   halantyam on tiṅ ādeśa (p in tip → it)
    1.3.9   tasya lopaḥ (tip → ti)

  STAGE 4 — vikaraṇa insertion (gaṇa-based)
    3.1.68  kartari śap  [bhvādi]  (insert śap between dhātu and tiṅ)
    3.4.113 tiṅśit sārvadhatukam  (śap is śit → sārvadhatuka)
    1.3.8   laśakvataddhite  (ś in śap → it)
    1.3.3   halantyam  (p in śap → it)
    1.3.9   tasya lopaḥ  (śap → a)
    1.3.10  samānānudeśaḥ

  STAGE 5 — aṅgakārya
    1.4.13  yāsmāt pratyayavidhi… → aṅga saṃjñā
    1.1.5   kṅiti ca (blocks guṇa/vṛddhi for kit/ṅit — guard)
    7.3.84  sārvadhatukārdhadhatukayoḥ (guṇa: ik-vowel → guṇa)

  STAGE 6 — sandhi
    6.1.78  eco'yavāyāvaḥ  (EC + AC → split: o+a → av)

  STAGE 7 — merge (structural)

Gaṇa → vikaraṇa map (implemented in _apply_vikarana):
  1  bhvādi  → śap  (3.1.68)
  4  divādi  → śyan (3.1.69)
  6  tudādi  → śa   (3.1.77)
  (others extendable)
"""
# ── CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected ──
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Optional

import sutras  # noqa: F401  — side-effect: registers all sūtras

from engine       import apply_rule
from engine.state import State, Term
from pipelines.it_prakarana import run_it_prakarana
from core.phases.tripadi import execute_tripadi_phase
from phonology.varna import parse_slp1_upadesha_sequence, mk as _mk

from core.canonical_pipelines import (
    P00_krt_it_lopa,
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_lat_vartamane_tip_and_sap,
    P00_lashakvataddhite_it_lopa_chain,
    P00_tin_tusma_audit_halantyam_lopa,
    P00_anga_guna_audit_1_4_13_1_1_5_7_3_84,
    P01_samjna_dhatu_class,
    P06a_pratyaya_adhikara_3_1_1_to_3,

    P00_tripadi_rutva_visarga,
    P00_san_kit_kngiti,
    P00_parasmai_tin_adesha,
    P00_tin_adesha_base,
    P00_lac_lat_attach,
    P00_lat_vartamane,
    P00_guna_7_3_84,
    P00_guna_7_3_86,
    P00_tanadi_u_guna,
    P00_juhotyadi_slu_dvitva_abhyasakarya,
    P00_hal_it_lopa,
    P00_jha_adesha,
    P00_sap_luk,
    P00_guna_rapara_ayadi,
    P00_ngit_At_iy_guna,
    P00_at_or_At_agama,
    P00_tripadi_8_4_55_visarga,
    P00_luk_samjna_60_62,
    P00_stri_4_1_wap,
    P00_san_dvitva,
    P00_hal_anit_guna,
    P00_lit_ta_esh_it_lopa,
    P00_mRj_abhyasa_hrasva,
    P00_at_agama_it_lopa,
    P00_tripadi_anusvara_parasavarna,
    P00_ru_visarga_pair,
    P00_tripadi_samyoganta_ru_visarga,
    P00_adadi_tere_3_4_79,
    P00_adadi_sap_luk_tere,
    P00_san_dirgha_hrasva,
    P00_guna_sandhi_7_3_84_6_1_78,
)

from pipelines.dhatupatha import get_dhatu_row, _payload, _envelope

# ─────────────────────────────────────────────────────────────────────────────
# DATA LOADING (Art. 6: data/inputs only)
# ─────────────────────────────────────────────────────────────────────────────

_TIN_JSON = Path(__file__).resolve().parent.parent / "data" / "inputs" / "tin_upadesha.json"


@lru_cache(maxsize=1)
def _tin_data() -> dict:
    with open(_TIN_JSON, encoding="utf-8") as f:
        return json.load(f)


# Gaṇa → vikaraṇa upadeśa SLP1.  Only common gaṇas covered; extend as needed.
_GANA_VIKARANA: dict[int, str] = {
    1: "Sap",   # bhvādi  — 3.1.68 kartari śap
    4: "SyaN",  # divādi  — 3.1.69
    6: "Sa",    # tudādi  — 3.1.77
}

# Lakāra name normalization (SLP1 upadeśa → tin_upadesha key prefix).
_LAKARA_KEY: dict[str, str] = {
    "laT": "laT",
    "liT": "liT",
    "luT": "luT",
    "lRT": "lRT",
    "loT": "loT",
    "laG": "laN",
    "liG": "liN",
    "luG": "luN",
    "lRG": "lfN",
    "AsIrliG": "AsIrliN",
    "luG_karmani": "luN-karmani",
}


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _upadesha_to_id_map() -> dict[str, str]:
    """Reverse map: upadesha_slp1 → dhātupātha canonical id.

    Indexed by:
      1. Exact upadesha_slp1 (e.g. 'BU', 'paci~', 'paWa~')
      2. Trailing-~ stripped form (e.g. 'paci' from 'paci~')
      3. raw_dhatu_after_it_lopa_slp1 (e.g. 'pac', 'paW', 'nI') — lets
         callers use the clean post-IT-lopa form as the lookup key.
    """
    env = _envelope(_payload())
    m: dict[str, str] = {}
    for e in env["entries"]:
        up  = e.get("upadesha_slp1", "")
        raw = e.get("raw_dhatu_after_it_lopa_slp1", "")
        eid = e.get("id", "")
        if not eid:
            continue
        if up:
            m[up] = eid
            clean = up.rstrip("~")
            if clean and clean not in m:
                m[clean] = eid
        # raw post-IT-lopa form (e.g. 'paW' for 'paWa~') — lower priority,
        # do not override upadesha-key mappings already set.
        if raw and raw not in m:
            m[raw] = eid
    return m


def _dhatu_row_by_upadesha(upadesha_slp1: str) -> dict:
    """
    Return dhātupātha row for upadeśa SLP1, path id, or canonical id.

    Accepts upadeśa SLP1 (``BU``), ashtadhyayi path id (``01.0001``),
    canonical id (``BvAdi_01_0001``), or alias (``BvAdi_BU``).
    """
    from pipelines.dhatupatha import resolve_dhatu_identifier

    try:
        return resolve_dhatu_identifier(upadesha_slp1)
    except KeyError as e:
        raise KeyError(
            f"dhātu {upadesha_slp1!r} not found in dhātupātha. "
            "Use upadeśa SLP1 (e.g. 'BU', 'pac'), path id (01.0001), "
            "or id (BvAdi_01_0001)."
        ) from e


def _atmane_tin_upadesha(state: State, purusha: int, vacana: int) -> State:
    """3.4.77/3.4.78 ātmanepada tiṅ in upadeśa form (त, आताम्, झ … इट्, महिङ्)
    → 1.4.100 → it-lopa of the tiṅ."""
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    return P00_tin_tusma_audit_halantyam_lopa(state)


def _build_dhatu_term(row: dict, prayoga: str = "kartari", lakara: str = "laT") -> Term:
    """Construct a Term from a dhātupātha row (delegates to tape_init)."""
    from engine.tape_init.tinanta import dhatu_term_from_row

    return dhatu_term_from_row(row, prayoga, lakara)


def _resolve_pada_from_gate(state: State) -> str:
    """Read 1.3.78 paribhāṣā gate to determine pada (recipe layer only)."""
    gate = state.paribhasha_gates.get("prayoga_1_3_78_seza_kartari_parasmaipada", {})
    if isinstance(gate, dict) and gate.get("active"):
        return "parasmai"
    return "atmane"


def _select_tin_adesha(lakara_slp1: str, pada: str, purusha: int, vacana: int) -> str:
    """
    Look up the tiṅ ādeśa from data/inputs/tin_upadesha.json.
    Returns SLP1 string (e.g. 'tip', 'ta', 'mas').
    """
    tin = _tin_data()
    lak_key = _LAKARA_KEY.get(lakara_slp1, lakara_slp1)
    key = f"{lak_key}-{pada}-{purusha}-{vacana}"
    adesha = tin.get(key)
    if adesha is None:
        raise KeyError(
            f"tin_upadesha has no entry for {key!r}. "
            f"Check data/inputs/tin_upadesha.json — laṭ entries: {lak_key}-{pada}-{{3,2,1}}-{{1,2,3}}"
        )
    return adesha


def _prep_bhave(state: State) -> State:
    """3.4.69 prayoga gates + *akarmaka* default on dhātu (bhāve kartari)."""
    for t in state.terms:
        if "dhatu" in t.tags:
            t.meta.setdefault("karmakatva", "akarmaka")
            break
    return apply_rule("3.4.69", state)


def _karmani_yak_it_and_ngiti(state: State) -> State:
    """*yaḳ* it-lopa (**1.3.3** / **1.3.9**) + *ṅit* mark for **7.2.81** / **1.1.5**."""
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)
    for t in state.terms:
        if "vikarana" not in t.tags:
            continue
        stem = "".join(v.slp1 for v in t.varnas)
        if stem in {"ya", "y"} or (t.meta.get("upadesha_slp1") or "").strip() in {"yak", "ya"}:
            t.tags.add("kngiti")
            t.tags.add("ngiti_vikaraṇa")
            break
    state = _samprasarana(state)           # वच् → उच्यते, यज् → इज्यते, ग्रह् → गृह्यते
    # 6.4.51 णेरनिटि — the ṇijanta's ṇi drops before aniṭ yak: चोरि → चोर् (चोर्यते)
    state = apply_rule("6.4.51", state)
    state = apply_rule("6.1.45", state)    # ग्लायते
    state = apply_rule("6.4.48", state)    # अतो लोपः: कक्ख+य → कक्ख्यते
    state = apply_rule("6.4.66", state)    # घुमास्था…हलि: पीयते, स्थीयते, दीयते
    state = apply_rule("6.4.24", state)    # अनिदितां हल उपधायाः क्ङिति: तुम्फ् → तुफ्यते
    state = apply_rule("7.1.100", state)   # ॠत इद्धातोः: नॄ → निर् (+8.2.77 नीर्यते)
    state = apply_rule("1.1.51", state)
    state = apply_rule("7.4.25", state)    # अकृत्सार्वधातुकयोर्दीर्घः: क्षु → क्षूयते
    state = apply_rule("7.4.29", state)    # गुणोऽर्तिसंयोगाद्योः: स्मृ → स्मर्यते (before riṅ)
    # 7.4.28 रिङ् शयग्लिङ्क्षु — ṛ-final aṅga before yak: कृ → क्रि (क्रियते)
    return apply_rule("7.4.28", state)


def _karmani_apply_yak(state: State) -> State:
    """**3.1.67** inserts *yaḳ*; recipe runs it-lopa + *ṅit* saṃjñā only."""
    state = apply_rule("3.1.67", state)
    return _karmani_yak_it_and_ngiti(state)


def _bhave_atmanepada_tin_after_lopa(state: State, *, kartari_atmane: bool = False) -> State:
    """After ``P00_tin_tusma``: 1.4.100 + 3.4.79/80 on bhāve paths, and on
    kartari ātmanepada where the caller opts in.

    Opt-in because 3.4.79 rewrites the ādeśa's upadeśa (ta → te), which hides
    it from later identity checks: a spine that inserts its vikaraṇa *after*
    this point loses śap (loṭ: एध्धे). lṛṭ inserts sya without such a check, so
    it opts in (एधिष्यते); the loṭ spine still needs 3.4.90/91/93 first."""
    if state.meta.get("prayoga") != "bhave" and not kartari_atmane:
        return state
    state = apply_rule("1.4.100", state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("3.4.80", state)
    return state


# ─────────────────────────────────────────────────────────────────────────────
# VIKARAṆA STAGE (gaṇa-specific)
# ─────────────────────────────────────────────────────────────────────────────

# gaṇas whose vikaraṇa is a u (śnu 3.1.73, u 3.1.79): the spines' yaṇ/ayādi
# and yāsuṭ steps key on this, not on "gaṇa 8" alone (सुन्वन्तु, असुन्वन्).
_U_VIKARANA_GANAS = (5, 8)


def _samprasarana(state: State) -> State:
    """6.1.15 वचिस्वपियजादीनां किति / 6.1.16 ग्रहिज्या… ङिति च mark the yaṇ;
    1.1.45 makes it ik, 6.1.108 सम्प्रसारणाच्च takes the next vowel, 6.4.2 हलः
    lengthens an aṅga-final one after a hal. Each self-gates."""
    for sid in ("6.1.15", "6.1.16", "1.1.45", "6.1.108", "6.4.2"):
        state = apply_rule(sid, state)
    return state


def _sit_adesha(state: State) -> State:
    """शिति: the dhātu before a śit vikaraṇa — 7.3.74 शमामष्टानां दीर्घः श्यनि,
    7.3.75 ष्ठिवुक्लम्याचमां शिति, 7.3.76 क्रमः परस्मैपदेषु, 7.3.77 इषुगमियमां छः,
    7.3.78 पाघ्रा… (पिब, जिघ्र, तिष्ठ, सीद …), then 6.1.73 छे च (गछ → गत्छ; 8.4.40 → गच्छ).
    Each self-gates on its own roots."""
    for sid in ("7.3.74", "7.3.75", "7.3.76", "7.3.77", "7.3.78", "6.1.73"):
        state = apply_rule(sid, state)
    # 6.1.97 अतो गुणे at once for an a-final dhātu + the vikaraṇa's a (पिब+अ → पिब,
    # कक्ख+अ); the spine's own 6.1.97 then still has vikaraṇa + tiṅ (अपिबन्).
    i = next((k for k, t in enumerate(state.terms[:-1]) if "dhatu" in t.tags), None)
    if i is not None and state.terms[i].varnas and state.terms[i].varnas[-1].slp1 == "a" \
            and state.terms[i + 1].varnas[:1] and state.terms[i + 1].varnas[0].slp1 == "a":
        state = apply_rule("6.1.97", state)
        state.terms[i].meta.pop("6_1_97_tinganta_done", None)
        state.terms[i].meta["6_1_85_antadivat_a"] = True
    return state


def _apply_vikarana(state: State, gana: int) -> State:
    """
    Insert and process the vikaraṇa pratyaya based on gaṇa.

    Gaṇa 1 bhvādi: 3.1.68 kartari śap.
    Gaṇa 4 divādi: 3.1.69 śyan.
    Gaṇa 6 tudādi: 3.1.77 śa.
    Other gaṇas: raise NotImplementedError.

    After insertion, the vikaraṇa's it-markers are processed
    (1.3.3 / 1.3.8 / 1.3.9 / 1.3.10) and 3.4.113 marks it sārvadhatuka.
    """
    if gana == 1:
        # 3.1.68 kartari śap
        state.meta["3_1_68_kartari_recipe"] = True
        state = apply_rule("3.1.68", state)
        # śap is śit — 3.4.113 now marks both śap (as śit) and ti (tiṅ) sārvadhatuka.
        state = apply_rule("3.4.113", state)
        # Process śap it-markers: 1.3.3 (p→it) + 1.3.8 (ś→it) + 1.3.9 (lopa) + 1.3.10
        state = P00_lashakvataddhite_it_lopa_chain(state)
        return _sit_adesha(state)

    if gana == 4:
        # 3.1.68 utsarga (inserts Śap), then 3.1.69 apavāda (Śap→Śyan)
        state.meta["3_1_68_kartari_recipe"] = True
        state = apply_rule("3.1.68", state)   # utsarga: insert Śap
        state = apply_rule("3.1.69", state)   # apavāda: Śap → Śyan
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        state = _sit_adesha(state)
        # 1.2.4 already ran once against the bare tiṅ-ādeśa (before śyan
        # existed on the tape) earlier in the spine; re-run it now that
        # śyan (a-pit — "Syan" carries no प्-इत्, unlike śap's "Sap") is on
        # the tape, so 1.1.5 sees it and blocks 7.3.84's guṇa: दीव्यति, not
        # देव्यति. Pop-then-recall is this repo's existing idiom for a
        # second 1.2.4 pass (see the upasarga+kṛ ātmanepada spine above).
        state.samjna_registry.pop("1.2.4_sarvadhatukam_apit", None)
        state = apply_rule("1.2.4", state)
        # 6.4.24 अनिदितां हल उपधायाः क्ङिति: nasal upadhā drops before the ṅit
        # vikaraṇa (स्कुभ्नाति, रज्यति)
        state = apply_rule("6.4.24", state)
        # 7.3.82 मिदेर्गुणः — apavāda for मिद् specifically: guṇa still fires
        # (मेद्यति) even though श्यन् now blocks it generally per 1.2.4/1.1.5
        # above. Glass-box, scoped to मिद्'s own upadeśa in its cond() — a
        # no-op for every other divādi root.
        state = apply_rule("7.3.82", state)
        # 7.3.79 ज्ञाजनोर्जा — जन् + श्यन् → जा (जायते); scoped to jan / jñā in its own cond(), a no-op otherwise
        state = apply_rule("7.3.79", state)
        return state

    if gana == 6:
        # 3.1.77 tudādi śa — cond checks gana==6 + no existing Śa.
        state = apply_rule("3.1.77", state)
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        state = _sit_adesha(state)
        # śa is apit, so 1.2.4 सार्वधातुकमपित् makes it ṅit and 1.1.5 blocks
        # guṇa: तुदति, पुरति, कृषति — not *तोदति. Same second 1.2.4 pass as śyan.
        state.samjna_registry.pop("1.2.4_sarvadhatukam_apit", None)
        state = apply_rule("1.2.4", state)
        state = _samprasarana(state)       # 6.1.16 ङिति: वृश्चति, पृच्छति, विचति
        # 6.4.24 अनिदितां हल उपधायाः क्ङिति: nasal upadhā drops before the ṅit
        # vikaraṇa (स्कुभ्नाति, रज्यति)
        state = apply_rule("6.4.24", state)
        state = apply_rule("7.1.59", state)    # शे मुचादीनाम्: मुञ्चति, लिम्पति, तृम्फति
        # 7.4.28 रिङ् शयग्लिङ्क्षु: ṛ-final aṅga before śa (मृ → म्रियते)
        state = apply_rule("7.4.28", state)
        state = apply_rule("7.1.100", state)   # ॠत इद्धातोः: कॄ → किर् (किरति)
        state = apply_rule("1.1.51", state)
        state = apply_rule("6.4.77", state)    # अचि…इयङुवङौ: नुवति, म्रियते, धियति
        return state

    if gana == 2:
        # 3.1.68 kartari śap, then 2.4.72 अदिप्रभृतिभ्यः शपः: luk — the ending
        # attaches to the root itself (याति, एति, अयात्).
        state.meta["3_1_68_kartari_recipe"] = True
        state = apply_rule("3.1.68", state)
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        state = P00_sap_luk(state)             # 2.4.72 → 7.3.89 (क्षौति) → 7.2.76 (रोदिति)
        return state

    if gana == 7:
        # 3.1.78 रुधादिभ्यः श्नम्: na after the root's last vowel (1.1.47 mit);
        # 6.4.111 श्नसोरल्लोपः drops its a before a weak ending (रुन्धः).
        state = apply_rule("1.1.47", state)
        state = apply_rule("3.1.78", state)
        state = apply_rule("6.4.23", state)    # श्नान्नलोपः: हिनस्ति, भनक्ति
        state = apply_rule("6.4.111", state)
        return state

    if gana == 5:
        # 3.1.73 स्वादिभ्यः श्नुः: nu after the dhātu; śnu is apit, so a second
        # 1.2.4 pass makes it ṅit (1.1.5: no guṇa of the root). Strong forms
        # take guṇa of nu's u later (सुनोति); 6.1.77 gives सुन्वन्ति.
        state = apply_rule("3.1.73", state)
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        state.samjna_registry.pop("1.2.4_sarvadhatukam_apit", None)
        state = apply_rule("1.2.4", state)
        return state

    if gana == 9:
        # 3.1.81 क्र्यादिभ्यः श्ना; śnā is apit → ṅit by a second 1.2.4 pass (root
        # keeps no guṇa). Weak endings: 6.4.113 ई हल्यघोः (क्रीणीतः), 6.4.112
        # श्नाभ्यस्तयोरातः (क्रीणन्ति); strong pit ones keep nā (क्रीणाति).
        state = apply_rule("3.1.81", state)
        state = apply_rule("7.3.80", state)    # प्वादीनां ह्रस्वः: लू → लु (लुनाति)
        state = apply_rule("7.3.79", state)    # ज्ञाजनोर्जा: ज्ञा + श्ना → जा (जानाति); scoped to jñā / jan
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        state.samjna_registry.pop("1.2.4_sarvadhatukam_apit", None)
        state = apply_rule("1.2.4", state)
        # 6.4.24 अनिदितां हल उपधायाः क्ङिति: nasal upadhā drops before the ṅit
        # vikaraṇa (स्कुभ्नाति, रज्यति)
        state = apply_rule("6.4.24", state)
        if not state.meta.get("liG_yasut_expected"):   # liṅ: after yāsuṭ/sīyuṭ
            state = apply_rule("6.4.113", state)
            state = apply_rule("6.4.112", state)
        return state

    if gana == 8:
        # 3.1.79 tanādi u-vikaraṇa + root guṇa (7.3.84) + rapara (1.1.51).
        # 3.4.110 kit-upadha (a→u for weak/ṅit forms) fires from the spine's 1.1.5 path.
        # NOTE: the second guṇa (u→o for strong parasmaipada forms like karoti)
        # requires 7.3.84 to fire on the u-vikaraṇa; this is not yet wired into the
        # bhuvādi spine — strong forms currently give *karuti* not *karoti*.
        state = P00_tanadi_u_guna(state)   # 3.1.79 + 7.3.84 + 1.1.51
        return state

    if gana == 3:
        # juhotyādi: śluḥ → dvitva → abhyāsa-kārya (no vikaraṇa syllable
        # stands between dhātu and tiṅ, so 7.3.84's guṇa site below is the
        # tiṅ ādeśa itself, exactly as 1.2.4 already tagged it at line 514).
        state = P00_juhotyadi_slu_dvitva_abhyasakarya(state)
        # 7.1.4 अदभ्यस्तात् (apavāda of 7.1.3 झोऽन्तः): abhyasta jhi → ati, not
        # anti (जुह्वति). Must run before P00_jha_adesha's 7.1.3 below.
        state = apply_rule("7.1.4", state)
        # NOTE (next session): jhaṣ-initial roots (भृ, भी, धा…) still need
        # 8.4.54 अभ्यासे चर्च (बिभर्ति, not भिभर्ति) — but that's a tripāḍī
        # rule and opening 8.2.1 this early regresses हु (guṇa/1.1.5 site
        # logic downstream in this generic bhvādi spine assumes tripāḍī
        # hasn't opened yet). Needs the full execute_tripadi_phase()
        # integration _derive_lit() already uses, not a bare apply_rule
        # add here. Verified with bench.ashtadhyayi_gold --lakara laT:
        # हु is 9/9 (0 errors, was ~everywhere before); भृ/भी/दा/धा/etc.
        # remain in the gaṇa-3 error set (see bench --dump for exact cells).
        return state

    raise NotImplementedError(
        f"vikaraṇa for gaṇa {gana} not yet implemented in pipelines/tinanta.py. "
        "Extend _apply_vikarana() with the appropriate sūtra."
    )


# ─────────────────────────────────────────────────────────────────────────────
# PADA MERGE (structural, mirrors subanta._pada_merge)
# ─────────────────────────────────────────────────────────────────────────────

def _pada_merge(state: State) -> None:
    """Structural merge. Delegates to engine.phases.pada_merger.pada_merge."""
    from engine.phases.pada_merger import pada_merge
    pada_merge(state)


# upasarga | dhātu junction: a + ā → ā (avāpnoti), i + u → yu (paryupāsate), a + e → ai/e … Each rule gates
# itself on the tape, so this is a no-op unless an upasarga Term is present.
_UPASARGA_JUNCTION_RULES = ("6.1.94", "6.1.101", "6.1.97", "6.1.87", "6.1.88", "6.1.77")


def _merge_pada(state: State) -> State:
    """Sandhi at the upasarga | dhātu boundary (pre-tripāḍī, while the Terms are still apart), then the merge."""
    if any("upasarga" in t.tags for t in state.terms):
        for sid in _UPASARGA_JUNCTION_RULES:
            state = apply_rule(sid, state)
        # the upasarga is its own pada until the merge: pada-final m → anusvāra (8.3.23), then parasavarṇa
        # (8.4.58, after the merge): सम् + जानाति → सञ्जानाति; before य/ह the anusvāra stays (संयाति, संहरते)
        for sid in ("8.2.1", "8.3.23"):
            state = apply_rule(sid, state)
        _pada_merge(state)
        return apply_rule("8.4.58", state)   # anusvāra before a stop → its varga's nasal (संजय → सञ्जय)
    _pada_merge(state)
    return state


def _run_lat_kartari_bhuvadi_spine(
    state: State,
    *,
    gana: int,
    lakara: str,
    pada_key: str,
    purusha: int,
    vacana: int,
) -> State:
    """
    STAGE 3–8: bhvādi laṭ kartari spine (lakāra → tiṅ → vikaraṇa → aṅga → sandhi → merge).

    Shared by ``derive()`` and ``derive_autonomous_tinanta()`` (Phase 5 M5).
    Recipe coordinates (puruṣa/vacana/pada) enter only here via tiṅ lookup.
    """
    # 3.1.91 dhātoḥ adhikāra + 3.2.123 vartamāne laṭ + laṭ placeholder attach
    state = P00_lac_lat_attach(state)

    tin_adesha = _select_tin_adesha(lakara, pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    state = _apply_vikarana(state, gana)
    state = P00_jha_adesha(state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)
    state = apply_rule("7.3.101", state)
    state = P00_guna_7_3_84(state)
    # 1.1.51 उरण् रपरः: guṇa of ṛ is ar, not a (वृत् → वर्तते, not वतते) —
    # the lṛṭ/lṛṅ spines already complete it; this laṭ spine did not.
    state = apply_rule("1.1.51", state)
    # 6.4.110 ata ut sārvadhatuke — tanādi weak forms: upadha a→u (kar→kur before kṅit tiṅ)
    state = apply_rule("6.4.110", state)
    # 6.4.108 nityaṃ karoteḥ — kṛ: drop u-vikaraṇa before non-val suffix (kurvaḥ, kurmaḥ)
    state = apply_rule("6.4.108", state)

    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — IK-final vikaraṇa + AC-initial suffix (kuru+anti → kurv+anti)
    state = apply_rule("6.4.87", state)   # हुश्नुवोः सार्वधातुके (apavāda of 6.4.77)
    state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)
    state = apply_rule("6.1.97", state)

    # 3.4.79 टित आत्मनेपदानां टेरे — ātmanepada tiṅ-ādeśas need their ṭi
    # replaced by e (ta → te, giving pacate); self-excludes parasmaipada
    # ādeśas via the 1.4.99 tag, so safe to call unconditionally here.
    # This general bhvādi-kartari spine never called it at all: any plain
    # gaṇa-1 root resolved ātmanepada (not one of the special-cased roots
    # with their own dedicated spine above) silently kept the bare tiṅ
    # vowel — pacate came out pacata (Prakriyotsava sweep bug #14).
    state = apply_rule("3.4.79", state)
    # 3.4.80 थासः से (एधथाः → एधसे) and 6.1.97 अतो गुणे for the ए that 3.4.79
    # just made (एध + ए → एधे, not एधए); both self-gate, vacuous otherwise.
    state = apply_rule("3.4.80", state)
    state = apply_rule("6.1.97", state)
    # आतो ङितः for the duals: एध + आते → एध + इय्ते (7.2.81) → इते (6.1.66
    # लोपो व्योर्वलि) → एधेते (6.1.87 आद्गुणः).
    state = P00_ngit_At_iy_guna(state)

    if gana == 3:
        # 6.4.112 श्नाऽभ्यस्तयोरातः (घु अभ्यस्त branch): दा/धा's own ā drops
        # before a weak (kṅit) sārvadhātuka tiṅ — दत्तः, दद्वः, ददति.
        state = apply_rule("6.4.112", state)
        # 8.4.54 अभ्यासे चर्च (जश्त्व of a jhaṣ-initial abhyāsa: भृ → बिभर्ति,
        # not भिभर्ति) is asiddhavat tripāḍī and needs the abhyāsa Term still
        # distinct — must fire before _pada_merge collapses the terms, same
        # placement _derive_lit() uses (8.2.1 opens the zone; execute_tripadi_
        # phase() below skips both as already-done via their gates).
        state = apply_rule("8.2.1", state)
        state = apply_rule("8.4.54", state)

    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)
    return state


# ─────────────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# LIṬ (PERFECT / PAROKṢA) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

# liṭ parasmaipada ādeśas (after 3.4.82)
_LIT_PARASMAI_ADESHA: dict[tuple, str] = {
    (3, 1): "Ral",   # ṇal → residue a (R cuṭu-it, l halantyam-it)
    (3, 2): "atus",  # atus → atuḥ (tripāḍī)
    (3, 3): "us",    # us → uḥ (tripāḍī)
    (2, 1): "Tal",   # thal → residue ta (T halantyam-it, l halantyam-it) + iṭ
    (2, 2): "aTus",  # aTus → aTuḥ
    (2, 3): "a",     # a
    (1, 1): "Ral",   # same as 3sg + 7.1.91 audit
    (1, 2): "va",    # va + iṭ
    (1, 3): "ma",    # ma + iṭ
}


def _lit_needs_it(purusha: int, vacana: int) -> bool:
    """True for consonant-initial liṭ ādeśa residues that need iṭ āgama."""
    return (purusha, vacana) in {(2, 1), (1, 2), (1, 3)}


def _it_agama(state: State) -> State:
    """7.2.35 आर्धधातुकस्येड् वलादेः, preceded by its pratiṣedha 7.2.10 एकाच
    उपदेशेऽनुदात्तात् (which, when it holds, blocks 7.2.35: पक्ता, पक्ष्यते),
    then 7.2.58 गमेरिट् परस्मैपदेषु, which re-grants iṭ over that niṣedha."""
    state = apply_rule("6.1.45", state)   # आदेच उपदेशेऽशिति: ग्लै → ग्ला (ग्लाता)
    state = apply_rule("7.2.10", state)
    state = apply_rule("7.2.35", state)
    return apply_rule("7.2.58", state)


def _needs_am_lit(state: State) -> bool:
    """3.1.36 इजादेश्च गुरुमतोऽनृच्छः — decided on the dhātu's own varṇas."""
    from sutras.adhyaya_3.pada_1.sutra_3_1_36 import ijadi_gurumat_anrcchah
    d = next((t for t in state.terms if "dhatu" in t.tags), None)
    return d is not None and (bool(d.meta.get("sanadi_pratyayanta"))      # 3.1.35
                              or ijadi_gurumat_anrcchah("".join(v.slp1 for v in d.varnas)))


def _derive_lit_am(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Periphrastic liṭ for any ijādi gurumān dhātu: एध् → एधाञ्चक्रे / -चकार.

      3.2.115 liṭ → 3.1.36 ām → 2.4.81 āmaḥ (liṭ-luk; एध + आम् → एधाम्)
      → 3.1.40 कृञ्चानुप्रयुज्यते लिटि: कृ's own liṭ, derived by this engine in
        the main root's pada (1.3.63 आम्प्रत्ययवत् कृञोऽनुप्रयोगस्य)
      → join → 8.3.23 मोऽनुस्वारः → 8.4.58 परसवर्णः (म् → ञ् before च).

    ponytail: only the kṛ anuprayoga; the as/bhū variants (एधामास) are not
    generated, and 3.1.35/37/38/39 (kās-pratyaya, day-ay-ās, optional uṣ/vid/
    jāgṛ, bhī/hrī/bhṛ/hu) are not routed here yet.
    """
    state.meta["lakara"] = "liT"
    state.meta["liT_lakara_recipe"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("3.1.35", state)      # pratyayānta: चोरि + आम्
    state = apply_rule("3.1.36", state)      # ijādi gurumān: एध + आम्
    state = apply_rule("6.4.55", state)      # णेः अय् before ām: चोरयाम्
    state = apply_rule("2.4.81", state)
    stem = state.terms[-1]
    before = state.flat_slp1()
    kf = derive("qukfY", "liT", "kartari", purusha, vacana, pada=pada_key)
    state.trace.extend(kf.trace)             # कृ's own prakriyā, step by step
    state.terms = [Term(kind="prakriti", varnas=list(stem.varnas) + [v for t in kf.terms for v in t.varnas],
                        tags={"pada", "anga"}, meta={"upadesha_slp1": stem.meta.get("upadesha_slp1", "")})]
    state.emit_structural(
        "__ANUPRAYOGA_3_1_40__", form_before=before, form_after=state.flat_slp1(),
        why_dev="३.१.४० कृञ्चानुप्रयुज्यते लिटि — आमन्तात् परं कृञो लिडन्तम् (पदं १.३.६३ आम्प्रत्ययवत्)।",
        type_label="अनुप्रयोगः")
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.3.23", state)      # मोऽनुस्वारः: आम् + चकार
    # full tripādī over the joined pada: 8.3.24/8.4.58 (उंख् → उङ्ख्), 8.4.40
    # (उत्छ → उच्छ), 8.2.78 (ऊर्दाञ्चक्रे) …
    return P00_tripadi_rutva_visarga(state)


def _lit_thal_guna(state: State) -> State:
    """Guṇa before liṭ thal, which is pit through its sthānī sip (1.1.56) and so
    not kit (1.2.5) — but not ṇit, so no 7.2.116 vṛddhi: चकर्थ, चिचेतिथ."""
    state.meta["liT_strong_recipe"] = True
    state = P00_guna_7_3_84(state)
    state.meta.pop("liT_strong_recipe", None)
    return apply_rule("1.1.51", state)


def _derive_lit(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a liṭ (perfect / parokṣa) form starting from the post-1.3.78 state.
    Implements the full 9-cell bhū liṭ parasmaipada pipeline.
    """
    state.meta["lakara"] = "liT"
    # ── Stage 3: liṭ attachment ──────────────────────────────────────────────
    state.meta["liT_lakara_recipe"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # 3.4.77 lasya adhikāra (scope for tiṅ substitution)
    tin_adesha_std = _select_tin_adesha("liT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha_std)

    # IT on tiṅ ādeśa
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.115 (1st) + 3.4.82 liṭ-specific ādeśa ───────────────────────────
    # Reset gate for first call
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)

    if pada_key == "atmane":
        # ātmanepada liṭ: 3.4.81 लिटस्तझयोरेशिरेच् (ta → e, jha → ire); the
        # rest by 3.4.79 टेरे (liṭ is ṭit) and 3.4.80 थासः से:
        #   पस्पर्धे पस्पर्धाते पस्पर्धिरे · पस्पर्धिषे … · पस्पर्धे …महे
        lit_adesha = None
        state.meta["liT_esh_recipe"] = True
        state = P00_lit_ta_esh_it_lopa(state)
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.80", state)
    else:
        lit_adesha = _LIT_PARASMAI_ADESHA[(purusha, vacana)]
        state.meta["liT_82_adesha_form"] = lit_adesha
        state.meta["liT_82_recipe"] = True
        state = apply_rule("3.4.82", state)

        # IT on liṭ ādeśa (1.3.4 tusma, 1.3.3 halantyam, 1.3.7 cuṭū, 1.3.9 lopa)
        state = apply_rule("1.3.4", state)
        state = P00_hal_it_lopa(state)

    # ── 3.4.115 (2nd audit) + optional 7.1.91 ────────────────────────────────
    # Reset gate for second call
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)

    if purusha == 1 and vacana == 1 and lit_adesha == "Ral":
        state.meta["Nal_uttama_recipe"] = True
        state = apply_rule("7.1.91", state)

    # iṭ before a val-initial ending: parasmai tha/va/ma, ātmane se/dhve/vahe/mahe
    needs_it = ((purusha, vacana) in {(2, 1), (2, 3), (1, 2), (1, 3)} if pada_key == "atmane"
                else _lit_needs_it(purusha, vacana))

    if needs_it:
        # ── iṭ path: iṭ → dvitva → vuk (6.4.88 needs abhyāsa for liṭ context) ──
        if lit_adesha != "Tal":          # thal is pit (1.1.56), not kit
            state = apply_rule("1.2.5", state)
        state.meta["liT_krsrbhr_recipe"] = True
        state = apply_rule("7.2.13", state)
        state = apply_rule("7.2.63", state)   # ऋतो भारद्वाजस्य: जहर्थ
        state = apply_rule("7.2.35", state)
        # IT on iṭ: iṭ has T as halantyam-it
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        # 1.4.13 aṅga saṃjñā
        state = apply_rule("1.4.13", state)
        # dvitva BEFORE vuk: 6.4.88 requires abhyāsa present to detect liṭ context
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.45", state)   # आदेच उपदेशेऽशिति: ग्लै → ग्ला, धे → धा
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        # 7.4.60 halādiḥ śeṣaḥ — trim CVC abhyāsa to CV (e.g. paW → pa)
        state = apply_rule("7.4.60", state)
        state = apply_rule("7.4.62", state)   # कुहोश्चुः (जहार, जघ्रौ)
        state = apply_rule("6.1.73", state)   # छे च: abhyāsa च + छ् (चच्छाद)
        # 6.4.88 vuk (abhyāsa now present → liṭ context confirmed)
        state = apply_rule("6.4.88", state)
        # IT on vuk (u and k are it-marked)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        if lit_adesha == "Tal":
            state = _lit_thal_guna(state)   # चिचेतिथ
    else:
        # ── NO-iṭ path: dvitva FIRST, then 1.4.13, vuk ───────────────────────
        # ṇal and thal are pit through their sthānī (tip/sip/mip, 1.1.56), so
        # 1.2.5 असंयोगाल्लिट् कित् does not make them kit.
        if lit_adesha not in ("Ral", "Tal"):
            state = apply_rule("1.2.5", state)
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.45", state)   # आदेच उपदेशेऽशिति: ग्लै → ग्ला, धे → धा
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        # 7.4.60 halādiḥ śeṣaḥ — trim CVC abhyāsa to CV (e.g. paW → pa)
        state = apply_rule("7.4.60", state)
        state = apply_rule("7.4.62", state)   # कुहोश्चुः (जहार, जघ्रौ)
        state = apply_rule("6.1.73", state)   # छे च: abhyāsa च + छ् (चच्छाद)
        if lit_adesha == "Ral":
            # 7.2.115 अचो ञ्णिति: a vowel-final root before ṇal — नी → नै (निनाय);
            # not भू, whose vuk (6.4.88) makes it hal-final (बभूव)
            _d = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
            if _d is not None and "".join(v.slp1 for v in _d.varnas) != "BU":
                state = apply_rule("7.2.115", state)
            # liṭ strong: guṇa first (IK-upadha: cit→cet, kṛ ṛ→a+rapara_pending)
            state.meta["liT_strong_recipe"] = True
            state = P00_guna_7_3_84(state)
            state.meta.pop("liT_strong_recipe", None)
            # 1.1.51 uRaN rapara — resolves root ṛ→ar (kṛ → kar)
            state = apply_rule("1.1.51", state)
            # 7.2.116 ato upadhāyāḥ — vṛddhi of a-upadha (paṭh→pāṭh; kṛ now kar→kār)
            state = apply_rule("7.2.116", state)
        elif lit_adesha == "Tal":
            state = _lit_thal_guna(state)   # चकर्थ (kṛ: no iṭ, 7.2.13)
        # 1.4.13 aṅga saṃjñā
        state = apply_rule("1.4.13", state)
        # 6.4.88 vuk
        state = apply_rule("6.4.88", state)
        # IT on vuk (u and k are it-marked)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

    # ── 7.4.66 urat (abhyāsa ṛ→ā) — fires before hrasva so ā→a ────────────
    state = apply_rule("7.4.66", state)
    # In liṭ the abhyāsa ṛ-replacement carries no rapara (yaṅ context only)
    for _t in state.terms:
        if "abhyasa" in _t.tags:
            _t.meta.pop("urN_rapara_pending", None)
            _t.meta.pop("urN_rapara_after_index", None)

    # ── 7.4.59 hrasva (abhyāsa U→u, Ā→a) ────────────────────────────────────
    state = apply_rule("7.4.59", state)

    # ── 6.4.120 ata ekahalmadhye — weak liṭ: a→e for CVC roots (tan→ten, etc.) ─
    state = apply_rule("6.4.120", state)
    # 6.4.98 गमहनजनखनघसां लोपः क्ङित्यनङि — जग्मतुः, जघ्नुः (self-gates)
    state = apply_rule("6.4.98", state)

    # ── 7.4.73 bhavateraḥ (abhyāsa u→a) — only for bhū ─────────────────────────
    _dht = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    _dht_up = (_dht.meta.get("upadesha_slp1") or "").strip() if _dht else ""
    if _dht_up in {"BU", "BU~"}:
        state.meta["bhU_abhyasa_recipe"] = True
        state = apply_rule("7.4.73", state)

    # ── आदन्त: 7.1.34 आत औ णलः (ददौ), 6.4.64 आतो लोप इटि च (ददतुः, ददिथ, ददे)
    for sid in ("7.4.10", "7.4.11", "7.1.34", "6.4.64", "6.1.88"):
        state = apply_rule(sid, state)

    # ── ajādi dhātus: 7.4.70 अत आदेः, 7.4.71 नुट्, 6.4.78 इयङ्/उवङ्, then the
    #    abhyāsa + dhātu savarṇa merge (6.1.101): आट, आनर्द, इयेख, ईखतुः
    for sid in ("7.4.70", "7.4.71", "6.4.78"):
        state = apply_rule(sid, state)
    _ab = next((k for k, t in enumerate(state.terms[:-1]) if "abhyasa" in t.tags), None)
    if _ab is not None and state.terms[_ab].varnas and state.terms[_ab + 1].varnas \
            and state.terms[_ab].varnas[-1].slp1 in "aAiIuU" \
            and state.terms[_ab + 1].varnas[0].slp1 in "aAiIuU":
        state = apply_rule("6.1.101", state)          # आ+अट् → आट, इ+इख् → ईख्
    state = apply_rule("6.4.77", state)               # शिश्रिये; 6.4.82: निन्यिरे

    # ── 1.4.14 pada saṃjñā ───────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.77 iko yaṇ aci — IK-final root + vowel-initial suffix/iṭ ────────
    # (fires at term boundary before merge; resolves kṛ ṛ→r before atuH/uH/iṭ)
    state = apply_rule("6.4.87", state)   # हुश्नुवोः सार्वधातुके (apavāda of 6.4.77)
    state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)   # एचोऽयवायावः: निनै+अ → निनाय, निने+इथ → निनयिथ

    # ── TRIPĀḌĪ: 8.2.1 + 8.4.54 must fire pre-merge (abhyāsa term visible) ──
    state = apply_rule("8.2.1", state)    # opens tripadi_zone
    # 8.3.78 इणः षीध्वंलुङ्लिटां धोऽङ्गात् — dhve after an iṆ-final aṅga: चकृढ्वे
    state = apply_rule("8.3.78", state)
    state = apply_rule("8.4.54", state)   # carc on abhyāsa term

    # ── MERGE then full post-merge Tripāḍī spine ──────────────────────────────
    state = _merge_pada(state)
    state = execute_tripadi_phase(state)  # 8.2.1/8.4.54 skip (already done)

    return state


def _derive_lit_ad_gas(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* → *ghas* *liṭ* kartari (2.4.40): जघास, जक्षतुः, … per clip prakriyā.

    Uses *liṭ* parasmaipada ādeśas (3.4.82), *kit* (1.2.5), reduplication, *7.2.116*
    (ṇal cells), *6.4.98*/*6.4.100*, *7.4.60*/*7.4.62*/*7.4.59*, tripāḍī *8.3.60*/*8.4.55*.
    """
    lit_adesha = _LIT_PARASMAI_ADESHA[(purusha, vacana)]
    ral_path = lit_adesha == "Ral"
    needs_it = _lit_needs_it(purusha, vacana)
    kit_path = lit_adesha in {"atus", "aTus", "us", "va", "ma", "th", "a"}

    state.meta["lakara"] = "liT"
    state.meta["liT_lakara_recipe"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("2.4.40", state)
    state = run_it_prakarana(state)

    tin_std = _select_tin_adesha("liT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_std)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)
    state.meta["liT_82_adesha_form"] = lit_adesha
    state.meta["liT_82_recipe"] = True
    state = apply_rule("3.4.82", state)
    state = apply_rule("1.3.4", state)
    state = P00_hal_it_lopa(state)

    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)

    if purusha == 1 and vacana == 1:
        state.meta["Nal_uttama_recipe"] = True
        state = apply_rule("7.1.91", state)

    if kit_path and not ral_path:
        state = apply_rule("1.2.5", state)

    if needs_it:
        state = apply_rule("7.2.13", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("6.4.98", state)
    else:
        if kit_path and lit_adesha in {"atus", "aTus"}:
            state = apply_rule("6.4.100", state)
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        if ral_path:
            state = apply_rule("1.4.13", state)
            state = apply_rule("7.2.116", state)
        else:
            state = apply_rule("1.4.13", state)
            state = apply_rule("6.4.98", state)

    for t in state.terms:
        if (
            "abhyasa" in t.tags
            and kit_path
            and not needs_it
            and lit_adesha in {"atus", "us", "aTus"}
        ):
            t.meta["7_4_60_first_hal_only"] = True
    state = apply_rule("7.4.60", state)
    state = apply_rule("7.4.62", state)
    state = apply_rule("6.1.73", state)

    if kit_path and lit_adesha in {"atus", "us", "aTus", "va", "ma"} and not needs_it:
        state = apply_rule("7.4.59", state)

    state = apply_rule("1.4.14", state)
    # Pre-merge: open Tripāḍī zone; 8.4.54 needs the abhyāsa term separate.
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.4.54", state)
    state = _merge_pada(state)
    # Post-merge: record pre-8.3.60 form for P034 arm, then full spine.
    flat_pre = state.flat_slp1()
    state = apply_rule("8.3.60", state)
    if flat_pre in ("jaGsatus", "jaGsus"):
        state = apply_rule("8.4.55", state)
    state = execute_tripadi_phase(state)  # 8.2.1/8.4.54/8.3.60/8.4.55 skip (done)
    return state


# ─────────────────────────────────────────────────────────────────────────────
# LUṬ (ANADYATANA BHAVIṢYAT / PERIPHRASTIC FUTURE) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

# 2.4.85 prathama ādeśas (SLP1) for luṭ
_LUT_PRATHAMA_ADESHA: dict[tuple, str] = {
    (3, 1): "qA",    # ḍā  (q=ḍit cuṭu + A)
    (3, 2): "rO",    # rau (r+O=au)
    (3, 3): "ras",   # ras (r+a+s)
}

_LUT_AD_PRATHAMA_ADESHA: dict[tuple, str] = {
    (3, 1): "qA",
    (3, 2): "ras",   # clip: तास्+रस् → ता+रः (not rau)
    (3, 3): "ras",
}


def _lut_prathama_adesha(state: State, purusha: int, vacana: int) -> str | None:
    table = _LUT_AD_PRATHAMA_ADESHA if state.meta.get("_luT_ad_spine") else _LUT_PRATHAMA_ADESHA
    return table.get((purusha, vacana))


def _derive_luT(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a luṭ (periphrastic future / anadyatana bhaviṣyat) form starting
    from the post-1.3.78 state.  Implements the full 9-cell bhū luṭ parasmaipada
    pipeline via the sūtra-driven approach.

    Structural order:
      1. 3.3.3 + 3.3.15 → luṭ lakāra attachment
      2. 3.1.33 → tāsi vikaraṇa insertion (tAs before luṭ placeholder)
      3. 3.4.77 + 3.4.78 → tiṅ ādeśa; 1.4.99; 1.3.4/1.3.3/1.3.9 → IT on tiṅ
      4. Cell-specific: 2.4.85 (prathama), 7.2.35 (iṭ on tāsi), s-lopa rules
      5. 1.4.13, 7.3.84 (guṇa), optional s-lopa (after guṇa), 1.4.14, 6.1.78
      6. _pada_merge + tripāḍī (8.2.1 / 8.2.66 / 8.3.15)
    """
    # ── Stage: 3.3.3 bhavishyat adhikāra ───────────────────────────────────
    state = apply_rule("3.3.3", state)

    # ── Stage: 3.3.15 — attach luṭ lakāra placeholder ──────────────────────
    state.meta["luT_recipe"] = True
    state = apply_rule("3.3.15", state)
    state.meta.pop("luT_recipe", None)
    # IT on luṭ upadeśa (vacuous — luṭ has no anunāsika or live hal-it)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.1.33 — insert tāsi vikaraṇa before luṭ placeholder ────────
    state.meta["tasi_luT_recipe"] = True
    state = apply_rule("3.1.33", state)
    state.meta.pop("tasi_luT_recipe", None)
    if state.meta.get("_luT_apply_114"):
        state.meta["lakara"] = "luT"
        state = apply_rule("3.4.114", state)

    # ── Stage: 3.4.77 lasya + 3.4.78 tiṅ ādeśa ─────────────────────────────
    tin_adesha_std = _select_tin_adesha("luT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha_std)
    # IT on tiṅ ādeśa: 1.3.4 (tusma protect) + 1.3.3 (halantyam) + 1.3.9 (lopa)
    #   tip→ti, sip→si, mip→mi; tas/Tas/vas/mas retain (tusma-s protected); Ta/jhi vacuous
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── Cell-specific pipeline ───────────────────────────────────────────────
    is_prathama = (purusha == 3)

    if purusha == 3 and vacana == 1:
        # 3sg: 2.4.85(ti→qA), set dit_pratyaya, 7.2.35(iṭ before tāsi while qA has q=val),
        #      1.3.7(q→it), 1.3.9(lope q→A), 1.4.13, 7.3.84, 6.4.143(tAs→t), 1.4.14, 6.1.78
        adesha = _lut_prathama_adesha(state, 3, 1)
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        # Mark the qA term as ḍit so 6.4.143 can find it
        if state.terms:
            state.terms[-1].meta["dit_pratyaya"] = True
        # 7.2.35: insert iṭ into tāsi before qA (q is val → fires)
        state = _it_agama(state)
        # 1.3.7: q(ḍ, cuṭu)→it on qA term; 1.3.9: lope q → A
        state = apply_rule("1.3.7", state)
        state = apply_rule("1.3.9", state)
        # 1.4.13 aṅga saṃjñā, 7.3.84 guṇa (BU→Bo)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = P00_guna_7_3_84(state)
        # 6.4.143: tāsi (i+t+A+s) → (i+t) before A (ḍit) — ṭi-lopa
        state = apply_rule("6.4.143", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 2:
        # 3du: 7.2.35(iṭ into tāsi while tas has t=val), 1.2.4,
        #      2.4.85(tas→rO), 1.4.13, 7.3.84, 7.4.51(tāsi→tA before r), 1.4.14, 6.1.78
        state = _it_agama(state)
        state = apply_rule("1.2.4", state)
        adesha = _lut_prathama_adesha(state, 3, 2)
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = P00_guna_7_3_84(state)
        # 7.4.51: drop s from tāsi before r (rO starts with r)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 3:
        # 3pl: 7.2.35(iṭ into tāsi while jhi has j=val), 1.2.4,
        #      2.4.85(jhi→ras), 1.4.13, 7.3.84, 7.4.51(tāsi→tA before r), 1.4.14, 6.1.78
        state = _it_agama(state)
        state = apply_rule("1.2.4", state)
        adesha = _lut_prathama_adesha(state, 3, 3)
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = P00_guna_7_3_84(state)
        # 7.4.51: drop s from tāsi before r (ras starts with r)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 1:
        # 2sg: 7.2.35(iṭ into tāsi while si has s=val), 1.4.13, 7.3.84,
        #      7.4.50(tāsi→tA before si), 1.4.14, 6.1.78
        state = _it_agama(state)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = P00_guna_7_3_84(state)
        # 7.4.50: drop s from tāsi before si (si starts with s)
        state.meta["tasa_lopa_recipe"] = True
        state = apply_rule("7.4.50", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    else:
        # Non-prathama, non-2sg cells: 2du (Tas), 2pl (Ta), 1sg (mi), 1du (vas), 1pl (mas)
        # 7.2.35: insert iṭ into tāsi (tāsi starts with t=val → always fires)
        # No 2.4.85; no s-lopa rule for these cells.
        state = _it_agama(state)
        # 1.2.4 for cells whose tiṅ is sārvadhatuka apit (most of them)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = P00_guna_7_3_84(state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    # 6.4.19 च्छ्वोः शूडनुनासिके च: प्रच्छ्-specific तुक्+छ् → श् before the
    # ārdhadhātuka तास् (प्रष्टा). Vacuous for every other root.
    state = apply_rule("6.4.19", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    state = _merge_pada(state)
    if state.meta.get("_luT_ad_spine"):
        state.meta.pop("_luT_ad_spine", None)
        state.meta.pop("_luT_skip_guna", None)
        state.meta.pop("luT_ad_ekac_spine", None)
        state = apply_rule("8.2.1", state)
        state = P00_tripadi_8_4_55_visarga(state)
        state = apply_rule("8.4.68", state)
    else:
        state = P00_tripadi_rutva_visarga(state)

    return state


def _derive_luT_ad(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* *luṭ* kartari (अत्ता …): *tāsi* + **3.4.114**, **7.2.10** (no iṭ), no *guṇa*,
    **6.4.143** (3sg), tripāḍī **8.4.55** (खरि च).
    """
    state.meta["ekac_dhatu"] = True
    state.meta["luT_ad_ekac_spine"] = True
    state.meta["_luT_skip_guna"] = True
    state.meta["_luT_ad_spine"] = True
    state.meta["_luT_apply_114"] = True
    state = apply_rule("7.2.10", state)
    state = _derive_luT(state, pada_key, purusha, vacana)
    state.meta.pop("_luT_apply_114", None)
    return state


# ─────────────────────────────────────────────────────────────────────────────
# LAṄ (ANADHYATANA BHŪTA / IMPERFECT) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def _derive_laG(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a laṅ (imperfect / anadhyatana past) form starting from the
    post-1.3.78 state.  Implements the full 9-cell bhū laṅ parasmaipada pipeline.

    Key differences from laṭ:
      • 3.2.111 (not 3.2.123) attaches the lakāra and tags dhātu with aT_agama_context
      • 3.4.100 itaś ca: drops 'i' from tip→t, sip→s, jhi→jh
      • 3.4.101: tas→tām, Tas→tam, Ta→ta, mi(from mip)→am
      • 3.4.99:  vas→v, mas→m (ṅit s-lopa)
      • 7.1.3:   jh→ant  (after 3.4.100 has dropped 'i' from jhi)
      • 6.4.71:  aṭ augment prepended to dhātu (via aT_agama_context tag)
      • Tripāḍī: 8.2.39 jhal→jaś (t→d) + 8.4.56 vā avasāne (d→t back)
                 8.2.23 saṃyogāntasya lopaḥ (3pl: drop final t of ant→an)
    """
    state.meta["lakara"] = "laG"

    # ── Stage: 3.2.111 laṅ attachment ───────────────────────────────────────
    # 3.2.111 act attaches laG placeholder AND tags dhātu with aT_agama_context.
    state = apply_rule("3.2.111", state)
    # Trace: 1.3.3 (halantyam G → it, pre-stripped) + 1.3.9 (G lopa, vacuous)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa ───────────────────────────────────
    tin_adesha = _select_tin_adesha("laG", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = _bhave_atmanepada_tin_after_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ─────────────────────────────────
    state = apply_rule("3.4.113", state)

    # 1.2.4 apit → kṅit: fires on tiṅ ādeśa (jhi, tas…) BEFORE vikaraṇa,
    # matching laṭ pipeline ordering and preventing mis-tagging of śap.
    state = apply_rule("1.2.4", state)

    # ── Stage: vikaraṇa (śap for bhvādi gaṇa) ───────────────────────────────
    gana: int = state.terms[0].meta.get("gana", 1)
    state = _apply_vikarana(state, gana)

    # ── Stage: laṅ-specific tiṅ substitutions ───────────────────────────────
    # 3.4.101 (apavāda) BEFORE 3.4.100: tas→tām, Tas→tam, Ta→ta, mi→am
    state = apply_rule("3.4.101", state)
    # 3.4.100: ti→t, si→s, jhi→jh (final 'i' dropped in laṅ/luṅ/lṛṅ)
    state = apply_rule("3.4.100", state)
    # 3.4.99: vas→v, mas→m (ṅit final 's' dropped)
    state = apply_rule("3.4.99", state)

    # 7.1.3: jh (2 varnas after 3.4.100) → ant  (vacuous for non-3pl cells)
    state = P00_jha_adesha(state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    # 6.4.71 aṭ + it-lopa (aṭ T is conceptual)
    state = P00_at_agama_it_lopa(state)

    state = apply_rule("1.1.5", state)
    # 7.3.101: 'a' of śap → 'ā' before yañ-initial tiṅ ādeśa (v of 'v', m of 'm')
    state = apply_rule("7.3.101", state)
    # 7.3.93 ब्रुव ईट् must precede 7.3.84's guṇa (ब्रू-specific ī āgama on
    # tip/sip/mip; see _derive_laT_adadi_kartari for the same ordering).
    # Vacuous for every other root — cond() requires dhātu surface == "brU".
    state = apply_rule("7.3.93", state)
    # 7.3.84: guṇa (IK-vowel of dhātu; BU(Ū) → Bo)
    state = P00_guna_7_3_84(state)
    state = apply_rule("6.4.110", state)   # अकुरुताम्, अकुर्वन्
    state = apply_rule("6.4.108", state)
    # 6.1.68 हल्ङ्याब्भ्यो…सुतिस्यपृक्तं हल्: the apṛkta t/s after an aṅga that is
    # hal-final once guṇa + raparatva have applied (अजागर् + स् → अजागः)
    state = apply_rule("6.1.68", state)

    # ── Stage: pada + sandhi ─────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — tanādi gana 8: vikaraṇa-u + AC-initial tiṅ (tan+u+ant → tanvant)
    if gana in _U_VIKARANA_GANAS:
        state = apply_rule("6.4.87", state)   # हुश्नुवोः सार्वधातुके (apavāda of 6.4.77)
        state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)
    # 6.1.97: a+a → a (3pl: śap-a + ant-a; 1sg: śap-a + am-a)
    state = apply_rule("6.1.97", state)
    # ātmanepada: ṅit आताम्/आथाम् after a (7.2.81 → 6.1.66 → 6.1.87: ऐधेताम्),
    # and a + इ of iṭ → ए (6.1.87: ऐधे). All self-gate; parasmaipada untouched.
    state = P00_ngit_At_iy_guna(state)
    # after the ātmanepada dual trio, so ā-initial endings reach 7.2.81 first
    state = apply_rule("6.1.101", state)   # अकः सवर्णे दीर्घः: क्रीणा + अम् → अक्रीणाम्

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    state = _merge_pada(state)
    state = execute_tripadi_phase(state)  # 8.2.39/8.4.56/8.2.66/8.3.15/8.2.23/8.4.68 fire naturally

    return state


# ─────────────────────────────────────────────────────────────────────────────
# LIṄ (ĀŚĪR / BENEDICTIVE) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────
# LUṄ (ADYATANA BHŪTA / AORIST) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────


def _derive_luG_ad(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* → *ghas* *luṅ* kartari (2.4.37): अघसत्, अघसताम्, … per clip prakriyā.

    Differs from *bhū* *luṅ*: tiṅ before *ghas*; *cli*→*aṅ* (3.1.55), not *sic*/*2.4.77*;
    no *vuk*/*6.1.66*; *6.4.71* *aṭ* only.
    """
    state.meta["lakara"] = "luG"
    state.meta["luG_recipe"] = True
    state = apply_rule("3.2.110", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("luG", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("2.4.37", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state.meta["cli_luG_recipe"] = True
    state = apply_rule("3.1.43", state)
    state = apply_rule("3.1.55", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state = apply_rule("3.4.114", state)
    state = apply_rule("3.4.101", state)
    state = apply_rule("3.4.100", state)
    if purusha == 3 and vacana == 3:
        state = P00_jha_adesha(state)
    state = apply_rule("3.4.99", state)
    state = apply_rule("6.1.66", state)
    state = apply_rule("1.2.4", state)
    state = apply_rule("1.4.13", state)
    state = P00_at_agama_it_lopa(state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("6.1.97", state)

    state = _merge_pada(state)
    state = execute_tripadi_phase(state)  # rules fire based on phonological state
    return state


def _can_anga(state: State, pada_key: str) -> State:
    """caṅ-luṅ aṅga: 6.4.51 णेरनिटि (चोरि → चोर्), 7.4.1 णौ चङ्युपधाया ह्रस्वः (चुर्),
    6.1.11 चङि (चुचुर्), the abhyāsa (7.4.60/62/59/66, 8.4.54), 7.4.93 सन्वद्भाव →
    7.4.79 सन्यतः, 7.4.94 दीर्घो लघोः (चूचुर्). Ātmanepada: आतो ङितः (अचूचुरेताम्)."""
    for sid in ("6.4.51", "7.4.1", "6.1.11", "7.4.60", "7.4.62", "7.4.66", "7.4.59",
                "7.4.93", "7.4.79", "7.4.94", "8.4.54", "6.1.73", "6.4.77"):
        state = apply_rule(sid, state)
    for t in state.terms:                     # 7.4.66's rapara belongs to yaṅ only
        if "abhyasa" in t.tags:
            t.meta.pop("urN_rapara_pending", None)
            t.meta.pop("urN_rapara_after_index", None)
    if pada_key == "atmane":
        state = apply_rule("6.1.97", state)
        state = P00_ngit_At_iy_guna(state)
    return state


def _derive_luG(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a luṅ (aorist / adyatana bhūta) form from the post-1.3.78 state.
    Full 9-cell bhū luṅ parasmaipada pipeline.

    Key features:
      • 3.2.110 attaches luG (+ aT_agama_context on dhātu)
      • 3.1.43 cli inserted; 3.1.44 cli→sic
      • 2.4.77 (gāti-sthā-ghu-pā-bhū) luk of sic in parasmaipada → sic deleted
      • 3.4.101 tiṅ substitutions (tas→tām etc.) AFTER sic deletion
      • 3.4.100 i-lopa (ti→t, si→s, jhi→jh)
      • 7.1.3 jh→ant (3pl only)
      • 3.4.99 s-lopa (vas→va, mas→ma)
      • 6.4.71 aṭ augment (6.4.71)
      • 6.4.88 vuk augment (bhū only) → [v,u~,k] → after it-lopa → [v]
      • 6.1.66 v (vuk) drops before HAL-initial tiṅ; stays before AC-initial
      • NO guṇa (vuk intervenes; 7.3.84 not called)
      • Tripāḍī: 8.2.39/8.4.56, 8.2.66/8.3.15, 8.2.23

    Expected forms (bhū):
      3sg → अभूत्  3du → अभूताम्  3pl → अभूवन्
      2sg → अभूः   2du → अभूतम्   2pl → अभूत
      1sg → अभूवम् 1du → अभूव    1pl → अभूम
    """
    state.meta["lakara"] = "luG"

    # ── Stage: 3.2.110 luṅ attachment ───────────────────────────────────────
    state.meta["luG_recipe"] = True
    state = apply_rule("3.2.110", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)
    state = apply_rule("2.4.43", state)  # हन् → वध (न्यवधीत् / अवधीत्)

    # ── Stage: cli/sic chain (before lakāra substitution: 3.1.43 needs luG) ──
    state.meta["cli_luG_recipe"] = True
    state = apply_rule("3.1.43", state)   # inserts cli before luG placeholder
    state = apply_rule("3.1.48", state)   # णिश्रिद्रुस्रुभ्यः कर्तरि चङ् (अचूचुरत्)
    # 3.1.55 cli→aṅ for puṣyādi/dyutādi (parasmaipada only); structural cond (dyut+cli)
    if pada_key == "parasmai":
        state = apply_rule("3.1.55", state)
    state = apply_rule("3.1.44", state)   # cli → sic; vacuous if 3.1.55 already fired
    # 3.1.45 शल इगुपधादनिटः क्सः (apavāda of 3.1.44 for शल्-अंत इक्-उपधा अनिट्
    # roots): marks the recipe so 7.2.3/7.3.96 skip वृद्धि/ईट् below (अशिक्षत्,
    # not अशैक्षीत्). Vacuous for every other root shape.
    state = apply_rule("3.1.45", state)

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa ────────────────────────────────────
    tin_adesha = _select_tin_adesha("luG", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)  # drops p-it of tiṅ; c-it of sic
    state = apply_rule("1.4.100", state)   # taṅ-ādeśa → ātmanepada (gates 7.2.1/7.2.3, 1.2.11)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── sic-luk (2.4.77 गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु) vs sic kept ──────
    # Decided by 2.4.77's own condition (root identity + parasmaipada), not by
    # seṭ/aniṭ — that is 7.2.10's question, asked inside _it_agama below.
    from sutras.adhyaya_2.pada_4.sutra_2_4_77 import cond as _sic_luk_cond
    _is_anit = _sic_luk_cond(state)       # name kept: this branch = the sic-luk spine
    _caN = any((t.meta.get("upadesha_slp1") or "").strip() == "caG" for t in state.terms)

    if _caN:
        pass                              # caṅ is aniṭ and ṅit: no iṭ, guṇa or sic-vṛddhi
    elif _is_anit:
        # ── aniṭ path: 2.4.77 luk of sic (gāti-sthā-ghu-pā-bhū) ─────────────
        state = apply_rule("2.4.77", state)
    else:
        # ── seṭ path: 7.2.35 iṭ insertion before sic ─────────────────────────
        for _t in state.terms:
            if (_t.meta.get("upadesha_slp1") or "").strip() == "sic":
                _t.tags.add("ardhadhatuka")
        state.meta["7_2_35_allow_sic"]      = True
        state.meta["luN_sic_ardhadhatuka"]  = True
        state = _it_agama(state)
        # No IT lopa needed: P00 already dropped sic's c-IT; iṭ 'i' has no T marker
        state.meta.pop("7_2_35_allow_sic", None)
        state.meta.pop("luN_sic_ardhadhatuka", None)
        # 7.3.86 laghūpadha guṇa before sic+iṭ (structural: dyut+i → dyot+i)
        state = P00_guna_7_3_86(state)
        if pada_key == "atmane":
            # jhal-ādi sic is kit after ik-near hal / ṛ (1.2.11/12: अतुत्त, अकृत);
            # otherwise guṇa (अमोदिष्ट, अभविष्ट). No sic-vṛddhi: 7.2.1 is parasmaipada.
            state = apply_rule("1.2.11", state)
            state = apply_rule("1.2.12", state)
            state = P00_guna_rapara_ayadi(state)
        # वध (2.4.43) is a-anta: 6.4.48 before sici vṛddhi / 7.2.7.
        state = apply_rule("6.4.48", state)
        state = apply_rule("1.1.56", state)
        # sici vṛddhi (parasmaipada): 7.2.1 for a vowel-final aṅga (नी → नै);
        # 7.2.3 for a hal-final one, only when iṭ was blocked (7.2.4 नेटि):
        # पच् → पाच् (अपाक्षीत्). Both self-gate on sic + parasmaipada.
        state = apply_rule("7.2.1", state)
        state = apply_rule("1.1.51", state)   # ṛ-vṛddhi is ār (अहार्षीत्)
        if "7.2.35" in state.blocked_sutras:
            state = apply_rule("7.2.3", state)
        if pada_key != "atmane":
            # 7.2.4 नेटि kept vṛddhi off a seṭ hal-final aṅga: plain guṇa (अमोटीत्, अमर्दीत्)
            state = P00_guna_rapara_ayadi(state)

    # ── Stage: 1.2.4 apit sārvadhatuka → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: tiṅ substitutions ─────────────────────────────────────────────
    state = apply_rule("3.4.101", state)   # tas→tām, Tas→tam, Ta→ta, mi→am

    if not _is_anit and not _caN and (purusha, vacana) == (3, 3):
        # seṭ 3pl: jher jus (3.4.108) → [u, s] instead of 7.1.3 jh→anti
        state = apply_rule("3.4.108", state)

    state = apply_rule("3.4.100", state)   # ti→t, si→s, jhi→jh

    _aG = any((t.meta.get("upadesha_slp1") or "").strip() in ("aG", "caG") for t in state.terms)
    if _is_anit or pada_key == "atmane" or _aG or state.meta.get("_3_1_45_ksa_recipe"):
        state = P00_jha_adesha(state)     # jh→ant; ātmane after sic: 7.1.5 → at (ऐधिषत); क्स is अनिट् too (अशिक्षन्)

    if _caN:
        state = _can_anga(state, pada_key)
    state = apply_rule("3.4.99", state)    # vas→va, mas→ma
    if _aG or state.meta.get("_3_1_45_ksa_recipe"):
        state = apply_rule("7.3.101", state)  # अतो दीर्घो यञि: अपुषाव, अपुषाम; क्स: अशिक्षाव, अशिक्षाम
    if _aG:
        state = apply_rule("6.1.97", state)   # अतो गुणे: aṅ-a + an/am → अपुषन्, अपुषम्

    # ── seṭ: for tip/sip-derived cells, sic-s + iṭ-i → ī via 7.2.35 ───────────
    # Discriminate by tiṅ upadesha (Art.2§2c: upadesha identity is allowed).
    # After 3.4.100 drops i from tip/sip, upadesha_slp1 remains "tip"/"sip".
    _tin_t = next(
        (t for t in state.terms if t.kind == "pratyaya" and "tin_adesha_3_4_78" in t.tags),
        None,
    )
    _tin_up = (_tin_t.meta.get("upadesha_slp1") or "").strip() if _tin_t else ""
    if not _is_anit and not _caN and _tin_up in {"tip", "sip"}:
        for _t in state.terms:
            if (_t.meta.get("upadesha_slp1") or "").strip() == "sic":
                _t.tags.add("seT_sic_it_lopa_context")
                break
        state = _it_agama(state)

    # aniṭ sic before an apṛkta t/s: 7.3.96 अस्तिसिचोऽपृक्ते (īṭ) — अनैषीत्, अपाक्षीः.
    # (The seṭ path above reaches ī through iṭ + 8.2.28.)
    if not _is_anit and not _caN and "7.2.35" in state.blocked_sutras:
        state = apply_rule("7.3.96", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # 6.4.71 aṭ augment; skip it-lopa for seṭ to avoid re-processing sic 's'
    state = P00_at_or_At_agama(state)     # ajādi: āṭ + vṛddhi (ऐधिष्ट)
    if _is_anit:
        state = P00_hal_it_lopa(state)

    if _is_anit:
        # 6.4.88 vuk augment (bhuvo vug-luṅ-liṭoḥ) — aniṭ/bhū only
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

        # 6.1.66 v of vuk drops before HAL; stays before AC
        state = apply_rule("6.1.66", state)

    # 6.1.77 iko yaṇ aci — IK→yaṇ before AC (fires for upasarga+aṭ junctions,
    # e.g. vi+a → vy+a in vyadyutat). Must run AFTER vuk so that ū of bhū is
    # separated from anti by vuk-v (preventing spurious ū→v change in abhūvant).
    # 6.1.101 (अकः सवर्णे दीर्घः) is the apavāda: आङ्+अट् → आ (उपागमत्, not उपआअगमत्).
    state = apply_rule("6.4.87", state)   # हुश्नुवोः सार्वधातुके (apavāda of 6.4.77)
    for _ in range(4):
        before = state.flat_slp1()
        state = apply_rule("6.1.101", state)
        if state.flat_slp1() == before:
            break
    state = apply_rule("6.1.77", state)
    # vṛddhi vowel + iṭ: 6.1.78 एचोऽयवायावः (अलौ + इ → अलाव् + इ: अलावीत्)
    state = apply_rule("6.1.78", state)
    # 6.1.97 अतो गुणे: क्स (3.1.45) is the first सिच्-family recipe whose own
    # vikaraṇa ends in अ, so 1sg मि→अम् (3.4.101) collides with it (अशिक्षअम्
    # → अशिक्षम्). Vacuous for सिच् itself (no vowel to collide).
    state = apply_rule("6.1.97", state)

    state = apply_rule("1.4.14", state)

    # 6.4.19 च्छ्वोः शूडनुनासिके च: प्रच्छ्-specific तुक्+छ् → श् before the
    # ārdhadhātuka सिच् (अप्राक्षीत्). Vacuous for every other root.
    state = apply_rule("6.4.19", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    state = _merge_pada(state)
    # 8.3.59/8.4.41 fire based on phonological state; no coordinate guard needed.
    state = execute_tripadi_phase(state)

    return state


# ─────────────────────────────────────────────────────────────────────────────

def _derive_ashir_liG(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive an āśīr-liṅ (benedictive) form from the post-1.3.78 state.
    Full 9-cell bhū āśīr-liṅ parasmaipada pipeline.

    Key differences from vidhi-liṅ:
      NO śap; 3.4.104 yāsuṭ is KIT → blocks guṇa; 3.4.107 suṭ before t/T tiṅ;
      8.2.29 drops yāsuṭ-s and conditional suṭ-s; 6.1.66 drops 2sg sip-s.
    """
    state.meta["lakara"]    = "AsIrliG"
    state.meta["ashir_liG"] = True

    state = apply_rule("3.3.173", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.116", state)

    state = apply_rule("3.4.101", state)
    state = apply_rule("3.4.108", state)
    state = apply_rule("3.4.100", state)
    state = apply_rule("3.4.99",  state)

    state.meta["ashir_yasut_recipe"] = True
    state = apply_rule("3.4.104", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state.meta["suw_recipe"] = True
    state = apply_rule("3.4.107", state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)
    state = apply_rule("6.4.51", state)    # णेरनिटि before aniṭ yāsuṭ: छोट्यात्, चोर्यात्
    state = apply_rule("6.1.45", state)    # ग्लायात्
    state.meta["ashir_7_4_25_recipe"] = True
    state = apply_rule("7.4.25", state)    # ज्रीयात्, चीयात्
    state = apply_rule("7.4.29", state)    # स्मर्यात्
    state = apply_rule("7.4.28", state)    # रिङ् … लिङ्क्षु: घ्रियात्, क्रियात्
    state = apply_rule("1.4.14", state)

    state = apply_rule("6.1.66", state)

    state = apply_rule("8.2.1", state)     # पूर्वत्रासिद्धम्: 8.2.29 is tripādī
    state.meta["ashir_8_2_29_recipe"] = True
    state = apply_rule("8.2.29", state)
    state.meta.pop("ashir_8_2_29_recipe", None)

    state = _merge_pada(state)
    state = execute_tripadi_phase(state)

    return state


# ─────────────────────────────────────────────────────────────────────────────
# LIṄ (VIDHI / OPTATIVE) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def _derive_liG(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a vidhi-liṅ (optative) form starting from the post-1.3.78 state.
    Implements the full 9-cell bhū vidhi-liṅ parasmaipada pipeline.

    Sūtra order:
      3.3.161  vidhiliṅoḥ      — attach liG lakāra
      1.3.2/3/9               — it-lopa on liG upadeśa
      3.4.77 + 3.4.78         — tiṅ ādeśa (laT ādeśas: tip/tas/jhi/…)
      1.4.99                  — parasmaipada saṃjñā
      1.3.4/3/9               — it-lopa on tiṅ
      3.4.113                 — tiṅ is sārvadhatuka
      1.2.4                   — apit sārvadhatuka → kṅit
      3.1.68 (+ chain)        — śap vikaraṇa
      3.4.101                 — tas→tām, Tas→tam, Ta→ta, mi→am  (apavāda)
      3.4.108                 — jhi → jus → [u,s]  (j cuṭu-it pre-dropped)
      3.4.100                 — ti→t, si→s  (i-lopa)
      3.4.99                  — vas→va, mas→ma  (s-lopa)
      3.4.103                 — yāsuṭ [y,A,s] inserted before tiṅ ādeśa
      7.2.79                  — drop 's' of yāsuṭ: [y,A,s] → [y,A]
      7.2.80                  — [y,A] → [i,y] when preceded by 'a'
      6.1.66                  — 'y' of [i,y] drops before HAL-initial tiṅ
      1.4.13                  — aṅga saṃjñā
      6.1.87                  — ādguṇaḥ: a + i → e  (śap-a + yāsuṭ-i)
      7.3.84                  — guṇa (BU → Bo)
      1.4.14                  — pada saṃjñā
      6.1.78                  — eco'yavāyāvaḥ (o + e → av + e)
      __MERGE__               — structural pada merge
      8.2.1                   — pūrvatrāsiddham
      8.2.66                  — sasajuṣo ruḥ (s → r for 2sg/3pl visarga)
      8.3.15                  — ru → ḥ
    """
    state.meta["lakara"] = "liG"

    # ── Stage: 3.3.161 vidhiliṅ attachment ──────────────────────────────────
    state.meta["liG_vidhi_recipe"] = True
    state = apply_rule("3.3.161", state)

    # IT on liG upadeśa (G is halantyam-it; anunaasika vacuous)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 lasya + 3.4.78 tiṅ ādeśa (standard laT set) ──────────
    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = _bhave_atmanepada_tin_after_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ─────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 1.2.4 apit → kṅit ────────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: vikaraṇa (śap for bhvādi) ────────────────────────────────────
    gana: int = state.terms[0].meta.get("gana", 1)
    # For tanādi gana 8: block early guṇa of vikaraṇa u until yāsuṭ (ṅit) arrives.
    # 3.3.161's act pops liG_vidhi_recipe, so we use a persistent guard flag.
    if gana in _U_VIKARANA_GANAS or gana == 9:
        state.meta["liG_yasut_expected"] = True
    state = _apply_vikarana(state, gana)

    # ── Stage: liṅ-specific tiṅ substitutions ───────────────────────────────
    # 3.4.101 (apavāda) BEFORE 3.4.108/3.4.100: tas→tām, Tas→tam, Ta→ta, mi→am
    state = apply_rule("3.4.101", state)
    # ātmanepada liṅ: 3.4.105 झस्य रन् (एधेरन्), 3.4.106 इटोऽत् (एधेय) — both
    # self-gate on their ādeśa and a liṅ sthānī; parasmaipada untouched.
    state = apply_rule("3.4.105", state)
    state = apply_rule("3.4.106", state)
    # 3.4.108: jhi → jus → [u,s]  (only fires for 3pl)
    state = apply_rule("3.4.108", state)
    # 3.4.100: ti→t, si→s  (i-lopa; skips [u,s] from jus, tām, am, etc.)
    state = apply_rule("3.4.100", state)
    # 3.4.99: vas→va, mas→ma  (s-lopa for uttama 1du/1pl)
    state = apply_rule("3.4.99", state)

    if pada_key == "atmane":
        # ── 3.4.102 लिङः सीयुट् (ātmanepada): सीय् before the tiṅ, 7.2.79 drops its s,
        #    6.1.66 its y before a hal — एधेत, द्विषीत, सुन्वीत, क्रीणीत
        state.meta["vidhi_liG"] = True
        state.meta["sIyuw_recipe"] = True
        state.meta["karmani_liG_recipe"] = True      # = "sīyuṭ before the tiṅ ādeśa"
        state = apply_rule("3.4.102", state)
        state.meta.pop("liG_yasut_expected", None)
        state = apply_rule("7.2.79", state)
        state = apply_rule("6.1.66", state)
    else:
        # ── Stage: 3.4.103 yāsuṭ insertion ─────────────────────────────────────
        state.meta["yasut_recipe"] = True
        state = apply_rule("3.4.103", state)
        # yāsuṭ is now present with kngiti tag — lift the pre-block flag
        state.meta.pop("liG_yasut_expected", None)
        # 6.4.111 श्नसोरल्लोपः — the a of अस् drops before the ṅit yāsuṭ (स्यात्, स्याम्); scoped to the root
        # अस् in its own cond(), a no-op for every other root on this spine.
        state = apply_rule("6.4.111", state)

        # ── Stage: yāsuṭ processing ──────────────────────────────────────────────
        # 7.2.79: [y,A,s] → [y,A]  (drop final 's' of yāsuṭ)
        state = apply_rule("7.2.79", state)
        # 7.2.80: [y,A] → [i,y]  (when preceded by 'a')
        state = apply_rule("7.2.80", state)
        # 6.1.66: 'y' of [i,y] drops before HAL-initial tiṅ (t,s,m,v,…)
        state = apply_rule("6.1.66", state)

    if gana == 9:
        # the ṅit yāsuṭ / sīyuṭ is now next to श्ना: 6.4.113 ई हल्यघोः (क्रीणीयात्),
        # 6.4.112 श्नाभ्यस्तयोरातः before a vowel (क्रीणीत)
        state = apply_rule("6.4.113", state)
        state = apply_rule("6.4.112", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    # 6.1.96 usy apadāntāt — tanādi gana 8: yā + us → y + us (drop ā before 3pl us)
    state = apply_rule("6.1.96", state)   # उस्यपदान्तात्: या+उस् → य्+उस् (कुर्युः, क्रीणीयुः)
    # 6.1.87: a + i → e  (śap-a + yāsuṭ-i remnant)
    state = apply_rule("6.1.87", state)
    state = apply_rule("6.1.101", state)   # अकः सवर्णे दीर्घः: या + अम् → याम्
    # 7.3.84: guṇa (IK-vowel of dhātu → guṇa; tanādi vikaraṇa blocked by yāsuṭ kṅit)
    state = P00_guna_7_3_84(state)
    if gana in _U_VIKARANA_GANAS:
        state = apply_rule("6.4.110", state)   # अत उत् सार्वधातुके: कर् → कुर् (ṅit yāsuṭ)
        state = apply_rule("6.4.109", state)   # ये च: कुरु+यात् → कुर्यात्

    # ── Stage: pada + sandhi ────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — tanādi gana 8: vikaraṇa-u + AC-initial tiṅ
    state = apply_rule("6.4.87", state)   # हुश्नुवोः सार्वधातुके (apavāda of 6.4.77)
    state = apply_rule("6.1.77", state)    # सुनु+ईत → सुन्वीत; तनु+यात् untouched
    state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)

    return state


def _derive_liG_ad(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* *liṅ* kartari (अद्यात् … अद्याम): *śap* + **2.4.72** *luk*, *yāsuṭ* + **7.2.79**,
    **3.4.107** *suṭ* (तिथोः), no *guṇa*; **8.2.39**/**8.4.56** (3sg), tripāḍī **8.2.66**/**8.3.15**.
    """
    state.meta["lakara"] = "liG"
    state.meta["_liG_ad_spine"] = True
    state.meta["_liG_skip_guna"] = True

    state.meta["liG_vidhi_recipe"] = True
    state = apply_rule("3.3.161", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = P00_sap_luk(state)

    state = apply_rule("3.4.101", state)
    state = apply_rule("3.4.108", state)
    state = apply_rule("3.4.100", state)
    state = apply_rule("3.4.99", state)

    state.meta["yasut_recipe"] = True
    state = apply_rule("3.4.103", state)

    state = apply_rule("7.2.79", state)

    state.meta["suw_recipe"] = True
    state = apply_rule("3.4.107", state)
    state.meta.pop("suw_recipe", None)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.101", state)
    state = apply_rule("8.2.1", state)     # पूर्वत्रासिद्धम्: 8.2.29 is tripādī
    state.meta["liG_ad_8_2_29_suw_recipe"] = True
    state = apply_rule("8.2.29", state)
    state.meta.pop("liG_ad_8_2_29_suw_recipe", None)

    state = _merge_pada(state)
    if purusha == 3 and vacana == 1:
        state = apply_rule("8.2.1", state)
        state = apply_rule("8.2.39", state)
        state = apply_rule("8.4.56", state)
        state = apply_rule("8.4.68", state)
    elif purusha == 3 and vacana == 3:
        state = apply_rule("8.2.1", state)
        state = apply_rule("6.1.96", state)
        state = apply_rule("8.2.66", state)
        state = apply_rule("8.3.15", state)
        state = apply_rule("8.4.68", state)
    elif purusha == 2 and vacana == 1:
        state = P00_tripadi_rutva_visarga(state)
        state = apply_rule("8.4.68", state)
    else:
        state = apply_rule("8.4.68", state)

    state.meta.pop("_liG_ad_spine", None)
    state.meta.pop("_liG_skip_guna", None)
    return state


# ─────────────────────────────────────────────────────────────────────────────
# LṚṬ (SĀMĀNYA BHAVIṢYAT / SIMPLE FUTURE) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def _derive_lRT(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a lṛṭ (simple future / sāmānya bhaviṣyat) form starting from the
    post-1.3.78 state.  Implements the full 9-cell bhū lṛṭ parasmaipada pipeline.

    Sūtra order:
      3.3.13  lṛṭ śeṣe ca         — attach lṛṭ lakāra
      1.3.2/3/9                   — it-lopa on lṛṭ upadeśa (anunaasika + halantyam)
      3.4.77 + 3.4.78             — tiṅ ādeśa selection
      1.4.99                      — parasmaipada saṃjñā
      1.3.4 / 1.3.3 / 1.3.9      — it-lopa on tiṅ ādeśa
      3.4.113                     — tiṅ is sārvadhatuka
      3.1.33                      — insert *sya* vikaraṇa (s+y+a) after dhātu
      3.4.114                     — *sya* is ārdhadhātuka (śeṣa)
      7.2.35                      — iṭ āgama before *sya* (val-initial ārdhadhātuka)
      1.3.3 / 1.3.9               — trace steps for iṭ it-lopa (vacuous)
      1.2.4                       — sārvadhatuka apit → kṅit (for tas, vas, mas etc.)
      7.1.3                       — jhi → anti (3pl only)
      1.4.13                      — aṅga saṃjñā
      1.1.5                       — kṅiti guard
      7.3.101                     — ato dīrgho yañi (uttama: a→ā before m/v)
      7.3.84                      — guṇa (IK → guṇa, e.g. BU → Bo)
      1.4.14                      — pada saṃjñā
      6.1.78                      — eco'yavāyāvaḥ (EC + AC split: o+i → av+i)
      6.1.97                      — ato guṇe (a+a → a, for 3pl anti)
      __MERGE__                   — structural pada merge
      8.2.1                       — pūrvatrāsiddham (tripāḍī gate)
      8.2.66                      — sasajuṣo ruḥ (pada-final s → ru)
      8.3.15                      — kharavaṣānayoḥ visarjanīyaḥ (ru → ḥ)
      8.3.59                      — ādeśapratyayayoḥ (s → ṣ after IK, e.g. in sya)
      8.4.68                      — a a iti (trace marker)
    """
    # ── Stage: 3.3.13 lṛṭ śeṣe ca ──────────────────────────────────────────
    state.meta["lakara"] = "lRT"
    state = apply_rule("3.3.3", state)
    state.meta["lfT_recipe"] = True
    state = apply_rule("3.3.13", state)
    state.meta.pop("lfT_recipe", None)

    # IT on lṛṭ upadeśa (anunāsika R → it via 1.3.2; halantyam T pre-stripped).
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 lasya + 3.4.78 tiṅ ādeśa ─────────────────────────────
    tin_adesha = _select_tin_adesha("lRT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)

    # IT on tiṅ ādeśa (1.3.4 tusma guard + 1.3.3 halantyam + 1.3.9 lopa)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = _bhave_atmanepada_tin_after_lopa(state, kartari_atmane=True)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ─────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 3.1.33 insert *sya* vikaraṇa after dhātu ────────────────────
    state = apply_rule("3.1.33", state)

    # ── Stage: 3.4.114 mark *sya* as ārdhadhātuka ───────────────────────────
    state = apply_rule("3.4.114", state)

    # ── Stage: 7.2.35 iṭ before *sya* (val-initial ārdhadhātuka) ────────────
    # Fires naturally via _ardhadhatuka_vikarana_index: sya is ardhadhatuka,
    # not krt, not done, starts with 's' (val consonant).
    state = _it_agama(state)

    # Trace steps for iṭ it-lopa (iṭ's T is conceptual; vacuous in engine).
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 1.2.4 sārvadhatuka apit → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: 7.1.3 jhi → anti (3pl only; vacuous for other cells) ─────────
    state = P00_jha_adesha(state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)
    # 7.3.101 ato dīrgho yañi: 'a' of *sya* → 'ā' before yañ-initial tiṅ
    # (m of mip/mas, v of vas).  Vacuous for non-yañ-initial ādeśas.
    state = apply_rule("7.3.101", state)
    # 7.3.84 guṇa: IK-vowel of dhātu (Ū of BU) → guṇa (o).
    if not state.meta.get("_lRT_skip_guna"):
        state = P00_guna_7_3_84(state)
        # 1.1.51 uraṇ raparaḥ: guṇa of ṛ/ḷ (→ a) is always followed by r/l
        # (kf → kar, not bare ka) — 7.3.84 sets urN_rapara_pending, sibling
        # _derive_lRG already completes it; _derive_lRT was missing this call.
        state = apply_rule("1.1.51", state)

    # ── Stage: pada saṃjñā + sandhi ─────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.78 eco'yavāyāvaḥ: EC + AC → split (o + i from iṭ → av + i).
    state = apply_rule("6.1.78", state)
    # 6.1.97 ato guṇe: a + a → a (fires for 3pl after jhi→anti: sya+anti).
    state = apply_rule("6.1.97", state)
    # ātmanepada duals, as in the laṭ spine: sya + आते → स्य + इय्ते (7.2.81)
    # → इते (6.1.66) → स्येते (6.1.87) — एधिष्येते, not एधिष्यआते.
    state = P00_ngit_At_iy_guna(state)

    # 6.4.19 च्छ्वोः शूडनुनासिके च: प्रच्छ्-specific तुक्+छ् → श् before the
    # ārdhadhātuka स्य (प्रक्ष्यति). Vacuous for every other root.
    state = apply_rule("6.4.19", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    state = _merge_pada(state)
    if state.meta.get("_lRT_ad_spine"):
        state.meta.pop("_lRT_ad_spine", None)
        state.meta.pop("_lRT_skip_guna", None)
        state.meta.pop("lRT_ad_ekac_spine", None)
        state = apply_rule("8.2.1", state)
        state = P00_tripadi_8_4_55_visarga(state)
        state = P00_tripadi_anusvara_parasavarna(state)
        state = apply_rule("8.4.68", state)
    else:
        state = P00_tripadi_rutva_visarga(state)
        state = apply_rule("8.3.59", state)   # s → ṣ after IK in pratyaya (sya → ṣya)
        state = apply_rule("8.4.68", state)   # trace marker

    return state


def _derive_lRT_ad(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* *lṛṭ* kartari (अत्स्यति …): *sya* + **7.2.10** (no iṭ), no *guṇa*,
    tripāḍī **8.4.55** (खरि च), **8.3.24**/**8.4.58** (3pl).
    """
    state.meta["ekac_dhatu"] = True
    state.meta["lRT_ad_ekac_spine"] = True
    state.meta["_lRT_skip_guna"] = True
    state.meta["_lRT_ad_spine"] = True
    state = apply_rule("7.2.10", state)
    return _derive_lRT(state, pada_key, purusha, vacana)


def _derive_lRG_ad(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* *lṛṅ* kartari (आत्स्यत् …): *sya* + **7.2.10** (no iṭ), **6.4.72** *āṭ*,
    no *guṇa*; tripāḍī **8.4.55** (खरि च).
    """
    state.meta["ekac_dhatu"] = True
    state.meta["lRG_ad_ekac_spine"] = True
    state.meta["_lRG_skip_guna"] = True
    state.meta["lRG_ad_spine"] = True
    state = apply_rule("7.2.10", state)

    state.meta["lakara"] = "lRG"
    state = apply_rule("3.3.139", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("lRG", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("3.1.33", state)

    state = apply_rule("3.4.114", state)

    state = apply_rule("3.4.101", state)
    state = apply_rule("3.4.100", state)
    state = P00_jha_adesha(state)
    state = apply_rule("3.4.99", state)
    state = apply_rule("1.2.4", state)
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)
    state = apply_rule("6.4.72", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)
    state = apply_rule("6.1.90", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.97", state)

    state = _merge_pada(state)
    state = apply_rule("8.2.1", state)
    if purusha == 3 and vacana == 1:
        state = apply_rule("8.2.39", state)
        state = apply_rule("8.4.56", state)
    if purusha == 3 and vacana == 3:
        state = apply_rule("8.2.23", state)
    if purusha == 2 and vacana == 1:
        state = P00_ru_visarga_pair(state)
    state = P00_tripadi_8_4_55_visarga(state)
    state = apply_rule("8.4.68", state)
    state.meta.pop("lRG_ad_spine", None)
    state.meta.pop("lRG_ad_ekac_spine", None)
    state.meta.pop("_lRG_skip_guna", None)
    return state


# ─────────────────────────────────────────────────────────────────────────────
# LOṬ (ĀJÑĀRTHA / IMPERATIVE) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def _derive_loT(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a loṭ (imperative / ājñārtha) form from the post-1.3.78 state.
    Full 9-cell bhū loṭ parasmaipada pipeline.

    Key features:
      • 3.3.162 loṭ attachment (trace marker); placeholder appended inline
      • Same tiṅ ādeśas as laT (tip/tas/jhi/sip/Tas/Ta/mip/vas/mas)
      • 3.4.113 sārvadhatuka + śap vikaraṇa
      • 3.4.89: mip→ni (apavāda to 3.4.101; call first — 1sg: bhavāni)
      • 3.4.101: tas→tām (3du), Tas→tam (2du), Ta→ta (2pl)
      • 3.4.87: sip→hi (2sg — before 3.4.86 sees 'si')
      • 7.1.3: jhi→anti (with 'i' intact — no 3.4.100 for loṭ)
      • 3.4.86: i→u (ti→tu 3sg; anti→antu 3pl; skips hi/ni)
      • 3.4.99: s-lopa (vas→va 1du; mas→ma 1pl)
      • 6.4.105: delete 'hi' after 'a' (2sg: bhava+hi → bhava)
      • 7.3.101: a→ā before yañ (ni 1sg, va 1du, ma 1pl)
      • 7.3.84: guṇa (bhū → bho; śap is sārvadhatuka)
      • 6.1.78/6.1.97 sandhi; Tripāḍī

    Expected forms (bhū):
      3sg → भवतु     3du → भवताम्   3pl → भवन्तु
      2sg → भव       2du → भवतम्    2pl → भवत
      1sg → भवानि    1du → भवाव     1pl → भवाम
    """
    state.meta["lakara"] = "loT"

    # ── Stage: 3.3.162 loṭ attachment (trace) + inline placeholder ───────────
    state.meta["loT_recipe"] = True
    state = apply_rule("3.3.162", state)
    state.meta.pop("3_3_162_loT_done", None)
    loT_varnas = parse_slp1_upadesha_sequence("loT")
    if loT_varnas and loT_varnas[-1].slp1 == "T":
        loT_varnas = loT_varnas[:-1]
    loT_term = Term(
        kind="pratyaya",
        varnas=loT_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "loT"},
    )
    state.terms.append(loT_term)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa (same laT base set) ─────────────────
    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    # ātmanepada: 3.4.79 टेरे / 3.4.80 थासः से (safe before śap now that the
    # ṭi-replaced ādeśas stay sārvadhātuka — 3.4.113 inventory)
    state = _bhave_atmanepada_tin_after_lopa(state, kartari_atmane=pada_key == "atmane")

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 1.2.4 apit → kṅit ─────────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: śap vikaraṇa (3.1.68 for bhvādi gaṇa 1) ──────────────────────
    gana: int = state.terms[0].meta.get("gana", 1)
    # 3.4.87 सेर्ह्यपिच्च belongs to the tiṅ-ādeśa stage: हि (apit) must exist
    # before the vikaraṇa's aṅga operations look at the ending (तनु, कुरु).
    state = apply_rule("3.4.87", state)
    state = _apply_vikarana(state, gana)

    # ── Stage: loṭ-specific tiṅ substitutions ────────────────────────────────
    # 3.4.89 FIRST (mi→ni, apavāda to 3.4.101's mi→am for 1sg)
    state = apply_rule("3.4.89", state)

    # 3.4.101: tas→tām (3du), Tas→tam (2du), Ta→ta (2pl)
    # mi→am won't fire since mi is already ni for 1sg
    state = apply_rule("3.4.101", state)

    # 3.4.87: sip→hi BEFORE 3.4.86 (prevent 'si' being seen by i→u rule)
    state = apply_rule("3.4.87", state)

    # 7.1.3: jhi→anti (has_i=True — loṭ retains 'i', unlike laṅ which drops it first)
    state = P00_jha_adesha(state)

    # 3.4.86: i→u (ti→tu for 3sg; anti→antu for 3pl; skip hi from 3.4.87, ni from 3.4.89)
    state = apply_rule("3.4.86", state)

    # 3.4.99: s-lopa (vas→va for 1du; mas→ma for 1pl)
    state = apply_rule("3.4.99", state)
    # ātmanepada loṭ: 3.4.91 सवाभ्यां वामौ (se → sva, dhve → dhvam),
    # 3.4.90 आमेतः (te → tām, ante → antām), 3.4.93 एत ऐ (uttama e → ai).
    # All self-gate on a loṭ sthānī ending in e; parasmaipada untouched.
    state = apply_rule("3.4.91", state)
    state = apply_rule("3.4.90", state)
    state = apply_rule("3.4.93", state)

    # 6.4.105: delete 'hi' after short 'a' of aṅga (2sg: bhava+hi → bhava)
    state = apply_rule("3.1.83", state)   # हलः श्नः शानज्झौ (स्कुभान)
    state = apply_rule("6.4.105", state)
    # 6.4.106 उतश्च प्रत्ययादसंयोगपूर्वात्: हि drops after a pratyaya-u (सुनु, तनु)
    state = apply_rule("6.4.106", state)

    # ── Stage: aṅgakārya + guṇa (1.4.13 → 1.1.5 → 7.3.84) ────────────────────
    # Must run BEFORE 3.4.92 below: the aṅga-final vowel that takes guṇa here
    # (śap-a for gaṇa 1, vikaraṇa-u for gaṇa 8) has to be settled before
    # āḍ-āgama inserts a new term after it.
    state = P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(state)
    # kṛ weak forms: 6.4.110 अत उत् सार्वधातुके (कर् → कुर्), 6.4.108 नित्यं करोतेः
    state = apply_rule("6.4.110", state)
    state = apply_rule("6.4.108", state)

    # 3.4.92: āḍ-āgama before the uttama-puruṣa tiṅ (ni/va/ma) — karavāṇi.
    # Placed after guṇa (so gaṇa-8's u→o has already happened; the āṭ vowel
    # then meets o, not bare u — 6.1.78 below turns o+ac into av, giving
    # kar-o + A → kar-av-A = karavā) and before 7.3.101 (so 7.3.101, which
    # only fires when the term directly before ni/va/ma still ends in 'a',
    # correctly declines once āṭ sits between them — a-vikaraṇa gaṇas were
    # reaching bhavāni only by 7.3.101 coincidentally producing the same
    # dīrgha; the real mechanism for *every* gaṇa is this āgama).
    state = apply_rule("3.4.92", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # 7.3.101: a→ā before yañ-initial tiṅ — harmless/no-op for uttama-puruṣa
    # now that 3.4.92 has already inserted āṭ between aṅga and ni/va/ma;
    # kept for any other yañ-initial tiṅ-ādeśa this spine might see.
    state = apply_rule("7.3.101", state)

    # ── Stage: pada + sandhi ─────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — only for tanādi (gana 8): vikaraṇa-u + antu (tanu+antu → tanvantu)
    if gana in _U_VIKARANA_GANAS:
        state = apply_rule("6.4.87", state)   # हुश्नुवोः सार्वधातुके (apavāda of 6.4.77)
        state = apply_rule("6.1.77", state)
    # 6.1.78 (eco'yavAyAvaH) must run BEFORE 6.1.97 below: it needs the śap
    # term's own 'a' still present to find the dhātu+śap boundary (bho+a →
    # bhav); 6.1.97 empties that term's varnas as its ekādeśa, which would
    # make 6.1.78's adjacent-term scan skip straight past it.
    state = apply_rule("6.1.78", state)
    # ātmanepada duals, before any a + ā sandhi can swallow the ā:
    # 7.2.81 आतो ङितः → 6.1.66 → 6.1.87 (एध + आताम् → एधेताम्).
    state = P00_ngit_At_iy_guna(state)
    # 6.1.97: a+a → a (3pl: śap-a + antu-a → bhavantu) — tried BEFORE 6.1.101
    # below: both structurally match plain a+a, but 6.1.97's ekādeśa (single
    # a) is what's attested here, not 6.1.101's dīrgha. Emptying śap's 'a'
    # here also removes it from 6.1.101's flat phoneme scan, so 6.1.101
    # correctly finds nothing left to merge on this junction afterward.
    state = apply_rule("6.1.97", state)
    # 6.1.101 akaH savarRe dIrghaH — a-vikaraṇa gaṇas' śap-a meeting āṭ's A
    # (bhava + A → bhavā, savarṇa-dīrgha; also 6.1.77's own apavāda).
    state = apply_rule("6.1.101", state)
    # āṭ/a + ai (6.1.88 वृद्धिरेचि: एधै, एधावहै).
    state = apply_rule("6.1.88", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)
    # 8.4.1/8.4.2 rashAByAM no RaH (+ its aw-kupvAN-vyavAya extension) — only
    # relevant to a cell that actually took 3.4.92's āṭ-āgama (uttama-puruṣa
    # ni/va/ma; karavāNi's r...n crosses the vikaraṇa's yaṇ-v + āṭ's A).
    # Gated on that, not called unconditionally: 8.4.2's existing vyavāya
    # scan doesn't treat yaṇ letters as blockers, so calling it for every
    # cell would also wrongly ṇ-ify gaṇa-8's *other* r...v...n words (e.g.
    # 3pl karvantu, where no āgama is involved and the yaṇ-v genuinely
    # should block — a real gap in 8.4.2 itself, out of this fix's scope).
    if state.samjna_registry.get("3.4.92_AT_uttama"):
        state = apply_rule("8.4.1", state)
        state = apply_rule("8.4.2", state)
    state = apply_rule("8.4.68", state)

    return state


def _derive_loT_ad(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    *ad* *loṭ* kartari (अत्तु … अदाम): *śap* + **2.4.72** *luk*, loṭ *tiṅ* spine,
    **3.4.92** *āṭ* (uttama), **6.4.101** *hi*→*dh* (2sg), no *guṇa*;
    tripāḍī **8.4.55** (खरि च) / **8.3.24**/**8.4.58** (3pl).
    """
    state.meta["lakara"] = "loT"
    state.meta["_loT_ad_spine"] = True
    state.meta["_loT_skip_guna"] = True

    state.meta["loT_recipe"] = True
    state = apply_rule("3.3.162", state)
    state.meta.pop("3_3_162_loT_done", None)
    loT_varnas = parse_slp1_upadesha_sequence("loT")
    if loT_varnas and loT_varnas[-1].slp1 == "T":
        loT_varnas = loT_varnas[:-1]
    state.terms.append(
        Term(
            kind="pratyaya",
            varnas=loT_varnas,
            tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
            meta={"upadesha_slp1": "loT"},
        )
    )
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = P00_sap_luk(state)

    if purusha == 1 and vacana == 1:
        state = apply_rule("3.4.89", state)

    state = apply_rule("3.4.101", state)

    if purusha == 2 and vacana == 1:
        state = apply_rule("3.4.87", state)

    state = P00_jha_adesha(state)

    state = apply_rule("3.4.86", state)

    state = apply_rule("3.4.99", state)

    if purusha == 1:
        state = apply_rule("3.4.92", state)
        if any("aTa_agama" in t.tags for t in state.terms):
            state = apply_rule("1.3.3", state)
            state = apply_rule("1.3.9", state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)

    if purusha == 2 and vacana == 1:
        state = apply_rule("6.4.101", state)

    state = apply_rule("1.4.14", state)

    state = _merge_pada(state)
    if purusha == 3 and vacana == 3:
        state = P00_tripadi_anusvara_parasavarna(state)
        state = apply_rule("8.4.68", state)
    elif purusha == 2 and vacana == 1:
        state = apply_rule("8.4.68", state)
    else:
        state = apply_rule("8.2.1", state)
        state = apply_rule("8.4.55", state)
        state = apply_rule("8.4.68", state)

    return state


# ─────────────────────────────────────────────────────────────────────────────
# LṚṄ (KRIYĀTIPATTI / CONDITIONAL) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def _dhatu_has_ṛ_anga(state: State) -> bool:
    """Dhātu aṅga still contains SLP1 ``f`` (ऋ) after it-lopa — e.g. ``vftu~`` → ``vft``."""
    for t in state.terms:
        if "dhatu" in t.tags:
            return any(v.slp1 == "f" for v in t.varnas)
    return False


def _attach_upasargas(state: State, upasargas: list[str] | None) -> State:
    """Prepend upadeśa prefix *Terms* before the *dhātu*; **1.4.59** *upasarga* saṃjñā."""
    if not upasargas:
        return state
    dhatu_i = next((i for i, t in enumerate(state.terms) if "dhatu" in t.tags), None)
    if dhatu_i is None:
        return state
    prefix: list[Term] = []
    for up in upasargas:
        prefix.append(
            Term(
                kind="upasarga",
                varnas=list(parse_slp1_upadesha_sequence(up)),
                tags={"pratyaya", "upadesha"},
                meta={"upadesha_slp1": up},
            )
        )
    before = state.flat_slp1()
    state.terms = prefix + state.terms
    state.emit_structural("__UPASARGA__", form_before=before, form_after=state.flat_slp1(),
                          why_dev="विवक्षितः उपसर्गः धातोः पूर्वं प्रयुज्यते (१.४.८० ते प्राग्धातोः)।")
    state = apply_rule("1.4.59", state)
    dh = next((t for t in state.terms if "dhatu" in t.tags), None)
    if dh is not None:
        for t in state.terms:
            if "upasarga" not in t.tags:
                continue
            up = (t.meta.get("upadesha_slp1") or "").strip()
            if up == "vi":
                dh.tags.add("vi_prefix")
            elif up in {"parA", "para"}:
                dh.tags.add("parA_prefix")
    return state


def _yam_with_A_upasarga(state: State) -> bool:
    """P010 tape: ``AN`` + ``yam`` *dhātu* (after it-lopa)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "yam":
            return False
        if i == 0:
            return False
        prev = state.terms[i - 1]
        if "upasarga" not in prev.tags:
            return False
        up = (prev.meta.get("upadesha_slp1") or "").strip().replace("~", "")
        while up and up[-1] in {"N", "Y", "R"}:
            up = up[:-1]
        return up == "A"
    return False


def _is_adadi_dhatu(state: State) -> bool:
    """Gaṇa 2 (अदादि) on the primary *dhātu* *Term*."""
    for t in state.terms:
        if "dhatu" in t.tags and t.meta.get("gana") == 2:
            return True
    return False


def _adadi_dhatu_stem_slp1(state: State) -> str:
    """Post–it-lopa *dhātu* stem on tape (e.g. ``ad``, ``As``)."""
    for t in state.terms:
        if "dhatu" in t.tags:
            return "".join(v.slp1 for v in t.varnas)
    return ""


def _derive_laT_adadi_kartari(state: State, purusha: int, vacana: int) -> State:
    """
    Adādi laṭ kartari parasmaipada (अद्भक्षणे → अत्ति … अद्मः): *śap* + **2.4.72** *luk*,
    no *guṇa*; tripāḍī **8.4.55** (खरि च), **8.2.66**/**8.3.15**, **8.3.24**/**8.4.58** (3pl).
    """
    state.meta["lakara"] = "laT"
    state = P00_lat_vartamane(state)
    _tin = _select_tin_adesha("laT", "parasmai", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, _tin)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = P00_sap_luk(state)
    # 7.3.93 ब्रुव ईट् (ब्रू-specific ī āgama on tip/sip/mip) → 7.3.84 guṇa
    # (ऊ→ओ) → 6.1.78 एचोऽयवायावः (ओ+ī → av+ī). All three scope themselves
    # to their own structural condition (brU root; ik-final dhātu; ec+ac
    # boundary) and are no-ops for अद्/अस्/दुह् — none of those roots end
    # in an ik vowel, so 7.3.84 (and downstream 6.1.78) simply decline.
    state = apply_rule("7.3.93", state)
    state = P00_guna_7_3_84(state)
    state = apply_rule("6.1.78", state)
    # 6.4.111 श्नसोरल्लोपः — अस् root's own initial a before an apit
    # sārvadhātuka tiṅ (tas/jhi/vas/mas…). Scoped to upadesha_slp1=="as"
    # in the sūtra's own cond(); a vacuous no-op for every other root
    # (अद्, दुह्, ब्रू…) sharing this spine.
    state = apply_rule("6.4.111", state)
    # 7.4.50 तासस्त्योर्लोपः — अस्+सि → असि (s of the root before s-initial sip)
    state = apply_rule("7.4.50", state)
    state = P00_jha_adesha(state)
    # 6.4.77 अचि श्नु धातुभ्रुवां य्वोरियुवङौ — ū-final dhātu + a-initial
    # affix → uv (ब्रू+अन्ति → ब्रुव्+अन्ति, after 7.1.3 turns jhi → anti).
    # General (any ū-final dhātu), decisively a no-op for अद्/अस्/दुह्.
    state = apply_rule("6.4.77", state)
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.4.14", state)
    # 6.1.101 अकः सवर्णे दीर्घः — ā-final root + a-initial affix (या + अन्ति → यान्ति); a no-op for the
    # consonant-final roots (अद्, दुह्) and for अस् / ब्रू, whose a / ū are gone or changed by now.
    state = apply_rule("6.1.101", state)
    # 8.2.32 दादेर्धातोर्घः — द्-initial ह्-final dhātu (दुह्, दिह्…) → घ् before
    # a झल्-initial affix (दुह्+ति → दुघ्+ति, apavāda to 8.2.31 हो ढः). Needs
    # the still-separate dhātu/tiṅ terms, so it runs pre-merge like 8.2.7's
    # own pre-merge branch; a no-op for अद्/अस्/ब्रू (none start with द्).
    state = apply_rule("8.2.32", state)
    state = _merge_pada(state)
    state = apply_rule("8.2.1", state)
    state = P00_tripadi_8_4_55_visarga(state)
    state = P00_tripadi_anusvara_parasavarna(state)
    # 8.4.53 झलां जश् झशि — jhal→jaś before jhaṣ (दुघ्+धि→दुग्धि). Not in
    # the universal tripadi spine (over-broad there, see core/phases/tripadi.py);
    # scoped here explicitly, a no-op for अद्/अस्/ब्रू (no jhal-before-jhaṣ site).
    state = apply_rule("8.4.53", state)
    state = apply_rule("8.4.68", state)
    return state


def _derive_laT_adadi(state: State, purusha: int, vacana: int) -> State:
    """
    Adādi laṭ ātmanepada spine (P008 *āste*): *śap* insertion, **2.4.72** *luk*,
    **3.4.79** *ṭere*, no *guṇa* / *tripāḍī* block (matches corrected-v2 P008).

    Only for gaṇa-2 roots resolved *ātmanepadī* — the dispatcher routes a
    *parasmaipadī* gaṇa-2 root to ``_derive_laT_adadi_kartari`` instead.
    """
    state.meta["lakara"] = "laT"
    state = P00_lat_vartamane(state)
    _tin = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, _tin)
    state.meta["3_1_68_kartari_recipe"] = True
    state = P00_jha_adesha(state)   # 3pl: 7.1.5 (at) → 7.1.3: आसते, not *आग्झे*
    state = P00_adadi_sap_luk_tere(state)
    # 8.2.32 दादेर्धातोर्घः — द्-initial ह्-final dhātu (दुह्→दुग्धे) needs the
    # same pre-merge tripadi entry the kartari-parasmai spine already has;
    # a no-op for आस्/अद् etc. (this function's original P008 आस्ते case),
    # none of which are द्-initial ह्-final.
    state = apply_rule("8.2.32", state)
    state = _merge_pada(state)
    state = apply_rule("8.2.1", state)
    state = P00_tripadi_8_4_55_visarga(state)
    state = P00_tripadi_anusvara_parasavarna(state)
    # 8.4.53 झलां जश् झशि — jhal→jaś before jhaṣ (दुघ्+धे→दुग्धे). Not in
    # the universal tripadi spine (over-broad there, see core/phases/tripadi.py);
    # scoped here explicitly, a no-op for आस्/अद् (no jhal-before-jhaṣ site).
    state = apply_rule("8.4.53", state)
    return state


def _derive_laT_yam_Anga(state: State, purusha: int, vacana: int) -> State:
    """
    ``AN`` + ``yam`` laṭ (P010 *āyacchate*): **1.3.28**, *śap*, **7.3.77**, *ṅ*-lopa, **3.4.79**.
    """
    state.meta["lakara"] = "laT"
    state = apply_rule("1.3.28", state)
    state = P00_lac_lat_attach(state)
    _tin2 = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, _tin2)
    state = apply_rule("3.4.113", state)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    # Do not run *halantyam*/*lopa* on ``yam`` as *upadeśa* (only on *śap*); keep ``m`` for **7.3.78**.
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    state = run_it_prakarana(state)
    state = apply_rule("7.3.77", state)     # इषुगमियमां छः: यम् → यछ्
    state = apply_rule("6.1.73", state)     # छे च: यत्छ् (8.4.40 → यच्छ्)
    state = run_it_prakarana(state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    state = _merge_pada(state)
    return P00_tripadi_rutva_visarga(state)     # 8.4.40: यत्छ → यच्छ


def _jYA_apa_check(state: State) -> bool:
    """P012 tape: ``apa`` + ``jYA`` *dhātu* (1.3.44 apahnave jñaḥ → ātmanepada; 3.1.81 śnā)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "jYA":
            return False
        if i == 0:
            return False
        prev = state.terms[i - 1]
        if "upasarga" not in prev.tags:
            return False
        return (prev.meta.get("upadesha_slp1") or "").strip() == "apa"
    return False


def _krI_with_upasarga_check(state: State) -> bool:
    """P009 tape: upasarga + ``krI`` *dhātu* (3.1.81 śnā; ātmanepada by 1.3.72 svarita-ñit)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "krI":
            return False
        if i == 0:
            return False
        return "upasarga" in state.terms[i - 1].tags
    return False


def _derive_laT_jYA_apa(state: State, purusha: int, vacana: int) -> State:
    """
    ``apa`` + ``jYA`` laṭ ātmanepada (P012 *apajānīte*): **1.3.44** context.

    Chain: **3.1.91** → P06a → **3.2.123** → laṭ → **3.4.77** → **3.4.78** (ta) →
    **3.1.81** (śnā) → **7.3.79** (jñā→jā) → **1.3.8** / **1.3.9** →
    **6.4.113** → **1.1.64** → **3.4.79** → merge.
    """
    state.meta["lakara"] = "laT"
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state = apply_rule("3.1.81", state)
    state = apply_rule("7.3.79", state)
    state = run_it_prakarana(state)
    state = apply_rule("6.4.113", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    state = _merge_pada(state)
    return state


def _kyaz_merge(state: State, stem_slp1: str) -> None:
    """Merge prātipadika + kyaz residue (``ya``) → dhātu ``stem_slp1 + y``."""
    if len(state.terms) < 2:
        return
    stem, sfx = state.terms[0], state.terms[1]
    sfx_flat = "".join(v.slp1 for v in sfx.varnas)
    sfx_tail = [sfx.varnas[0]] if sfx_flat == "ya" else list(sfx.varnas)
    merged = Term(
        kind="prakriti",
        varnas=list(stem.varnas) + sfx_tail,
        tags={"dhatu", "anga", "sanadi"},
        meta={},
    )
    state.terms = [merged] + state.terms[2:]
    form = state.flat_slp1()
    state.emit_structural(
        "__MERGE__",
        form_before=form,
        form_after=form,
        why_dev=f"{stem_slp1} + य्-अवशेष → {stem_slp1}य (kyaz-dhātu)।",
        type_label="धातु-संयोगः",
    )


def derive_denominative_laT(
    nominal_slp1: str,
    purusha: int,
    vacana: int,
) -> State:
    """
    Kyaz denominative laṭ parasmaipada — P016 *lohitāyati*.

    Chain: **1.2.45** → **3.1.13** (kyaz) → **1.3.8/3/9** → merge → **3.1.32** →
    **3.1.91** → P06a → **3.2.123** → laṭ → **3.4.77** → **3.4.78** (tip) →
    **3.1.68** (śap) → **1.3.3/8/9** → **3.4.113** → **7.4.25** → merge.
    """
    import sutras  # noqa: F401  trigger sutra registration

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(nominal_slp1)),
        tags=set(),
        meta={},
    )
    state = State(terms=[stem], meta={}, trace=[], samjna_registry={})
    state = apply_rule("1.2.45", state)
    state = apply_rule("3.1.13", state)
    state = run_it_prakarana(state)
    _kyaz_merge(state, nominal_slp1)
    state = apply_rule("3.1.32", state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "parasmai", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = run_it_prakarana(state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("7.4.25", state)
    state = apply_rule("6.1.101", state)
    state = _merge_pada(state)
    return state


def _merge_two_terms_to_pratipadika(state: State, why: str) -> None:
    """Merge first two terms into a single prātipadika Term."""
    if len(state.terms) < 2:
        return
    a, b = state.terms[0], state.terms[1]
    merged = Term(
        kind="prakriti",
        varnas=list(a.varnas) + list(b.varnas),
        tags={"anga", "prātipadika"},
        meta=dict(a.meta),
    )
    state.terms = [merged] + state.terms[2:]
    form = state.flat_slp1()
    state.emit_structural(
        "__MERGE__",
        form_before=form,
        form_after=form,
        why_dev=why,
        type_label="अच्-संयोगः",
    )


def derive_anukarana_laT(
    anukarana_slp1: str,
    purusha: int,
    vacana: int,
) -> State:
    """
    Anukaraṇa (sound-imitation) kyaz laṭ — P017 *paṭapaṭāyati*.

    Chain: **1.2.45** → **6.1.1** (dvitva) → **5.4.57** (qāc) → **8.1.2** →
    **6.1.97** → **1.3.7/3/9** → **1.4.18** → **6.4.143** (ṭi-lopa) →
    merge → **3.1.13** (kyaz) → **1.3.8/3/9** → merge → **3.1.32** →
    laṭ spine → merge.
    """
    import sutras  # noqa: F401

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(anukarana_slp1)),
        tags={"anga"},
        meta={"upadesha_slp1": anukarana_slp1},
    )
    state = State(terms=[stem], meta={}, trace=[], samjna_registry={})
    state = apply_rule("1.2.45", state)
    state = apply_rule("6.1.1", state)    # dvitva (structural for prātipadika)
    state = apply_rule("5.4.57", state)   # qāc suffix
    state = apply_rule("8.1.2", state)
    state = apply_rule("6.1.97", state)
    state = run_it_prakarana(state)
    state = apply_rule("1.4.18", state)
    state = apply_rule("6.4.143", state)  # ṭi-lopa (structural: bha+stem+dit)
    # After 6.4.143, stem has lost final ṭi syllables. The next term is qāc residue
    # (a/A). Merge them to get the prātipadika for kyaz.
    stem_now = "".join(v.slp1 for v in state.terms[0].varnas) if state.terms else ""
    _merge_two_terms_to_pratipadika(state, f"{stem_now} + qAc-residue → {stem_now}A")
    state = apply_rule("3.1.13", state)   # kyaz (structural: fires for this stem)
    state = run_it_prakarana(state)
    # Merge prātipadika + kyaz residue (ya → y) → dhātu
    stem_after = "".join(v.slp1 for v in state.terms[0].varnas) if state.terms else ""
    _kyaz_merge(state, stem_after)
    state = apply_rule("3.1.32", state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "parasmai", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = run_it_prakarana(state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.1.64", state)
    state = _merge_pada(state)
    return state


def derive_periphrastic_lit(
    dhatu_slp1: str,
    purusha: int,
    vacana: int,
) -> State:
    """
    Periphrastic liṭ (ām + kṛñ anuprayoga) — P014 *īkṣāñcakre*: the general liṭ
    spine, which takes the ām path (3.1.36) for an ijādi gurumān root.
    e.g. derive_periphrastic_lit('Ikz', 3, 1) → 'IkzAYcakre'
    """
    return derive(dhatu_slp1, "liT", "kartari", purusha, vacana, pada="atmane")


def _curadi_nic(state: State) -> State:
    """3.1.25 …चुरादिभ्यो णिच् → it-lopa (1.3.7/1.3.3/1.3.9) → aṅga before the
    ārdhadhātuka ṇic (7.2.116 अत उपधायाः: तड् → ताड्; 7.3.84/86 guṇa: चुर् → चोर्)
    → 3.1.32 सनाद्यन्ता धातवः: dhātu + इ is one dhātu (चोरि)."""
    state = apply_rule("3.1.25", state)
    state = P00_hal_it_lopa(state)          # Ṇ (1.3.7 cuṭū) + c (1.3.3) of ṇic
    state = apply_rule("6.4.48", state)    # अतो लोपः: adanta कथ/गण/वेल (1.1.57 then bars 7.2.116)
    state = apply_rule("7.2.115", state)   # अचो ञ्णिति: च्यु → च्यौ (च्यावयति)
    state = apply_rule("7.2.116", state)   # अत उपधायाः: तड् → ताड्
    # laghūpadha guṇa (चुर् → चोर्), r of ṛ-vṛddhi (पार्), ayādi (च्याव्+इ)
    state = P00_guna_rapara_ayadi(state)
    state = apply_rule("6.4.92", state)    # मितां ह्रस्वः: ज्ञाप् → ज्ञप् (ज्ञपयति)
    dh = next(t for t in state.terms if "dhatu" in t.tags)
    keep = {k: dh.meta[k] for k in ("kartari_atmanepada_licensed",) if k in dh.meta}
    if dh.meta.get("6_4_48_a_lopa_done"):
        keep["aglopa"] = True               # अनग्लोपे (7.4.93): कथ् → अचकथत्
    before = state.flat_slp1()
    di = state.terms.index(dh)
    stem = [v for t in state.terms[di:] for v in t.varnas]
    prayoga = dh.tags & {"kartari", "karmani", "bhave"} or {"kartari"}
    state.terms = state.terms[:di] + [Term(kind="prakriti", varnas=stem, tags={"dhatu", "anga"} | prayoga,
                        meta={**keep, "upadesha_slp1": "".join(v.slp1 for v in stem), "gana": 1,
                              "nijanta": True, "sanadi_pratyayanta": True,
                              "anit_dhatu": False, "set_dhatu": True})]
    state.emit_structural("__MERGE__", form_before=before, form_after=state.flat_slp1(),
                          why_dev="३.१.३२ सनाद्यन्ता धातवः — धातु + णिच् = नूतनधातुः।",
                          type_label="धातु-मेलनम्")
    return apply_rule("3.1.32", state)


def _nic_merge(state: State) -> None:
    """Merge dhātu + ṇic residue (``i``) + yuk(y) → secondary dhātu."""
    # After 3.1.26 inserts ṇic as "i" or "Ric" and 7.3.37 inserts yuk (y),
    # merge the three pieces into a single secondary dhātu term.
    if len(state.terms) < 2:
        return
    parts: list[str] = []
    for t in state.terms:
        parts.extend(v.slp1 for v in t.varnas)
    merged_slp1 = "".join(parts)
    merged = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(merged_slp1)),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": merged_slp1},
    )
    state.terms = [merged]
    form = state.flat_slp1()
    state.emit_structural(
        "__MERGE__",
        form_before=form,
        form_after=form,
        why_dev=f"dhātu + ṇic-i + yuk → {merged_slp1} (Ṇic-dhātu)।",
        type_label="धातु-मेलनम्",
    )


def _derive_laT_nic_atmane(state: State, purusha: int, vacana: int) -> State:
    """
    Ṇic causative laṭ ātmanepada — P015 *pāyayate*.

    Chain: **3.1.26** (ṇic) → **1.3.7/3/9** → **7.3.37** (yuk) → merge →
    **3.1.32** → **3.1.91** → P06a → **3.2.123** → laṭ → **3.4.77** →
    **3.4.78** (ta) → **3.1.68** (śap) → **1.3.3/8/9** → **3.4.113** →
    **1.1.64** → **3.4.79** → **7.3.84** → **6.1.78** → merge.
    """
    state.meta["lakara"] = "laT"
    state.meta["nic_recipe"] = "nic"
    # Tag dhātu for 3.1.26 emit_Ric_tape (for 1.3.7 to find R)
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("emit_Ric_tape")
            break
    state = apply_rule("3.1.26", state)
    state = run_it_prakarana(state)
    state = apply_rule("7.3.37", state)
    _nic_merge(state)
    state = apply_rule("3.1.32", state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = run_it_prakarana(state)
    state = P00_adadi_tere_3_4_79(state)
    state = P00_guna_sandhi_7_3_84_6_1_78(state)
    state = _merge_pada(state)
    return state


def _san_check(state: State) -> bool:
    """P013 tape: any *dhātu* — sanādi desiderative path (``san_recipe = 'san'``)."""
    return state.meta.get("san_recipe") == "san"


def _derive_laT_san_atmane(state: State, purusha: int, vacana: int) -> State:
    """
    Sanādi (desiderative) laṭ ātmanepada — P013 *śuśrūṣate*.

    Chain: **3.1.7** (san) → **1.2.8** → **1.1.5** → **3.1.32** (saṃjñā) →
    **6.1.1** (dvitva, structural) → **6.1.4** → **6.4.16** (dīrgha before san) →
    **7.4.60** (abhyāsa hrasva) → **3.1.91** → P06a → **3.2.123** → laṭ →
    **3.4.77** → **3.4.78** (ta) → **3.1.68** (śap) → **1.3.3/8/9** →
    **3.4.113** → **1.1.64** → **3.4.79** → merge → **6.1.97** → **8.2.1** →
    **8.3.59**.
    """
    state.meta["lakara"] = "laT"
    # 3.1.7: san suffix (structural via san_recipe coordination key)
    state = P00_san_kit_kngiti(state)
    state = apply_rule("3.1.32", state)
    # 6.1.1: dvitva — fires structurally (dhātu + sanādi on tape)
    state = P00_san_dvitva(state)
    # 6.4.16 dīrgha + 7.4.60 abhyāsa hrasva
    state = P00_san_dirgha_hrasva(state)
    # Tiṅ spine (ātmanepada 3sg laṭ)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = run_it_prakarana(state)
    state = P00_adadi_tere_3_4_79(state)
    state = _merge_pada(state)
    state = apply_rule("6.1.97", state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.3.59", state)
    return state


def _dyut_vi_check(state: State) -> bool:
    """P018-B tape: ``vi`` + ``dyut`` *dhātu* — ātmanepada luṅ (kartrabhiprāya 1.3.72)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "dyut":
            return False
        if i == 0:
            return False
        return (state.terms[i - 1].meta.get("upadesha_slp1") or "").strip() == "vi"
    return False


def _kf_with_upasarga_check(state: State) -> bool:
    """P011 tape: upasarga + ``kf`` *dhātu* (gana 8 tanādi; 3.1.79 u-vikaraṇa; ātmanepada)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "kf":
            return False
        if t.meta.get("gana") != 8:
            return False
        if i == 0:
            return False
        return "upasarga" in state.terms[i - 1].tags
    return False


def _derive_laT_kf_u_atmane(state: State, purusha: int, vacana: int) -> State:
    """
    upasarga + ``kf`` (qukfY) laṭ ātmanepada (P011-A *utkurute*, P011-B *upaskurute*):
    **3.1.79** u-vikaraṇa + **7.3.84** guṇa.

    Chain: **6.1.135**/**6.1.139** (suṭ, if applicable) → **3.1.91** → P06a →
    **3.2.123** → laṭ → **3.4.77** → **3.4.78** (ta) → **3.1.79** (u) →
    **7.3.84** → **1.1.51** → **1.2.4** → **1.1.64** → **3.4.79** →
    **6.4.110** → merge → **8.2.1** → **8.4.55**.
    """
    state.meta["lakara"] = "laT"
    # suṭ agama for upa + kf (6.1.135/6.1.139) — fires structurally if conditions met.
    state = apply_rule("6.1.135", state)
    state = apply_rule("6.1.139", state)
    # 1.3.3/1.3.9 on suṭ it-marker only — guard upasarga terms so their final
    # hal (e.g. 'd' in ud) is not misread as halantyam it.
    for t in state.terms:
        if "upasarga" in t.tags:
            t.tags.discard("upadesha")
    state = run_it_prakarana(state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state = P00_tanadi_u_guna(state)
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    state.samjna_registry.pop("1.2.4_sarvadhatukam_apit", None)
    state = apply_rule("1.2.4", state)
    state = apply_rule("1.1.5", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("6.4.110", state)
    state = _merge_pada(state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.4.55", state)
    return state


def _derive_laT_krI_sna_atmane(state: State, purusha: int, vacana: int) -> State:
    """
    upasarga + ``krI`` laṭ ātmanepada (P009 *parikrīṇīte*): **3.1.81** śnā + tripāḍī.

    Chain: **3.1.91** → P06a → **3.2.123** → laṭ → **3.4.77** → **3.4.78** (ta) →
    **3.1.81** (śnā) → **1.3.8** / **1.3.9** → **6.4.113** → **1.1.64** →
    **3.4.79** → **8.2.1** → **8.4.2** → merge.
    """
    state.meta["lakara"] = "laT"
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state = apply_rule("3.1.81", state)
    state = run_it_prakarana(state)
    state = apply_rule("6.4.113", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.4.2", state)
    state = _merge_pada(state)
    return state


def _derive_lRG_ṛ_dhatu(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Lṛṅ for ṛ-roots (वृत् etc.): P019-aligned spine — ``sy`` + 7.3.86 ṛ→ar, no iṭ/7.3.84 bhū path.

    Tiṅ selection uses *parasmaipada* (corrected P019 / ``parasmaipada (vā)``), not the
    1.3.78 gate from dhātupāṭha (``vftu~`` is labelled आत्मनेपदी).
    """
    _ = pada_key  # gate may be *atmane*; P019 spine is parasmaipada
    pada_key = "parasmai"
    state.meta["lakara"] = "lRG"
    state = apply_rule("3.3.139", state)
    _tin = _select_tin_adesha("lRG", pada_key, purusha, vacana)
    state = P00_tin_adesha_base(state, _tin)
    # Halantyam + it-lopa on tiṅ ādeśa: ``tip`` → ``ti`` (required before 3.1.33 ``sy``).
    state = run_it_prakarana(state)
    state = apply_rule("3.1.33", state)
    state = apply_rule("3.4.100", state)
    state = P00_guna_7_3_86(state)
    state = apply_rule("1.1.51", state)
    state = apply_rule("6.4.71", state)
    state = apply_rule("6.1.73", state)
    state = run_it_prakarana(state)
    state = _merge_pada(state)
    return state


def _derive_lRG(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a lṛṅ (conditional / kriyātipatti) form from the post-1.3.78 state.
    Full 9-cell bhū lṛṅ parasmaipada pipeline.

    Key features:
      • 3.3.139 attaches lṛṅ (+ aT_agama_context on dhātu)
      • 3.1.33 inserts sya vikaraṇa (s+y+a) after dhātu
      • 3.4.114 marks sya as ārdhadhātuka
      • 7.2.35 inserts iṭ before sya (val-initial ārdhadhātuka)
      • 3.4.101 tiṅ substitutions (tas→tām, thas→tam, tha→ta, mi→am)
      • 3.4.100 i-lopa (ti→t, si→s, jhi→jh)
      • 7.1.3 jh→ant (3pl)
      • 3.4.99 s-lopa (vas→va, mas→ma)
      • 6.4.71 aṭ augment (lṛṅ is in luṅ/laṅ/lṛṅ group)
      • 7.3.101 ato dīrgho yañi (1du/1pl: sya-a→ā before v/m)
      • 7.3.84 guṇa (bhū → bho; NOT blocked — sya is ārdhadhātuka, not kit)
      • 6.1.78 ecoyavāyāvaḥ (bho+i → bhav+i)
      • 6.1.97 ato guṇe (3pl: sya+ant → sy+ant; 1sg: sya+am → sy+am)
      • Tripāḍī: 8.2.39/8.4.56, 8.2.23, 8.2.66/8.3.15, 8.3.59

    Expected forms (bhū):
      3sg → अभविष्यत्   3du → अभविष्यताम्  3pl → अभविष्यन्
      2sg → अभविष्यः    2du → अभविष्यतम्   2pl → अभविष्यत
      1sg → अभविष्यम्   1du → अभविष्याव    1pl → अभविष्याम

    Ṛ-dhātus (``vftu~`` …): use ``_derive_lRG_ṛ_dhatu`` (P019 spine).
    """
    _dh = next((t for t in state.terms if "dhatu" in t.tags), None)
    if _dh is not None and "वृतादिः" in (_dh.meta.get("antarganas") or ()) and _dhatu_has_ṛ_anga(state) \
            and "karmani" not in _dh.tags:
        # वृतादि (1.3.92 वृद्भ्यः स्यसनोः parasmaipada, 7.2.59 no iṭ): अवर्त्स्यत्
        return _derive_lRG_ṛ_dhatu(state, pada_key, purusha, vacana)

    state.meta["lakara"] = "lRG"

    # ── Stage: 3.3.139 lṛṅ attachment ───────────────────────────────────────
    state = apply_rule("3.3.139", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa ────────────────────────────────────
    tin_adesha = _select_tin_adesha("lRT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = _bhave_atmanepada_tin_after_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 3.1.33 insert sya vikaraṇa after dhātu ───────────────────────
    state = apply_rule("3.1.33", state)

    # ── Stage: 3.4.114 mark sya as ārdhadhātuka ─────────────────────────────
    state = apply_rule("3.4.114", state)

    # ── Stage: 7.2.35 iṭ before sya (val-initial ārdhadhātuka) ─────────────
    state = _it_agama(state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 1.2.4 apit sārvadhatuka → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: tiṅ substitutions (laṅ-style) ────────────────────────────────
    state = apply_rule("3.4.101", state)   # tas→tām, Tas→tam, Ta→ta, mi→am (apavāda)
    state = apply_rule("3.4.100", state)   # ti→t, si→s, jhi→jh
    state = P00_jha_adesha(state)     # jh→ant (3pl)
    state = apply_rule("3.4.99", state)    # vas→va, mas→ma

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)

    # 6.4.71 aṭ + it-lopa (lṛṅ group)
    state = P00_at_agama_it_lopa(state)

    # 7.3.101 ato dīrgho yañi: sya-a → ā before yañ-initial tiṅ (v of va, m of ma)
    state = apply_rule("7.3.101", state)

    # 7.3.84 guṇa (bhū → bho; ārdhadhātuka sya triggers)
    state = P00_guna_7_3_84(state)

    # ── Stage: pada saṃjñā + sandhi ─────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)    # bho+i(ṭ) → bhav+i
    state = P00_ngit_At_iy_guna(state)     # ātmane: ऐधिष्येताम्, ऐधिष्ये
    state = apply_rule("6.1.97", state)    # a+a → a (3pl: sya+ant; 1sg: sya+am)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)   # full phase (8.4.40 अच्छेत्स्यत …)
    state = apply_rule("8.3.59", state)    # s→ṣ after IK (sya→ṣya)

    return state


def _derive_karmani_laG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani laṅ (passive imperfect / anadhyatana bhūta) for bhvādi dhātus.

    Key sūtras: 1.3.13 (ātmanepada), 3.2.111 (laṅ + aṭ āgama context),
    3.1.67 (yaḳ), 6.4.71 (aṭ prepended to dhātu), 7.1.3 (Ja→anta, 3pl),
    7.2.81 (ā→iy for 3du/2du), 6.1.66 (y-lopa), 7.3.101 (1du/1pl yā),
    6.1.87 (a+i→e), 6.1.97 pararūpa (3pl a+a→a).

    No 3.4.79/3.4.80 (laṅ is not ṭit → ṭi→e doesn't apply in laṅ).

    Expected: अभूयत अभूयेताम् अभूयन्त अभूयथाः अभूयेथाम् अभूयध्वम्
              अभूये अभूयावहि अभूयामहि
    """
    state.meta["lakara_liG"] = False
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    state = apply_rule("1.3.13", state)

    # 3.2.111 laṅ attachment (tags dhātu with aT_agama_context)
    state = apply_rule("3.2.111", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("laG", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    state = _karmani_apply_yak(state)

    # No 3.4.79/3.4.80 — laṅ is not ṭit

    state = apply_rule("1.4.13", state)

    # 6.4.71 aṭ + it-lopa
    state = P00_at_agama_it_lopa(state)

    state = apply_rule("1.1.5", state)

    state = apply_rule("7.4.25", state)

    # 7.1.3 jho'ntaḥ: karmani 3pl Ja → anta (no prior 3.4.79, so just J→ant+a)
    state = P00_jha_adesha(state)

    state = apply_rule("7.2.81", state)

    # 6.1.66 y-lopa (drop y from iy before HAL)
    state = apply_rule("6.1.66", state)

    # 7.3.101 ato dīrgho yañi (1du/1pl: a of ya → ā before v/m)
    state = apply_rule("7.3.101", state)

    state = apply_rule("1.4.14", state)

    # 6.1.87 ādguṇaḥ: ya-a + i/iy → e (1sg, 3du/2du)
    state = apply_rule("6.1.87", state)

    # 6.1.97 pararūpa: ya-a + a (3pl anta-a) → a
    state = apply_rule("6.1.97", state)

    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)

    return state


def _derive_karmani_liG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani vidhi-liṅ (passive optative) for bhvādi dhātus.

    Key sūtras: 1.3.13, 3.3.161 (vidhiliṅ), 3.1.67 (yaḳ), 3.4.102 (sīyuṭ),
    7.2.79 (s-lopa of sīyuṭ), 6.1.66 (y-lopa before HAL), 6.1.87 (a+ī→e),
    7.3.101 (1du/1pl yā), 7.1.3 (Ja→anta, 3pl).

    No 7.2.81 (sīyuṭ [I,y] sits between yaḳ and tiṅ, breaking ṅit chain).
    No 3.4.79/3.4.80 (vidhiliṅ not ṭit for ātmanepada ṭi-substitution).

    Expected: भूयेत भूयेयाताम् भूयेयन्त भूयेथाः भूयेयाथाम् भूयेध्वम्
              भूयेयि भूयेवहि भूयेमहि
    """
    state.meta["lakara"]   = "liG"
    state.meta["vidhi_liG"] = True
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    state = apply_rule("1.3.13", state)

    state.meta["liG_vidhi_recipe"] = True
    state = apply_rule("3.3.161", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    state = _karmani_apply_yak(state)

    # 3.4.105 Ja→ran (3pl)
    state.meta["Ja_ran_recipe"] = True
    state = apply_rule("3.4.105", state)
    # 3.4.106 इटोऽत् — liṅ's uttama iṭ → a (क्रियेय, not क्रियेयि)
    state = apply_rule("3.4.106", state)

    # No 3.4.79/3.4.80 (vidhiliṅ not ṭit for ātmanepada ṭi-substitution)

    # 3.4.102 sīyuṭ insertion between yaḳ and tiṅ (karmani: use tiṅ ādeśa, not liG placeholder)
    state.meta["sIyuw_recipe"] = True
    state.meta["karmani_liG_recipe"] = True
    state = apply_rule("3.4.102", state)

    # 7.2.79 s-lopa: drop 's' of sīyuṭ [s,I,y] → [I,y]
    state = apply_rule("7.2.79", state)

    # 6.1.66: y of sīyuṭ-remnant [I,y] drops before HAL-initial tiṅ
    state = apply_rule("6.1.66", state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)

    state = apply_rule("7.4.25", state)

    # 7.1.3 jho'ntaḥ: 3pl ran already substituted (3.4.105), vacuous here
    state = P00_jha_adesha(state)

    # 7.3.101 ato dīrgho yañi (1du/1pl: a of ya → ā before v/m of sīyuṭ or tiṅ)
    state = apply_rule("7.3.101", state)

    state = apply_rule("1.4.14", state)

    # 6.1.87 ādguṇaḥ: ya-a + ī (from sīyuṭ-I) → ye
    state = apply_rule("6.1.87", state)

    # 6.1.97 pararūpa: 3pl ya-a + ran-a/anta-a → a
    state = apply_rule("6.1.97", state)

    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)

    return state


def _derive_karmani_ashir_liG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmaṇi āśīr-liṅ (passive benedictive): 1.3.13 ātmanepada, then the shared
    ātmanepada spine below.

    Expected: भविषीष्ट भविषीयास्ताम् भविषीरन् भविषीष्ठाः भविषीयास्थाम्
              भविषीध्वम् भविषीय भविषीवहि भविषीमहि
    """
    state.meta["lakara"]    = "AsIrliG"
    state.meta["ashir_liG"] = True
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    state = apply_rule("1.3.13", state)
    return _derive_ashir_liG_atmane(state, purusha, vacana)


def _derive_ashir_liG_atmane(state: State, purusha: int, vacana: int) -> State:
    """Āśīrliṅ in ātmanepada (एधिषीष्ट) — kartari and karmaṇi share it: the
    liṅ is ārdhadhātuka here (3.4.116), so no yak; sīyuṭ (3.4.102) not yāsuṭ.

    त/आताम्/झ… (3.4.78) → 3.4.105 झस्य रन् → 3.4.106 इटोऽत् → 3.4.102 सीयुट्
    → 3.4.107 सुट् तिथोः → 6.1.66 य्-लोप before val → 7.2.35 इट् → tripāḍī
    (8.3.59 षत्व, 8.4.41 ष्टुत्व)."""
    state.meta["lakara"]    = "AsIrliG"
    state.meta["ashir_liG"] = True
    state = apply_rule("3.3.173", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state = _atmane_tin_upadesha(state, purusha, vacana)

    state = apply_rule("3.4.116", state)
    state = apply_rule("3.4.105", state)   # झस्य रन्
    state = apply_rule("3.4.106", state)   # इटोऽत्

    state.meta["sIyuw_recipe"] = True
    state = apply_rule("3.4.102", state)   # सीयुट्
    state.meta["suw_recipe"] = True
    state = apply_rule("3.4.107", state)   # सुट् तिथोः
    state.meta.pop("suw_recipe", None)
    state = apply_rule("6.1.66", state)    # लोपो व्योर्वलि: सीय् + स्/र/व/म/ध

    state = apply_rule("1.4.13", state)
    state = _it_agama(state)
    state = apply_rule("1.2.11", state)
    state = apply_rule("1.2.12", state)
    state = P00_hal_anit_guna(state)
    state = apply_rule("1.1.51", state)

    state = apply_rule("1.4.14", state)

    # 6.1.78 eco'yavāyāvaḥ (bho → bhav)
    state = apply_rule("6.1.78", state)

    state = _merge_pada(state)
    state = execute_tripadi_phase(state)

    return state


def _derive_karmani_luG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmaṇi luṅ 3sg (the only cell with चिण्; the others take सिच्).

    3.2.110 लुङ् → 3.1.43 च्लि → त (3.4.78) → 3.1.66 च्लि → चिण् before त →
    1.3.7/1.3.3/1.3.9 leave इ → 6.4.104 चिणो लुक् deletes त → ṇit vṛddhi
    (7.2.115 / 7.2.116) → aṭ.  Expected: अभावि, अपाचि, अकारि, ऐधि.
    """
    state.meta["lakara"] = "luG_karmani"
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    state = apply_rule("1.3.13", state)

    # 3.2.110 luṅ attachment: attaches luG placeholder + tags dhātu aT_agama_context
    state.meta["luG_recipe"] = True
    state = apply_rule("3.2.110", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state.meta["cli_luG_recipe"] = True
    state = apply_rule("3.1.43", state)    # च्लि लुङि

    state = _atmane_tin_upadesha(state, purusha, vacana)

    state = apply_rule("3.1.66", state)    # च्लि → चिण् before त
    state = P00_krt_it_lopa(state)         # चिण्: 1.3.7 च्, 1.3.3 ण्, 1.3.9
    state = apply_rule("6.4.104", state)   # चिणो लुक्: त deleted

    state = apply_rule("1.4.13", state)

    # ṇit चिण् (ārdhadhātuka, no iṭ): 7.2.115 अचो ञ्णिति, 7.2.116 अत उपधायाः
    state = apply_rule("6.4.51", state)    # णेरनिटि: चोरि + इ → अचोरि
    state = apply_rule("6.1.45", state)    # ग्लै → ग्ला
    state = apply_rule("7.3.33", state)    # आतो युक् चिण्कृतोः: अग्लायि, अदायि
    state.meta["7_2_115_karmani_lut_arm"] = True
    state = apply_rule("7.2.115", state)
    state = apply_rule("7.2.116", state)   # अत उपधायाः before ṇit ciṇ: अपाचि, अदाधि
    state = P00_guna_rapara_ayadi(state)   # laghūpadha guṇa: अमोदि, अतोदि

    state = P00_at_or_At_agama(state)      # aṭ; ajādi āṭ + vṛddhi: ऐधि

    state = apply_rule("1.4.14", state)

    # 6.1.78 eco'yavāyāvaḥ: O (au) → Av (bhO → bhav)
    state = apply_rule("6.1.78", state)

    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)
    state = apply_rule("8.3.59", state)   # suṭ-s → ṣ (z) after ciṇ-i (iK)

    return state


def _derive_karmani_luT(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani luṭ (passive periphrastic future) for bhvādi dhātus.

    Key structure: 1.3.13 → ātmanepada tiṅ ādeśa → 3.4.113 → 3.1.33 (tāsi) →
    3.4.79/3.4.80/2.4.85 → 7.2.35 (iṭ before tāsi) → 7.3.84 (guṇa) →
    tāsi-specific modifications → 6.1.78 → tripāḍī.

    Guṇa path (via 7.2.35+7.3.84): bhU(U→o) → bho + ita = bhavita → bhavitā
    Verified forms: भविता भवितारौ भवितारः भवितासे भवितासाथे भविताध्वे
                    भविताहे भवितास्वहे भवितास्महे
    """
    # ── Tag dhātu for bhāva/karma ──────────────────────────────────────────
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada ─────────────────────────────────
    state = apply_rule("1.3.13", state)
    return _derive_luT_atmane(state, purusha, vacana)


def _derive_luT_atmane(state: State, purusha: int, vacana: int) -> State:
    """Luṭ in ātmanepada — kartari (एधिता, एधितासे) and karmaṇi alike: tāsi is
    ārdhadhātuka, so no yak intervenes and one spine serves both prayogas."""
    # ── 3.3.3 + 3.3.15: luṭ attachment ───────────────────────────────────
    state = apply_rule("3.3.3", state)
    state.meta["luT_recipe"] = True
    state = apply_rule("3.3.15", state)
    state.meta.pop("luT_recipe", None)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 3.1.33: insert tāsi vikaraṇa ──────────────────────────────────────
    state.meta["tasi_luT_recipe"] = True
    state = apply_rule("3.1.33", state)
    state.meta.pop("tasi_luT_recipe", None)

    # ── 3.4.77 + 3.4.78: ātmanepada tiṅ ādeśa ────────────────────────────
    tin_adesha = _select_tin_adesha("luT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Cell-specific tiṅ processing + tāsi modifications ─────────────────
    if purusha == 3 and vacana == 1:
        # 3sg: ta → ḍā via 2.4.85, IT-lopa on ḍ, then 7.2.35 iṭ, 7.3.84 guṇa, 6.4.143
        adesha = _LUT_PRATHAMA_ADESHA[(3, 1)]
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        if state.terms:
            state.terms[-1].meta["dit_pratyaya"] = True
        # IT-lopa on ḍā: q(ḍ) is cuṭu → IT, drops → ā
        state = apply_rule("1.3.7", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("3.4.114", state)
        # 7.2.35 iṭ before tāsi (tāsi is ardhadhatuka, val-initial)
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state = apply_rule("6.4.143", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)  # bho→bhav

    elif purusha == 3 and vacana == 2:
        # 3du: Atam → rau via 2.4.85, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.51 ri ca
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        adesha = _LUT_PRATHAMA_ADESHA[(3, 2)]
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        state = apply_rule("3.4.114", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 3:
        # 3pl: Ja → ras via 2.4.85, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.51 ri ca
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        adesha = _LUT_PRATHAMA_ADESHA[(3, 3)]
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        state = apply_rule("3.4.114", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 1:
        # 2sg: TAs → se via 3.4.80, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.50 tāsas lopa
        state = apply_rule("3.4.80", state)   # thās → se
        state = apply_rule("3.4.114", state)
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state.meta["tasa_lopa_recipe"] = True
        state = apply_rule("7.4.50", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 2:
        # 2du: ATAm → ATe via 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 3:
        # 2pl: Dvam → Dve via 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa, 8.2.25 s-lopa before dh
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 1 and vacana == 1:
        # 1sg: iT → i → e via 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.52 s→h before e
        state = apply_rule("3.4.79", state)  # iT→i→e
        state = apply_rule("3.4.114", state)
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state = apply_rule("7.4.52", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    else:
        # 1du (vahi) and 1pl (mahi): 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa, no tāsi mod
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state = _it_agama(state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = P00_guna_7_3_84(state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī (full phase: 8.2.25 tāsdhve → tādhve, 8.4.58 अङ्किता …)
    state = _merge_pada(state)
    return P00_tripadi_rutva_visarga(state)


def _derive_bhave_laT(state: State, purusha: int, vacana: int) -> State:
    """
    Bhāve laṭ (present, akarmaka roots): ātmanepada tiṅ + śap vikaraṇa (no yaḳ).

    Example: bhū + laṭ bhāve 3sg → भवते (not karmaṇi भूयते).
    """
    # Tag dhātu for bhāva prayoga (needed by 7.2.81 structural cond)
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    state = P00_lat_vartamane(state)

    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    gana: int = next(
        (t.meta.get("gana", 1) for t in state.terms if "dhatu" in t.tags),
        1,
    )
    state = _apply_vikarana(state, gana)

    state = apply_rule("3.4.79", state)
    state = apply_rule("3.4.80", state)
    state = apply_rule("1.2.4", state)
    state = P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(state)
    state = P00_jha_adesha(state)
    state = apply_rule("7.2.81", state)
    state = apply_rule("6.1.66", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)
    state = apply_rule("6.1.87", state)
    state = apply_rule("6.1.97", state)
    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)
    return state


def _derive_karmani_laT(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani laṭ (passive present) for bhvādi dhātus.

    Key sūtras: 1.3.13 (ātmanepada), 3.1.67 (yaḳ vikaraṇa), 3.4.78 (tiṅ ādeśa),
    3.4.79 (ṭi→e), 3.4.80 (thās→se), 7.1.3 (jha→ante), 7.2.81 (ā→iy),
    6.1.66 (y-lopa), 6.1.87 (a+i→e), 6.1.97 (a+a/e pararūpa), 7.3.101 (yañi dīrgha).

    Example: bhū + laṭ karmani 3sg → भूयते
    """
    # ── Tag dhātu for bhāva/karma prayoga ────────────────────────────────
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada in karmani ─────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.2.123 vartamāne laṭ ────────────────────────────────────────────
    state = P00_lat_vartamane(state)

    # ── 3.4.77 lasya ─────────────────────────────────────────────────────
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    # ── 1.4.100 lakāratāṅānāv ātmanepadam ────────────────────────────────
    state = apply_rule("1.4.100", state)

    # ── IT-prakaraṇa on tiṅ ādeśa (1.3.4/1.3.3/1.3.9) ───────────────────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── 1.2.4 sārvadhatukam apit ─────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    state = _karmani_apply_yak(state)

    # ── 3.4.114 ārdhadhātukam śeṣaḥ (vacuous trace step) ─────────────────
    state = apply_rule("3.4.114", state)

    # ── 3.4.79: ṭita ātmanepada ṭere (terminal vowel+rest → e) ───────────
    state = apply_rule("3.4.79", state)

    # ── 3.4.80: thāsasse (2sg: thās → se) ────────────────────────────────
    state = apply_rule("3.4.80", state)

    # ── 1.2.4 second pass (sārvadhatukam apit — yaḳ context) ──────────────
    state = apply_rule("1.2.4", state)

    # ── 1.4.13 aṅga-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # ── 1.1.5 kṅiti ca: block guṇa before yaḳ (kit) ──────────────────────
    state = apply_rule("1.1.5", state)

    state = apply_rule("7.4.25", state)

    # ── 7.1.3: jho'ntaḥ (karmani 3pl: Je → ante) ─────────────────────────
    state = P00_jha_adesha(state)

    state = apply_rule("7.2.81", state)

    # ── 6.1.66: lopo vyorvali (drop y from iy before val) ─────────────────
    state = apply_rule("6.1.66", state)

    # ── 7.3.101 ato dīrgho yañi (1du/1pl: ya → yā before v/m) ────────────
    state = apply_rule("7.3.101", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.87 ādguṇaḥ (3du/2du: ya(a)+ite(i) → ye+te cross-term) ────────
    state = apply_rule("6.1.87", state)

    # ── 6.1.97 ato guṇe (3pl: a+a→a, 1sg: a+e→e pararūpa) ───────────────
    state = apply_rule("6.1.97", state)

    # ── STRUCTURAL: pada merge ────────────────────────────────────────────
    state = _merge_pada(state)
    # ── TRIPĀḌĪ ──────────────────────────────────────────────────────────
    state = P00_tripadi_rutva_visarga(state)

    return state


def _derive_karmani_lRT(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani lṛṭ (passive simple future) for bhvādi dhātus.

    Structural order: 1.3.13 → lṛṭ attachment → tiṅ ādeśa (ātmanepada) →
    3.4.113 → sya vikaraṇa (3.1.33) → 3.4.114 → 3.4.79/3.4.80 (ṭi-e) →
    6.4.62 (ciṇvat iṭ before sya) → 7.2.115 (vṛddhi U→au) →
    7.1.3 (3pl Je→ante), 7.2.81+6.1.66 (3du/2du ā→iy→i-lopa) →
    7.3.101 (1du/1pl sya-a→ā) → 6.1.78 (O→āv) → 6.1.87/6.1.97 →
    tripāḍī (8.3.59: s→ṣ after iṭ-i).

    Verified seṭ forms (bhū): भाविष्यते भाविष्येते भाविष्यन्ते
                               भाविष्यसे भाविष्येथे भाविष्यध्वे
                               भाविष्ये  भाविष्यावहे भाविष्यामहे
    """
    # ── Tag dhātu for bhāva/karma ──────────────────────────────────────────
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada ─────────────────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.3.13 lṛṭ śeṣe ca ───────────────────────────────────────────────
    state.meta["lakara"] = "lRT"
    state = apply_rule("3.3.3", state)
    state.meta["lfT_recipe"] = True
    state = apply_rule("3.3.13", state)
    state.meta.pop("lfT_recipe", None)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 3.4.77 + 3.4.78: ātmanepada tiṅ ādeśa ────────────────────────────
    tin_adesha = _select_tin_adesha("lRT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── 3.1.33 insert sya vikaraṇa ───────────────────────────────────────
    # Inserted BEFORE P00_tin_tusma so tiṅ is at index 2 (not 1) when 1.3.3
    # fires. This avoids a samjna_registry key collision for 1sg (tiṅ=iw):
    # if tiṅ were at index 1 during IT-lopa AND iṭ is later inserted at
    # index 1 by 6.4.62, both would generate ("it_halantyam", 1, "iw") → R2.
    state = apply_rule("3.1.33", state)

    # ── 3.4.114 mark sya ārdhadhātuka ────────────────────────────────────
    state = apply_rule("3.4.114", state)

    # ── IT-lopa on tiṅ ādeśa (tiṅ now at index 2 after sya insertion) ────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.79: ṭi→e on tiṅ ādeśa (skips TAs — handled by 3.4.80) ───────
    state = apply_rule("3.4.79", state)

    # ── 3.4.80: thās→se (2sg) ────────────────────────────────────────────
    state = apply_rule("3.4.80", state)

    # ── 6.4.62: ciṇvat iṭ before sya (bhāvakarmaṇa) ─────────────────────
    state = apply_rule("6.4.62", state)
    # IT-lopa on iṭ (T of iw is halantyam IT)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 1.2.4 sārvadhatuka apit → kṅit ───────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── 7.1.3 Ja→ante (3pl: Je→ante; vacuous for other cells) ────────────
    state = P00_jha_adesha(state)

    state = apply_rule("7.2.81", state)

    # ── 6.1.66 lopo vyorvali (drop y from iy before HAL) ─────────────────
    state = apply_rule("6.1.66", state)

    # ── 1.4.13 aṅga-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # ── 7.2.115 vṛddhi (ciṇvat arm set by 6.4.62) ─────────────────────────
    state = apply_rule("7.2.115", state)

    # ── 7.3.101 ato dīrgho yañi (1du/1pl: sya-a→ā before v/m) ────────────
    state = apply_rule("7.3.101", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.78 eco'yavāyāvaḥ (bhau+i → bhāv+i via O→Av) ─────────────────
    state = apply_rule("6.1.78", state)

    # ── 6.1.87 ādguṇaḥ (a+i→e: 3du sya-a+ite-i, 2du sya-a+iTe-i) ────────
    state = apply_rule("6.1.87", state)

    # ── 6.1.97 ato guṇe (a+a→a: 3pl; a+e→e pararūpa: 1sg) ────────────────
    state = apply_rule("6.1.97", state)

    # ── MERGE ─────────────────────────────────────────────────────────────
    state = _merge_pada(state)
    # ── TRIPĀḌĪ ───────────────────────────────────────────────────────────
    state = P00_tripadi_rutva_visarga(state)
    state = apply_rule("8.3.59", state)   # s→ṣ after iṭ-i (in sya: iṣya)
    state = apply_rule("8.4.68", state)

    return state


def _derive_karmani_loT(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani loṭ (passive imperative) for bhvādi dhātus.

    Key sūtras: 1.3.13 (ātmanepada), 3.3.162 (loṭ), 3.1.67 (yaḳ),
    3.4.79 (ṭi→e), 3.4.80 (thās→se), 3.4.90 (e→ām, non-uttama),
    3.4.91 (se→sva, dhve→dhvam), 3.4.93 (e→ai, uttama),
    3.4.92 (āṭ for uttama), 7.1.3 (J→ant for 3pl),
    7.2.81 (ā→iy for 3du/2du), 6.1.66 (y-lopa), 6.1.87 (a+i→e),
    6.1.90 (āṭ+ai→ai, 1sg), 6.1.88 (a+ai→ai), 6.1.101 (a+ā→ā, 1du/1pl).

    Verified forms (bhū): भूयताम् भूयेताम् भूयन्ताम्
                          भूयस्व  भूयेथाम् भूयध्वम्
                          भूयै    भूयावहै  भूयामहै
    """
    # ── Tag dhātu for bhāva/karma prayoga ──────────────────────────────────
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada in karmani ─────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.3.162 loṭ ca ────────────────────────────────────────────────────
    state.meta["loT_recipe"] = True
    state = apply_rule("3.3.162", state)
    state.meta.pop("3_3_162_loT_done", None)
    loT_varnas = parse_slp1_upadesha_sequence("loT")
    if loT_varnas and loT_varnas[-1].slp1 == "T":
        loT_varnas = loT_varnas[:-1]
    loT_term = Term(
        kind="pratyaya",
        varnas=loT_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "loT"},
    )
    state.terms.append(loT_term)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 3.4.77 lasya + 3.4.78 tiṅ ādeśa (ātmanepada, laT base) ──────────
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)

    # ── IT-prakaraṇa on tiṅ ādeśa ─────────────────────────────────────────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── 1.2.4 sārvadhatuka apit → kṅit ──────────────────────────────────
    state = apply_rule("1.2.4", state)

    state = _karmani_apply_yak(state)

    # ── 3.4.114 ārdhadhātuka śeṣa (vacuous trace) ─────────────────────────
    state = apply_rule("3.4.114", state)

    # ── 3.4.79: ṭita ātmanepada ṭere (ṭi → e) ────────────────────────────
    state = apply_rule("3.4.79", state)

    # ── 3.4.80: thāsasse (2sg: thAs → se) ────────────────────────────────
    state = apply_rule("3.4.80", state)

    # ── 3.4.90: āmeta (non-uttama: e → ām: te/Ate/Je/ATe → tAm/AtAm/JAm/ATAm)
    state = apply_rule("3.4.90", state)

    # ── 3.4.91: savābhyāṃ vāmau (2sg: se→sva; 2pl: Dve→Dvam) ────────────
    state.meta["loT_karmani_recipe"] = True
    state = apply_rule("3.4.91", state)
    state.meta.pop("loT_karmani_recipe", None)

    # ── 3.4.93: eta ai (uttama: terminal e → E/ai) ────────────────────────
    state = apply_rule("3.4.93", state)

    # ── 3.4.92: āḍuttamasya picca (attach āṭ before uttama tiṅ) ──────────
    state = apply_rule("3.4.92", state)
    # IT-prakaraṇa on āṭ only when 3.4.92 actually inserted it (uttama cells)
    if any("aTa_agama" in t.tags for t in state.terms):
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

    # ── 1.2.4 second pass (sārvadhatuka apit context) ─────────────────────
    state = apply_rule("1.2.4", state)

    # ── 1.4.13 aṅga-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # ── 1.1.5 kṅiti ca: block guṇa before yaḳ ────────────────────────────
    state = apply_rule("1.1.5", state)

    state = apply_rule("7.4.25", state)

    # ── 7.1.3: jho'ntaḥ (karmani 3pl: JAm → antAm) ───────────────────────
    state = P00_jha_adesha(state)

    state = apply_rule("7.2.81", state)

    # ── 6.1.66: lopo vyorvali (drop y from iy before HAL) ─────────────────
    state = apply_rule("6.1.66", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.87: ādguṇaḥ (3du/2du: ya-a + itAm/iTAm-i → yetAm/yeThAm) ───
    state = apply_rule("6.1.87", state)

    # ── 6.1.97: ato guṇe (3pl: delete ya-a before antAm-a, pararūpa) ─────
    state = apply_rule("6.1.97", state)

    # ── 6.1.90: āṭaśca (1sg: del āṭ-ā before ai; prereq for 6.1.88) ──────
    state = apply_rule("6.1.90", state)

    # ── 6.1.88: vṛddhireci (1sg: ya-a + E→E, ya becomes y) ───────────────
    state = apply_rule("6.1.88", state)

    # ── 6.1.101: akaḥ savarṇe dīrgha (1du/1pl: ya-a + āṭ-ā → yā) ────────
    state = apply_rule("6.1.101", state)

    # ── MERGE + TRIPĀḌĪ ───────────────────────────────────────────────────
    state = _merge_pada(state)
    state = P00_tripadi_rutva_visarga(state)
    state = apply_rule("8.4.68", state)

    return state


def _bootstrap_tinanta_derivation(
    row: dict,
    lakara: str,
    prayoga: str,
    *,
    upasargas: list[str] | None = None,
    pada: str | None = None,
    san_recipe: bool = False,
    nic_recipe: bool = False,
    purusha: int = 3,
    vacana: int = 1,
) -> tuple[State, int, str | None, bool]:
    """
    STAGE 0–2: dhātupātha → tape init → it-lopa → (kartari) pada-nirṇaya.

    Returns ``(state, gana, pada_key, complete)``.  When ``complete`` is True,
    ``state`` is the final derivation (nic/san early exit) and dispatch is skipped.
    """
    from engine.tape_init.tinanta import build_tinanta_recipe_state

    gana: int = row.get("gana", 1)
    state = build_tinanta_recipe_state(row, lakara, prayoga)
    state = P01_samjna_dhatu_class(state)
    state = P00_bhuvadi_dhatu_it_anunasik_hal(state)
    if gana == 10:
        # curādi: 3.1.25 ṇic svārthe, then the ṇijanta is a new dhātu (3.1.32)
        # conjugated with śap like any bhvādi root: चोरयति, ताडयति.
        state = _curadi_nic(state)
        gana = 1
    state = _attach_upasargas(state, upasargas)

    if nic_recipe and lakara == "laT":
        return _derive_laT_nic_atmane(state, purusha, vacana), gana, None, True

    if san_recipe and lakara == "laT":
        state.meta["san_recipe"] = "san"
        return _derive_laT_san_atmane(state, purusha, vacana), gana, None, True

    if prayoga == "kartari":
        state = apply_rule("1.3.28", state)
        state = apply_rule("1.3.12", state)
        state = apply_rule("1.3.19", state)  # विपराभ्यां जेः
        state = apply_rule("1.3.72", state)  # स्वरितञितः कर्त्रभिप्राये
        state = apply_rule("1.3.78", state)

    pada_key = pada if pada in ("parasmai", "atmane") else _resolve_pada_from_gate(state)
    return state, gana, pada_key, False


def _dispatch_tinanta_spine(
    state: State,
    *,
    gana: int,
    lakara: str,
    prayoga: str,
    pada_key: str,
    purusha: int,
    vacana: int,
) -> State:
    """
    STAGE 3+: lakāra/prayoga dispatch after bootstrap.

    Shared by ``derive()`` and ``derive_autonomous_tinanta()`` (Phase 5 M5).
    """
    if prayoga == "bhave":
        # भावकर्मणोः — bhāve and karmaṇi share one morphology: yak in the
        # sārvadhātuka lakāras (3.1.67 सार्वधातुके यक्), ātmanepada throughout
        # (1.3.13). So bhāve runs the karmaṇi spines after its own 3.4.69 gate.
        state = _prep_bhave(state)
        prayoga = "karmani"

    if prayoga == "karmani":
        if lakara == "laT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_laT(state, purusha, vacana)
        if lakara == "liT":
            # liṭ is ārdhadhātuka (3.4.115): no yak, so karmaṇi liṭ is the general
            # liṭ in ātmanepada (1.3.13) — ām-liṭ included: एधाञ्चक्रे, चोरयाञ्चक्रे.
            for t in state.terms:
                if "dhatu" in t.tags:
                    t.tags.add("bhava_karma_usage")
                    break
            state = apply_rule("1.3.13", state)
            prayoga, pada_key = "kartari", "atmane"
        if lakara == "luT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_luT(state, purusha, vacana)
        if lakara == "lRT":
            # sya is ārdhadhātuka: no yak (3.1.67 is sārvadhātuke only), so
            # karmaṇi/bhāve lṛṭ is the general lṛṭ in ātmanepada (करिष्यते).
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_lRT(state, "atmane", purusha, vacana)
        if lakara == "loT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_loT(state, purusha, vacana)
        if lakara == "laG":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_laG(state, purusha, vacana)
        if lakara == "liG":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_liG(state, purusha, vacana)
        if lakara == "AsIrliG":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_ashir_liG(state, purusha, vacana)
        if lakara == "luG":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            if (purusha, vacana) == (3, 1):
                return _derive_karmani_luG(state, purusha, vacana)   # 3.1.66 ciṇ (त only)
            # every other cell: sic, as in kartari — luṅ in ātmanepada (1.3.13)
            for t in state.terms:
                if "dhatu" in t.tags:
                    t.tags.add("bhava_karma_usage")
                    break
            state = apply_rule("1.3.13", state)
            return _derive_luG(state, "atmane", purusha, vacana)
        if lakara == "lRG":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            # sya is ārdhadhātuka: no yak — general lṛṅ in ātmanepada (अपक्ष्यत)
            return _derive_lRG(state, "atmane", purusha, vacana)
        if prayoga == "karmani":
            raise NotImplementedError(f"karmani prayoga for lakāra {lakara!r} not yet implemented")

    if lakara in ("liT",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lit_ad_gas(state, pada_key, purusha, vacana)

    if lakara in ("liT",) and _needs_am_lit(state):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lit_am(state, pada_key, purusha, vacana)

    if lakara in ("liT",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lit(state, pada_key, purusha, vacana)

    if lakara in ("luG",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_luG_ad(state, pada_key, purusha, vacana)

    if lakara in ("luG",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_luG(state, pada_key, purusha, vacana)

    if lakara in ("luT",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_luT_ad(state, pada_key, purusha, vacana)

    if lakara in ("luT",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        if pada_key == "atmane":
            return _derive_luT_atmane(state, purusha, vacana)
        return _derive_luT(state, pada_key, purusha, vacana)

    if lakara in ("AsIrliG",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_ashir_liG(state, pada_key, purusha, vacana)

    if lakara in ("AsIrliG",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        if pada_key == "atmane":
            return _derive_ashir_liG_atmane(state, purusha, vacana)
        return _derive_ashir_liG(state, pada_key, purusha, vacana)

    if lakara in ("liG",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_liG_ad(state, pada_key, purusha, vacana)

    if lakara in ("liG",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_liG(state, pada_key, purusha, vacana)

    if lakara in ("laG",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_laG(state, pada_key, purusha, vacana)

    if lakara in ("lRT",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lRT_ad(state, pada_key, purusha, vacana)

    if lakara in ("lRT",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lRT(state, pada_key, purusha, vacana)

    if lakara in ("lRG",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lRG_ad(state, pada_key, purusha, vacana)

    if lakara in ("lRG",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lRG(state, pada_key, purusha, vacana)

    if lakara in ("loT",) and _is_adadi_dhatu(state) and pada_key == "parasmai":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_loT_ad(state, pada_key, purusha, vacana)

    if lakara in ("loT",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_loT(state, pada_key, purusha, vacana)

    if lakara in ("laT",) and _is_adadi_dhatu(state) and pada_key == "parasmai":
        # P008's 2sg spine was proven only via अद् (stem=="ad"); 2.4.72 अदः
        # शपः is itself root-scoped so it stays a correct no-op for every
        # other gaṇa-2 root (अस्, दुह्, ब्रू…) resolved parasmaipada.
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_laT_adadi_kartari(state, purusha, vacana)

    if lakara in ("laT",) and _is_adadi_dhatu(state):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_laT_adadi(state, purusha, vacana)

    if lakara in ("laT",) and _yam_with_A_upasarga(state):
        return _derive_laT_yam_Anga(state, purusha, vacana)

    if lakara in ("laT",) and _jYA_apa_check(state):
        return _derive_laT_jYA_apa(state, purusha, vacana)

    if lakara in ("laT",) and _krI_with_upasarga_check(state):
        return _derive_laT_krI_sna_atmane(state, purusha, vacana)

    if lakara in ("laT",) and _kf_with_upasarga_check(state):
        return _derive_laT_kf_u_atmane(state, purusha, vacana)

    return _run_lat_kartari_bhuvadi_spine(
        state,
        gana=gana,
        lakara=lakara,
        pada_key=pada_key,
        purusha=purusha,
        vacana=vacana,
    )


def derive(
    dhatu_upadesha: str,
    lakara: str,
    prayoga: str,        # "kartari" | "karmani" | "bhave"
    purusha: int,        # 3 = prathama, 2 = madhyama, 1 = uttama
    vacana: int,         # 1 = eka, 2 = dvi, 3 = bahu
    *,
    upasargas: list[str] | None = None,
    pada: str | None = None,    # "parasmai" | "atmane" | None (auto-detect)
    san_recipe: bool = False,   # True → desiderative (sanādi) spine
    nic_recipe: bool = False,   # True → Ṇic causative spine
) -> State:
    """
    Derive a tiṅanta form via the Aṣṭādhyāyī.

    Parameters
    ----------
    dhatu_upadesha : SLP1 upadeśa string from dhātupātha (e.g. "BU", "pac", "kf").
    lakara         : SLP1 lakāra name (e.g. "laT", "liT", "loT", "laG").
    prayoga        : "kartari" | "karmani" | "bhave".
    pada           : Optional pada override "parasmai" | "atmane". When set, skips
                     the automatic 1.3.12/1.3.78 pada detection. Useful for ubhayapadi
                     roots where the context selects a specific pada (e.g. P018-B).
    purusha        : 3 (prathama), 2 (madhyama), 1 (uttama).
    vacana         : 1 (ekavacana), 2 (dvivacana), 3 (bahuvacana).

    Returns
    -------
    State with full glass-box trace in state.trace and surface in state.flat_dev().

    Example
    -------
    >>> s = derive("BU", "laT", "kartari", 3, 1)
    >>> s.flat_dev()
    'भवति'
    """
    if prayoga not in ("kartari", "karmani", "bhave"):
        raise ValueError(f"prayoga must be 'kartari'|'karmani'|'bhave', got {prayoga!r}")
    if purusha not in (1, 2, 3):
        raise ValueError(f"purusha must be 1/2/3, got {purusha!r}")
    if vacana not in (1, 2, 3):
        raise ValueError(f"vacana must be 1/2/3, got {vacana!r}")

    from engine.core_loop import derive_autonomous_tinanta

    return derive_autonomous_tinanta(
        dhatu_upadesha,
        lakara,
        prayoga,
        purusha,
        vacana,
        upasargas=upasargas,
        pada=pada,
        san_recipe=san_recipe,
        nic_recipe=nic_recipe,
    )


def derive_all_readings(*args, **kwargs) -> list:
    """Every legitimate surface this cell can produce, one per वा/विभाषा
    combination actually reached (``engine.vikalpa.explore``) — same
    arguments as ``derive()``. ``derive()`` itself still returns exactly one
    reading (the sūtras' own ``vibhasha_default``), so existing callers are
    unaffected; this is the opt-in for a caller that wants every branch, not
    just the default one (docs/FINAL_PLAN_2026-09.md item 6, "optional forms
    are still single-output").

    Returns a list of ``engine.vikalpa.Branch`` (``.surface_dev``,
    ``.surface_slp1``, ``.choices``, ``.state``); exactly one element when no
    वा rule was reached, matching ``derive()``'s own shape in that case.
    """
    from engine.vikalpa import explore
    return explore(lambda: derive(*args, **kwargs))


# ─────────────────────────────────────────────────────────────────────────────
# CONVENIENCE WRAPPERS — imported from tests/fixtures for backward compat.
# Phase 5: new tests should import from tests.fixtures.tinanta_paradigms.
# ─────────────────────────────────────────────────────────────────────────────
from tests.fixtures.tinanta_paradigms import (  # noqa: E402,F401
    derive_bhavati, derive_bhavataH, derive_bhavanti,
    derive_bhavasi, derive_bhavathah, derive_bhavatha,
    derive_bhavami, derive_bhavavah, derive_bhavamah,
    derive_bhavisyati, derive_bhavisyatah, derive_bhavisyanti,
    derive_bhavisyasi, derive_bhavisyathah, derive_bhavisyatha,
    derive_bhavisyami, derive_bhavisyavah, derive_bhavisyamah,
    derive_abhavat, derive_abhavataM, derive_abhavan,
    derive_abhavaH, derive_abhavataM2, derive_abhavata,
    derive_abhavam, derive_abhavaV, derive_abhavAma,
    derive_bhavet, derive_bhavetam, derive_bhaveyuH,
    derive_bhaveH, derive_bhavetam2, derive_bhaveta,
    derive_bhaveyam, derive_bhaveva, derive_bhavema,
    derive_bhuyat, derive_bhuyastam, derive_bhuyasuh,
    derive_bhuyah, derive_bhuyastam2, derive_bhuyasta,
    derive_bhuyasam, derive_bhuyasva, derive_bhuyasma,
    derive_abhut, derive_abhutam, derive_abhuvan,
    derive_abhuh, derive_abhutam2, derive_abhuta,
    derive_abhuvam, derive_abhuva, derive_abhuma,
    derive_abhavisyat, derive_abhavisyatam, derive_abhavisyan,
    derive_abhavisyah, derive_abhavisyatam2, derive_abhavisyata,
    derive_abhavisyam, derive_abhavisyav, derive_abhavisyam2,
)
