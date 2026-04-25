"""
Canonical *prakriyā* orchestration: **only** ``apply_rule`` + structural helpers
(CONSTITUTION Art. 3, 7, 11).  Rule *logic* lives in ``sutras/``; *conflict*
resolution is the dispatcher (``asiddha`` / *pratiṣedha* / *rajpopat*), not
recipe list order.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
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
    if (
        len(s.terms) >= 2
        and s.terms[0].kind == "prakriti"
        and s.terms[1].kind == "pratyaya"
        and "taddhita" in s.terms[1].tags
    ):
        s.terms[0].tags.add("taddhitānta")
        s.terms[1].tags.add("taddhitānta")


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
    s.meta[META_1_4_45_LOCUS] = (0,)
    s = apply_rule("1.4.23", s)
    s = apply_rule("1.4.45", s)
    s = apply_rule("2.3.36", s)
    return s


def P05_vrddha_pada_bootstrap(s: State) -> State:
    """*vṛddhi* / *vṛddha-pada* + *pratyayalakṣaṇa* (1.1.1, 1.1.73, 1.1.62)."""
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = apply_rule("1.1.62", s)
    return s


def P06_taddhita_adhikara_stack(s: State) -> State:
    """*pratyaya* (3.1.1–3) + *taddhite* (4.1.76) + *śeṣe* (4.2.92)."""
    s = apply_rule("3.1.1", s)
    s = apply_rule("3.1.2", s)
    s = apply_rule("3.1.3", s)
    s = apply_rule("4.1.76", s)
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
    """8.2.1 *pūrvatrāsiddham* + 8.2.66 *ru* + 8.3.15 *visarjanīya*."""
    for sid in ("8.2.1", "8.2.66", "8.3.15"):
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
]
