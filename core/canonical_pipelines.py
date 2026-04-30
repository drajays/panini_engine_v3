"""
Canonical *prakriyā* orchestration: **only** ``apply_rule`` + structural helpers
(CONSTITUTION Art. 3, 7, 11).  Rule *logic* lives in ``sutras/``; *conflict*
resolution is the dispatcher (``asiddha`` / *pratiṣedha* / *rajpopat*), not
recipe list order.
"""
from __future__ import annotations

from collections.abc import Callable

import sutras  # noqa: F401

from engine import apply_rule
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.preflight_lopa_samjna import apply_preflight_luk_samjna_block

from sutras.adhyaya_1.pada_4.sutra_1_4_45 import (
    META_LOCUS_INDICES as META_1_4_45_LOCUS,
)
from sutras.adhyaya_2.pada_3.sutra_2_3_36 import (
    META_LOCATIVE as META_2_3_36_LOCATIVE,
)
from sutras.adhyaya_4.pada_2.sutra_4_2_114 import (
    META_ELIGIBLE_INDICES as META_4_2_114_SHEcA,
)
from sutras.adhyaya_4.pada_3.sutra_4_3_53 import META_ELIGIBLE as META_4_3_53_ELIGIBLE
from sutras.adhyaya_4.pada_3.sutra_4_3_53 import META_JATI_BLOCK as META_4_3_25_JATI

# Same as ``pipelines.subanta.META_SALIYA_TADDHITA_SUBANTA_CONTINUATION`` (avoids
# *subanta* import in ``P01_subanta_bootstrap`` and breaks import cycles).
_META_SALIYA_SUBANTA = "sAlIya_taddhita_subanta_continuation"

# ── *śālā* + *mālā* shared motor (P04–P12) ─────────────────────────────────

def build_salIya_initial_state() -> State:
    """*Śālā* (strī, ā-anta) — see ``pipelines/taddhita_salIya`` long docstring."""
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("SAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    stem.tags.add("strīliṅga")
    stem.tags.add("TAp_anta")
    s = State(terms=[stem])
    s.meta["prakriya_sAlIya"] = True
    s.meta["linga"] = "strīliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta[META_4_3_53_ELIGIBLE] = True
    s.meta.pop(META_4_3_25_JATI, None)
    s.meta[META_2_3_36_LOCATIVE] = "SAlAyAm"
    return s


def build_malIya_initial_state() -> State:
    """
    *Mālā* (strī, ā-anta) for *mālīya* prakriyā — same *Cha* spine as *śālīya*,
    different *prakṛti* and locative note (**2.3.36** registry).
    """
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "mAlA"},
    )
    stem.tags.add("strīliṅga")
    stem.tags.add("TAp_anta")
    s = State(terms=[stem])
    s.meta["prakriya_sAlIya"] = True
    s.meta["prakriya_mAlIya"] = True
    s.meta["linga"] = "strīliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta[META_4_3_53_ELIGIBLE] = True
    s.meta.pop(META_4_3_25_JATI, None)
    s.meta[META_2_3_36_LOCATIVE] = "mAlAyAm"
    return s


def _append_taddhita_cah(s: State) -> None:
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("CaH"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "CaH"},
    )
    s.terms.append(pr)


def _annotate_taddhit_anta_pada(s: State) -> None:
    if not s.meta.get("prakriya_sAlIya"):
        return
    s.meta["taddhitānta_pada_slp1"] = s.flat_slp1()
    t0 = next((t for t in s.terms if t.kind == "prakriti"), None)
    t1 = next(
        (
            t
            for t in s.terms
            if t.kind == "pratyaya"
            and "taddhita" in t.tags
            and not term_is_sup_luk_ghost(t)
        ),
        None,
    )
    if t0 is not None and t1 is not None:
        t0.tags.add("taddhitānta")
        t1.tags.add("taddhitānta")


def P04_taddhita_prathama_sup_block(s: State) -> State:
    """*ṅyāp-prātipadikāt* + *prātipadika* + (optional *strī* ṭāp) + *sup* (4.1.1–4.1.2)."""
    s = apply_rule("4.1.1", s)
    s = apply_rule("1.2.45", s)
    if "TAp_anta" not in s.terms[0].tags:
        s = apply_rule("4.1.3", s)
        s = apply_rule("4.1.4", s)
    s = apply_rule("4.1.2", s)
    return s


def P03_taddhita_karaka_tatra_bhava(s: State) -> State:
    """*samarthā* / *prāg-dīvyat* / *tatra bhava* + *kāraka* / *adhikaraṇa* / saptamī smṛti."""
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.83", s)
    s = apply_rule("4.3.53", s)
    s = P00_locative_adhikarana_to_saptami_2_3_36(s, locus_indices=(0,))
    return s


def P05_vrddha_pada_bootstrap(s: State) -> State:
    """*vṛddhi* / *vṛddha-pada* + *pratyayalakṣaṇa* (1.1.1, 1.1.73, 1.1.62)."""
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = apply_rule("1.1.62", s)
    return s


def P00_vrddhi_prayoga_readiness(s: State) -> State:
    """
    When a downstream sūtra **uses vṛddhi-saṃjñā** for operational work, this
    “readiness” slice is commonly scheduled first (teaching/prayoga order):

      1.1.1 → 1.1.3 → 1.1.4 → 1.1.5 → 1.1.6 → 1.1.50

    It registers the vṛddhi definiens (1.1.1), the *ik* guṇa/vṛddhi gate (1.1.3),
    and the key paribhāṣā gates (1.1.4–1.1.6), plus *sthānāntaratamaḥ* (1.1.50)
    which supplies `sthanantara_vrddhi` / `sthanantara_guna` maps used by vidhis.
    """
    for sid in ("1.1.1", "1.1.3", "1.1.4", "1.1.5", "1.1.6", "1.1.50"):
        s = apply_rule(sid, s)
    return s


