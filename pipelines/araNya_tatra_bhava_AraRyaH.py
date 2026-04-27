"""
pipelines/araNya_tatra_bhava_AraRyaH.py — आरण्यः (अरण्ये भवः) glass-box pipeline.

Semantic contract: "araNye BavaH" (locative + residence/existence sense) from
prātipadika "araNya" (a-stem, napuṃsaka in tradition; engine uses puṃ for
subanta output -H).

Target surface (SLP1): "AraRyaH" (आरण्यः).

This is a minimal pipeline: it reuses canonical scheduling blocks to avoid
duplication (tests/constitutional/test_no_new_duplicates.py).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_adi_vrddhi_then_bha_then_bhasya,
    P00_it_chain_for_nit_taddhita_nya,
    P00_taddhita_internal_Ni_luk_1_2_46_2_4_71,
    P00_taddhita_Ni_locative_then_tatra_bhava_adhikara,
)
from pipelines.subanta import build_initial_state, run_subanta_pipeline

from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA
def _make_araNya_state() -> State:
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("araNya"),
        tags={"anga"},
        meta={"upadesha_slp1": "araNya"},
    )
    # prātipadika for subanta/sup attachment.
    t.tags.add("prātipadika")
    # Linga is mostly irrelevant to this taddhita spine; keep meta for UI.
    s = State(terms=[t], meta={"linga": "napuMsaka"}, trace=[])
    return s


def _append_nya_pratyaya(s: State) -> None:
    """
    Vārttika/gaṇa: "araNyAdibhyaH YyaH" (ñya) in the sense tatra-bhava.

    Engine representation: keep only the **it-marker** 'Y' (ñ) as the upadeśa.
    1.3.5 marks it, 1.3.9 deletes it while preserving `it_markers={'Y'}`,
    which licenses 7.2.117 ādi-vṛddhi; the surface suffix is treated as
    “absorbed” into the stem in this minimal model (target: AraRya).
    """
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Y"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "Y"},
    )
    s.terms.append(pr)


def _structural_merge_to_pratipadika(s: State, *, upadesha_slp1: str) -> State:
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    before = s.flat_slp1()
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__ARANYA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "आरण्य-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "अरण्य + (ञ्य-शेष) → एकं प्रातिपदिकम् (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s


def derive_AraRya_pratipadika() -> State:
    """
    Taddhita leg: araNya + (internal locative Ni) + ñya → AraRya (prātipadika).
    """
    s = _make_araNya_state()

    # I–II. *saptamī* *Ni* + *taddhita* *adhikāra* + **4.3.53** *tatra bhavaḥ*
    s = P00_taddhita_Ni_locative_then_tatra_bhava_adhikara(s)
    _append_nya_pratyaya(s)

    # III–IV. prātipadika + medial *sup* *luk* (shared *Ni*+*taddhita* frame)
    s = P00_taddhita_internal_Ni_luk_1_2_46_2_4_71(s)

    # V. it-saṃjñā + lopa on ñya: need 1.3.5 for initial Y (ñ)
    s = P00_it_chain_for_nit_taddhita_nya(s)

    # VI. aṅga
    # VI–IX. aṅga + ādi-vṛddhi + bha + bhasya
    s = P00_adi_vrddhi_then_bha_then_bhasya(s)

    # Merge into one prātipadika for subanta handoff.
    return _structural_merge_to_pratipadika(s, upadesha_slp1=s.flat_slp1().strip())


def derive_AraRyaH() -> State:
    """
    Full: taddhita stem + subanta prathamā ekavacana (target: AraRyaH).
    """
    t = derive_AraRya_pratipadika()
    stem = t.flat_slp1().strip()
    s = build_initial_state(stem, 1, 1, "pulliṅga")

    # Carry over trace/registries so the final State is a single auditable run.
    s.trace = [dict(st) for st in t.trace]
    s.samjna_registry = dict(t.samjna_registry)
    s.paribhasha_gates = dict(t.paribhasha_gates)
    s.adhikara_stack = [dict(e) for e in t.adhikara_stack]
    s.blocked_sutras = set(t.blocked_sutras)
    s.niyama_gates = dict(t.niyama_gates)
    s.atidesha_map = dict(t.atidesha_map)
    s.vibhasha_forks = [dict(f) for f in t.vibhasha_forks]
    s.nipatana_flag = t.nipatana_flag
    s.tripadi_zone = t.tripadi_zone
    s.phase = t.phase
    s.meta = {**t.meta, **s.meta}
    # Prevent subanta preflight from re-running our generic taddhita avayava hooks.
    s.meta.pop(META_TADDHITA_AVAYAVA, None)
    return run_subanta_pipeline(s)


__all__ = ["derive_AraRya_pratipadika", "derive_AraRyaH"]

