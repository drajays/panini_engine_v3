"""
pipelines/taddhita.py — canonical taddhita derivation functions.

Exposes glass-box taddhita prakriyās without demo-specific naming.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P06b_pratyaya_through_taddhite_4_1_76,
    P00_anabhihite_shashthi_shese_2_3_50,
    P00_attach_sup_from_pratipadika,
    P00_taddhita_it_lopa_chain,
    P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi,
)
from pipelines.subanta import (
    _pada_merge,
    run_subanta_preflight_through_1_4_7,
    run_subanta_sup_attach_and_finish,
)
from sutras.adhyaya_2.pada_3.sutra_2_3_50 import (
    META_OVERRIDE_VV as META_2_3_50_OVERRIDE_VV,
    META_SHESE_ELIGIBLE as META_2_3_50_ELIGIBLE,
)
from sutras.adhyaya_1.pada_3.sutra_1_3_7 import META_P004_B_Yya_CUTU


def _normalize_merged_pratipadika(s: State, *, upadesha_slp1: str) -> None:
    if not s.terms:
        return
    t0 = s.terms[0]
    t0.kind = "prakriti"
    for tg in ("prātipadika", "anga", "pulliṅga"):
        t0.tags.add(tg)
    t0.tags.discard("pada")
    t0.meta["upadesha_slp1"] = upadesha_slp1


def derive_kauYjAyanyaH() -> State:
    """
    P004-A: kuñja + cphaña (4.1.98) + yañ (4.1.105) → kauñjāyanyaḥ
    — pulliṅga prathamā ekavacana.
    """
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kuYja")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "kuYja"},
    )
    stem.tags.add("pulliṅga")
    s = State(terms=[stem], meta={}, trace=[])
    s.meta["caPhaya_taddhita_frame"] = True
    s.meta["linga"] = "pulliṅga"
    s.meta[META_2_3_50_ELIGIBLE] = True

    s = apply_rule("2.1.1", s)
    s = P00_anabhihite_shashthi_shese_2_3_50(s)
    s = P00_attach_sup_from_pratipadika(s)
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.92", s)
    s = apply_rule("4.1.98", s)

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.50", s)
    s = P06b_pratyaya_through_taddhite_4_1_76(s)
    s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)

    s = apply_rule("6.4.1", s)
    for sid in ("1.3.7", "1.3.3", "1.3.8", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)

    s = apply_rule("7.1.2", s)
    s = P00_taddhita_it_lopa_chain(s)

    s = apply_rule("7.2.117", s)
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = apply_rule("1.1.60", s)

    _pada_merge(s)
    _normalize_merged_pratipadika(s, upadesha_slp1="kauYjAyana")

    # Stage 2: yuvāpatya yañ
    s = apply_rule("4.1.105", s)

    s = apply_rule("6.4.1", s)
    for sid in ("1.3.3", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)

    _pada_merge(s)
    _normalize_merged_pratipadika(s, upadesha_slp1="kauYjAyanaya")

    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta.pop(META_2_3_50_ELIGIBLE, None)
    s.meta.pop(META_2_3_50_OVERRIDE_VV, None)
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


def derive_SANqikyaH() -> State:
    """
    P004-B: śaṇḍika (SaRqika) + ñya (4.3.92) → śāṇḍikyaḥ
    — pulliṅga prathamā ekavacana.
    """
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("SaRqika")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "SaRqika"},
    )
    stem.tags.add("pulliṅga")
    s = State(terms=[stem], meta={}, trace=[])
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"

    s = apply_rule("2.1.1", s)
    s = P00_attach_sup_from_pratipadika(s)
    s = apply_rule("4.3.92", s)

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.50", s)
    s = P06b_pratyaya_through_taddhite_4_1_76(s)
    s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)

    s = apply_rule("6.4.1", s)
    s.meta[META_P004_B_Yya_CUTU] = True
    for sid in ("1.3.7", "1.3.3", "1.3.8", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)

    s = apply_rule("7.2.117", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)

    _pada_merge(s)
    if s.terms:
        t0 = s.terms[0]
        t0.kind = "prakriti"
        for tg in ("prātipadika", "anga", "pulliṅga"):
            t0.tags.add(tg)
        t0.tags.discard("pada")

    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s