def P00_guna_prayoga_readiness(s: State) -> State:
    """
    When a downstream sūtra **uses guṇa-saṃjñā** for operational work, this
    “readiness” slice is commonly scheduled first (teaching/prayoga order):

      1.1.2 → 1.1.3 → 1.1.4 → 1.1.5 → 1.1.6 → 1.1.50

    (Same as vṛddhi slice but without 1.1.1.)
    """
    for sid in ("1.1.2", "1.1.3", "1.1.4", "1.1.5", "1.1.6", "1.1.50"):
        s = apply_rule(sid, s)
    return s


def P00_anabhihite_shashthi_shese_2_3_50(s: State) -> State:
    """Open 2.3.1 and apply 2.3.50 (caller must set eligibility meta)."""
    s = apply_rule("2.3.1", s)
    s = apply_rule("2.3.50", s)
    return s


def P00_attach_sup_from_pratipadika(s: State) -> State:
    """Common subanta/taddhita entry: 4.1.1 → 1.2.45 → 4.1.2."""
    s = apply_rule("4.1.1", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("4.1.2", s)
    return s


def P00_it_halantyam_lopa_yathasankhyam(s: State) -> State:
    """Minimal it chain used in several recipes: 1.3.3 → 1.3.9 → 1.3.10."""
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.3.10", s)
    return s


def P00_dhatu_upadesha_it_lopa(s: State) -> State:
    """Common dhātu bootstrap: 1.3.1 → 1.3.2 → 1.3.3 → 1.3.9."""
    for sid in ("1.3.1", "1.3.2", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    return s


def P00_upadesha_it_1_3_1_2_5(s: State) -> State:
    """Small it-slice used by some dhātu rows: 1.3.1 → 1.3.2 → 1.3.5."""
    for sid in ("1.3.1", "1.3.2", "1.3.5"):
        s = apply_rule(sid, s)
    return s


def P00_upadesha_it_anunasik_hal_lopa(s: State) -> State:
    """Common it-slice: 1.3.2 → 1.3.3 → 1.3.9 (anunāsika + hal)."""
    for sid in ("1.3.2", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    return s


def P00_bhuvadi_dhatu_it_anunasik_hal(s: State) -> State:
    """1.3.1 → *anunāsika*/*hal* *it* slice → drop ``upadesha`` on the primary dhātu."""
    s = apply_rule("1.3.1", s)
    s = P00_upadesha_it_anunasik_hal_lopa(s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    return s


def P00_yang_adhikara_yaG_append_sanadi(s: State) -> State:
    """
    *yaṅ* spine opening shared by *yaṅ*+*aC* glass-box recipes (e.g. *loluv*,
    *marīmṛja*):

    **3.1.22** → **3.1.91** → ``P06a_pratyaya_adhikara_3_1_1_to_3`` → structural
    *yaṅ* → **3.1.32**.
    """
    s = apply_rule("3.1.22", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    yang = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("yaG"),
        tags={"pratyaya", "sanadi", "upadesha"},
        meta={"upadesha_slp1": "yaG"},
    )
    s.terms.append(yang)
    s = apply_rule("3.1.32", s)
    return s


def P00_yang_dvitva_abhyasa_gate(s: State) -> State:
    """**6.1.1** → **6.1.9** → second **6.1.1** (*dvitva*) → **6.1.4** (*pūrvaḥ abhyāsaḥ*)."""
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.9", s)
    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)
    return s


def P00_yang_ac_three_term_frame(s: State) -> State:
    """Reframe as ``[abhyāsa, dhātu, aC]`` with *ārdhadhātuka* ``a`` (*ac*)."""
    ac = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("a"),
        tags={"pratyaya", "upadesha", "ardhadhatuka"},
        meta={"upadesha_slp1": "a"},
    )
    s.terms = [s.terms[0], s.terms[1], ac]
    return s


def P00_yang_luk_2_4_74_and_1_1_4(s: State) -> State:
    """Arm **2.4.74** (*yaṅ*-*luk* before *aC*) and register **1.1.4**."""
    s.meta["2_4_74_yang_luk_arm"] = True
    s = apply_rule("2.4.74", s)
    s = apply_rule("1.1.4", s)
    return s


def P00_subanta_prathama_su_tripadi_visarga(s: State) -> State:
    """Structural *pada* merge + *su* *it* + **8.2.66** / **8.3.15** (*r* / visarga)."""
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s.terms[0].tags.add("prātipadika")
    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_attach_su_it_lopa(s)
    _pada_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


def P00_ciY_dhatu_hal_it_then_bhuvadi(s: State) -> State:
    """**1.3.3** → **1.3.9** (*ñ* *lopa*) → drop ``upadesha`` → **1.3.1** (*ciñ* → *ci*)."""
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.3.1", s)
    return s


def P00_ciY_kartari_krt_nistha_adhikara_prefix(s: State) -> State:
    """
    Shared *kartari* *kṛt* spine before **3.2.102** arms *kta* / *ktavatu~*:

      ``krt_artha`` → **3.1.1–3** → **3.1.91** → **3.4.67**
    """
    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.4.67", s)
    return s


# Alias (broader name for *ktavatu~* recipes beyond *ciñ*).
P00_dhatu_kartari_krt_nistha_adhikara_prefix = P00_ciY_kartari_krt_nistha_adhikara_prefix


def P00_Yanta_hal_dhatu_it_then_bhuvadi(s: State) -> State:
    """*Y*-final *upadeśa* (e.g. ``ciY``, ``stuY``): **1.3.3** → **1.3.9** → *upadeśa* off → **1.3.1**."""
    return P00_ciY_dhatu_hal_it_then_bhuvadi(s)


def P00_anunasikadi_bhuvadi_dhatu_it_chain(s: State) -> State:
    """
    *Bhūvādi* *upadeśa* with medial/final *anunāsika* *ac* *it* (e.g. ``Bidi~``,
    ``mfzu~``): **1.3.1** → **1.3.2** → **1.3.3** → **1.3.9** → drop ``upadesha`` → **1.3.1**.
    """
    s = apply_rule("1.3.1", s)
    for sid in ("1.3.2", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.3.1", s)
    return s


def P00_kF_dhatu_bhuvadi(s: State) -> State:
    """``kF`` (*ḍukṛñ* slice): **1.3.1** (*dhātu*) then drop ``upadesha`` tag."""
    s = apply_rule("1.3.1", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    return s


def P00_ktavatu_kartari_nistha_opening(
    s: State,
    *,
    target_upadesha_slp1: str,
    dhatu_bootstrap: Callable[[State], State],
) -> State:
    """
    Shared *kartari* + *ktavatu~* opening after ``dhatu_bootstrap``:

      **3.2.102** (with ``3_2_102_target_upadesha_slp1``) → *it* chain →
      ``P00_krt_ardhadhatuka_ekac_it_and_guna_audit``.
    """
    s = dhatu_bootstrap(s)
    s = P00_dhatu_kartari_krt_nistha_adhikara_prefix(s)
    s.meta["3_2_102_target_upadesha_slp1"] = target_upadesha_slp1
    s.meta["3_2_102_ktavatu_arm"] = True
    s = apply_rule("3.2.102", s)
    s = P00_lashakvataddhite_anunasikanta_it_lopa_chain(s)
    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)
    return s


def P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(s: State) -> State:
    """Shared *aṅga* + *guṇa* audit: **1.4.13** → **1.1.5** → **7.3.84**."""
    s = apply_rule("1.4.13", s)
    s = apply_rule("1.1.5", s)
    s = apply_rule("7.3.84", s)
    return s


def P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s: State) -> State:
    """
    After *kṛt* *it*-*lopa*: **3.4.114** → *ekāc* *anudātta* *iṭ* block (**7.2.10** /
    **7.2.35**) → ``P00_anga_guna_audit_1_4_13_1_1_5_7_3_84`` (*citaḥ* / *jiṣṇu* …).
    """
    s = apply_rule("3.4.114", s)
    # Compute ekāc dynamically from current dhātu tape (post-it-lopa) if caller
    # has not already provided the flags (e.g. from a dhātupāṭha row).
    from phonology.pratyahara import is_ekac_upadesha

    def _ekac_default() -> bool:
        for t in s.terms:
            if "dhatu" not in t.tags:
                continue
            up = (t.meta.get("upadesha_slp1") or "").strip()
            if up:
                return is_ekac_upadesha(up)
        return is_ekac_upadesha(s.flat_slp1())

    s.meta["ekac_dhatu"] = bool(s.meta.get("ekac_dhatu", _ekac_default()))
    s.meta.setdefault("udatta_dhatu", False)
    s = apply_rule("7.2.10", s)
    s = apply_rule("7.2.35", s)
    s = P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(s)
    return s


def P00_pratipadika_prathama_sup_after_stem_merge(s: State) -> State:
    """
    *Pada* merge of stem → *prātipadika* + *su* *it* + second merge (before Tripāḍī
    *ru* / *visarga* or *ṣ*/*ṇ* clusters).
    """
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s.terms[0].tags.add("prātipadika")
    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_attach_su_it_lopa(s)
    _pada_merge(s)
    return s


def P00_lashakvataddhite_it_lopa_chain(s: State) -> State:
    """Common it-chain for pratyayas like Sap/SyaN: 1.3.3 → 1.3.8 → 1.3.9 → 1.3.10."""
    for sid in ("1.3.3", "1.3.8", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)
    return s


def P00_taddhita_Ni_locative_then_tatra_bhava_adhikara(s: State) -> State:
    """
    Shared opening for *tatra-bhava* recipes with internal *saptamī* *Ni*
    (``araNya``, ``vaipASa``):

      **2.1.1** → **1.2.45** → ``P00_locative_adhikarana_to_saptami_2_3_36`` →
      **4.1.1** → **4.1.2** → ``P00_taddhita_samartha_pragdivyata_adhikaras`` →
      **4.3.53** (caller must arm ``META_ELIGIBLE`` for **4.3.53**) → **3.1.1–3**.
    """
    from sutras.adhyaya_4.pada_3.sutra_4_3_53 import META_ELIGIBLE as _META_453

    s = apply_rule("2.1.1", s)
    s = apply_rule("1.2.45", s)
    s = P00_locative_adhikarana_to_saptami_2_3_36(s, locus_indices=(0,))
    s = apply_rule("4.1.1", s)
    s = apply_rule("4.1.2", s)
    s = P00_taddhita_samartha_pragdivyata_adhikaras(s)
    s.meta[_META_453] = True
    s = apply_rule("4.3.53", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    return s


def P00_taddhita_internal_Ni_luk_1_2_46_2_4_71(s: State) -> State:
    """
    Shared frame after internal *Ni* + *taddhita* ``Term`` is appended (``araNya``,
    ``vaipASa``): **1.2.46** with ``META_TADDHITA_AVAYAVA`` + **2.4.71** *luk*.

    Caller must have set ``META_TADDHITA_AVAYAVA`` and appended the *taddhita*
    ``Term`` (``ñya`` / *aṇ*, …) before calling.
    """
    from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA

    s.meta[META_TADDHITA_AVAYAVA] = True
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    return s


def P00_taddhita_aR_it_hal_antyam_slice(s: State) -> State:
    """
    *It* slice on *aṇ* / *aR* after **2.4.71** (``aupagu``, ``vaipASa``):
    **1.1.60** → **1.3.2** → ``P00_it_halantyam_lopa_yathasankhyam``.
    """
    s = apply_rule("1.1.60", s)
    s = apply_rule("1.3.2", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    return s


def P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s: State) -> State:
    """
    Shared *taddhita*+*internal sup* block after the *taddhita* ``Term`` is on
    the tape (``pipelines/taddhita_itika_etikAyana``, ``pipelines/gomAn_prathamA_go_matup``):

      **1.2.46** → **2.4.71** *luk* → **1.1.62** → **1.4.13**

    Caller must arm ``pratipadika_avayava_ready`` / ``2_4_71_luk_arm`` inputs
    via **1.2.46** / this helper (this routine sets them immediately before
    **2.4.71**).
    """
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("1.1.62", s)
    s = apply_rule("1.4.13", s)
    return s


def P00_matup_it_lopa_chain(s: State) -> State:
    """
    *It*-lopa on *matu~p* (pedagogy order: **1.3.3** *hal* → **1.3.2** *anunāsika*
    → **1.3.9** → **1.3.10**), matching *gomān* / *yavamān* notes.
    """
    for sid in ("1.3.3", "1.3.2", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)
    return s


def P00_ugit_pratipadika_prathama_sup_tail(s: State) -> State:
    """
    Shared *subanta* tail for a single merged *prātipadika* tagged ``ugit``
    (*matup* / *ktavatu~* residues): **4.1.2** *su*, **1.1.43** / **1.1.47** /
    **7.1.70** / **6.4.1+6.4.14**, **1.2.41** + **6.1.68**, *pada* merge,
    **8.2.1** + **8.2.23**.

    Caller supplies ``State`` with exactly one ``Term`` (stem surface already
    merged); this routine adds ``ugit`` / ``prātipadika`` / ``anga`` on
    ``terms[0]`` and sets ``vibhakti_vacana`` to ``1-1``.
    """
    from pipelines.subanta import _pada_merge

    t0 = s.terms[0]
    t0.tags.add("ugit")
    t0.tags.add("prātipadika")
    t0.tags.add("anga")
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta["1_1_43_arm"] = True
    s = apply_rule("4.1.2", s)
    for sid in ("1.3.2", "1.3.9"):
        s = apply_rule(sid, s)
    s = apply_rule("1.1.43", s)
    s.meta.pop("1_1_43_arm", None)
    s = apply_rule("1.1.47", s)
    s.meta["7_1_70_arm"] = True
    s = apply_rule("7.1.70", s)
    s.meta.pop("7_1_70_arm", None)
    s = apply_rule("6.4.1", s)
    s.meta["6_4_14_arm"] = True
    s = apply_rule("6.4.14", s)
    s.meta.pop("6_4_14_arm", None)
    s = apply_rule("1.2.41", s)
    s.meta["6_1_68_arm"] = True
    s = apply_rule("6.1.68", s)
    s.meta.pop("6_1_68_arm", None)
    s = apply_rule("1.4.14", s)
    s = apply_rule("1.1.7", s)
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s.meta["8_2_23_arm"] = True
    s = apply_rule("8.2.23", s)
    s.meta.pop("8_2_23_arm", None)
    return s


def P00_lashakvataddhite_anunasikanta_it_lopa_chain(s: State) -> State:
    """
    *It*-chain for *ktavatu~* (final *anunāsika* *ac* is *it* per **1.3.2**):

      1.3.3 → 1.3.8 → 1.3.2 → 1.3.9 → 1.3.10
    """
    for sid in ("1.3.3", "1.3.8", "1.3.2", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)
    return s


def P00_ciY_ktavatu_nistha_prathama_tail(s: State) -> State:
    """
    *Ciñ* + *ktavatu~* → *citavān* (prathamā-ekavacana): merge **[ci, tavat]**,
    *sup* **4.1.2**, **1.1.43** / **1.1.47** / **7.1.70** / **6.4.1+6.4.14**,
    **1.2.41** + **6.1.68**, *pada* merge, **8.2.1** + **8.2.23**.

    Caller must leave exactly ``[dhātu+pratyaya surface …]`` as two ``Term``s
    after **7.3.84** (same frame as ``P00_pratipadika_prathama_sup_after_stem_merge``
    but *sup* is attached **before** the first merge so **7.1.70** sees two terms).

    Optional ``state.meta["ktavatu_mfz_stuta_arm"]``: after the first merge, run
    **8.4.40** (*z*+*t* → *z*+*w*) under ``8_4_40_pre_tripadi_arm`` (*mṛṣ*+*t*).

    Optional ``state.meta["6_1_111_nn_t_lopa_arm"]``: **6.1.111** on the two-term
    tape before merge (*Binn* + *tavat* → *Binn* + *avat* for *bhid*).
    """
    from pipelines.subanta import _pada_merge

    if s.meta.get("6_1_111_nn_t_lopa_arm"):
        s = apply_rule("6.1.111", s)
    _pada_merge(s)
    if s.meta.pop("ktavatu_mfz_stuta_arm", None):
        s.meta["8_4_40_pre_tripadi_arm"] = True
        s = apply_rule("8.4.40", s)
        s.meta.pop("8_4_40_pre_tripadi_arm", None)
    return P00_ugit_pratipadika_prathama_sup_tail(s)


def P00_luN_lakara_cli_sic(s: State) -> State:
    """
    luṅ spine: attach luG placeholder + cli + sic, then run minimal it-chain on sic.

    Canonicalizes:
      3.2.110 → 3.4.69 → (3.1.43 → 3.1.44) → P00_it_halantyam_lopa_yathasankhyam
    """
    s.meta["3_2_110_luG_arm"] = True
    s = apply_rule("3.2.110", s)
    s = apply_rule("3.4.69", s)
    s.meta["3_1_43_cli_luG_arm"] = True
    s = apply_rule("3.1.43", s)
    s = apply_rule("3.1.44", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    # After it-lopa, ``sic`` is no longer in upadeśa-state; otherwise later generic
    # it-chains (e.g. tiṅ it-lopa in ``P00_tip_to_t_aprkta``) would incorrectly
    # re-tag the remaining ``s`` as halantyam-it and delete it.
    for t in s.terms:
        if (t.meta.get("upadesha_slp1") or "").strip() == "sic":
            t.tags.discard("upadesha")
    return s


def P00_tip_to_t_aprkta(s: State) -> State:
    """
    Canonical tiṅ selection for 3sg parasmaipada in these luṅ recipes:
      3.4.77 → 3.4.78 (+meta tip) → 1.4.99 → it-lopa on tip → 3.4.100 → 1.2.41
    """
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tip"
    s = apply_rule("3.4.78", s)
    s = apply_rule("1.4.99", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("3.4.100", s)
    s = apply_rule("1.2.41", s)
    return s


def P00_tip_to_ti(s: State) -> State:
    """Canonical tiṅ selection for 3sg parasmaipada: 3.4.77 → 3.4.78(tip) → 1.4.99 → it-lopa (p) ⇒ ti."""
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tip"
    s = apply_rule("3.4.78", s)
    s = apply_rule("1.4.99", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


def P00_tin_tas_adesh_full(s: State) -> State:
    """
    *Laṭ* → *tas* (3rd dual *parasmaipada*) with *tiṅ* / *pada* saṃjñā slice.

    Caller must set ``1_4_22_affix_class`` to ``\"dvi\"`` on the primary *dhātu*
    ``Term`` (``dvi_eka_1_4_22.DVI_EKA_NIMITTA_KEY``) before **3.4.77**.
    """
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tas"
    s = apply_rule("3.4.78", s)
    for sid in ("1.4.99", "1.4.100", "1.3.78", "1.4.101", "1.4.108", "1.4.102", "1.4.22"):
        s = apply_rule(sid, s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


def P00_laG_tin_tas_tAm_adesh_block(s: State) -> State:
    """
    *Laṅ* (``state.meta['lakara'] == 'laG'``) → *lac* resolved to *tas*,
    then **3.4.101** *tas* → **tām**, then the usual *tiṅ* / *pada* saṃjñā slice
    and minimal *tin* it-lopa (same trailing block as ``P00_tin_tas_adesh_full``, but with
    **3.4.101** inserted immediately after **3.4.78**).

    Caller must set ``1_4_22_affix_class`` on the *dhātu* Term and already have appended
    the *lac* placeholder (**3.2.111**) before **3.4.77**.
    """
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tas"
    s = apply_rule("3.4.78", s)
    s = apply_rule("3.4.101", s)
    for sid in ("1.4.99", "1.4.100", "1.3.78", "1.4.101", "1.4.108", "1.4.102", "1.4.22"):
        s = apply_rule(sid, s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


def P00_lat_vartamane_tas_and_sap(s: State) -> State:
    """
    Common laṭ 3rd dual *parasmaipada* spine:

      3.1.91 → (3.1.1–3) → 3.2.123 → +laT → ``P00_tin_tas_adesh_full`` → 3.1.68 (*Sap*).
    """
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)
    s = P00_tin_tas_adesh_full(s)
    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)
    return s


def P00_tin_jhi_adesh_full(s: State) -> State:
    """
    *Laṭ* → *jhi* (3rd plural *parasmaipada*) with *tiṅ* / *pada* saṃjñā slice.

    Do **not** set ``1_4_22_affix_class`` for *bahuvacana* (*1.4.22* *cond* false).
    """
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "jhi"
    s = apply_rule("3.4.78", s)
    for sid in ("1.4.99", "1.4.100", "1.3.78", "1.4.101", "1.4.108", "1.4.102", "1.4.22"):
        s = apply_rule(sid, s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


def P00_lat_vartamane_jhi_and_sap(s: State) -> State:
    """
    Common laṭ 3rd plural *parasmaipada* spine:

      3.1.91 → (3.1.1–3) → 3.2.123 → +laT → ``P00_tin_jhi_adesh_full`` → 3.1.68 (*Sap*).
    """
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)
    s = P00_tin_jhi_adesh_full(s)
    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)
    return s


def P00_lat_vartamane_tip_and_sap(s: State) -> State:
    """
    Common laṭ 3sg kartari spine used in demos:
      3.1.91 → (3.1.1–3) → 3.2.123 → +laT (structural) → tip→ti → 3.1.68 (Sap)
    """
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)
    s = P00_tip_to_ti(s)
    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)
    return s


def P00_tripadi_rutva_visarga(s: State) -> State:
    """Common Tripāḍī tail for prathamā-ekavacana su: 8.2.1 → 8.2.66 → 8.3.15."""
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


def P00_ciY_lat_tas_snu_tripadi_tail(s: State) -> State:
    """
    After ``P00_lat_vartamane_tas_and_sap`` (*ciñ* … *tas* + *Sap*):

      **3.1.73** (*śnu* for *Sap*) → *it* on *ś* → **3.4.113** →
      ``P00_anga_guna_audit_1_4_13_1_1_5_7_3_84`` → **1.4.14** → *pada* merge →
      ``P00_tripadi_rutva_visarga`` (*cinutaḥ*).
    """
    s.meta["3_1_73_snu_arm"] = True
    s = apply_rule("3.1.73", s)
    s.meta.pop("3_1_73_snu_arm", None)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = apply_rule("3.4.113", s)
    s = P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(s)
    s = apply_rule("1.4.14", s)
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


def P00_ciY_lat_jhi_snu_tripadi_tail(s: State) -> State:
    """
    After ``P00_lat_vartamane_jhi_and_sap`` (*ciñ* … *jhi* + *Sap*):

      **3.1.73** → *it* → **7.1.3** (*jhi* → *anti*) → **3.4.113** →
      ``P00_anga_guna_audit_1_4_13_1_1_5_7_3_84`` → **6.1.72** → **6.1.77**
      (``6_1_77_ik_yan_aci_general_arm``: *nu* + *anti* → *nv*) → **1.4.14** →
      *pada* merge → ``P00_tripadi_rutva_visarga`` (*cinvanti*).

    *Śāstra note:* **6.4.77** / **6.4.87** (*śnu* + *aca* + *sārvadhātuke*) are not
    split here; the recipe arms only the **6.1.77** *yaṇ* outcome (*cinvanti*).
    """
    s.meta["3_1_73_snu_arm"] = True
    s = apply_rule("3.1.73", s)
    s.meta.pop("3_1_73_snu_arm", None)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s.meta["7_1_3_jho_anta_arm"] = True
    s = apply_rule("7.1.3", s)
    s.meta.pop("7_1_3_jho_anta_arm", None)
    s = apply_rule("3.4.113", s)
    s = P00_anga_guna_audit_1_4_13_1_1_5_7_3_84(s)
    s = apply_rule("6.1.72", s)
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.77", s)
    s.meta.pop("6_1_77_ik_yan_aci_general_arm", None)
    s = apply_rule("1.4.14", s)
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


def P00_attach_su_it_lopa(s: State) -> State:
    """Common prathamā-ekavacana sup: 4.1.2 → 1.3.2 → 1.3.9."""
    for sid in ("4.1.2", "1.3.2", "1.3.9"):
        s = apply_rule(sid, s)
    return s


def P00_taddhita_it_lopa_chain(s: State) -> State:
    """
    Common taddhita it-chain (k-it etc.):
      1.3.3 (halantyam) → 1.3.8 (laśakvataddhite) → 1.3.9 (tasya lopaḥ) → 1.3.10
    """
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.3.10", s)
    return s


def P00_locative_adhikarana_to_saptami_2_3_36(s: State, *, locus_indices=(0,)) -> State:
    """
    Glass-box helper: caller provides locus analysis (1.4.45) and opts into
    deriving vibhakti_vacana from adhikaraṇa via 2.3.36 (→ 7-1).
    """
    from sutras.adhyaya_1.pada_4.sutra_1_4_45 import META_LOCUS_INDICES
    from sutras.adhyaya_2.pada_3.sutra_2_3_36 import META_AUTO_SET_VIBHAKTI_VACANA

    s.meta[META_LOCUS_INDICES] = tuple(locus_indices)
    s = apply_rule("1.4.23", s)
    s = apply_rule("1.4.45", s)
    s.meta[META_AUTO_SET_VIBHAKTI_VACANA] = True
    s = apply_rule("2.3.36", s)
    return s


def P00_taddhita_samartha_pragdivyata_adhikaras(s: State) -> State:
    """Common taddhita entry adhikāras: 4.1.76 → 4.1.82 → 4.1.83."""
    s = apply_rule("4.1.76", s)
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.83", s)
    return s


def P00_adi_vrddhi_then_bha_then_bhasya(s: State) -> State:
    """
    Common glass-box taddhita slice:
      1.4.13 → 6.4.1 → (vṛddhi readiness) → 7.2.117 → 1.4.18 → 6.4.129
    """
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)
    s = P00_vrddhi_prayoga_readiness(s)
    s = apply_rule("7.2.117", s)
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    return s


def P00_it_chain_for_nit_taddhita_nya(s: State) -> State:
    """ñ-it in taddhita (ñya): 1.3.2 → 1.3.5 → 1.3.3 → 1.3.9 → 1.3.10."""
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.5", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.3.10", s)
    return s


def P06a_pratyaya_adhikara_3_1_1_to_3(s: State) -> State:
    """*Dhātu* / *pratyaya* *adhikāra* (**3.1.1**–**3.1.3**) — shared by kṛt and *taddhita* legs."""
    s = apply_rule("3.1.1", s)
    s = apply_rule("3.1.2", s)
    s = apply_rule("3.1.3", s)
    return s


def P06b_pratyaya_through_taddhite_4_1_76(s: State) -> State:
    """**3.1.1**–**3.1.3** + **4.1.76** *taddhite* (before *śeṣe* **4.2.92** in full **P06**)."""
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("4.1.76", s)
    return s


def P06_taddhita_adhikara_stack(s: State) -> State:
    """*pratyaya* (3.1.1–3) + *taddhite* (4.1.76) + *śeṣe* (4.2.92)."""
    s = P06b_pratyaya_through_taddhite_4_1_76(s)
    s = apply_rule("4.2.92", s)
    return s


def P07_cha_vidhanam_4_2_114(s: State) -> State:
    """
    *vṛddhāc chaḥ* + 4.2.71 / 4.2.113 (audit) + *CaH* (structural).
    *Śeṣa* *adhikāra* licence for **4.2.114** is **P06**; *CaH* lives here.
    """
    s.meta[META_4_2_114_SHEcA] = (0,)
    s = apply_rule("4.2.114", s)
    s = apply_rule("4.2.71", s)
    s = apply_rule("4.2.113", s)
    _append_taddhita_cah(s)
    return s


def P02_pratipadika_1_2_46_taddhita_anga(s: State) -> State:
    """*kṛt-tad-dhita* prātipadika on taddhita-anta (1.2.46) + *luk* *arm*."""
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    return s


def P08_sup_luk_2_4_71(s: State) -> State:
    """*sū* *luk* + 1.1.60/61/62 in *luk* order."""
    s = apply_rule("2.4.71", s)
    s = apply_rule("1.1.60", s)
    s = apply_rule("1.1.61", s)
    s = apply_rule("1.1.62", s)
    return s


def P09_anga_6_4_1(s: State) -> State:
    """*aṅga* (1.4.13) + *aṅgasya* (6.4.1)."""
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)
    return s


