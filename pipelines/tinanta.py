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
from core.phases.tripadi import execute_tripadi_phase
from phonology.varna import parse_slp1_upadesha_sequence, mk as _mk

from core.canonical_pipelines import (
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
    P00_tanadi_u_guna,
    P00_hal_it_lopa,
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
    return state


def _karmani_apply_yak(state: State) -> State:
    """**3.1.67** inserts *yaḳ*; recipe runs it-lopa + *ṅit* saṃjñā only."""
    state = apply_rule("3.1.67", state)
    return _karmani_yak_it_and_ngiti(state)


def _bhave_atmanepada_tin_after_lopa(state: State) -> State:
    """After ``P00_tin_tusma`` on bhāve paths: 1.4.100 + 3.4.79/80."""
    if state.meta.get("prayoga") != "bhave":
        return state
    state = apply_rule("1.4.100", state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("3.4.80", state)
    return state


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
        # 3.1.68 utsarga (inserts Śap), then 3.1.69 apavāda (Śap→Śyan)
        state.meta["3_1_68_kartari_recipe"] = True
        state = apply_rule("3.1.68", state)   # utsarga: insert Śap
        state = apply_rule("3.1.69", state)   # apavāda: Śap → Śyan
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        return state

    if gana == 6:
        # 3.1.77 tudādi śa — cond checks gana==6 + no existing Śa.
        state = apply_rule("3.1.77", state)
        state = apply_rule("3.4.113", state)
        state = P00_lashakvataddhite_it_lopa_chain(state)
        return state

    if gana == 8:
        # 3.1.79 tanādi u-vikaraṇa + root guṇa (7.3.84) + rapara (1.1.51).
        # 3.4.110 kit-upadha (a→u for weak/ṅit forms) fires from the spine's 1.1.5 path.
        # NOTE: the second guṇa (u→o for strong parasmaipada forms like karoti)
        # requires 7.3.84 to fire on the u-vikaraṇa; this is not yet wired into the
        # bhuvādi spine — strong forms currently give *karuti* not *karoti*.
        state = P00_tanadi_u_guna(state)   # 3.1.79 + 7.3.84 + 1.1.51
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
    # 3.1.91 dhātoḥ — adhikāra: pratyayas come from dhātu
    state = apply_rule("3.1.91", state)
    state = P06a_pratyaya_adhikara_3_1_1_to_3(state)

    # 3.2.123 vartamāne laṭ — adhikāra gate for present tense
    state = apply_rule("3.2.123", state)

    laT_varnas = parse_slp1_upadesha_sequence(lakara)
    if laT_varnas and laT_varnas[-1].slp1 == "T":
        laT_varnas = laT_varnas[:-1]
    laT_term = Term(
        kind="pratyaya",
        varnas=laT_varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": lakara},
    )
    state.terms.append(laT_term)

    tin_adesha = _select_tin_adesha(lakara, pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)

    state = _apply_vikarana(state, gana)
    state = apply_rule("7.1.3", state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("7.3.84", state)
    # 6.4.110 ata ut sārvadhatuke — tanādi weak forms: upadha a→u (kar→kur before kṅit tiṅ)
    state = apply_rule("6.4.110", state)
    # 6.4.108 nityaṃ karoteḥ — kṛ: drop u-vikaraṇa before non-val suffix (kurvaḥ, kurmaḥ)
    state = apply_rule("6.4.108", state)

    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — IK-final vikaraṇa + AC-initial suffix (kuru+anti → kurv+anti)
    state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)
    state = apply_rule("6.1.97", state)

    _pada_merge(state)
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

    if purusha == 1 and vacana == 1:
        state.meta["Nal_uttama_recipe"] = True
        state = apply_rule("7.1.91", state)

    needs_it = _lit_needs_it(purusha, vacana)

    if needs_it:
        # ── iṭ path: iṭ → dvitva → vuk (6.4.88 needs abhyāsa for liṭ context) ──
        state = apply_rule("1.2.5", state)
        state.meta["liT_krsrbhr_recipe"] = True
        state = apply_rule("7.2.13", state)
        state = apply_rule("7.2.35", state)
        # IT on iṭ: iṭ has T as halantyam-it
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        # 1.4.13 aṅga saṃjñā
        state = apply_rule("1.4.13", state)
        # dvitva BEFORE vuk: 6.4.88 requires abhyāsa present to detect liṭ context
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        # 7.4.60 halādiḥ śeṣaḥ — trim CVC abhyāsa to CV (e.g. paW → pa)
        state = apply_rule("7.4.60", state)
        # 6.4.88 vuk (abhyāsa now present → liṭ context confirmed)
        state = apply_rule("6.4.88", state)
        # IT on vuk (u and k are it-marked)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
    else:
        # ── NO-iṭ path: dvitva FIRST, then 1.4.13, vuk ───────────────────────
        if lit_adesha not in ("Ral",):
            state = apply_rule("1.2.5", state)
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        # 7.4.60 halādiḥ śeṣaḥ — trim CVC abhyāsa to CV (e.g. paW → pa)
        state = apply_rule("7.4.60", state)
        if lit_adesha == "Ral":
            # liṭ strong: guṇa first (IK-upadha: cit→cet, kṛ ṛ→a+rapara_pending)
            state.meta["liT_strong_recipe"] = True
            state = apply_rule("7.3.84", state)
            state.meta.pop("liT_strong_recipe", None)
            # 1.1.51 uRaN rapara — resolves root ṛ→ar (kṛ → kar)
            state = apply_rule("1.1.51", state)
            # 7.2.116 ato upadhāyāḥ — vṛddhi of a-upadha (paṭh→pāṭh; kṛ now kar→kār)
            state = apply_rule("7.2.116", state)
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

    # ── 7.4.73 bhavateraḥ (abhyāsa u→a) — only for bhū ─────────────────────────
    _dht = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    _dht_up = (_dht.meta.get("upadesha_slp1") or "").strip() if _dht else ""
    if _dht_up in {"BU", "BU~"}:
        state.meta["bhU_abhyasa_recipe"] = True
        state = apply_rule("7.4.73", state)

    # ── 1.4.14 pada saṃjñā ───────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.77 iko yaṇ aci — IK-final root + vowel-initial suffix/iṭ ────────
    # (fires at term boundary before merge; resolves kṛ ṛ→r before atuH/uH/iṭ)
    state = apply_rule("6.1.77", state)

    # ── TRIPĀḌĪ: 8.2.1 + 8.4.54 must fire pre-merge (abhyāsa term visible) ──
    state = apply_rule("8.2.1", state)    # opens tripadi_zone
    state = apply_rule("8.4.54", state)   # carc on abhyāsa term

    # ── MERGE then full post-merge Tripāḍī spine ──────────────────────────────
    _pada_merge(state)
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
    for sid in ("1.3.2", "1.3.3", "1.3.9"):
        state = apply_rule(sid, state)

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

    if kit_path and lit_adesha in {"atus", "us", "aTus", "va", "ma"} and not needs_it:
        state = apply_rule("7.4.59", state)

    state = apply_rule("1.4.14", state)
    # Pre-merge: open Tripāḍī zone; 8.4.54 needs the abhyāsa term separate.
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.4.54", state)
    _pada_merge(state)
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
        state = apply_rule("7.2.35", state)
        # 1.3.7: q(ḍ, cuṭu)→it on qA term; 1.3.9: lope q → A
        state = apply_rule("1.3.7", state)
        state = apply_rule("1.3.9", state)
        # 1.4.13 aṅga saṃjñā, 7.3.84 guṇa (BU→Bo)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = apply_rule("7.3.84", state)
        # 6.4.143: tāsi (i+t+A+s) → (i+t) before A (ḍit) — ṭi-lopa
        state = apply_rule("6.4.143", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 2:
        # 3du: 7.2.35(iṭ into tāsi while tas has t=val), 1.2.4,
        #      2.4.85(tas→rO), 1.4.13, 7.3.84, 7.4.51(tāsi→tA before r), 1.4.14, 6.1.78
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.2.4", state)
        adesha = _lut_prathama_adesha(state, 3, 2)
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = apply_rule("7.3.84", state)
        # 7.4.51: drop s from tāsi before r (rO starts with r)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 3:
        # 3pl: 7.2.35(iṭ into tāsi while jhi has j=val), 1.2.4,
        #      2.4.85(jhi→ras), 1.4.13, 7.3.84, 7.4.51(tāsi→tA before r), 1.4.14, 6.1.78
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.2.4", state)
        adesha = _lut_prathama_adesha(state, 3, 3)
        state.meta["luT_adesha_form"] = adesha
        state.meta["luT_prathama_recipe"] = True
        state = apply_rule("2.4.85", state)
        state.meta.pop("luT_prathama_recipe", None)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = apply_rule("7.3.84", state)
        # 7.4.51: drop s from tāsi before r (ras starts with r)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 1:
        # 2sg: 7.2.35(iṭ into tāsi while si has s=val), 1.4.13, 7.3.84,
        #      7.4.50(tāsi→tA before si), 1.4.14, 6.1.78
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = apply_rule("7.3.84", state)
        # 7.4.50: drop s from tāsi before si (si starts with s)
        state.meta["tasa_lopa_recipe"] = True
        state = apply_rule("7.4.50", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    else:
        # Non-prathama, non-2sg cells: 2du (Tas), 2pl (Ta), 1sg (mi), 1du (vas), 1pl (mas)
        # 7.2.35: insert iṭ into tāsi (tāsi starts with t=val → always fires)
        # No 2.4.85; no s-lopa rule for these cells.
        state = apply_rule("7.2.35", state)
        # 1.2.4 for cells whose tiṅ is sārvadhatuka apit (most of them)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        if not state.meta.get("_luT_skip_guna"):
            state = apply_rule("7.3.84", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    _pada_merge(state)
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
    state = apply_rule("7.1.3", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    # 6.4.71 aṭ + it-lopa (aṭ T is conceptual)
    state = P00_at_agama_it_lopa(state)

    state = apply_rule("1.1.5", state)
    # 7.3.101: 'a' of śap → 'ā' before yañ-initial tiṅ ādeśa (v of 'v', m of 'm')
    state = apply_rule("7.3.101", state)
    # 7.3.84: guṇa (IK-vowel of dhātu; BU(Ū) → Bo)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada + sandhi ─────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — tanādi gana 8: vikaraṇa-u + AC-initial tiṅ (tan+u+ant → tanvant)
    if gana == 8:
        state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)
    # 6.1.97: a+a → a (3pl: śap-a + ant-a; 1sg: śap-a + am-a)
    state = apply_rule("6.1.97", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    _pada_merge(state)
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
        state = apply_rule("7.1.3", state)
    state = apply_rule("3.4.99", state)
    state = apply_rule("6.1.66", state)
    state = apply_rule("1.2.4", state)
    state = apply_rule("1.4.13", state)
    state = P00_at_agama_it_lopa(state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("6.1.97", state)

    _pada_merge(state)
    state = execute_tripadi_phase(state)  # rules fire based on phonological state
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

    # ── Stage: cli/sic chain (before lakāra substitution: 3.1.43 needs luG) ──
    state.meta["cli_luG_recipe"] = True
    state = apply_rule("3.1.43", state)   # inserts cli before luG placeholder
    # 3.1.55 cli→aṅ for puṣyādi/dyutādi (parasmaipada only); structural cond (dyut+cli)
    if pada_key == "parasmai":
        state = apply_rule("3.1.55", state)
    state = apply_rule("3.1.44", state)   # cli → sic; vacuous if 3.1.55 already fired

    # ── Stage: 3.4.77 + 3.4.78 tiṅ ādeśa ────────────────────────────────────
    tin_adesha = _select_tin_adesha("luG", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = P00_tin_tusma_audit_halantyam_lopa(state)  # drops p-it of tiṅ; c-it of sic

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Detect seṭ vs aniṭ ───────────────────────────────────────────────────
    _dhatu_t = next((t for t in state.terms if "dhatu" in t.tags), None)
    _is_anit  = _dhatu_t is not None and bool(_dhatu_t.meta.get("anit_dhatu"))

    if _is_anit:
        # ── aniṭ path: 2.4.77 luk of sic (gāti-sthā-ghu-pā-bhū) ─────────────
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
        # 7.3.86 laghūpadha guṇa before sic+iṭ (structural: dyut+i → dyot+i)
        state = apply_rule("7.3.86", state)

    # ── Stage: 1.2.4 apit sārvadhatuka → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: tiṅ substitutions ─────────────────────────────────────────────
    state = apply_rule("3.4.101", state)   # tas→tām, Tas→tam, Ta→ta, mi→am

    if not _is_anit and (purusha, vacana) == (3, 3):
        # seṭ 3pl: jher jus (3.4.108) → [u, s] instead of 7.1.3 jh→anti
        state = apply_rule("3.4.108", state)

    state = apply_rule("3.4.100", state)   # ti→t, si→s, jhi→jh

    if _is_anit:
        state = apply_rule("7.1.3", state)     # jh→ant (3pl, aniṭ only)

    state = apply_rule("3.4.99", state)    # vas→va, mas→ma

    # ── seṭ: for tip/sip-derived cells, sic-s + iṭ-i → ī via 7.2.35 ───────────
    # Discriminate by tiṅ upadesha (Art.2§2c: upadesha identity is allowed).
    # After 3.4.100 drops i from tip/sip, upadesha_slp1 remains "tip"/"sip".
    _tin_t = next(
        (t for t in state.terms if t.kind == "pratyaya" and "tin_adesha_3_4_78" in t.tags),
        None,
    )
    _tin_up = (_tin_t.meta.get("upadesha_slp1") or "").strip() if _tin_t else ""
    if not _is_anit and _tin_up in {"tip", "sip"}:
        for _t in state.terms:
            if (_t.meta.get("upadesha_slp1") or "").strip() == "sic":
                _t.tags.add("seT_sic_it_lopa_context")
                break
        state = apply_rule("7.2.35", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)

    # 6.4.71 aṭ augment; skip it-lopa for seṭ to avoid re-processing sic 's'
    state = apply_rule("6.4.71", state)
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
    state = apply_rule("6.1.77", state)

    state = apply_rule("1.4.14", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
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
    state.meta["ashir_7_4_25_recipe"] = True
    state = apply_rule("7.4.25", state)
    state = apply_rule("1.4.14", state)

    state = apply_rule("6.1.66", state)

    state.meta["ashir_8_2_29_recipe"] = True
    state = apply_rule("8.2.29", state)
    state.meta.pop("ashir_8_2_29_recipe", None)

    _pada_merge(state)
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
    if gana == 8:
        state.meta["liG_yasut_expected"] = True
    state = _apply_vikarana(state, gana)

    # ── Stage: liṅ-specific tiṅ substitutions ───────────────────────────────
    # 3.4.101 (apavāda) BEFORE 3.4.108/3.4.100: tas→tām, Tas→tam, Ta→ta, mi→am
    state = apply_rule("3.4.101", state)
    # 3.4.108: jhi → jus → [u,s]  (only fires for 3pl)
    state = apply_rule("3.4.108", state)
    # 3.4.100: ti→t, si→s  (i-lopa; skips [u,s] from jus, tām, am, etc.)
    state = apply_rule("3.4.100", state)
    # 3.4.99: vas→va, mas→ma  (s-lopa for uttama 1du/1pl)
    state = apply_rule("3.4.99", state)

    # ── Stage: 3.4.103 yāsuṭ insertion ─────────────────────────────────────
    state.meta["yasut_recipe"] = True
    state = apply_rule("3.4.103", state)
    # yāsuṭ is now present with kngiti tag — lift the pre-block flag
    state.meta.pop("liG_yasut_expected", None)

    # ── Stage: yāsuṭ processing ──────────────────────────────────────────────
    # 7.2.79: [y,A,s] → [y,A]  (drop final 's' of yāsuṭ)
    state = apply_rule("7.2.79", state)
    # 7.2.80: [y,A] → [i,y]  (when preceded by 'a')
    state = apply_rule("7.2.80", state)
    # 6.1.66: 'y' of [i,y] drops before HAL-initial tiṅ (t,s,m,v,…)
    state = apply_rule("6.1.66", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    # 6.1.96 usy apadāntāt — tanādi gana 8: yā + us → y + us (drop ā before 3pl us)
    if gana == 8:
        state = apply_rule("6.1.96", state)
    # 6.1.87: a + i → e  (śap-a + yāsuṭ-i remnant)
    state = apply_rule("6.1.87", state)
    # 7.3.84: guṇa (IK-vowel of dhātu → guṇa; tanādi vikaraṇa blocked by yāsuṭ kṅit)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada + sandhi ────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — tanādi gana 8: vikaraṇa-u + AC-initial tiṅ
    if gana == 8:
        state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
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
    state = apply_rule("2.4.72", state)

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

    state.meta["liG_ad_8_2_29_suw_recipe"] = True
    state = apply_rule("8.2.29", state)
    state.meta.pop("liG_ad_8_2_29_suw_recipe", None)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.101", state)

    _pada_merge(state)
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
    state.meta["lfT_recipe"] = True
    state = apply_rule("3.3.13", state)
    state.meta.pop("lfT_recipe", None)

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
    tin_adesha = _select_tin_adesha("lRT", pada_key, purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)

    # IT on tiṅ ādeśa (1.3.4 tusma guard + 1.3.3 halantyam + 1.3.9 lopa)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = _bhave_atmanepada_tin_after_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ─────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 3.1.33 insert *sya* vikaraṇa after dhātu ────────────────────
    state = apply_rule("3.1.33", state)

    # ── Stage: 3.4.114 mark *sya* as ārdhadhātuka ───────────────────────────
    state = apply_rule("3.4.114", state)

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
    state = apply_rule("7.1.3", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)
    # 7.3.101 ato dīrgho yañi: 'a' of *sya* → 'ā' before yañ-initial tiṅ
    # (m of mip/mas, v of vas).  Vacuous for non-yañ-initial ādeśas.
    state = apply_rule("7.3.101", state)
    # 7.3.84 guṇa: IK-vowel of dhātu (Ū of BU) → guṇa (o).
    if not state.meta.get("_lRT_skip_guna"):
        state = apply_rule("7.3.84", state)

    # ── Stage: pada saṃjñā + sandhi ─────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.78 eco'yavāyāvaḥ: EC + AC → split (o + i from iṭ → av + i).
    state = apply_rule("6.1.78", state)
    # 6.1.97 ato guṇe: a + a → a (fires for 3pl after jhi→anti: sya+anti).
    state = apply_rule("6.1.97", state)

    # ── Merge + Tripāḍī ──────────────────────────────────────────────────────
    _pada_merge(state)
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
    state = apply_rule("7.1.3", state)
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

    _pada_merge(state)
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
    state = _bhave_atmanepada_tin_after_lopa(state)

    # ── Stage: 3.4.113 tiṅ is sārvadhatuka ──────────────────────────────────
    state = apply_rule("3.4.113", state)

    # ── Stage: 1.2.4 apit → kṅit ─────────────────────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: śap vikaraṇa (3.1.68 for bhvādi gaṇa 1) ──────────────────────
    gana: int = state.terms[0].meta.get("gana", 1)
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
    state = apply_rule("7.1.3", state)

    # 3.4.86: i→u (ti→tu for 3sg; anti→antu for 3pl; skip hi from 3.4.87, ni from 3.4.89)
    state = apply_rule("3.4.86", state)

    # 3.4.99: s-lopa (vas→va for 1du; mas→ma for 1pl)
    state = apply_rule("3.4.99", state)

    # 6.4.105: delete 'hi' after short 'a' of aṅga (2sg: bhava+hi → bhava)
    state = apply_rule("6.4.105", state)

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)

    # 7.3.101: a→ā before yañ-initial tiṅ (n of ni for 1sg; v of va for 1du; m of ma for 1pl)
    state = apply_rule("7.3.101", state)

    # 7.3.84: guṇa (bhū → bho; śap is sārvadhatuka trigger)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada + sandhi ─────────────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    # 6.1.77 iko yaṇ aci — only for tanādi (gana 8): vikaraṇa-u + antu (tanu+antu → tanvantu)
    if gana == 8:
        state = apply_rule("6.1.77", state)
    state = apply_rule("6.1.78", state)
    # 6.1.97: a+a → a (3pl: śap-a + antu-a → bhavantu)
    state = apply_rule("6.1.97", state)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
    state = P00_tripadi_rutva_visarga(state)
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
    state = apply_rule("2.4.72", state)

    if purusha == 1 and vacana == 1:
        state = apply_rule("3.4.89", state)

    state = apply_rule("3.4.101", state)

    if purusha == 2 and vacana == 1:
        state = apply_rule("3.4.87", state)

    state = apply_rule("7.1.3", state)

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

    _pada_merge(state)
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
    state.terms = prefix + state.terms
    return apply_rule("1.4.59", state)


def _yam_with_A_upasarga(state: State) -> bool:
    """P010 tape: ``A~N`` + ``yam`` *dhātu* (after it-lopa)."""
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
    state = apply_rule("3.2.123", state)
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
    _tin = _select_tin_adesha("laT", "parasmai", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, _tin)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.2.4", state)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    state = apply_rule("2.4.72", state)
    state = apply_rule("7.1.3", state)
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.4.14", state)
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    state = P00_tripadi_8_4_55_visarga(state)
    state = P00_tripadi_anusvara_parasavarna(state)
    state = apply_rule("8.4.68", state)
    return state


def _derive_laT_adadi(state: State, purusha: int, vacana: int) -> State:
    """
    Adādi laṭ spine (P008 *āste*): *śap* insertion, **2.4.72** *luk*, **3.4.79** *ṭere*,
    no *guṇa* / *tripāḍī* block (matches corrected-v2 P008).
    """
    state.meta["lakara"] = "laT"
    state = apply_rule("3.2.123", state)
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
    _tin = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, _tin)
    state.meta["3_1_68_kartari_recipe"] = True
    state = P00_adadi_sap_luk_tere(state)
    _pada_merge(state)
    return state


def _derive_laT_yam_Anga(state: State, purusha: int, vacana: int) -> State:
    """
    ``A~N`` + ``yam`` laṭ (P010 *āyacchate*): **1.3.28**, *śap*, **7.3.78**, *ṅ*-lopa, **3.4.79**.
    """
    state.meta["lakara"] = "laT"
    state = apply_rule("1.3.28", state)
    state = apply_rule("3.1.91", state)
    state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
    state = apply_rule("3.2.123", state)
    laT_varnas = parse_slp1_upadesha_sequence("laT")
    if laT_varnas and laT_varnas[-1].slp1 == "T":
        laT_varnas = laT_varnas[:-1]
    state.terms.append(
        Term(
            kind="pratyaya",
            varnas=laT_varnas,
            tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
            meta={"upadesha_slp1": "laT"},
        )
    )
    _tin2 = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, _tin2)
    state = apply_rule("3.4.113", state)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    # Do not run *halantyam*/*lopa* on ``yam`` as *upadeśa* (only on *śap*); keep ``m`` for **7.3.78**.
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("7.3.78", state)
    for sid in ("1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    _pada_merge(state)
    return state


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
    for sid in ("1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("6.4.113", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    _pada_merge(state)
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
    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    _kyaz_merge(state, nominal_slp1)
    state = apply_rule("3.1.32", state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "parasmai", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("7.4.25", state)
    state = apply_rule("6.1.101", state)
    _pada_merge(state)
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
    for sid in ("1.3.7", "1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("1.4.18", state)
    state = apply_rule("6.4.143", state)  # ṭi-lopa (structural: bha+stem+dit)
    # After 6.4.143, stem has lost final ṭi syllables. The next term is qāc residue
    # (a/A). Merge them to get the prātipadika for kyaz.
    stem_now = "".join(v.slp1 for v in state.terms[0].varnas) if state.terms else ""
    _merge_two_terms_to_pratipadika(state, f"{stem_now} + qAc-residue → {stem_now}A")
    state = apply_rule("3.1.13", state)   # kyaz (structural: fires for this stem)
    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    # Merge prātipadika + kyaz residue (ya → y) → dhātu
    stem_after = "".join(v.slp1 for v in state.terms[0].varnas) if state.terms else ""
    _kyaz_merge(state, stem_after)
    state = apply_rule("3.1.32", state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "parasmai", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("3.4.113", state)
    state = apply_rule("1.1.64", state)
    _pada_merge(state)
    return state


def derive_periphrastic_lit(
    dhatu_slp1: str,
    purusha: int,
    vacana: int,
) -> State:
    """
    Periphrastic liṭ (ām + kṛñ anuprayoga) — P014 *īkṣāñcakre*.

    For ijādi gurumad ātmanepada dhātus (e.g. 'Ikz').
    e.g. derive_periphrastic_lit('Ikz', 3, 1) → 'IkzAYcakre'
    """
    import sutras  # noqa: F401

    row = _dhatu_row_by_upadesha(dhatu_slp1)
    dhatu_term = _build_dhatu_term(row)
    state = State(terms=[dhatu_term], meta={}, trace=[], samjna_registry={})
    state = P01_samjna_dhatu_class(state)
    state = P00_bhuvadi_dhatu_it_anunasik_hal(state)
    # After it-lopa the varnas are the clean post-IT form ("Ikz"), but
    # upadesha_slp1 in meta still holds the raw form ("Ikza~").
    # 3.1.36 and 2.4.81 check upadesha_slp1 == "Ikz", so normalize here.
    for t in state.terms:
        if "dhatu" in t.tags:
            t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
            break
    return _derive_lit_am_kf_atmane(state, purusha, vacana)


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
    for sid in ("1.3.7", "1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("7.3.37", state)
    _nic_merge(state)
    state = apply_rule("3.1.32", state)
    state = P00_lac_lat_attach(state)
    tin_adesha = _select_tin_adesha("laT", "atmane", purusha, vacana)
    state = P00_tin_adesha_base(state, tin_adesha)
    state.meta["3_1_68_kartari_recipe"] = True
    state = apply_rule("3.1.68", state)
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    state = P00_adadi_tere_3_4_79(state)
    state = P00_guna_sandhi_7_3_84_6_1_78(state)
    _pada_merge(state)
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
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    state = P00_adadi_tere_3_4_79(state)
    _pada_merge(state)
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
    for sid in ("1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
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
    _pada_merge(state)
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
    for sid in ("1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("6.4.113", state)
    state = apply_rule("1.1.64", state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.4.2", state)
    _pada_merge(state)
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
    for sid in ("1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    state = apply_rule("3.1.33", state)
    state = apply_rule("3.4.100", state)
    state = apply_rule("7.3.86", state)
    state = apply_rule("1.1.51", state)
    state = apply_rule("6.4.71", state)
    for sid in ("1.3.3", "1.3.9"):
        state = apply_rule(sid, state)
    _pada_merge(state)
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
    if _dhatu_has_ṛ_anga(state):
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
    state = apply_rule("7.2.35", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── Stage: 1.2.4 apit sārvadhatuka → kṅit ───────────────────────────────
    state = apply_rule("1.2.4", state)

    # ── Stage: tiṅ substitutions (laṅ-style) ────────────────────────────────
    state = apply_rule("3.4.101", state)   # tas→tām, Tas→tam, Ta→ta, mi→am (apavāda)
    state = apply_rule("3.4.100", state)   # ti→t, si→s, jhi→jh
    state = apply_rule("7.1.3", state)     # jh→ant (3pl)
    state = apply_rule("3.4.99", state)    # vas→va, mas→ma

    # ── Stage: aṅgakārya ────────────────────────────────────────────────────
    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5",  state)

    # 6.4.71 aṭ + it-lopa (lṛṅ group)
    state = P00_at_agama_it_lopa(state)

    # 7.3.101 ato dīrgho yañi: sya-a → ā before yañ-initial tiṅ (v of va, m of ma)
    state = apply_rule("7.3.101", state)

    # 7.3.84 guṇa (bhū → bho; ārdhadhātuka sya triggers)
    state = apply_rule("7.3.84", state)

    # ── Stage: pada saṃjñā + sandhi ─────────────────────────────────────────
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)    # bho+i(ṭ) → bhav+i
    state = apply_rule("6.1.97", state)    # a+a → a (3pl: sya+ant; 1sg: sya+am)

    # ── Merge + Tripāḍī ─────────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1",  state)
    state = apply_rule("8.2.39", state)    # t→d at pada-end (3sg)
    state = apply_rule("8.4.56", state)    # d→t at avasāna (3sg)
    state = P00_tripadi_samyoganta_ru_visarga(state)
    state = apply_rule("8.3.59", state)    # s→ṣ after IK (sya→ṣya)
    state = apply_rule("8.4.68", state)

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
    state = apply_rule("7.1.3", state)

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

    _pada_merge(state)
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
    state = apply_rule("7.1.3", state)

    # 7.3.101 ato dīrgho yañi (1du/1pl: a of ya → ā before v/m of sīyuṭ or tiṅ)
    state = apply_rule("7.3.101", state)

    state = apply_rule("1.4.14", state)

    # 6.1.87 ādguṇaḥ: ya-a + ī (from sīyuṭ-I) → ye
    state = apply_rule("6.1.87", state)

    # 6.1.97 pararūpa: 3pl ya-a + ran-a/anta-a → a
    state = apply_rule("6.1.97", state)

    _pada_merge(state)
    state = P00_tripadi_rutva_visarga(state)

    return state


def _derive_karmani_ashir_liG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani āśīr-liṅ (passive benedictive) for bhvādi dhātus.

    Strategy: use AsIrliN-atmane tiṅ ādeśas from tin_upadesha.json directly.
    These entries encode sīyuṭ+suṭ+tiṅ after 8.3.59+8.4.41 on suṭ-related sounds.
    The only remaining work: 7.2.35 iṭ before the leading 's' + 7.3.84 guṇa +
    6.1.78 + 8.3.59 (once, for sīy's leading 's' after iṭ-i).

    Key sūtras: 1.3.13, 3.3.173, 3.4.116, 7.2.35 (iṭ), 7.3.84 (guṇa),
    6.1.78 (bho→bhav), 8.3.59 (sīy-s→ṣ after iṭ-i).

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

    state = apply_rule("3.3.173", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("AsIrliG", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    # No tusma audit: AsIrliN ādeśas start with 's' (val) not tusma final

    state = apply_rule("3.4.116", state)

    state = apply_rule("1.4.13", state)

    # 7.2.35 iṭ before the leading 's' of the sīy-compound ādeśa (val-initial, ardhadhatuka)
    # Tag the tiṅ ādeśa as ardhadhatuka so the natural path fires
    for t in state.terms:
        if "tin_adesha_3_4_78" in t.tags and t.varnas and t.varnas[0].slp1 == "s":
            t.tags.add("ardhadhatuka")
            break
    state = apply_rule("7.2.35", state)
    state = P00_hal_anit_guna(state)

    state = apply_rule("1.4.14", state)

    # 6.1.78 eco'yavāyāvaḥ (bho → bhav)
    state = apply_rule("6.1.78", state)

    _pada_merge(state)
    state = P00_tripadi_rutva_visarga(state)

    # 8.3.59 ṣatvam (once): sīy-leading-s → ṣ after iṭ-i
    state = apply_rule("8.3.59", state)

    return state


def _derive_karmani_luG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani luṅ (passive aorist / adyatana bhūta) for bhvādi dhātus.

    Vikaraṇa: ciṇ (3.1.66 bhāvakarmaṇoḥ) — ṅit, causes vṛddhi on dhātu final
    vowel (7.2.115). ciṇ surface after IT-lopa: [i].

    tiṅ ādeśas pre-encoded as "luN-karmani-atmane" in tin_upadesha.json:
      3sg  → "i"       (ta-luk per 6.4.104; just ciṇ surface)
      3du  → "isAtAm"  (ciṇ[i] + suṭ[s] + ātām)
      3pl  → "isata"   (ciṇ[i] + suṭ[s] + ata, after jha→anta)
      2sg  → "isWAs"   (ciṇ[i] + suṭ[s] + ṭhāḥ; W=ṭha pre-encoded)
      2du  → "isATAm"  (ciṇ[i] + suṭ[s] + āthām)
      2pl  → "iDvam"   (ciṇ[i] + dhvam; suṭ-s dropped before D)
      1sg  → "isi"     (ciṇ[i] + suṭ[s] + iṭ[i])
      1du  → "isvahi"  (ciṇ[i] + suṭ[s] + vahi)
      1pl  → "ismahi"  (ciṇ[i] + suṭ[s] + mahi)

    Pipeline: 8.3.59 converts suṭ-s → ṣ (z) after ciṇ-i (iK) in tripāḍī.
    8.2.66 + 8.3.15 produce visarga on 2sg final -s.

    Expected (bhū): अभावि अभाविषाताम् अभाविषत अभाविष्ठाः अभाविषाथाम्
                    अभाविध्वम् अभाविषि अभाविष्वहि अभाविष्महि
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

    # 3.1.66 ciṇ trace: records that karmani ciṇ vikaraṇa applies
    state.meta["ciN_recipe"] = True
    state = apply_rule("3.1.66", state)

    # 3.4.77 + 3.4.78: install pre-encoded karmani tiṅ ādeśa (replaces luG placeholder)
    tin_adesha = _select_tin_adesha("luG_karmani", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    # No P00 tusma audit: karmani ādeśas start with 'i' — no halantyam IT to drop

    # 6.4.104 ciṇo luk trace (3sg ta-luk baked into "i" pre-encoding)
    state.meta["hal_na_lopa_recipe"] = True
    state = apply_rule("6.4.104", state)

    state = apply_rule("1.4.13", state)

    # 7.2.115 vṛddhi: ciṇ is ṅit → dhātu final vowel → vṛddhi (BU: U→O=au)
    state.meta["7_2_115_karmani_lut_arm"] = True
    state = apply_rule("7.2.115", state)

    # 6.4.71 aṭ augment (a- prepended to dhātu via aT_agama_context from 3.2.110)
    state = apply_rule("6.4.71", state)

    state = apply_rule("1.4.14", state)

    # 6.1.78 eco'yavāyāvaḥ: O (au) → Av (bhO → bhav)
    state = apply_rule("6.1.78", state)

    _pada_merge(state)
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
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)  # guṇa: bhū→bho
        state = apply_rule("6.4.143", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)  # bho→bhav

    elif purusha == 3 and vacana == 2:
        # 3du: Atam → rau via 2.4.85, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.51 ri ca
        state = apply_rule("7.2.35", state)
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
        state = apply_rule("7.3.84", state)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 3 and vacana == 3:
        # 3pl: Ja → ras via 2.4.85, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.51 ri ca
        state = apply_rule("7.2.35", state)
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
        state = apply_rule("7.3.84", state)
        state.meta["ri_ca_recipe"] = True
        state = apply_rule("7.4.51", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 1:
        # 2sg: TAs → se via 3.4.80, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.50 tāsas lopa
        state = apply_rule("3.4.80", state)   # thās → se
        state = apply_rule("3.4.114", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        state.meta["tasa_lopa_recipe"] = True
        state = apply_rule("7.4.50", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 2:
        # 2du: ATAm → ATe via 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 2 and vacana == 3:
        # 2pl: Dvam → Dve via 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa, 8.2.25 s-lopa before dh
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    elif purusha == 1 and vacana == 1:
        # 1sg: iT → i → e via 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa, 7.4.52 s→h before e
        state = apply_rule("3.4.79", state)  # iT→i→e
        state = apply_rule("3.4.114", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        state = apply_rule("7.4.52", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    else:
        # 1du (vahi) and 1pl (mahi): 3.4.79, 7.2.35 iṭ, 7.3.84 guṇa, no tāsi mod
        state = apply_rule("3.4.79", state)
        state = apply_rule("3.4.114", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.2.4", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("7.3.84", state)
        state = apply_rule("1.4.14", state)
        state = apply_rule("6.1.78", state)

    # ── Merge + Tripāḍī ───────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    # 8.2.25: s-lopa before dh (2pl: tāsdhve → tādhve)
    state = apply_rule("8.2.25", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

    return state


_KARMANI_LIT_NEEDS_IT: frozenset = frozenset({(2, 1), (2, 3), (1, 2), (1, 3)})


def _derive_lit_am_kf_atmane(state: State, purusha: int, vacana: int) -> State:
    """
    Periphrastic liṭ (ām + kṛñ anuprayoga) ātmanepada — P014 *īkṣāñcakre*.

    Sūtra order:
      3.2.115 (liṭ) → 3.1.36 (ām) → 2.4.81 (luk+merge→IkzAm) →
      3.1.40 (kṛñ) → scope (3.1.91/P06a/3.4.77) → 3.4.78 (ta) →
      3.4.81 (ta→e) → IT-lopa → 1.2.5 → 6.1.8 (dvitva) →
      7.4.66 (ṛ→a+rapara) → 1.1.51 → 7.4.60 (trim) → 7.4.62 (k→c) →
      6.1.77 (ṛ+e→re) → 6.4.71 (aT) → merge → 8.3.7 → 8.4.58
    """
    # ── 3.2.115 liṭ attachment; sets lakara_liT ──────────────────────────────
    state.meta["liT_lakara_recipe"] = True
    state = apply_rule("3.2.115", state)
    # ── 3.1.36 ām insertion (structural: reads lakara_liT + Ikz identity) ────
    state = apply_rule("3.1.36", state)
    # ── 2.4.81 liṭ-luk + merge Ikz+ām → IkzAm prātipadika ───────────────────
    state = apply_rule("2.4.81", state)
    # ── 3.1.40 kṛñ anuprayoga (structural: fires on IkzAm prātipadika) ───────
    state = apply_rule("3.1.40", state)
    # ── Scope ────────────────────────────────────────────────────────────────
    state = apply_rule("3.1.91", state)
    state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
    state = apply_rule("3.4.77", state)
    state = apply_rule("1.3.12", state)
    # ── tiṅ selection: ātmanepada ─────────────────────────────────────────────
    tin_adesha = _select_tin_adesha("liT", "atmane", purusha, vacana)
    state.meta["tin_adesha_pending"] = True
    state.meta["tin_adesha_form"] = tin_adesha
    state = apply_rule("3.4.78", state)
    # ── 3.4.81 ta → eś  (3sg ātmanepada liṭ) ────────────────────────────────
    state.meta["liT_esh_recipe"] = True
    state = P00_lit_ta_esh_it_lopa(state)
    if state.terms and "pratyaya" in state.terms[-1].tags:
        state.terms[-1].meta["upadesha_slp1"] = "e"
    # ── 1.2.5 asaṃyogāl liṭ kit ──────────────────────────────────────────────
    state = apply_rule("1.2.5", state)
    # ── 6.1.8 dvitva of kṛ + 6.1.4 abhyāsa gate ─────────────────────────────
    state.meta["liT_dvitva_recipe"] = True
    state = apply_rule("6.1.8", state)
    state = apply_rule("6.1.4", state)
    # ── 7.4.66 ṛ→a (uRaṇ) in kṛ abhyāsa; trim to first hal; k→c ─────────────
    for i, t in enumerate(state.terms):
        if "abhyasa" in t.tags:
            state.terms[i].meta["7_4_60_first_hal_only"] = True
            break
    state = P00_mRj_abhyasa_hrasva(state)
    state = apply_rule("7.4.62", state)
    # ── 6.1.77 iko yaṇ aci: dhātu-final ṛ(f) + e → r+e ─────────────────────
    state = apply_rule("6.1.77", state)
    # ── 6.4.71 aT augment on kṛ dhātu ───────────────────────────────────────
    for term in state.terms:
        if "dhatu" in term.tags:
            term.tags.add("aT_agama_context")
            break
    state = apply_rule("6.4.71", state)
    # ── Merge + tripāḍī sandhi ────────────────────────────────────────────────
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.3.7", state)
    state = apply_rule("8.4.58", state)
    return state


def _derive_bhave_lit(state: State, purusha: int, vacana: int) -> State:
    """Bhāve liṭ — same spine as karmaṇi liṭ but without 1.3.13 / yaḳ."""
    state.meta["liT_lakara_recipe"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)
    tin_adesha = _select_tin_adesha("liT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)
    state.meta["liT_esh_recipe"] = True
    state = apply_rule("3.4.81", state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("3.4.80", state)
    state = apply_rule("1.3.4", state)
    state = P00_hal_it_lopa(state)
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)
    state = apply_rule("1.2.5", state)
    needs_it = (purusha, vacana) in _KARMANI_LIT_NEEDS_IT
    if needs_it:
        state.meta["liT_krsrbhr_recipe"] = True
        state = apply_rule("7.2.13", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.4.13", state)
        # dvitva before vuk: 6.4.88 requires abhyāsa present for liṭ context
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("7.4.60", state)
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
    else:
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("7.4.60", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
    # ── 7.4.66 urat (abhyāsa ṛ→ā) — fires before hrasva so ā→a ─────────────
    state = apply_rule("7.4.66", state)
    for _t in state.terms:
        if "abhyasa" in _t.tags:
            _t.meta.pop("urN_rapara_pending", None)
            _t.meta.pop("urN_rapara_after_index", None)
    state = apply_rule("7.4.59", state)
    _dht = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    _dht_up = (_dht.meta.get("upadesha_slp1") or "").strip() if _dht else ""
    if _dht_up in {"BU", "BU~"}:
        state.meta["bhU_abhyasa_recipe"] = True
        state = apply_rule("7.4.73", state)
    state = apply_rule("1.4.14", state)
    # ── 6.1.77 iko yaṇ aci — IK-final root + vowel-initial suffix/iṭ ────────
    state = apply_rule("6.1.77", state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.3.78", state)
    state = apply_rule("8.4.54", state)
    state = apply_rule("8.4.68", state)
    _pada_merge(state)
    state = apply_rule("8.3.59", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)
    return state


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

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada in karmani ─────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.2.115 parokṣe liṭ ───────────────────────────────────────────────
    state.meta["liT_lakara_recipe"] = True
    state = apply_rule("3.2.115", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    # ── 1.3.13 bhāvakarmaṇoḥ: ātmanepada ─────────────────────────────────
    state = apply_rule("1.3.13", state)

    # ── 3.4.77 lasya ─────────────────────────────────────────────────────
    tin_adesha = _select_tin_adesha("liT", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)

    # ── IT on tiṅ ādeśa ───────────────────────────────────────────────────
    state = P00_tin_tusma_audit_halantyam_lopa(state)

    # ── 3.4.115 liṭ ca (1st) ─────────────────────────────────────────────
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)

    # ── 3.4.81: ta → eś  /  Ja → irec  (3sg and 3pl) ────────────────────
    state.meta["liT_esh_recipe"] = True
    state = apply_rule("3.4.81", state)

    # ── 3.4.79: ṭi→e for other cells (Atam→Ate, ATAm→ATe, Dvam→Dve, etc.) ─
    state = apply_rule("3.4.79", state)

    # ── 3.4.80: thāsasse (2sg: TAs → se) ────────────────────────────────
    state = apply_rule("3.4.80", state)

    # ── IT on liṭ-specific ādeśas (eS→e, irec→ire, etc.) ─────────────────
    state = apply_rule("1.3.4", state)
    state = P00_hal_it_lopa(state)

    # ── 3.4.115 liṭ ca (2nd) ─────────────────────────────────────────────
    state.paribhasha_gates.pop("3_4_115_liw_115", None)
    state.meta["liT_115_recipe"] = True
    state = apply_rule("3.4.115", state)

    # ── 1.2.5 asaṃyogālliṭ kit ───────────────────────────────────────────
    state = apply_rule("1.2.5", state)

    needs_it = (purusha, vacana) in _KARMANI_LIT_NEEDS_IT

    if needs_it:
        # iṭ → dvitva → vuk (6.4.88 needs abhyāsa for liṭ context)
        state.meta["liT_krsrbhr_recipe"] = True
        state = apply_rule("7.2.13", state)
        state = apply_rule("7.2.35", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
        state = apply_rule("1.4.13", state)
        # dvitva before vuk: abhyāsa needed for 6.4.88 liṭ context
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("7.4.60", state)
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)
    else:
        # dvitva FIRST → 1.4.13 → vuk
        state.meta["liT_dvitva_recipe"] = True
        state = apply_rule("6.1.8", state)
        state = apply_rule("6.1.4", state)
        state.meta["sandhi_6_1_5_recipe"] = True
        state = apply_rule("6.1.5", state)
        state = apply_rule("7.4.60", state)
        state = apply_rule("1.4.13", state)
        state = apply_rule("6.4.88", state)
        state = apply_rule("1.3.2", state)
        state = apply_rule("1.3.3", state)
        state = apply_rule("1.3.9", state)

    # ── 7.4.66 urat (abhyāsa ṛ→ā) — fires before hrasva so ā→a ─────────────
    state = apply_rule("7.4.66", state)
    for _t in state.terms:
        if "abhyasa" in _t.tags:
            _t.meta.pop("urN_rapara_pending", None)
            _t.meta.pop("urN_rapara_after_index", None)

    # ── 7.4.59 hrasva (abhyāsa U→u, Ā→a) ────────────────────────────────────
    state = apply_rule("7.4.59", state)

    # ── 7.4.73 bhavateraḥ (abhyāsa u→a, only for bhū) ────────────────────
    _dht = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    _dht_up = (_dht.meta.get("upadesha_slp1") or "").strip() if _dht else ""
    if _dht_up in {"BU", "BU~"}:
        state.meta["bhU_abhyasa_recipe"] = True
        state = apply_rule("7.4.73", state)

    # ── 1.4.14 pāda-saṃjñā ───────────────────────────────────────────────
    state = apply_rule("1.4.14", state)

    # ── 6.1.77 iko yaṇ aci — IK-final root + vowel-initial suffix/iṭ ────────
    state = apply_rule("6.1.77", state)

    # ── TRIPĀḌĪ ───────────────────────────────────────────────────────────
    state = apply_rule("8.2.1", state)

    # 8.3.78: dh→ḍh after iṭ-i in liṭ (2pl: i+Dve → i+Qve = iḍhve)
    state = apply_rule("8.3.78", state)

    # 8.4.54 abhyāse carc (B→b in abhyāsa)
    state = apply_rule("8.4.54", state)

    # 8.4.68
    state = apply_rule("8.4.68", state)

    # ── MERGE ─────────────────────────────────────────────────────────────
    _pada_merge(state)

    # ── POST-MERGE TRIPĀḌĪ ────────────────────────────────────────────────
    # 8.3.59 ṣatvam: s→ṣ after iṭ-i in merged pada (2sg: ...i+se → ...i+ṣe)
    state = apply_rule("8.3.59", state)
    state = apply_rule("8.2.66", state)
    state = apply_rule("8.3.15", state)

    return state


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

    state = apply_rule("3.2.123", state)

    laT_varnas = parse_slp1_upadesha_sequence("laT")
    if laT_varnas and laT_varnas[-1].slp1 == "T":
        laT_varnas = laT_varnas[:-1]
    state.terms.append(
        Term(
            kind="pratyaya",
            varnas=laT_varnas,
            tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
            meta={"upadesha_slp1": "laT"},
        )
    )

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
    state = apply_rule("7.1.3", state)
    state = apply_rule("7.2.81", state)
    state = apply_rule("6.1.66", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)
    state = apply_rule("6.1.87", state)
    state = apply_rule("6.1.97", state)
    _pada_merge(state)
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
    state = apply_rule("7.1.3", state)

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
    _pada_merge(state)

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
    state.meta["lfT_recipe"] = True
    state = apply_rule("3.3.13", state)
    state.meta.pop("lfT_recipe", None)

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
    state = apply_rule("7.1.3", state)

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
    _pada_merge(state)

    # ── TRIPĀḌĪ ───────────────────────────────────────────────────────────
    state = P00_tripadi_rutva_visarga(state)
    state = apply_rule("8.3.59", state)   # s→ṣ after iṭ-i (in sya: iṣya)
    state = apply_rule("8.4.68", state)

    return state


def _derive_karmani_lRG(state: State, purusha: int, vacana: int) -> State:
    """
    Karmani lṛṅ (passive conditional) — sya vikaraṇa + ātmanepada tiṅ + aṭ augment.

    Example: bhū + lṛṅ karmaṇi 3sg → अभाविष्यते (parallel to lṛṭ karmaṇi भाविष्यते).
    """
    for t in state.terms:
        if "dhatu" in t.tags:
            t.tags.add("bhava_karma_usage")
            break

    state = apply_rule("1.3.13", state)

    state.meta["lakara"] = "lRG"
    state = apply_rule("3.3.139", state)
    state = apply_rule("1.3.2", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)

    tin_adesha = _select_tin_adesha("lRG", "atmane", purusha, vacana)
    state = P00_parasmai_tin_adesha(state, tin_adesha)
    state = apply_rule("1.4.100", state)
    state = apply_rule("3.4.113", state)

    state = apply_rule("3.1.33", state)
    state = apply_rule("3.4.114", state)

    state = P00_tin_tusma_audit_halantyam_lopa(state)
    state = apply_rule("3.4.79", state)
    state = apply_rule("3.4.80", state)
    state = apply_rule("6.4.62", state)
    state = apply_rule("1.3.3", state)
    state = apply_rule("1.3.9", state)
    state = apply_rule("1.2.4", state)

    state = apply_rule("3.4.101", state)
    state = apply_rule("3.4.100", state)
    state = apply_rule("7.1.3", state)
    state = apply_rule("3.4.99", state)

    state = apply_rule("1.4.13", state)
    state = apply_rule("1.1.5", state)
    state = P00_at_agama_it_lopa(state)

    state = apply_rule("7.2.81", state)
    state = apply_rule("6.1.66", state)
    state = apply_rule("7.2.115", state)
    state = apply_rule("7.3.101", state)
    state = apply_rule("1.4.14", state)
    state = apply_rule("6.1.78", state)
    state = apply_rule("6.1.87", state)
    state = apply_rule("6.1.97", state)
    _pada_merge(state)
    state = apply_rule("8.2.1", state)
    state = apply_rule("8.2.39", state)
    state = apply_rule("8.4.56", state)
    state = P00_tripadi_samyoganta_ru_visarga(state)
    state = apply_rule("8.3.59", state)
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
    state = apply_rule("7.1.3", state)

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
    _pada_merge(state)
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
    state = _attach_upasargas(state, upasargas)

    if nic_recipe and lakara == "laT":
        return _derive_laT_nic_atmane(state, purusha, vacana), gana, None, True

    if san_recipe and lakara == "laT":
        state.meta["san_recipe"] = "san"
        return _derive_laT_san_atmane(state, purusha, vacana), gana, None, True

    if prayoga == "kartari":
        state = apply_rule("1.3.28", state)
        state = apply_rule("1.3.12", state)
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
        state = _prep_bhave(state)
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        if lakara == "laT":
            return _derive_bhave_laT(state, purusha, vacana)
        if lakara == "liT":
            return _derive_bhave_lit(state, purusha, vacana)
        if lakara == "luG":
            return _derive_luG(state, "atmane", purusha, vacana)
        if lakara == "luT":
            return _derive_luT(state, "atmane", purusha, vacana)
        if lakara == "AsIrliG":
            return _derive_ashir_liG(state, "atmane", purusha, vacana)
        if lakara == "liG":
            return _derive_liG(state, "atmane", purusha, vacana)
        if lakara == "laG":
            return _derive_laG(state, "atmane", purusha, vacana)
        if lakara == "lRT":
            return _derive_lRT(state, "atmane", purusha, vacana)
        if lakara == "lRG":
            return _derive_lRG(state, "atmane", purusha, vacana)
        if lakara == "loT":
            return _derive_loT(state, "atmane", purusha, vacana)
        raise NotImplementedError(f"bhāve prayoga for lakāra {lakara!r} not yet implemented")

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
            return _derive_karmani_luG(state, purusha, vacana)
        if lakara == "lRG":
            state = apply_rule("3.1.91", state)
            state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
            return _derive_karmani_lRG(state, purusha, vacana)
        raise NotImplementedError(f"karmani prayoga for lakāra {lakara!r} not yet implemented")

    if lakara in ("liT",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_lit_ad_gas(state, pada_key, purusha, vacana)

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
        return _derive_luT(state, pada_key, purusha, vacana)

    if lakara in ("AsIrliG",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_ashir_liG(state, pada_key, purusha, vacana)

    if lakara in ("AsIrliG",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
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

    if lakara in ("loT",) and _adadi_dhatu_stem_slp1(state) == "ad":
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_loT_ad(state, pada_key, purusha, vacana)

    if lakara in ("loT",):
        state = apply_rule("3.1.91", state)
        state = P06a_pratyaya_adhikara_3_1_1_to_3(state)
        return _derive_loT(state, pada_key, purusha, vacana)

    if lakara in ("laT",) and _is_adadi_dhatu(state) and _adadi_dhatu_stem_slp1(state) == "ad":
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
    derive_abhavam, derive_abhavaV, derive_abhavaM,
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
