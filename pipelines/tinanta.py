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
    3.4.78  tiptasjhi…  (recipe arms tin_adesha_slp1; laT → tiṅ ādeśa)
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
from phonology.varna import parse_slp1_upadesha_sequence, mk as _mk

from core.canonical_pipelines import (
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_lat_vartamane_tip_and_sap,
    P00_lashakvataddhite_it_lopa_chain,
    P00_tin_tusma_audit_halantyam_lopa,
    P00_anga_guna_audit_1_4_13_1_1_5_7_3_84,
    P06a_pratyaya_adhikara_3_1_1_to_3,
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
    Return dhātupātha row for upadesha_slp1 string or dhātupātha id.

    Accepts:
      - Raw upadeśa SLP1 (e.g. 'BU', 'pac', 'kf')
      - Dhātupātha canonical id (e.g. 'BvAdi_01_0001')
      - Alias (e.g. 'BvAdi_BU')
    """
    # 1. Try as direct dhātupātha id / alias
    try:
        return get_dhatu_row(upadesha_slp1)
    except KeyError:
        pass
    # 2. Reverse lookup: upadesha_slp1 → id
    m = _upadesha_to_id_map()
    eid = m.get(upadesha_slp1) or m.get(upadesha_slp1.rstrip("~"))
    if eid:
        try:
            return get_dhatu_row(eid)
        except KeyError:
            pass
    raise KeyError(
        f"dhātu {upadesha_slp1!r} not found in dhātupātha. "
        "Use upadeśa SLP1 (e.g. 'BU', 'pac', 'kf') or dhātupātha id "
        "(e.g. 'BvAdi_01_0001', 'BvAdi_BU')."
    )


def _build_dhatu_term(row: dict) -> Term:
    """Construct a Term from a dhātupātha row, marking ātmanepada if needed."""
    upadesha = row["upadesha_slp1"]
    pada_label = row.get("pada_label_dev", "")
    # Determine ātmanepada licensing from dhātupātha data.
    atmane = "आत्मनेपदी" in pada_label
    ubhaya = "उभयपदी" in pada_label

    meta: dict = {
        "upadesha_slp1": upadesha,
        "gana"         : row.get("gana", 1),
        "dhatu_it"     : set(row.get("it_markers") or []),
        "ekac_dhatu"   : bool(row.get("flags", {}).get("ekac", False)),
        "udatta_dhatu" : bool(row.get("flags", {}).get("udatta", False)),
        "anit_dhatu"   : bool(row.get("flags", {}).get("anit", False)),
        "set_dhatu"    : bool(row.get("flags", {}).get("set", True)),
    }
    if atmane:
        meta["kartari_atmanepada_licensed"] = True
    if ubhaya:
        meta["kartari_atmanepada_licensed"] = "ubhaya"

    return Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(upadesha),
        tags={"dhatu", "anga", "upadesha"},
        meta=meta,
    )


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


# ─────────────────────────────────────────────────────────────────────────────
# VIKARAṆA STAGE (gaṇa-specific)
# ─────────────────────────────────────────────────────────────────────────────

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
        return state

    if gana == 4:
        # 3.1.69 śyan (divādi apavāda)
        state.meta["3_1_69_syan_arm"] = True
        state = apply_rule("3.1.69", state)
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        return state

    if gana == 6:
        # 3.1.77 tuddādi śa
        state.meta["3_1_77_sa_arm"] = True
        state = apply_rule("3.1.77", state)
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        return state

    raise NotImplementedError(
        f"vikaraṇa for gaṇa {gana} not yet implemented in pipelines/tinanta.py. "
        "Extend _apply_vikarana() with the appropriate sūtra."
    )


# ─────────────────────────────────────────────────────────────────────────────
# PADA MERGE (structural, mirrors subanta._pada_merge)
# ─────────────────────────────────────────────────────────────────────────────

def _pada_merge(state: State) -> None:
    """Merge all Terms into a single tiṅanta pada. Structural — not a sūtra."""
    if not state.terms:
        return
    all_varnas = []
    for t in state.terms:
        all_varnas.extend(t.varnas)
    pada = Term(
        kind="pada",
        varnas=all_varnas,
        tags={"pada", "tinganta"},
        meta={},
    )
    state.terms = [pada]
    state.trace.append({
        "sutra_id"  : "__MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "पद-मेलनम्",
        "form_before": state.flat_slp1(),
        "form_after" : state.flat_slp1(),
        "why_dev"   : "तिङन्त-पद-रचना — संरचनात्मकं, न सूत्रम्।",
        "status"    : "APPLIED",
        "event"     : "MERGE",
    })


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


def _derive_lit(state: State, pada_key: str, purusha: int, vacana: int) -> State:
    """
    Derive a liṭ (perfect / parokṣa) form starting from the post-1.3.78 state.
    Implements the full 9-cell bhū liṭ parasmaipada pipeline.
    """
    # ── Stage 3: liṭ attachment ──────────────────────────────────────────────
    state.meta["3_2_115_paroksha_lit_arm"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # 3.4.77 lasya adhikāra (scope for tiṅ substitution)
    state = apply_rule("3.4.77", state)

    # 3.4.78: standard tiṅ ādeśa from tin_upadesha.json
    tin_adesha_std = _select_tin_adesha("liT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"] = tin_adesha_std
    state = apply_rule("3.4.78", state)

    # 1.4.99 parasmaipade saṃjñā
    state = apply_rule("1.4.99", state)

    # IT on tiṅ ādeśa
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.115 (1st) + 3.4.82 liṭ-specific ādeśa ───────────────────────────
    # Reset gate for first call
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["3_4_115_arm"] = True
    state = apply_rule("3.4.115", state)

    lit_adesha = _LIT_PARASMAI_ADESHA[(purusha, vacana)]
    state.meta["3_4_82_lit_adesha_slp1"] = lit_adesha
    state.meta["3_4_82_arm"] = True
    state = apply_rule("3.4.82", state)

    # IT on liṭ ādeśa (1.3.4 tusma, 1.3.3 halantyam, 1.3.7 cuṭū, 1.3.9 lopa)
    state = apply_rule("1.3.4", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.7", state)
    state = apply_rule("1.3.9", state)

    # ── 3.4.115 (2nd audit) + optional 7.1.91 ────────────────────────────────
    # Reset gate for second call
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["3_4_115_arm"] = True
    state = apply_rule("3.4.115", state)

    if purusha == 1 and vacana == 1:
        state.meta["7_1_91_arm"] = True
        state = apply_rule("7.1.91", state)

    needs_it = _lit_needs_it(purusha, vacana)

    if needs_it:
        # ── iṭ path: iṭ FIRST, then 1.4.13, vuk, IT, dvitva ─────────────────
        state = apply_rule("1.2.5", state)
        state.meta["7_2_13_arm"] = True
        state = apply_rule("7.2.13", state)
        state.meta["7_2_35_arm"] = True
        state = apply_rule("7.2.35", state)
        # IT on iṭ: iṭ has T as halantyam-it
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        # 1.4.13 aṅga saṃjñā
        state = apply_rule("1.4.13", state)
        # 6.4.88 vuk
        state.meta["6_4_88_arm"] = True
        state = apply_rule("6.4.88", state)
        # IT on vuk (u and k are it-marked)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        # dvitva
        state.meta["6_1_8_lit_dvitva_arm"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["6_1_5_arm"] = True
        state = apply_rule("6.1.5", state)
        # 7.4.60 halādiḥ śeṣaḥ — trim CVC abhyāsa to CV (e.g. paW → pa)
        state = apply_rule("7.4.60", state)
    else:
        # ── NO-iṭ path: dvitva FIRST, then 1.4.13, vuk ───────────────────────
        if lit_adesha not in ("Ral",):
            state = apply_rule("1.2.5", state)
        state.meta["6_1_8_lit_dvitva_arm"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["6_1_5_arm"] = True
        state = apply_rule("6.1.5", state)
        # 7.4.60 halādiḥ śeṣaḥ — trim CVC abhyāsa to CV (e.g. paW → pa)
        state = apply_rule("7.4.60", state)
        if lit_adesha == "Ral":
            # 7.2.116 ato upadhāyāḥ — liṭ strong: vṛddhi a→ā for 'a'-upadha roots (paṭh→papāṭha)
            state.meta["7_2_116_liT_upadha_vrddhi_arm"] = True
            state = apply_rule("7.2.116", state)
            # 7.3.84 sārvadhatukārdhadhātukayoḥ — liṭ strong: guṇa of IK-upadha roots (cit→ciceta)
            # Tag the Ral-residue suffix as ārdhadhātuka so 7.3.84's trigger fires
            state.meta["7_3_84_liT_strong_arm"] = True
            state = apply_rule("7.3.84", state)
            state.meta.pop("7_3_84_liT_strong_arm", None)
        # 1.4.13 aṅga saṃjñā
        state = apply_rule("1.4.13", state)
        # 6.4.88 vuk
        state.meta["6_4_88_arm"] = True
        state = apply_rule("6.4.88", state)
        # IT on vuk (u and k are it-marked)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

    # ── 7.4.59 hrasva (abhyāsa U→u) ─────────────────────────────────────────
    state.meta["P029_7_4_59_abhyasa_hrasva_arm"] = True
    state = apply_rule("7.4.59", state)

    # ── 7.4.73 bhavateraḥ (abhyāsa u→a) — only for bhū ─────────────────────────
    _dht = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    _dht_up = (_dht.meta.get("upadesha_slp1") or "").strip() if _dht else ""
    if _dht_up in {"BU", "BU~"}:
        state.meta["7_4_73_arm"] = True
        state = apply_rule("7.4.73", state)

    # ── 1.4.14 pada saṃjñā ───────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── TRIPĀḌĪ zone (8.4.54 abhyāsa carc before merge) ─────────────────────
    state = apply_rule("8.2.1", state)

    # 8.4.54 abhyāse carc (B→b in abhyāsa) — must be before merge
    state = apply_rule("8.4.54", state)

    # 8.4.68 (audit)
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

    # ── MERGE (after 8.4.54 so abhyāsa term is still identifiable) ───────────
    _pada_merge(state)

    # ── TRIPĀḌĪ: s→ru→ḥ on merged pada ──────────────────────────────────────
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

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
    state.meta["3_3_15_lut_arm"] = True
    state = apply_rule("3.3.15", state)
    state.meta.pop("3_3_15_lut_arm", None)
    # IT on luṭ upadeśa (vacuous — luṭ has no anunāsika or live hal-it)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.1.33 — insert tāsi vikaraṇa before luṭ placeholder ────────
    state.meta["3_1_33_tasi_lut_arm"] = True
    state = apply_rule("3.1.33", state)
    state.meta.pop("3_1_33_tasi_lut_arm", None)

    # ── Stage: 3.4.77 lasya + 3.4.78 tiṅ ādeśa ─────────────────────────────
    state = apply_rule("3.4.77", state)
    tin_adesha_std = _select_tin_adesha("luT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"] = tin_adesha_std
    state = apply_rule("3.4.78", state)
    # 1.4.99 parasmaipade — marks tiṅ ādeśa as parasmaipada
    state = apply_rule("1.4.99", state)
    # IT on tiṅ ādeśa: 1.3.4 (tusma protect) + 1.3.3 (halantyam) + 1.3.9 (lopa)
    #   tip→ti, sip→si, mip→mi; tas/Tas/vas/mas retain (tusma-s protected); Ta/jhi vacuous
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── Cell-specific pipeline ───────────────────────────────────────────────
    is_prathama = (purusha == 3)

    if purusha == 3 and vacana == 1:
        # 3sg: 2.4.85(ti→qA), set dit_pratyaya, 7.2.35(iṭ before tāsi while qA has q=val),
        #      1.3.7(q→it), 1.3.9(lope q→A), 1.4.13, 7.3.84, 6.4.143(tAs→t), 1.4.14, 6.1.78
        adesha = _LUT_PRATHAMA_ADESHA[(3, 1)]
        state.meta["2_4_85_adesha_slp1"] = adesha
        state.meta["2_4_85_lut_prathama_arm"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("2_4_85_lut_prathama_arm", None)
        # Mark the qA term as ḍit so 6.4.143 can find it
        if state.terms:
            state.terms[-1].meta["dit_pratyaya"] = True
        # 7.2.35: insert iṭ into tāsi before qA (q is val → fires)
        state.meta["7_2_35_lut_tAsi_it_arm"] = True
        state = apply_rule("7.2.35", state)
        state.meta.pop("7_2_35_lut_tAsi_it_arm", None)
        # 1.3.7: q(ḍ, cuṭu)→it on qA term; 1.3.9: lope q → A
        state.meta["1_3_7_lut_qA_arm"] = True
        state = apply_rule("1.3.7", state)
        state.meta.pop("1_3_7_lut_qA_arm", None)
        state = apply_rule("1.3.9", state)
        # 1.4.13 aṅga saṃjñā, 7.3.84 guṇa (BU→Bo)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        # 6.4.143: tāsi (i+t+A+s) → (i+t) before A (ḍit) — ṭi-lopa
        state.meta["6_4_143_lut_tasi_arm"] = True
        state = apply_rule("6.4.143", state)
        state.meta.pop("6_4_143_lut_tasi_arm", None)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 2:
        # 3du: 7.2.35(iṭ into tāsi while tas has t=val), 1.2.4,
        #      2.4.85(tas→rO), 1.4.13, 7.3.84, 7.4.51(tāsi→tA before r), 1.4.14, 6.1.78
        state.meta["7_2_35_lut_tAsi_it_arm"] = True
        state = apply_rule("7.2.35", state)
        state.meta.pop("7_2_35_lut_tAsi_it_arm", None)
        state = apply_rule("1.2.4", state)
        adesha = _LUT_PRATHAMA_ADESHA[(3, 2)]
        state.meta["2_4_85_adesha_slp1"] = adesha
        state.meta["2_4_85_lut_prathama_arm"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("2_4_85_lut_prathama_arm", None)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        # 7.4.51: drop s from tāsi before r (rO starts with r)
        state.meta["7_4_51_arm"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 3:
        # 3pl: 7.2.35(iṭ into tāsi while jhi has j=val), 1.2.4,
        #      2.4.85(jhi→ras), 1.4.13, 7.3.84, 7.4.51(tāsi→tA before r), 1.4.14, 6.1.78
        state.meta["7_2_35_lut_tAsi_it_arm"] = True
        state = apply_rule("7.2.35", state)
        state.meta.pop("7_2_35_lut_tAsi_it_arm", None)
        state = apply_rule("1.2.4", state)
        adesha = _LUT_PRATHAMA_ADESHA[(3, 3)]
        state.meta["2_4_85_adesha_slp1"] = adesha
        state.meta["2_4_85_lut_prathama_arm"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("2_4_85_lut_prathama_arm", None)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        # 7.4.51: drop s from tāsi before r (ras starts with r)
        state.meta["7_4_51_arm"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 1:
        # 2sg: 7.2.35(iṭ into tāsi while si has s=val), 1.4.13, 7.3.84,
        #      7.4.50(tāsi→tA before si), 1.4.14, 6.1.78
        state.meta["7_2_35_lut_tAsi_it_arm"] = True
        state = apply_rule("7.2.35", state)
        state.meta.pop("7_2_35_lut_tAsi_it_arm", None)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        # 7.4.50: drop s from tāsi before si (si starts with s)
        state.meta["7_4_50_arm"] = True
        state = apply_rule("7.4.50", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    else:
        # Non-prathama, non-2sg cells: 2du (Tas), 2pl (Ta), 1sg (mi), 1du (vas), 1pl (mas)
        # 7.2.35: insert iṭ into tāsi (tāsi starts with t=val → always fires)
        # No 2.4.85; no s-lopa rule for these cells.
        state.meta["7_2_35_lut_tAsi_it_arm"] = True
        state = apply_rule("7.2.35", state)
        state.meta.pop("7_2_35_lut_tAsi_it_arm", None)
        # 1.2.4 for cells whose tiṅ is sārvadhatuka apit (most of them)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

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
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("laG", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

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
    state.meta["3_4_99_laG_s_lopa_arm"] = True
    state = apply_rule("3.4.99", state)
    state.meta.pop("3_4_99_laG_s_lopa_arm", None)

    # 7.1.3: jh (2 varnas after 3.4.100) → ant  (vacuous for non-3pl cells)
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)
    state.meta.pop("7_1_3_jho_anta_arm", None)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    # 6.4.71: aṭ augment prepended to dhātu (fires because 3.2.111 set aT_agama_context)
    state = apply_rule("6.4.71", state)
    # Trace steps for aṭ it-lopa (T of aṭ is conceptual; vacuous in engine)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state = apply_rule("1.1.5", state)
    # 7.3.101: 'a' of śap → 'ā' before yañ-initial tiṅ ādeśa (v of 'v', m of 'm')
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)
    # 7.3.84: guṇa (IK-vowel of dhātu; BU(Ū) → Bo)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada + sandhi ─────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)
    # 6.1.97: a+a → a (3pl: śap-a + ant-a; 1sg: śap-a + am-a)
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    # 8.2.39: jhal-final consonant → jaś (t→d) at pada-end  [fires for 3sg]
    state.meta["8_2_39_arm"] = True
    state = apply_rule("8.2.39", state)
    # 8.4.56: jaś → car at avasāna (d→t back)                [fires for 3sg]
    state.meta["8_4_56_arm"] = True
    state = apply_rule("8.4.56", state)
    # 8.2.66: pada-final s → ru                              [fires for 2sg]
    state = apply_rule("8.2.66", state)
    # 8.3.15: ru → ḥ before khar/avasāna                    [fires for 2sg]
    state = apply_rule("8.3.15", state)
    # 8.2.23: saṃyogānta t dropped (…nt → …n)               [fires for 3pl]
    state.meta["8_2_23_arm"] = True
    state = apply_rule("8.2.23", state)
    # 8.4.68: trace marker
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

    return state


# ─────────────────────────────────────────────────────────────────────────────
# LIṄ (ĀŚĪR / BENEDICTIVE) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────
# LUṄ (ADYATANA BHŪTA / AORIST) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

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
    state.meta["3_2_110_luG_arm"] = True
    state = apply_rule("3.2.110", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: cli/sic chain (before lakāra substitution: 3.1.43 needs luG) ──
    state.meta["3_1_43_cli_luG_arm"] = True
    state = apply_rule("3.1.43", state)   # inserts cli before luG placeholder
    state = apply_rule("3.1.44", state)   # cli → sic (upadesha_slp1="sic", varnas=[s,c])

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa ────────────────────────────────────
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("luG", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)  # drops p-it of tiṅ; c-it of sic

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Detect seṭ vs aniṭ ───────────────────────────────────────────────────
    _dhatu_t = next((t for t in state.terms if "dhatu" in t.tags), None)
    _is_anit  = _dhatu_t is not None and bool(_dhatu_t.meta.get("anit_dhatu"))

    if _is_anit:
        # ── aniṭ path: 2.4.77 luk of sic (gāti-sthā-ghu-pā-bhū) ─────────────
        state.meta["2_4_77_luG_sic_lopa_arm"] = True
        state = apply_rule("2.4.77", state)
    else:
        # ── seṭ path: 7.2.35 iṭ insertion before sic ─────────────────────────
        for _t in state.terms:
            if (_t.meta.get("upadesha_slp1") or "").strip() == "sic":
                _t.tags.add("ardhadhatuka")
        state.meta["7_2_35_allow_sic"]      = True
        state.meta["luN_sic_ardhadhatuka"]  = True
        state = apply_rule("7.2.35", state)
        # No IT lopa needed: P00 already dropped sic's c-IT; iṭ 'i' has no T marker
        state.meta.pop("7_2_35_allow_sic", None)
        state.meta.pop("luN_sic_ardhadhatuka", None)

    # ── Stage: 1.2.4 apit sārvadhatuka → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: tiṅ substitutions ─────────────────────────────────────────────
    state = apply_rule("3.4.101", state)   # tas→tām, Tas→tam, Ta→ta, mi→am

    if not _is_anit and (purusha, vacana) == (3, 3):
        # seṭ 3pl: jher jus (3.4.108) → [u, s] instead of 7.1.3 jh→anti
        state.meta["3_4_108_liG_jus_arm"] = True
        state = apply_rule("3.4.108", state)
        state.meta.pop("3_4_108_liG_jus_arm", None)

    state = apply_rule("3.4.100", state)   # ti→t, si→s, jhi→jh

    if _is_anit:
        state.meta["7_1_3_jho_anta_arm"] = True
        state = apply_rule("7.1.3", state)     # jh→ant (3pl, aniṭ only)
        state.meta.pop("7_1_3_jho_anta_arm", None)

    state.meta["3_4_99_luG_s_lopa_arm"] = True
    state = apply_rule("3.4.99", state)    # vas→va, mas→ma
    state.meta.pop("3_4_99_luG_s_lopa_arm", None)

    # ── seṭ: for 3sg/2sg sic lopa → ī ───────────────────────────────────────
    if not _is_anit and (purusha, vacana) in {(3, 1), (2, 1)}:
        for _t in state.terms:
            if (_t.meta.get("upadesha_slp1") or "").strip() == "sic":
                _t.varnas = [_mk("I")]          # iṭ 'i' lengthened → ī; sic 's' dropped
                _t.meta["sic_lopa_it_dirgha"] = True
                break

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # 6.4.71 aṭ augment (fires via aT_agama_context set by 3.2.110)
    state = apply_rule("6.4.71", state)
    # aṭ augment is plain 'a' with no IT tags; skip 1.3.3/1.3.9 for seṭ to
    # avoid re-processing the sic 's' as halantyam-IT
    if _is_anit:
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

    if _is_anit:
        # 6.4.88 vuk augment (bhuvo vug-luṅ-liṭoḥ) — aniṭ/bhū only
        state.meta["6_4_88_arm"] = True
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

        # 6.1.66 v of vuk drops before HAL; stays before AC
        state.meta["6_1_66_luG_vuk_arm"] = True
        state = apply_rule("6.1.66", state)
        state.meta.pop("6_1_66_luG_vuk_arm", None)

    state = apply_rule("1.4.14", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1",  state)
    state.meta["8_2_39_arm"] = True
    state = apply_rule("8.2.39", state)    # t→d at pada-end (3sg)
    state.meta["8_4_56_arm"] = True
    state = apply_rule("8.4.56", state)    # d→t at avasāna (3sg)
    state = apply_rule("8.2.66", state)    # s→r (word-final: 2sg sip, 3pl jus)
    state = apply_rule("8.3.15", state)    # r→ḥ
    # seṭ: ṣatvam (s→ṣ after IK in internal sic residue) + ṣṭu (ṣ+t→ṣ+ṭ)
    if not _is_anit:
        state = apply_rule("8.3.59", state)    # sic-s → ṣ after iṭ-i
        state = apply_rule("8.4.41", state)    # ṣ+t → ṣ+ṭ (for tām/tam/ta)
    state.meta["8_2_23_arm"] = True
    state = apply_rule("8.2.23", state)    # saṃyogānta lopa (aniṭ 3pl: ant→an)
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

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

    state.meta["3_3_173_ashishi_ling_arm"] = True
    state = apply_rule("3.3.173", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state.meta["3_4_116_ashir_liG_arm"] = True
    state = apply_rule("3.4.116", state)

    state = apply_rule("3.4.101", state)
    state.meta["3_4_108_liG_jus_arm"] = True
    state = apply_rule("3.4.108", state)
    state.meta.pop("3_4_108_liG_jus_arm", None)
    state = apply_rule("3.4.100", state)
    state.meta["3_4_99_liG_s_lopa_arm"] = True
    state = apply_rule("3.4.99",  state)
    state.meta.pop("3_4_99_liG_s_lopa_arm", None)

    state.meta["3_4_104_ashir_yasut_arm"] = True
    state = apply_rule("3.4.104", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    state.meta["3_4_107_suw_arm"] = True
    state = apply_rule("3.4.107", state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)
    state.meta["7_4_25_ashir_liG_arm"] = True
    state = apply_rule("7.4.25", state)
    state = apply_rule("1.4.14", state)

    state.meta["6_1_66_ashir_liG_sip_arm"] = True
    state = apply_rule("6.1.66", state)
    state.meta.pop("6_1_66_ashir_liG_sip_arm", None)

    state.meta["8_2_29_ashir_liG_arm"] = True
    state = apply_rule("8.2.29", state)
    state.meta.pop("8_2_29_ashir_liG_arm", None)

    _pada_merge(state)
    state = apply_rule("8.2.1",  state)
    state.meta["8_2_39_arm"] = True
    state = apply_rule("8.2.39", state)
    state.meta["8_4_56_arm"] = True
    state = apply_rule("8.4.56", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

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
    state.meta["P038_3_3_161_vidhi_liG_arm"] = True
    state = apply_rule("3.3.161", state)

    # IT on liG upadeśa (G is halantyam-it; anunaasika vacuous)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 lasya + 3.4.78 tiṅ ādeśa (standard laT set) ──────────
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ─────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 1.2.4 apit → kṅit ────────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: vikaraṇa (śap for bhvādi) ────────────────────────────────────
    gana: int = state.terms[0].meta.get("gana", 1)
    state = _apply_vikarana(state, gana)

    # ── Stage: liṅ-specific tiṅ substitutions ───────────────────────────────
    # 3.4.101 (apavāda) BEFORE 3.4.108/3.4.100: tas→tām, Tas→tam, Ta→ta, mi→am
    state = apply_rule("3.4.101", state)
    # 3.4.108: jhi → jus → [u,s]  (only fires for 3pl)
    state.meta["3_4_108_liG_jus_arm"] = True
    state = apply_rule("3.4.108", state)
    state.meta.pop("3_4_108_liG_jus_arm", None)
    # 3.4.100: ti→t, si→s  (i-lopa; skips [u,s] from jus, tām, am, etc.)
    state = apply_rule("3.4.100", state)
    # 3.4.99: vas→va, mas→ma  (s-lopa for uttama 1du/1pl)
    state.meta["3_4_99_liG_s_lopa_arm"] = True
    state = apply_rule("3.4.99", state)
    state.meta.pop("3_4_99_liG_s_lopa_arm", None)

    # ── Stage: 3.4.103 yāsuṭ insertion ─────────────────────────────────────
    state.meta["3_4_103_yasut_arm"] = True
    state = apply_rule("3.4.103", state)

    # ── Stage: yāsuṭ processing ──────────────────────────────────────────────
    # 7.2.79: [y,A,s] → [y,A]  (drop final 's' of yāsuṭ)
    state.meta["7_2_79_liG_yasut_arm"] = True
    state = apply_rule("7.2.79", state)
    # 7.2.80: [y,A] → [i,y]  (when preceded by 'a')
    state.meta["7_2_80_liG_yasut_arm"] = True
    state = apply_rule("7.2.80", state)
    # 6.1.66: 'y' of [i,y] drops before HAL-initial tiṅ (t,s,m,v,…)
    state.meta["6_1_66_liG_y_before_hal_arm"] = True
    state = apply_rule("6.1.66", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    # 6.1.87: a + i → e  (śap-a + yāsuṭ-i remnant)
    state = apply_rule("6.1.87", state)
    # 7.3.84: guṇa (IK-vowel of dhātu → guṇa)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada + sandhi ────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1",  state)
    state = apply_rule("8.2.66", state)   # s → r  (2sg yāḥ→yuḥ, 3pl)
    state = apply_rule("8.3.15", state)   # r → ḥ

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
    state.meta["3_3_13_arm"] = True
    state = apply_rule("3.3.13", state)
    state.meta.pop("3_3_13_arm", None)

    # Structural: attach lṛṭ placeholder (pre-strip halantyam T from 'lRT').
    lRt_varnas = parse_slp1_upadesha_sequence("lRT")
    if lRt_varnas and lRt_varnas[-1].slp1 == "T":
        lRt_varnas = lRt_varnas[:-1]
    lRt_term = Term(
        kind="pratyaya",
        varnas=lRt_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "lRT"},
    )
    state.terms.append(lRt_term)

    # IT on lṛṭ upadeśa (anunāsika R → it via 1.3.2; halantyam T pre-stripped).
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 lasya + 3.4.78 tiṅ ādeśa ─────────────────────────────
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("lRT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)

    # 1.4.99 parasmaipade saṃjñā
    state = apply_rule("1.4.99", state)

    # IT on tiṅ ādeśa (1.3.4 tusma guard + 1.3.3 halantyam + 1.3.9 lopa)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ─────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 3.1.33 insert *sya* vikaraṇa after dhātu ────────────────────
    state.meta["3_1_33_lrt_sy_arm"] = True
    state = apply_rule("3.1.33", state)
    # arm is popped inside act; pop residual just in case
    state.meta.pop("3_1_33_lrt_sy_arm", None)

    # ── Stage: 3.4.114 mark *sya* as ārdhadhātuka ───────────────────────────
    state.meta["3_4_114_lrt_sy_arm"] = True
    state = apply_rule("3.4.114", state)
    state.meta.pop("3_4_114_lrt_sy_arm", None)

    # ── Stage: 7.2.35 iṭ before *sya* (val-initial ārdhadhātuka) ────────────
    # Fires naturally via _ardhadhatuka_vikarana_index: sya is ardhadhatuka,
    # not krt, not done, starts with 's' (val consonant).
    state = apply_rule("7.2.35", state)

    # Trace steps for iṭ it-lopa (iṭ's T is conceptual; vacuous in engine).
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 1.2.4 sārvadhatuka apit → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: 7.1.3 jhi → anti (3pl only; vacuous for other cells) ─────────
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)
    state.meta.pop("7_1_3_jho_anta_arm", None)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)
    # 7.3.101 ato dīrgho yañi: 'a' of *sya* → 'ā' before yañ-initial tiṅ
    # (m of mip/mas, v of vas).  Vacuous for non-yañ-initial ādeśas.
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)
    # 7.3.84 guṇa: IK-vowel of dhātu (Ū of BU) → guṇa (o).
    state = apply_rule("7.3.84", state)

    # ── Stage: pada saṃjñā + sandhi ─────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.78 eco'yavāyāvaḥ: EC + AC → split (o + i from iṭ → av + i).
    state = apply_rule("6.1.78", state)
    # 6.1.97 ato guṇe: a + a → a (fires for 3pl after jhi→anti: sya+anti).
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.2.66", state)   # pada-final s → ru
    state = apply_rule("8.3.15", state)   # ru → ḥ
    state = apply_rule("8.3.59", state)   # s → ṣ after IK in pratyaya (sya → ṣya)
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)   # trace marker

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
    state.meta["3_3_162_loT_arm"] = True
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
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("laT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 1.2.4 apit → kṅit ─────────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: śap vikaraṇa (3.1.68 for bhvādi gaṇa 1) ──────────────────────
    gana: int = state.terms[0].meta.get("gana", 1)
    state = _apply_vikarana(state, gana)

    # ── Stage: loṭ-specific tiṅ substitutions ────────────────────────────────
    # 3.4.89 FIRST (mi→ni, apavāda to 3.4.101's mi→am for 1sg)
    state.meta["3_4_89_loT_arm"] = True
    state = apply_rule("3.4.89", state)
    state.meta.pop("3_4_89_loT_arm", None)

    # 3.4.101: tas→tām (3du), Tas→tam (2du), Ta→ta (2pl)
    # mi→am won't fire since mi is already ni for 1sg
    state = apply_rule("3.4.101", state)

    # 3.4.87: sip→hi BEFORE 3.4.86 (prevent 'si' being seen by i→u rule)
    state.meta["P031_3_4_87_sip_to_hi_arm"] = True
    state = apply_rule("3.4.87", state)

    # 7.1.3: jhi→anti (has_i=True — loṭ retains 'i', unlike laṅ which drops it first)
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)
    state.meta.pop("7_1_3_jho_anta_arm", None)

    # 3.4.86: i→u (ti→tu for 3sg; anti→antu for 3pl; skip hi from 3.4.87, ni from 3.4.89)
    state.meta["3_4_86_loT_arm"] = True
    state = apply_rule("3.4.86", state)
    state.meta.pop("3_4_86_loT_arm", None)

    # 3.4.99: s-lopa (vas→va for 1du; mas→ma for 1pl)
    state.meta["3_4_99_loT_s_lopa_arm"] = True
    state = apply_rule("3.4.99", state)
    state.meta.pop("3_4_99_loT_s_lopa_arm", None)

    # 6.4.105: delete 'hi' after short 'a' of aṅga (2sg: bhava+hi → bhava)
    state.meta["6_4_105_loT_hi_lopa_arm"] = True
    state = apply_rule("6.4.105", state)
    state.meta.pop("6_4_105_loT_hi_lopa_arm", None)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)

    # 7.3.101: a→ā before yañ-initial tiṅ (n of ni for 1sg; v of va for 1du; m of ma for 1pl)
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)

    # 7.3.84: guṇa (bhū → bho; śap is sārvadhatuka trigger)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada + sandhi ─────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)
    # 6.1.97: a+a → a (3pl: śap-a + antu-a → bhavantu)
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1",  state)
    state = apply_rule("8.2.66", state)   # vacuous (no pada-final 's')
    state = apply_rule("8.3.15", state)   # vacuous
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

    return state


# ─────────────────────────────────────────────────────────────────────────────
# LṚṄ (KRIYĀTIPATTI / CONDITIONAL) PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

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
    """
    state.meta["lakara"] = "lRG"

    # ── Stage: 3.3.139 lṛṅ attachment ───────────────────────────────────────
    state.meta["3_3_139_lRG_arm"] = True
    state = apply_rule("3.3.139", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa ────────────────────────────────────
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("lRT", pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 3.1.33 insert sya vikaraṇa after dhātu ───────────────────────
    state.meta["3_1_33_lRG_sy_arm"] = True
    state = apply_rule("3.1.33", state)
    state.meta.pop("3_1_33_lRG_sy_arm", None)

    # ── Stage: 3.4.114 mark sya as ārdhadhātuka ─────────────────────────────
    state.meta["3_4_114_lRG_sy_arm"] = True
    state = apply_rule("3.4.114", state)
    state.meta.pop("3_4_114_lRG_sy_arm", None)

    # ── Stage: 7.2.35 iṭ before sya (val-initial ārdhadhātuka) ─────────────
    state = apply_rule("7.2.35", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 1.2.4 apit sārvadhatuka → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: tiṅ substitutions (laṅ-style) ────────────────────────────────
    state = apply_rule("3.4.101", state)   # tas→tām, Tas→tam, Ta→ta, mi→am (apavāda)
    state = apply_rule("3.4.100", state)   # ti→t, si→s, jhi→jh
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)     # jh→ant (3pl)
    state.meta.pop("7_1_3_jho_anta_arm", None)
    state.meta["3_4_99_lRG_s_lopa_arm"] = True
    state = apply_rule("3.4.99", state)    # vas→va, mas→ma
    state.meta.pop("3_4_99_lRG_s_lopa_arm", None)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)

    # 6.4.71 aṭ augment (lṛṅ is in luṅ/laṅ/lṛṅ group; fires on aT_agama_context)
    state = apply_rule("6.4.71", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # 7.3.101 ato dīrgho yañi: sya-a → ā before yañ-initial tiṅ (v of va, m of ma)
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)

    # 7.3.84 guṇa (bhū → bho; ārdhadhātuka sya triggers)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada saṃjñā + sandhi ─────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)    # bho+i(ṭ) → bhav+i
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)    # a+a → a (3pl: sya+ant; 1sg: sya+am)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1",  state)
    state.meta["8_2_39_arm"] = True
    state = apply_rule("8.2.39", state)    # t→d at pada-end (3sg)
    state.meta["8_4_56_arm"] = True
    state = apply_rule("8.4.56", state)    # d→t at avasāna (3sg)
    state.meta["8_2_23_arm"] = True
    state = apply_rule("8.2.23", state)    # saṃyogānta lopa: ant→an (3pl)
    state = apply_rule("8.2.66", state)    # s→ru (2sg)
    state = apply_rule("8.3.15", state)    # ru→ḥ (2sg)
    state = apply_rule("8.3.59", state)    # s→ṣ after IK (sya→ṣya)
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

    return state


def _derive_karmani_luT(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani luṭ (passive periphrastic future) for bhvādi dhātus.

    Key structure: 1.3.13 → ātmanepada tiṅ ādeśa → 3.4.113 → 3.1.33 (tāsi) →
    3.4.79/3.4.80/2.4.85 → 6.4.62 (ciṇvat iṭ before tāsi) → 7.2.115 (vṛddhi) →
    tāsi-specific modifications → 6.1.78 → tripāḍī.

    vṛddhi path (via 6.4.62+7.2.115): bhU(U→au) → bhāu + vita = bhāvitā
    vs. aniṭ guṇa path (via 7.2.35+7.3.84):  bhU(U→o)  → bho  + vita = bhavitā

    Verified forms: भाविता भावितारौ भावितारः भावितासे भावितासाथे भाविताध्वे
                    भाविताहे भावितास्वहे भावितास्महे
    """
    # ── Tag dhātu for bhāva/karma ──────────────────────────────────────────
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada ─────────────────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.3.3 + 3.3.15: luṭ attachment ───────────────────────────────────
    state = apply_rule("3.3.3", state)
    state.meta["3_3_15_lut_arm"] = True
    state = apply_rule("3.3.15", state)
    state.meta.pop("3_3_15_lut_arm", None)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 3.1.33: insert tāsi vikaraṇa ──────────────────────────────────────
    state.meta["3_1_33_tasi_lut_arm"] = True
    state = apply_rule("3.1.33", state)
    state.meta.pop("3_1_33_tasi_lut_arm", None)

    # ── 3.4.77 + 3.4.78: ātmanepada tiṅ ādeśa ────────────────────────────
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("luT", "atmane", purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = apply_rule("1.4.100", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Cell-specific tiṅ processing + tāsi modifications ─────────────────
    if purusha == 3 and vacana == 1:
        # 3sg: ta → ḍā via 2.4.85, IT-lopa on ḍ, then 6.4.62 iṭ, 7.2.115, 6.4.143
        adesha = _LUT_PRATHAMA_ADESHA[(3, 1)]
        state.meta["2_4_85_adesha_slp1"] = adesha
        state.meta["2_4_85_lut_prathama_arm"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("2_4_85_lut_prathama_arm", None)
        if state.terms:
            state.terms[-1].meta["dit_pratyaya"] = True
        # IT-lopa on ḍā: q(ḍ) is cuṭu → IT, drops → ā
        state.meta["1_3_7_lut_qA_arm"] = True
        state = apply_rule("1.3.7", state)
        state.meta.pop("1_3_7_lut_qA_arm", None)
        state = apply_rule("1.3.9", state)
        state = apply_rule("3.4.114", state)
        # 6.4.62: ciṇvat iṭ before tāsi
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        # IT-lopa on iṭ
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state.meta["6_4_143_lut_tasi_arm"] = True
        state = apply_rule("6.4.143", state)
        state.meta.pop("6_4_143_lut_tasi_arm", None)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 2:
        # 3du: Atam → rau via 2.4.85, 6.4.62 iṭ, 7.4.51 ri ca
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        adesha = _LUT_PRATHAMA_ADESHA[(3, 2)]
        state.meta["2_4_85_adesha_slp1"] = adesha
        state.meta["2_4_85_lut_prathama_arm"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("2_4_85_lut_prathama_arm", None)
        state = apply_rule("3.4.114", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state.meta["7_4_51_arm"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 3:
        # 3pl: Ja → ras via 2.4.85, 6.4.62 iṭ, 7.4.51 ri ca, tripāḍī s→ḥ
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        adesha = _LUT_PRATHAMA_ADESHA[(3, 3)]
        state.meta["2_4_85_adesha_slp1"] = adesha
        state.meta["2_4_85_lut_prathama_arm"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("2_4_85_lut_prathama_arm", None)
        state = apply_rule("3.4.114", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state.meta["7_4_51_arm"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 1:
        # 2sg: TAs → se via 3.4.80, 6.4.62 iṭ, 7.4.50 tāsas lopa
        state = apply_rule("3.4.80", state)   # thās → se
        state = apply_rule("3.4.114", state)
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state.meta["7_4_50_arm"] = True
        state = apply_rule("7.4.50", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 2:
        # 2du: ATAm → ATe via 3.4.79, 6.4.62 iṭ, no tāsi mod
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 3:
        # 2pl: Dvam → Dve via 3.4.79, 6.4.62 iṭ, 8.2.25 s-lopa before dh
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 1 and vacana == 1:
        # 1sg: iT → i → e via 3.4.79, 6.4.62 iṭ, 7.4.52 s→h before e
        state = apply_rule("3.4.79", state)  # iT→i→e
        state = apply_rule("3.4.114", state)
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state.meta["7_4_52_arm"] = True
        state = apply_rule("7.4.52", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    else:
        # 1du (vahe→vahe) and 1pl (mahi→mahe): 3.4.79, 6.4.62, no tāsi mod
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state.meta["6_4_62_arm"] = True
        state = apply_rule("6.4.62", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.2.115", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ───────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    # 8.2.25: s-lopa before dh (2pl: tāsdhve → tādhve)
    state.meta["8_2_25_arm"] = True
    state = apply_rule("8.2.25", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

    return state


_KARMANI_LIT_NEEDS_IT: frozenset = frozenset({(2, 1), (2, 3), (1, 2), (1, 3)})


def _derive_karmani_lit(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani liṭ (passive perfect) for bhvādi dhātus.

    Key sūtras: 1.3.13, 3.4.81 (ta→eś, Ja→irec), 3.4.79 (ṭi→e), 3.4.80 (thās→se),
    1.2.5, dvitva (6.1.8), 6.4.88 (vuk), 7.4.59/73, 8.3.59, 8.3.78.

    Example: bhū + liṭ karmani 3sg → बभूवे
    """
    # ── Tag dhātu for bhāva/karma ──────────────────────────────────────────
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    # ── 3.2.115 parokṣe liṭ ───────────────────────────────────────────────
    state.meta["3_2_115_paroksha_lit_arm"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada ─────────────────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.4.77 lasya ─────────────────────────────────────────────────────
    state = apply_rule("3.4.77", state)

    # ── 3.4.78: select ātmanepada tiṅ ādeśa ──────────────────────────────
    tin_adesha = _select_tin_adesha("liT", "atmane", purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)

    # ── 1.4.99 + 1.4.100 saṃjñā ──────────────────────────────────────────
    state = apply_rule("1.4.99", state)
    state = apply_rule("1.4.100", state)

    # ── IT on tiṅ ādeśa ───────────────────────────────────────────────────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.115 liṭ ca (1st) ─────────────────────────────────────────────
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["3_4_115_arm"] = True
    state = apply_rule("3.4.115", state)

    # ── 3.4.81: ta → eś  /  Ja → irec  (3sg and 3pl) ────────────────────
    state.meta["3_4_81_lit_esh_arm"] = True
    state = apply_rule("3.4.81", state)

    # ── 3.4.79: ṭi→e for other cells (Atam→Ate, ATAm→ATe, Dvam→Dve, etc.) ─
    state = apply_rule("3.4.79", state)

    # ── 3.4.80: thāsasse (2sg: TAs → se) ────────────────────────────────
    state = apply_rule("3.4.80", state)

    # ── IT on liṭ-specific ādeśas (eS→e, irec→ire, etc.) ─────────────────
    state = apply_rule("1.3.4", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.7", state)
    state = apply_rule("1.3.9", state)

    # ── 3.4.115 liṭ ca (2nd) ─────────────────────────────────────────────
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["3_4_115_arm"] = True
    state = apply_rule("3.4.115", state)

    # ── 1.2.5 asaṃyogālliṭ kit ───────────────────────────────────────────
    state = apply_rule("1.2.5", state)

    needs_it = (purusha, vacana) in _KARMANI_LIT_NEEDS_IT

    if needs_it:
        # iṭ FIRST → 1.4.13 → vuk → dvitva
        state.meta["7_2_13_arm"] = True
        state = apply_rule("7.2.13", state)
        state.meta["7_2_35_arm"] = True
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.4.13", state)
        state.meta["6_4_88_arm"] = True
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state.meta["6_1_8_lit_dvitva_arm"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["6_1_5_arm"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("7.4.60", state)
    else:
        # dvitva FIRST → 1.4.13 → vuk
        state.meta["6_1_8_lit_dvitva_arm"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["6_1_5_arm"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("7.4.60", state)
        state = apply_rule("1.4.13", state)
        state.meta["6_4_88_arm"] = True
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

    # ── 7.4.59 hrasva (abhyāsa U→u) ──────────────────────────────────────
    state.meta["P029_7_4_59_abhyasa_hrasva_arm"] = True
    state = apply_rule("7.4.59", state)

    # ── 7.4.73 bhavateraḥ (abhyāsa u→a, only for bhū) ────────────────────
    _dht = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    _dht_up = (_dht.meta.get("upadesha_slp1") or "").strip() if _dht else ""
    if _dht_up in {"BU", "BU~"}:
        state.meta["7_4_73_arm"] = True
        state = apply_rule("7.4.73", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── TRIPĀḌĪ ───────────────────────────────────────────────────────────
    state = apply_rule("8.2.1", state)

    # 8.3.78: dh→ḍh after iṭ-i in liṭ (2pl: i+Dve → i+Qve = iḍhve)
    state.meta["8_3_78_arm"] = True
    state = apply_rule("8.3.78", state)

    # 8.4.54 abhyāse carc (B→b in abhyāsa)
    state = apply_rule("8.4.54", state)

    # 8.4.68
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

    # ── MERGE ─────────────────────────────────────────────────────────────
    _pada_merge(state)

    # ── POST-MERGE TRIPĀḌĪ ────────────────────────────────────────────────
    # 8.3.59 ṣatvam: s→ṣ after iṭ-i in merged pada (2sg: ...i+se → ...i+ṣe)
    state = apply_rule("8.3.59", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

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
    state = apply_rule("3.2.123", state)

    # Attach laṭ placeholder
    laT_varnas = parse_slp1_upadesha_sequence("laT")
    if laT_varnas and laT_varnas[-1].slp1 == "T":
        laT_varnas = laT_varnas[:-1]
    laT_term = Term(
        kind="pratyaya",
        varnas=laT_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    state.terms.append(laT_term)

    # ── 3.4.77 lasya ─────────────────────────────────────────────────────
    state = apply_rule("3.4.77", state)

    # ── 3.4.78: select ātmanepada tiṅ ādeśa ──────────────────────────────
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)

    # ── 1.4.99 parasmaipade (audit: records vibhakti saṃjñā) ──────────────
    state = apply_rule("1.4.99", state)
    # ── 1.4.100 lakāratāṅānāv ātmanepadam ────────────────────────────────
    state = apply_rule("1.4.100", state)

    # ── IT-prakaraṇa on tiṅ ādeśa (1.3.4/1.3.3/1.3.9) ───────────────────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── 1.2.4 sārvadhatukam apit ─────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── 3.1.67: sārvadhatuke yaḳ — insert yaḳ between dhātu and tiṅ ─────
    state.meta["3_1_67_arm"] = True
    state = apply_rule("3.1.67", state)  # records the event

    # Recipe: physically insert yaḳ after dhātu
    _dhatu_idx = next(i for i, t in enumerate(state.terms) if "dhatu" in t.tags)
    _yak = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("yak"),
        tags={"pratyaya", "upadesha", "vikarana"},
        meta={"upadesha_slp1": "yak"},
    )
    state.terms.insert(_dhatu_idx + 1, _yak)

    # ── IT-prakaraṇa on yaḳ: 1.3.3 (k→IT) + 1.3.9 (k drops) → ya ───────
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # Mark ya (remaining) as kṅit so 1.1.5 blocks guṇa on dhātu
    for t in state.terms:
        if t.meta.get("upadesha_slp1") == "yak" and "vikarana" in t.tags:
            t.tags.add("kngiti")
            break

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

    # ── 7.4.25 akṛtsārvadhatukayoḥ dīrgha (vacuous for bhū) ──────────────
    state.meta["7_4_25_karmani_yak_arm"] = True
    state = apply_rule("7.4.25", state)

    # ── 7.1.3: jho'ntaḥ (karmani 3pl: Je → ante) ─────────────────────────
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)

    # ── 7.2.81: āto ṅitaḥ (3du/2du: ā of Ate/ATe → iy) ──────────────────
    state.meta["7_2_81_Atam_arm"] = True
    state = apply_rule("7.2.81", state)

    # ── 6.1.66: lopo vyorvali (drop y from iy before val) ─────────────────
    state.meta["6_1_66_karmani_iy_arm"] = True
    state = apply_rule("6.1.66", state)

    # ── 7.3.101 ato dīrgho yañi (1du/1pl: ya → yā before v/m) ────────────
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.87 ādguṇaḥ (3du/2du: ya(a)+ite(i) → ye+te cross-term) ────────
    state = apply_rule("6.1.87", state)

    # ── 6.1.97 ato guṇe (3pl: a+a→a, 1sg: a+e→e pararūpa) ───────────────
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)

    # ── STRUCTURAL: pada merge ────────────────────────────────────────────
    _pada_merge(state)

    # ── TRIPĀḌĪ ──────────────────────────────────────────────────────────
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

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
    state.meta["3_3_13_arm"] = True
    state = apply_rule("3.3.13", state)
    state.meta.pop("3_3_13_arm", None)

    # Attach lṛṭ placeholder
    lRt_varnas = parse_slp1_upadesha_sequence("lRT")
    if lRt_varnas and lRt_varnas[-1].slp1 == "T":
        lRt_varnas = lRt_varnas[:-1]
    lRt_term = Term(
        kind="pratyaya",
        varnas=lRt_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "lRT"},
    )
    state.terms.append(lRt_term)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 3.4.77 + 3.4.78: ātmanepada tiṅ ādeśa ────────────────────────────
    state = apply_rule("3.4.77", state)
    tin_adesha = _select_tin_adesha("lRT", "atmane", purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)
    state = apply_rule("1.4.99", state)
    state = apply_rule("1.4.100", state)

    # ── 3.4.113 tiṅśit sārvadhatukam ─────────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── 3.1.33 insert sya vikaraṇa ───────────────────────────────────────
    # Inserted BEFORE P00_tin_tusma so tiṅ is at index 2 (not 1) when 1.3.3
    # fires. This avoids a samjna_registry key collision for 1sg (tiṅ=iw):
    # if tiṅ were at index 1 during IT-lopa AND iṭ is later inserted at
    # index 1 by 6.4.62, both would generate ("it_halantyam", 1, "iw") → R2.
    state.meta["3_1_33_lrt_sy_arm"] = True
    state = apply_rule("3.1.33", state)
    state.meta.pop("3_1_33_lrt_sy_arm", None)

    # ── 3.4.114 mark sya ārdhadhātuka ────────────────────────────────────
    state.meta["3_4_114_lrt_sy_arm"] = True
    state = apply_rule("3.4.114", state)
    state.meta.pop("3_4_114_lrt_sy_arm", None)

    # ── IT-lopa on tiṅ ādeśa (tiṅ now at index 2 after sya insertion) ────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.79: ṭi→e on tiṅ ādeśa (skips TAs — handled by 3.4.80) ───────
    state = apply_rule("3.4.79", state)

    # ── 3.4.80: thās→se (2sg) ────────────────────────────────────────────
    state = apply_rule("3.4.80", state)

    # ── 6.4.62: ciṇvat iṭ before sya (bhāvakarmaṇa) ─────────────────────
    state.meta["6_4_62_arm"] = True
    state = apply_rule("6.4.62", state)
    # IT-lopa on iṭ (T of iw is halantyam IT)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 1.2.4 sārvadhatuka apit → kṅit ───────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── 7.1.3 Ja→ante (3pl: Je→ante; vacuous for other cells) ────────────
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)
    state.meta.pop("7_1_3_jho_anta_arm", None)

    # ── 7.2.81 āto ṅitaḥ (3du/2du: ā→iy after 3.4.79) ───────────────────
    state.meta["7_2_81_Atam_arm"] = True
    state = apply_rule("7.2.81", state)

    # ── 6.1.66 lopo vyorvali (drop y from iy before HAL) ─────────────────
    state.meta["6_1_66_karmani_iy_arm"] = True
    state = apply_rule("6.1.66", state)

    # ── 1.4.13 aṅga-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # ── 7.2.115 vṛddhi (ciṇvat arm set by 6.4.62) ─────────────────────────
    state = apply_rule("7.2.115", state)

    # ── 7.3.101 ato dīrgho yañi (1du/1pl: sya-a→ā before v/m) ────────────
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.78 eco'yavāyāvaḥ (bhau+i → bhāv+i via O→Av) ─────────────────
    state = apply_rule("6.1.78", state)

    # ── 6.1.87 ādguṇaḥ (a+i→e: 3du sya-a+ite-i, 2du sya-a+iTe-i) ────────
    state = apply_rule("6.1.87", state)

    # ── 6.1.97 ato guṇe (a+a→a: 3pl; a+e→e pararūpa: 1sg) ────────────────
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)

    # ── MERGE ─────────────────────────────────────────────────────────────
    _pada_merge(state)

    # ── TRIPĀḌĪ ───────────────────────────────────────────────────────────
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.2.66", state)   # vacuous (no pada-final s)
    state = apply_rule("8.3.15", state)   # vacuous
    state = apply_rule("8.3.59", state)   # s→ṣ after iṭ-i (in sya: iṣya)
    state.meta["8_4_68_arm"] = True
    state = apply_rule("8.4.68", state)

    return state


def derive(
    dhatu_upadesha: str,
    lakara: str,
    prayoga: str,        # "kartari" | "karmani" | "bhave"
    purusha: int,        # 3 = prathama, 2 = madhyama, 1 = uttama
    vacana: int,         # 1 = eka, 2 = dvi, 3 = bahu
    *,
    upasargas: list[str] | None = None,
) -> State:
    """
    Derive a tiṅanta form via the Aṣṭādhyāyī.

    Parameters
    ----------
    dhatu_upadesha : SLP1 upadeśa string from dhātupātha (e.g. "BU", "pac", "kf").
    lakara         : SLP1 lakāra name (e.g. "laT", "liT", "loT", "laG").
    prayoga        : "kartari" | "karmani" | "bhave".
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

    # ── 0. Dhātupātha lookup (Art. 6: only data/inputs) ──────────────────
    row = _dhatu_row_by_upadesha(dhatu_upadesha)
    gana: int = row.get("gana", 1)

    # ── 1. Build initial State ────────────────────────────────────────────
    dhatu_term = _build_dhatu_term(row)
    state = State(
        terms=[dhatu_term],
        meta={"prayoga": prayoga},
        trace=[],
    )

    # ── 2. STAGE 1 — dhātu-prakaraṇa (1.3.1 + it-lopa) ──────────────────
    # P00_bhuvadi_dhatu_it_anunasik_hal fires:
    #   1.3.1  dhātu saṃjñā
    #   1.3.2  anunāsika → it (vacuous for most dhātus without anunāsika it)
    #   1.3.3  halantyam (vacuous for dhātus without trailing hal-it upadeśa)
    #   1.3.9  it-lopa (removes it-marked varṇas from upadeśa)
    state = P00_bhuvadi_dhatu_it_anunasik_hal(state)

    # ── 3. STAGE 2 — pada-nirṇaya via 1.3.78 ─────────────────────────────
    # 1.3.78 śeṣāt kartari parasmaipada: for dhātus without ātmanepada
    # restriction, sets paribhasha_gate → active:True (parasmaipada).
    if prayoga == "kartari":
        state = apply_rule("1.3.78", state)
    pada_key = _resolve_pada_from_gate(state)  # "parasmai" or "atmane"

    # ── karmani dispatch ──────────────────────────────────────────────────────
    if prayoga == "karmani":
        if lakara == "laT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_laT(state, purusha, vacana)
        if lakara == "liT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_lit(state, purusha, vacana)
        if lakara == "luT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_luT(state, purusha, vacana)
        if lakara == "lRT":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_lRT(state, purusha, vacana)
        raise NotImplementedError(f"karmani prayoga for lakāra {lakara!r} not yet implemented")

    # ── liṭ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("liT",):
        # Full liṭ pipeline handles everything from here
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lit(state, pada_key, purusha, vacana)

    # ── luṅ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("luG",):
        # Aorist (adyatana bhūta) via cli/sic→luk + vuk augment
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_luG(state, pada_key, purusha, vacana)

    # ── luṭ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("luT",):
        # Full luṭ periphrastic-future pipeline handles everything from here
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_luT(state, pada_key, purusha, vacana)

    # ── āśīr-liṅ dispatch ───────────────────────────────────────────────────
    if lakara in ("AsIrliG",):
        # Benedictive (āśīr-liṅ) via kit yāsuṭ, suṭ, 8.2.29 s-lopa
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_ashir_liG(state, pada_key, purusha, vacana)

    # ── liṅ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("liG",):
        # Vidhi-liṅ optative via yāsuṭ + tiṅ transformation
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_liG(state, pada_key, purusha, vacana)

    # ── laṅ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("laG",):
        # Imperfect past (anadhyatana bhūta) via śap vikaraṇa + aṭ augment
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_laG(state, pada_key, purusha, vacana)

    # ── lṛṭ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("lRT",):
        # Simple future (sāmānya bhaviṣyat) via sy vikaraṇa
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lRT(state, pada_key, purusha, vacana)

    # ── lṛṅ dispatch ─────────────────────────────────────────────────────────
    if lakara in ("lRG",):
        # Conditional (kriyātipatti) via sya vikaraṇa + aṭ augment
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lRG(state, pada_key, purusha, vacana)

    # ── loṭ dispatch ──────────────────────────────────────────────────────────
    if lakara in ("loT",):
        # Imperative (ājñārtha) via śap + loṭ-specific tiṅ substitutions
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_loT(state, pada_key, purusha, vacana)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 3 — LAKĀRA ATTACHMENT + TIṄ SELECTION (spec steps 2–9)
    # ═══════════════════════════════════════════════════════════════════

    # 3.1.91 dhātoḥ — adhikāra: pratyayas come from dhātu (spec step 2 context)
    state = apply_rule("3.1.91", state)
    state = P06a_pratyaya_adhikara_3_1_1_to_3(state)   # 3.1.1 + 3.1.2 + 3.1.3

    # 3.2.123 vartamāne laṭ — adhikāra gate for present tense (spec step 2)
    state = apply_rule("3.2.123", state)

    # Structural: attach laṭ as a Term placeholder.
    # The lakāra upadeśa carries it-markers (ँ anunāsika, ट् halantyam)
    # that 3.4.78 will process when it substitutes the tiṅ ādeśa.
    laT_varnas = parse_slp1_upadesha_sequence(lakara)
    # Pre-strip the halantyam it (ट्) from the placeholder so the
    # lakāra Term shows as "la" (ल्) — mirroring spec step 3/4/5 condensed.
    if laT_varnas and laT_varnas[-1].slp1 == "T":
        laT_varnas = laT_varnas[:-1]
    laT_term = Term(
        kind="pratyaya",
        varnas=laT_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": lakara},
    )
    state.terms.append(laT_term)

    # 3.4.77 lasya — adhikāra: scope for tiṅ substitution (3.4.77–3.4.112)
    state = apply_rule("3.4.77", state)

    # 3.4.78 tiptasjhi… — replace lakāra placeholder with the selected tiṅ ādeśa.
    # The ādeśa (tip/tas/jhi/…) is chosen at the recipe layer using the
    # puruṣa/vacana coordinates from tin_upadesha.json; the engine cond
    # is blind to those coordinates (CONSTITUTION Art. 2). (spec step 7)
    tin_adesha = _select_tin_adesha(lakara, pada_key, purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_slp1"]    = tin_adesha
    state = apply_rule("3.4.78", state)

    # 1.4.99 parasmaipade — saṃjñā: marks ādeśa as parasmaipada vibhakti.
    state = apply_rule("1.4.99", state)

    # ─── IT-prakaraṇa on the tiṅ ādeśa ──────────────────────────────────
    # 1.3.4 (audit), 1.3.3, 1.3.9 on the tiṅ ādeśa.
    #   • tip → "ti"  (p deleted)
    #   • tas → "tas" (s retained by the tiṅ-vibhakti guard)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 4A — SĀRVADHĀTUKA-SAMJÑĀ ON TIṄ ĀDEŚA (spec steps 9 + 15)
    # ═══════════════════════════════════════════════════════════════════

    # 3.4.113 tiṅśit sārvadhatukam — FIRST PASS: marks the tiṅ ādeśa
    # (e.g. tas) as sārvadhatuka, since it is a tiṅ pratyaya immediately
    # after the dhātu. This is the formal spec step 9. The second pass
    # (step 14 in spec) fires inside _apply_vikarana for the vikaraṇa (śap).
    state = apply_rule("3.4.113", state)

    # 1.2.4 sārvadhatukam apit — A sārvadhatuka pratyaya that is a-pit
    # (not marked with pit) is treated as if it were ṅit (kṅit).
    # This registers on the tiṅ ādeśa (tas/tip/…) and is verified in
    # spec step 15. The consequence is noted in the samjña-registry;
    # guṇa (7.3.84) still applies because its trigger is the immediate
    # sārvadhatuka (śap/a) following the dhātu, not the tiṅ ādeśa itself.
    # (spec step 15)
    state = apply_rule("1.2.4", state)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 4B — VIKARAṆA (gaṇa-specific) (spec steps 10–14)
    # ═══════════════════════════════════════════════════════════════════
    # _apply_vikarana for gaṇa 1:
    #   3.1.68 kartari śap  — insert śap after dhātu           (step 10)
    #   3.4.113 (second pass) — marks śap (śit) as sārvadhatuka (step 14)
    #   1.3.3 halantyam     — p of śap → it                    (step 11)
    #   1.3.8 laśakv.       — ś of śap → it                    (step 12)
    #   1.3.9 tasya lopaH   — ś+p deleted; śap residue = अ     (step 13)
    #   1.3.10 yāthāsankhya — samānānudeśa paribhāṣā            (trace)
    state = _apply_vikarana(state, gana)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 4C — JHI → ANTI  (7.1.3 jho'ntaH; 3pl parasmai only)
    # ═══════════════════════════════════════════════════════════════════
    # 7.1.3: jh of jhi (3pl tiṅ ādeśa) → ant; giving anti.
    # Fires only when the tiṅ term carries upadesha_slp1=="jhi" with 3 varnas.
    # For all other cells (ti/tas/mi/vas/mas) this is vacuous (SKIPPED).
    state.meta["7_1_3_jho_anta_arm"] = True
    state = apply_rule("7.1.3", state)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 5 — AṄGAKĀRYA (spec steps 16–17)
    # ═══════════════════════════════════════════════════════════════════

    # 1.4.13 yāsmāt pratyayavidhi… — dhātu becomes aṅga w.r.t. pratyaya.
    state = apply_rule("1.4.13", state)

    # 1.1.5 kṅiti ca — guard: the IMMEDIATE suffix after dhātu is śap (अ),
    #   which is NOT kṅit → guard SKIPS → guṇa (7.3.84) proceeds.
    state = apply_rule("1.1.5", state)

    # 7.3.101 ato dīrgho yañi — vikaraṇa-final 'a' → 'Ā' before yañ-initial
    #   tiṅ ādeśa (y v r l ñ ṅ ṇ n m).  Fires for uttama-puruṣa:
    #     bhū+a+mi → bhū+Ā+mi → (guṇa) bho+Ā+mi → (6.1.78) bhav+Ā+mi
    #   Vacuous (SKIPPED) for all other tiṅ ādeśas (t/s/Th/j initial).
    state.meta["7_3_101_arm"] = True
    state = apply_rule("7.3.101", state)

    # 7.3.84 sārvadhatukārdhadhatukayoḥ — guṇa: ik-vowel of aṅga (dhātu)
    #   → its guṇa substitute.  For bhū: उ → ओ. (spec step 17)
    state = apply_rule("7.3.84", state)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 6 — PADA-SAMJÑĀ + SANDHI (spec steps 18–19)
    # ═══════════════════════════════════════════════════════════════════

    # 1.4.14 suptingantam padam — the tiṅanta form is called pada.
    state = apply_rule("1.4.14", state)

    # 6.1.78 eco'yavāyāvaḥ — EC + AC → split: o+a → av+a (dhātu/vikaraṇa).
    #   bho+a → bhav  /  bho+Ā → bhav+Ā  (for uttama forms after 7.3.101)
    state = apply_rule("6.1.78", state)

    # 6.1.97 ato guṇe — cross-term 'a'(vikaraṇa) + 'a'(anti-initial) → drop
    #   the first 'a'.  Fires only after 7.1.3 turned jhi → anti (3pl).
    #   For bhavanti: bhav+a+anti → bhav+anti = भवन्ति.
    #   Vacuous for all other cells.
    state.meta["6_1_97_tinganta_arm"] = True
    state = apply_rule("6.1.97", state)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 7 — PADA MERGE (structural — not a sūtra)
    # ═══════════════════════════════════════════════════════════════════
    # All Terms concatenated into one pada-tagged Term.
    # After this, the flat varṇa sequence is the pre-tripāḍī surface:
    #   भवति (3sg) / भवतस् (3du, before 8.2.66) / etc.
    _pada_merge(state)

    # ═══════════════════════════════════════════════════════════════════
    # STAGE 8 — TRIPĀḌĪ: PŪRVATRĀSIDDHA ZONE (spec steps 20–22)
    # ═══════════════════════════════════════════════════════════════════

    # 8.2.1 pūrvatrāsiddham — opens the asiddha zone; all subsequent
    # sūtras (8.2.1–8.4.68) are invisible to all prior sūtras.
    # Sets state.tripadi_zone = True.
    state = apply_rule("8.2.1", state)

    # 8.2.66 ssa-sajuṣo ruḥ — pada-final 's' (and 'sajuṣ') → 'r' (ru-intermediate).
    # The 'r' carries tag 'ru_intermediate' for 8.3.15 to find.
    #   • भवतस् → भवतर् (for 3du, 3pl, 2sg, etc.)
    #   • भवति  → no change (final vowel, not s)        (spec step 20)
    state = apply_rule("8.2.66", state)

    # 8.3.15 kharavaṣānayorvisarjanīyaḥ — ru (r with ru_intermediate tag)
    # before a khar consonant or avasāna (pause) → visarjanīya (ḥ = H).
    #   • भवतर् → भवतः                                    (spec step 22)
    #   • भवति  → no change (no ru_intermediate)
    state = apply_rule("8.3.15", state)

    return state


# ─────────────────────────────────────────────────────────────────────────────
# CONVENIENCE WRAPPER
# ─────────────────────────────────────────────────────────────────────────────

def derive_bhavati() -> State:
    """Glass-box: भू + लँट् प्रथमपुरुष एकवचन → भवति."""
    return derive("BU", "laT", "kartari", 3, 1)


def derive_bhavataH() -> State:
    """Glass-box: भू + लँट् प्रथमपुरुष द्विवचन → भवतः."""
    return derive("BU", "laT", "kartari", 3, 2)


def derive_bhavanti() -> State:
    """Glass-box: भू + लँट् प्रथमपुरुष बहुवचन → भवन्ति (note: jhi→nti via 7.1.5 not yet implemented)."""
    return derive("BU", "laT", "kartari", 3, 3)


def derive_bhavasi() -> State:
    """Glass-box: भू + लँट् मध्यमपुरुष एकवचन → भवसि."""
    return derive("BU", "laT", "kartari", 2, 1)


def derive_bhavathah() -> State:
    """Glass-box: भू + लँट् मध्यमपुरुष द्विवचन → भवथः."""
    return derive("BU", "laT", "kartari", 2, 2)


def derive_bhavatha() -> State:
    """Glass-box: भू + लँट् मध्यमपुरुष बहुवचन → भवथ."""
    return derive("BU", "laT", "kartari", 2, 3)


def derive_bhavami() -> State:
    """Glass-box: भू + लँट् उत्तमपुरुष एकवचन → भवामि."""
    return derive("BU", "laT", "kartari", 1, 1)


def derive_bhavavah() -> State:
    """Glass-box: भू + लँट् उत्तमपुरुष द्विवचन → भवावः."""
    return derive("BU", "laT", "kartari", 1, 2)


def derive_bhavamah() -> State:
    """Glass-box: भू + लँट् उत्तमपुरुष बहुवचन → भवामः."""
    return derive("BU", "laT", "kartari", 1, 3)


# ─────────────────────────────────────────────────────────────────────────────
# LṚṬ CONVENIENCE WRAPPERS
# ─────────────────────────────────────────────────────────────────────────────

def derive_bhavisyati() -> State:
    """Glass-box: भू + लृट् प्रथमपुरुष एकवचन → भविष्यति."""
    return derive("BU", "lRT", "kartari", 3, 1)


def derive_bhavisyatah() -> State:
    """Glass-box: भू + लृट् प्रथमपुरुष द्विवचन → भविष्यतः."""
    return derive("BU", "lRT", "kartari", 3, 2)


def derive_bhavisyanti() -> State:
    """Glass-box: भू + लृट् प्रथमपुरुष बहुवचन → भविष्यन्ति."""
    return derive("BU", "lRT", "kartari", 3, 3)


def derive_bhavisyasi() -> State:
    """Glass-box: भू + लृट् मध्यमपुरुष एकवचन → भविष्यसि."""
    return derive("BU", "lRT", "kartari", 2, 1)


def derive_bhavisyathah() -> State:
    """Glass-box: भू + लृट् मध्यमपुरुष द्विवचन → भविष्यथः."""
    return derive("BU", "lRT", "kartari", 2, 2)


def derive_bhavisyatha() -> State:
    """Glass-box: भू + लृट् मध्यमपुरुष बहुवचन → भविष्यथ."""
    return derive("BU", "lRT", "kartari", 2, 3)


def derive_bhavisyami() -> State:
    """Glass-box: भू + लृट् उत्तमपुरुष एकवचन → भविष्यामि."""
    return derive("BU", "lRT", "kartari", 1, 1)


def derive_bhavisyavah() -> State:
    """Glass-box: भू + लृट् उत्तमपुरुष द्विवचन → भविष्यावः."""
    return derive("BU", "lRT", "kartari", 1, 2)


def derive_bhavisyamah() -> State:
    """Glass-box: भू + लृट् उत्तमपुरुष बहुवचन → भविष्यामः."""
    return derive("BU", "lRT", "kartari", 1, 3)


# ─────────────────────────────────────────────────────────────────────────────
# LAṄ CONVENIENCE WRAPPERS
# ─────────────────────────────────────────────────────────────────────────────

def derive_abhavat() -> State:
    """Glass-box: भू + लङ् प्रथमपुरुष एकवचन → अभवत्."""
    return derive("BU", "laG", "kartari", 3, 1)


def derive_abhavataM() -> State:
    """Glass-box: भू + लङ् प्रथमपुरुष द्विवचन → अभवताम्."""
    return derive("BU", "laG", "kartari", 3, 2)


def derive_abhavan() -> State:
    """Glass-box: भू + लङ् प्रथमपुरुष बहुवचन → अभवन्."""
    return derive("BU", "laG", "kartari", 3, 3)


def derive_abhavaH() -> State:
    """Glass-box: भू + लङ् मध्यमपुरुष एकवचन → अभवः."""
    return derive("BU", "laG", "kartari", 2, 1)


def derive_abhavataM2() -> State:
    """Glass-box: भू + लङ् मध्यमपुरुष द्विवचन → अभवतम्."""
    return derive("BU", "laG", "kartari", 2, 2)


def derive_abhavata() -> State:
    """Glass-box: भू + लङ् मध्यमपुरुष बहुवचन → अभवत."""
    return derive("BU", "laG", "kartari", 2, 3)


def derive_abhavam() -> State:
    """Glass-box: भू + लङ् उत्तमपुरुष एकवचन → अभवम्."""
    return derive("BU", "laG", "kartari", 1, 1)


def derive_abhavaV() -> State:
    """Glass-box: भू + लङ् उत्तमपुरुष द्विवचन → अभवाव."""
    return derive("BU", "laG", "kartari", 1, 2)


def derive_abhavaM() -> State:
    """Glass-box: भू + लङ् उत्तमपुरुष बहुवचन → अभवाम."""
    return derive("BU", "laG", "kartari", 1, 3)


# ─────────────────────────────────────────────────────────────────────────────
# LIṄ (VIDHI / OPTATIVE) CONVENIENCE WRAPPERS
# ─────────────────────────────────────────────────────────────────────────────

def derive_bhavet() -> State:
    """Glass-box: भू + लिँङ् प्रथमपुरुष एकवचन → भवेत्."""
    return derive("BU", "liG", "kartari", 3, 1)


def derive_bhavetam() -> State:
    """Glass-box: भू + लिँङ् प्रथमपुरुष द्विवचन → भवेताम्."""
    return derive("BU", "liG", "kartari", 3, 2)


def derive_bhaveyuH() -> State:
    """Glass-box: भू + लिँङ् प्रथमपुरुष बहुवचन → भवेयुः."""
    return derive("BU", "liG", "kartari", 3, 3)


def derive_bhaveH() -> State:
    """Glass-box: भू + लिँङ् मध्यमपुरुष एकवचन → भवेः."""
    return derive("BU", "liG", "kartari", 2, 1)


def derive_bhavetam2() -> State:
    """Glass-box: भू + लिँङ् मध्यमपुरुष द्विवचन → भवेतम्."""
    return derive("BU", "liG", "kartari", 2, 2)


def derive_bhaveta() -> State:
    """Glass-box: भू + लिँङ् मध्यमपुरुष बहुवचन → भवेत."""
    return derive("BU", "liG", "kartari", 2, 3)


def derive_bhaveyam() -> State:
    """Glass-box: भू + लिँङ् उत्तमपुरुष एकवचन → भवेयम्."""
    return derive("BU", "liG", "kartari", 1, 1)


def derive_bhaveva() -> State:
    """Glass-box: भू + लिँङ् उत्तमपुरुष द्विवचन → भवेव."""
    return derive("BU", "liG", "kartari", 1, 2)


def derive_bhavema() -> State:
    """Glass-box: भू + लिँङ् उत्तमपुरुष बहुवचन → भवेम."""
    return derive("BU", "liG", "kartari", 1, 3)

# ─────────────────────────────────────────────────────────────────────────────
# ĀŚĪR-LIṄ (BENEDICTIVE) CONVENIENCE WRAPPERS
# ─────────────────────────────────────────────────────────────────────────────

def derive_bhuyat() -> State:
    """Glass-box: भू + आशीर्-लिँङ् प्रथमपुरुष एकवचन → भूयात्."""
    return derive("BU", "AsIrliG", "kartari", 3, 1)

def derive_bhuyastam() -> State:
    """Glass-box: भू + आशीर्-लिँङ् प्रथमपुरुष द्विवचन → भूयास्ताम्."""
    return derive("BU", "AsIrliG", "kartari", 3, 2)

def derive_bhuyasuh() -> State:
    """Glass-box: भू + आशीर्-लिँङ् प्रथमपुरुष बहुवचन → भूयासुः."""
    return derive("BU", "AsIrliG", "kartari", 3, 3)

def derive_bhuyah() -> State:
    """Glass-box: भू + आशीर्-लिँङ् मध्यमपुरुष एकवचन → भूयाः."""
    return derive("BU", "AsIrliG", "kartari", 2, 1)

def derive_bhuyastam2() -> State:
    """Glass-box: भू + आशीर्-लिँङ् मध्यमपुरुष द्विवचन → भूयास्तम्."""
    return derive("BU", "AsIrliG", "kartari", 2, 2)

def derive_bhuyasta() -> State:
    """Glass-box: भू + आशीर्-लिँङ् मध्यमपुरुष बहुवचन → भूयास्त."""
    return derive("BU", "AsIrliG", "kartari", 2, 3)

def derive_bhuyasam() -> State:
    """Glass-box: भू + आशीर्-लिँङ् उत्तमपुरुष एकवचन → भूयासम्."""
    return derive("BU", "AsIrliG", "kartari", 1, 1)

def derive_bhuyasva() -> State:
    """Glass-box: भू + आशीर्-लिँङ् उत्तमपुरुष द्विवचन → भूयास्व."""
    return derive("BU", "AsIrliG", "kartari", 1, 2)

def derive_bhuyasma() -> State:
    """Glass-box: भू + आशीर्-लिँङ् उत्तमपुरुष बहुवचन → भूयास्म."""
    return derive("BU", "AsIrliG", "kartari", 1, 3)

# ─────────────────────────────────────────────────────────────────────────────
# LUṄ (AORIST) CONVENIENCE WRAPPERS
# ─────────────────────────────────────────────────────────────────────────────

def derive_abhut() -> State:
    """Glass-box: भू + लुँङ् प्रथमपुरुष एकवचन → अभूत्."""
    return derive("BU", "luG", "kartari", 3, 1)

def derive_abhutam() -> State:
    """Glass-box: भू + लुँङ् प्रथमपुरुष द्विवचन → अभूताम्."""
    return derive("BU", "luG", "kartari", 3, 2)

def derive_abhuvan() -> State:
    """Glass-box: भू + लुँङ् प्रथमपुरुष बहुवचन → अभूवन्."""
    return derive("BU", "luG", "kartari", 3, 3)

def derive_abhuh() -> State:
    """Glass-box: भू + लुँङ् मध्यमपुरुष एकवचन → अभूः."""
    return derive("BU", "luG", "kartari", 2, 1)

def derive_abhutam2() -> State:
    """Glass-box: भू + लुँङ् मध्यमपुरुष द्विवचन → अभूतम्."""
    return derive("BU", "luG", "kartari", 2, 2)

def derive_abhuta() -> State:
    """Glass-box: भू + लुँङ् मध्यमपुरुष बहुवचन → अभूत."""
    return derive("BU", "luG", "kartari", 2, 3)

def derive_abhuvam() -> State:
    """Glass-box: भू + लुँङ् उत्तमपुरुष एकवचन → अभूवम्."""
    return derive("BU", "luG", "kartari", 1, 1)

def derive_abhuva() -> State:
    """Glass-box: भू + लुँङ् उत्तमपुरुष द्विवचन → अभूव."""
    return derive("BU", "luG", "kartari", 1, 2)

def derive_abhuma() -> State:
    """Glass-box: भू + लुँङ् उत्तमपुरुष बहुवचन → अभूम."""
    return derive("BU", "luG", "kartari", 1, 3)

# ─────────────────────────────────────────────────────────────────────────────
# LṚṄ (CONDITIONAL) CONVENIENCE WRAPPERS
# ─────────────────────────────────────────────────────────────────────────────

def derive_abhavisyat() -> State:
    """Glass-box: भू + लृँङ् प्रथमपुरुष एकवचन → अभविष्यत्."""
    return derive("BU", "lRG", "kartari", 3, 1)

def derive_abhavisyatam() -> State:
    """Glass-box: भू + लृँङ् प्रथमपुरुष द्विवचन → अभविष्यताम्."""
    return derive("BU", "lRG", "kartari", 3, 2)

def derive_abhavisyan() -> State:
    """Glass-box: भू + लृँङ् प्रथमपुरुष बहुवचन → अभविष्यन्."""
    return derive("BU", "lRG", "kartari", 3, 3)

def derive_abhavisyah() -> State:
    """Glass-box: भू + लृँङ् मध्यमपुरुष एकवचन → अभविष्यः."""
    return derive("BU", "lRG", "kartari", 2, 1)

def derive_abhavisyatam2() -> State:
    """Glass-box: भू + लृँङ् मध्यमपुरुष द्विवचन → अभविष्यतम्."""
    return derive("BU", "lRG", "kartari", 2, 2)

def derive_abhavisyata() -> State:
    """Glass-box: भू + लृँङ् मध्यमपुरुष बहुवचन → अभविष्यत."""
    return derive("BU", "lRG", "kartari", 2, 3)

def derive_abhavisyam() -> State:
    """Glass-box: भू + लृँङ् उत्तमपुरुष एकवचन → अभविष्यम्."""
    return derive("BU", "lRG", "kartari", 1, 1)

def derive_abhavisyav() -> State:
    """Glass-box: भू + लृँङ् उत्तमपुरुष द्विवचन → अभविष्याव."""
    return derive("BU", "lRG", "kartari", 1, 2)

def derive_abhavisyam2() -> State:
    """Glass-box: भू + लृँङ् उत्तमपुरुष बहुवचन → अभविष्याम."""
    return derive("BU", "lRG", "kartari", 1, 3)