def P10_chha_to_Iya(s: State) -> State:
    """*gauṇa* 1.1.54, *phadi* 7.1.2, *yathāsaṅkhy* 1.3.10."""
    s = apply_rule("1.1.54", s)
    s = apply_rule("7.1.2", s)
    s = apply_rule("1.3.10", s)
    return s


def P11_bha_adhikara(s: State) -> State:
    """*yaci bha* (1.4.18) + *bhasya* (6.4.129) + paribhāṣā 1.1.52 (when armed)."""
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("1.1.52", s)
    return s


def P12_anga_aa_lopa(s: State) -> State:
    """*yasyeti* (6.4.148) + *lopa* *saṃjñā* (1.1.60)."""
    s = apply_rule("6.4.148", s)
    s = apply_rule("1.1.60", s)
    return s


def P01_taddhita_bootstrap_idle(s: State) -> State:
    """
    *Śālīya* taddhita-anta spine: paribhāṣā **1.1.1/1.1.2/1.1.60**–**1.1.63** is not
    front-loaded; it appears in **P05** and **P08**/**P12** as the recipe demands.
    Identity here keeps the P01 id for tooling without mutating the trace.
    """
    return s


def run_taddhita_salIya_like(s: State, *, pada_merge: bool = False) -> State:
    """
    *śālā* / *mālā* *vṛddhāc-cha* → *īya* (full ``apply_rule`` path).
    """
    s = P01_taddhita_bootstrap_idle(s)
    s = P04_taddhita_prathama_sup_block(s)
    s = P03_taddhita_karaka_tatra_bhava(s)
    s = P05_vrddha_pada_bootstrap(s)
    s = P06_taddhita_adhikara_stack(s)
    s = P07_cha_vidhanam_4_2_114(s)
    s = P02_pratipadika_1_2_46_taddhita_anga(s)
    s = P08_sup_luk_2_4_71(s)
    s = P09_anga_6_4_1(s)
    s = P10_chha_to_Iya(s)
    s = P11_bha_adhikara(s)
    s = P12_anga_aa_lopa(s)
    _annotate_taddhit_anta_pada(s)
    if pada_merge:
        from pipelines.subanta import _pada_merge
        _pada_merge(s)
    return s


