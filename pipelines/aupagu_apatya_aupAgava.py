"""
pipelines/aupagu_apatya_aupAgava.py — औपगवः (उपगोः अपत्यम्) glass-box pipeline.

Goal: derive **औपगवः** from prātipadika **उपगु** under the semantic contract:
“उपगोः अपत्यं पुमान्” (tasya apatyam 4.1.92).

*Cross-check* user note ``…/my panini notes/औपगवः.md``: the **1.1.21** (आद्यन्तवदेकस्मिन्)
*paribhāṣā* is what lets the *ekāksara* **a** of **aṇ** be treated as both *ādi* and *anta*
so **3.1.3** (आद्युदात्तश् च, *adhikāra* via **P06a**) and **7.2.117**+… apply coherently for
*ekā* *varṇa* *pratyaya* (note compares this to *kartavya-*type **tavyat** + **3.1.3** *ādyudātta* in *pariś*).
*Śruti* / svara: v3 does not tag *udātta*/*anudātta* on *varṇa* rows; **1.2.29** / **6.1.158** are
not in this *prakriyā* trace, only the segmental SLP1 surface (``OpagavaH``).

This pipeline uses only `apply_rule` for sūtra applications (CONSTITUTION Art. 11).
The structural merge (``_structural_merge_to_pratipadika``) is not a sūtra.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_anabhihite_shashthi_shese_2_3_50,
    P00_attach_sup_from_pratipadika,
    P00_adi_vrddhi_then_bha_then_bhasya,
    P00_taddhita_samartha_pragdivyata_adhikaras,
    P00_taddhita_aR_it_hal_antyam_slice,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from pipelines.subanta import (
    build_initial_state,
    run_subanta_pipeline,
)
from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA


def _make_upagu_stem_state() -> State:
    upagu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("upagu"),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "upagu"},
    )
    upagu.tags.add("pulliṅga")
    return State(terms=[upagu], meta={"linga": "pulliṅga"}, trace=[])


def _append_taddhita_aR(s: State) -> None:
    pr = Term(
        kind="pratyaya",
        # NOTE: engine's pratyāhāra HAL is derived from Māheśvara-sūtras where
        # the character 'R' is reserved as an it-marker (for YAN). Therefore,
        # we represent aṇ's final ṇ as SLP1 'N' here so halantyam (1.3.3) can
        # treat it as HAL and record it in it_markers for 7.2.117.
        varnas=parse_slp1_upadesha_sequence("aN"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "aN"},
    )
    s.terms.append(pr)


def _structural_merge_to_pratipadika(s: State, *, upadesha_slp1: str) -> State:
    """Structural: merge all Terms into a single prātipadika+aṅga Term."""
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga", "pulliṅga"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    before = s.flat_slp1()
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__AUPAGAVA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "औपगव-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "तद्धित-प्रक्रियायां अङ्ग+प्रत्यय-संयोजनम् (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s


def derive_aupAgava_pratipadika() -> State:
    """
    Taddhita leg only: upagu + (ṣaṣṭhī Nas) + aṇ → aupAgava (SLP1: Opagava).
    """
    s = _make_upagu_stem_state()

    # 1.1.21 — ādyantavad ekasmin; jñāpaka for aṇ's single-a + 3.1.3 (user note, see docstring)
    s = apply_rule("1.1.21", s)

    # I. samarthya + ṣaṣṭhī (semantic contract)
    s = apply_rule("2.1.1", s)
    s.meta["2_3_50_sheSa_shashthi_eligible"] = True
    s = P00_anabhihite_shashthi_shese_2_3_50(s)   # vibhakti_vacana := 6-1

    # sup (ङस् / Nas)
    s = P00_attach_sup_from_pratipadika(s)

    # II. taddhita adhikāras + “tasya apatyam”
    s = P00_taddhita_samartha_pragdivyata_adhikaras(s)
    s = apply_rule("4.1.92", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    _append_taddhita_aR(s)

    # III. prātipadika tagging for the vyutpanna community
    s.meta[META_TADDHITA_AVAYAVA] = True
    s = apply_rule("1.2.46", s)

    # IV. sup-luk (remove Nas)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    # V. it-saṃjñā + lopa on aR (R = it ⇒ ṇit marker recorded)
    s = P00_taddhita_aR_it_hal_antyam_slice(s)

    # VI–VIII. aṅga + ādi-vṛddhi + bha + bhasya
    s = P00_adi_vrddhi_then_bha_then_bhasya(s)
    s = apply_rule("6.4.146", s)

    # X. eco ayavAyAvaH (o + a → av + a)
    s = apply_rule("6.1.78", s)

    # Structural merge to a one-term prātipadika for subanta handoff.
    return _structural_merge_to_pratipadika(s, upadesha_slp1=s.flat_slp1().strip())


def derive_aupAgavaH() -> State:
    """
    Full derivation: taddhita pratipadika + subanta prathamā-ekavacana (puṃ).
    Final expected surface: औपगवः (SLP1: OpagavaH).
    """
    t = derive_aupAgava_pratipadika()
    stem = t.flat_slp1().strip()

    # Subanta leg (reuse canonical pipeline); keep full trace by copying.
    s = build_initial_state(stem, 1, 1, "pulliṅga")
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
    merged_meta = {**t.meta, **s.meta}
    # Prevent a second preflight application of 2.3.50 in the subanta leg.
    merged_meta.pop("2_3_50_sheSa_shashthi_eligible", None)
    merged_meta.pop("2_3_50_override_vibhakti_vacana", None)
    s.meta = merged_meta
    return run_subanta_pipeline(s)


__all__ = ["derive_aupAgava_pratipadika", "derive_aupAgavaH"]