def derive_salIya(*, pada_merge: bool = False) -> State:
    return run_taddhita_salIya_like(build_salIya_initial_state(), pada_merge=pada_merge)


def derive_mAlIya(*, pada_merge: bool = False) -> State:
    return run_taddhita_salIya_like(build_malIya_initial_state(), pada_merge=pada_merge)


def derive_salIyaH() -> State:
    from pipelines.subanta import build_initial_state, run_subanta_pipeline  # noqa: PLC0415

    taddh = derive_salIya(pada_merge=False)
    s = build_initial_state(taddh.flat_slp1().strip(), 1, 1, "pulliṅga")
    s.trace = [dict(st) for st in taddh.trace]
    s.samjna_registry = dict(taddh.samjna_registry)
    s.paribhasha_gates = dict(taddh.paribhasha_gates)
    s.adhikara_stack = [dict(e) for e in taddh.adhikara_stack]
    s.blocked_sutras = set(taddh.blocked_sutras)
    s.niyama_gates = dict(taddh.niyama_gates)
    s.atidesha_map = dict(taddh.atidesha_map)
    s.vibhasha_forks = [dict(f) for f in taddh.vibhasha_forks]
    s.nipatana_flag = taddh.nipatana_flag
    s.tripadi_zone = taddh.tripadi_zone
    s.phase = taddh.phase
    merged = {**taddh.meta, **s.meta}
    merged[_META_SALIYA_SUBANTA] = True
    s.meta = merged
    return run_subanta_pipeline(s)


# ── Subanta P01 (bootstrap through 1.4.7) — moved from ``pipelines/subanta`` ─

def P01_subanta_bootstrap(s: State) -> State:
    s = apply_rule("1.4.14", s)
    if s.meta.get("2_3_46_matra_prathama_eligible"):
        s = apply_rule("2.3.1", s)
        s = apply_rule("2.3.46", s)
    if s.meta.get("2_3_50_sheSa_shashthi_eligible"):
        s = P00_anabhihite_shashthi_shese_2_3_50(s)
    s = apply_rule("4.1.1",  s)
    if any("strīliṅga" in t.tags for t in s.terms):
        s = apply_rule("4.1.3", s)
        s = apply_rule("4.1.4", s)
    s = apply_rule("1.1.1",  s)
    s = apply_rule("1.1.73", s)
    s = apply_rule("1.1.2",  s)
    s = P01_samjna_1_1_3_to_1_1_100(
        s,
        include_luk_block=not s.meta.get(_META_SALIYA_SUBANTA),
    )
    s = P01_samjna_1_1_15_to_1_1_24(s)
    s = apply_rule("1.2.72", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.1.27", s)
    s = apply_rule("1.1.29", s)  # *na bahuvrīhau* — strip **1.1.27** *sarvanama* on *bahuvrīhi* *aṅga*
    s = apply_rule("1.1.30", s)  # *tṛtīyā-samāse* — strip *sarvanāma* on *tṛtīyā*-*tatpuruṣa* *aṅga* (**1.1.30**)
    s = apply_rule("1.4.7",  s)
    return s


def P01_samjna_1_1_3_to_1_1_100(s: State, *, include_luk_block: bool) -> State:
    """
    Shared saṃjñā/paribhāṣā slice (used by multiple recipes):

    1.1.3 → 1.1.7 → (optional 1.1.60–1.1.63) → 1.1.8 → … → 1.1.14 → 1.1.100
    """
    s = apply_rule("1.1.3",  s)
    s = apply_rule("1.1.7",  s)
    if include_luk_block:
        s = apply_preflight_luk_samjna_block(s)  # 1.1.60–1.1.63
    s = apply_rule("1.1.8",  s)
    s = apply_rule("1.1.9",  s)
    s = apply_rule("1.1.10", s)
    s = apply_rule("1.1.11", s)
    s = apply_rule("1.1.12", s)
    s = apply_rule("1.1.13", s)
    s = apply_rule("1.1.14", s)
    s = apply_rule("1.1.100", s)
    return s


def P01_samjna_1_1_15_to_1_1_24(s: State) -> State:
    """
    Shared saṃjñā/paribhāṣā slice (used by multiple recipes):

    1.1.15 → 1.1.16 → 1.1.17 → 1.1.18 → 1.1.19 → 1.1.20 → 1.1.21 → 1.1.46 → 1.1.22 → 1.1.23 → 1.1.24
    """
    s = apply_rule("1.1.15", s)
    s = apply_rule("1.1.16", s)
    s = apply_rule("1.1.17", s)
    s = apply_rule("1.1.18", s)
    s = apply_rule("1.1.19", s)
    s = apply_rule("1.1.20", s)
    s = apply_rule("1.1.21", s)
    s = apply_rule("1.1.46", s)
    s = apply_rule("1.1.22", s)
    s = apply_rule("1.1.23", s)
    s = apply_rule("1.1.24", s)
    return s


# Leading *it* spine of ``pipelines.subanta.SUBANTA_RULE_IDS_POST_4_1_2`` (keep in sync).
_SUP_IT_CHAIN: tuple[str, ...] = (
    "1.3.2",
    "1.3.3",
    "1.3.4",
    "1.3.5",
    "1.3.6",
    "1.3.7",
    "1.3.8",
    "1.3.9",
    "1.3.10",
)


def sup_attach_it_chain(s: State) -> State:
    """**4.1.2** *sup* + **1.3.2**–**1.3.10** (*it* saṃjñā / *lopa* / *yathāsaṅkhyam*)."""
    s = apply_rule("4.1.2", s)
    for sid in _SUP_IT_CHAIN:
        s = apply_rule(sid, s)
    return s


# ── Subanta P13–P15: post **4.1.2** through tripāḍī ─────────────────────────

def P13_subanta_iti_anga_sandhi_to_pada(s: State) -> State:
    from pipelines.subanta import (  # noqa: PLC0415
        PADA_MERGE_STEP,
        SUBANTA_RULE_IDS_POST_4_1_2,
        _pada_merge,
    )
    t = SUBANTA_RULE_IDS_POST_4_1_2
    i8 = t.index("8.2.1")
    for rid in t[:i8]:
        if rid == PADA_MERGE_STEP:
            _pada_merge(s)
        else:
            s = apply_rule(rid, s)
    return s


def P14_tripadi_purvakhya_visarga(s: State) -> State:
    """8.2.1 *pūrvatrāsiddham* + 8.2.7 (narrow *krt_tfc*) + 8.2.66 *ru* + 8.3.15 *visarga*."""
    for sid in ("8.2.1", "8.2.7", "8.2.66", "8.3.15"):
        s = apply_rule(sid, s)
    return s


def P15_tripadi_shesha_sibilant_n(s: State) -> State:
    """8.3.59 + 8.4.1 + 8.4.2 (sheṣa tripāḍī in this subanta block)."""
    for sid in ("8.3.59", "8.4.1", "8.4.2"):
        s = apply_rule(sid, s)
    return s


def subanta_post_4_1_2(s: State) -> State:
    s = P13_subanta_iti_anga_sandhi_to_pada(s)
    s = P14_tripadi_purvakhya_visarga(s)
    return P15_tripadi_shesha_sibilant_n(s)


def run_subanta_sup_attach_and_finish(s: State) -> State:
    """*sup* after preflight, then P13–P15."""
    s = apply_rule("4.1.2",  s)
    return subanta_post_4_1_2(s)


__all__ = [
    "P01_subanta_bootstrap",
    "P01_taddhita_bootstrap_idle",
    "P02_pratipadika_1_2_46_taddhita_anga",
    "P03_taddhita_karaka_tatra_bhava",
    "P04_taddhita_prathama_sup_block",
    "P05_vrddha_pada_bootstrap",
    "P06_taddhita_adhikara_stack",
    "P06a_pratyaya_adhikara_3_1_1_to_3",
    "P06b_pratyaya_through_taddhite_4_1_76",
    "P07_cha_vidhanam_4_2_114",
    "P08_sup_luk_2_4_71",
    "P09_anga_6_4_1",
    "P10_chha_to_Iya",
    "P11_bha_adhikara",
    "P12_anga_aa_lopa",
    "P13_subanta_iti_anga_sandhi_to_pada",
    "P14_tripadi_purvakhya_visarga",
    "P15_tripadi_shesha_sibilant_n",
    "build_malIya_initial_state",
    "build_salIya_initial_state",
    "derive_mAlIya",
    "derive_salIya",
    "derive_salIyaH",
    "run_subanta_sup_attach_and_finish",
    "run_taddhita_salIya_like",
    "subanta_post_4_1_2",
    "sup_attach_it_chain",
]
