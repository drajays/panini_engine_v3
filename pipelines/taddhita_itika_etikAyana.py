"""
pipelines/taddhita_itika_etikAyana.py — *itika* + *Ṣaṣ* (*Nas*) + *phak* → *EtikAyana* / *EtikAyanaH*.

**Taddhita phase:** *itika* (prātipadika) + internal *sup* **6-1** (*Nas*), *samarthā*
**4.1.82** + **4.1.92** *apatya*, **4.1.99** *naḍādibhyaḥ phak* (appends *Pak*; *phak* is **kit**),
**1.2.46**, **2.4.71** *luk*; then **7.1.2** *ph*→*Āyana*, **7.2.118**
*kiti ca* (ādi-*vṛddhi* of *i* → *E*), **1.4.18** *bha*, **6.4.129** + **6.4.148**
(final *a* lopa before *Āyana*), **1.1.60** — surface ``EtikAyana`` from
``State.flat_slp1()``.

**Subanta phase (optional):** *prathama* *eka* *puṃ* on ``EtikAyana``;
``derive_EtikAyana_subanta`` runs preflight + **4.1.2** + **6.1.72** + **8.1.16** (user
*śikṣā* for *pada* + *saṃhitā* before **8.2.1**), then ``run_subanta_post_4_1_2`` for
**8.2.66** / **8.3.15** etc. — target ``EtikAyanaH``.
"""
from __future__ import annotations

import sutras  # noqa: F401  (registry)

from engine import apply_rule
from engine.lopa_ghost import term_sup_phonetically_live
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P06b_pratyaya_through_taddhite_4_1_76
from core.canonical_pipelines import P00_attach_sup_from_pratipadika
from core.canonical_pipelines import P00_anabhihite_shashthi_shese_2_3_50
from core.canonical_pipelines import P00_taddhita_it_lopa_chain
from core.canonical_pipelines import P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi
from pipelines.subanta import _pada_merge
from pipelines.subanta import (
    build_initial_state,
    run_subanta_post_4_1_2,
    run_subanta_preflight_through_1_4_7,
)

# User JSON (engine-optimized)
ADHIKARAS: tuple[str, ...] = (
    "4.1.1",
    "4.1.76",
    "4.1.82",
    "6.1.72",
    "6.4.129",
    "8.1.16",
    "8.2.1",
)


def build_itika_phak_initial_state() -> State:
    """*itika* *aṅga*; **4.1.2** will attach *Nas* (6-1) from ``vibhakti_vacana``."""
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("itika"),
        tags={"anga"},
        meta={"upadesha_slp1": "itika"},
    )
    stem.tags.add("pulliṅga")
    s = State(terms=[stem])
    s.meta["prakriya_itika_phak"] = True
    s.meta["linga"] = "pulliṅga"
    # Let 2.3.50 (ṣaṣṭhī śeṣe) set the coordinate in this glass-box pipeline.
    s.meta["2_3_50_sheSa_shashthi_eligible"] = True
    return s


def _annotate_itika_taddhitānta(s: State) -> None:
    if not s.meta.get("prakriya_itika_phak"):
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


def derive_taddhita_itika_EtikAyana() -> State:
    """
    *Taddhita* leg only: ``itika`` + *Nas* + *phak* → ``EtikAyana`` (SLP1 concat).
    """
    s = build_itika_phak_initial_state()
    # Glass-box orchestration (v3.0): use `apply_rule` only; avoid manual
    # pratyaya injection and avoid pipeline-level arming flags.
    #
    # NOTE: A fully universal autonomous taddhita scanner is staged separately
    # (`derive_taddhita_itika_EtikAyana_from_state`) and will replace this once
    # the resolver+lexicon coverage is complete for the 4.1.* domain.
    s = apply_rule("2.1.1", s)
    s = P00_anabhihite_shashthi_shese_2_3_50(s)
    s = P00_attach_sup_from_pratipadika(s)
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.92", s)
    s = apply_rule("4.1.99", s)
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.50", s)
    s = P06b_pratyaya_through_taddhite_4_1_76(s)
    s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)
    s = apply_rule("6.4.1", s)
    s = apply_rule("7.1.2", s)
    s = P00_taddhita_it_lopa_chain(s)
    s = apply_rule("7.2.118", s)
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = apply_rule("1.1.60", s)
    _annotate_itika_taddhitānta(s)
    return s


def derive_taddhita_itika_EtikAyana_from_state(s: State, *, max_steps: int = 400) -> State:
    """
    Scanner-style execution for the itika+phak taddhita leg.

    Rules may apply multiple times; we only suppress exact-repeat “no-progress”
    firings at the same state-site signature.
    """
    from engine.gates import asiddha_violates, is_blocked, is_frozen_by_nipatana
    from engine.registry import get_sutra
    from engine.resolver import resolve
    from engine.trace import TRACE_STATUSES_FIRED

    # Curated pool for this glass-box derivation (no global registry scan).
    pool: list[str] = [
        "2.1.1",
        "2.3.1", "2.3.50",
        "4.1.1", "4.1.2",
        "4.1.76", "4.1.82", "4.1.92", "4.1.99",
        "1.1.1", "1.1.50",
        "3.1.1", "3.1.2", "3.1.3",
        "1.2.45", "1.2.46",
        "2.4.71",
        "1.1.62", "1.4.13",
        "6.4.1",
        "7.1.2",
        "1.3.3", "1.3.8", "1.3.9", "1.3.10",
        "7.2.118",
        "1.4.18",
        "6.4.129", "6.4.148",
        "1.1.60",
    ]

    def _sig(st: State) -> tuple:
        return (
            st.flat_slp1(),
            tuple((t.kind, t.meta.get("upadesha_slp1"), tuple(sorted(t.tags)), len(t.varnas)) for t in st.terms),
            tuple((e.get("id"), e.get("scope_end")) for e in st.adhikara_stack),
            frozenset(st.blocked_sutras),
        )

    no_progress: set[tuple[str, tuple]] = set()
    for _ in range(max_steps):
        # Bridge slice: once the taddhita avayava community is named (1.2.46),
        # we must allow 2.4.71 (*luk*) on the internal sup before downstream
        # aṅgakārya/sandhi can stabilize.  The canonical helper both arms and
        # executes this constitutional block.
        if (
            any(term_sup_phonetically_live(t) for t in s.terms)
            and any(("taddhita" in t.tags and "pratyaya" in t.tags) for t in s.terms)
            and not s.samjna_registry.get("2.4.71")
            and s.samjna_registry.get("1.2.46_generic_pratipadika")
        ):
            s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)

        candidates: list[str] = []
        sig_before = _sig(s)
        for sid in pool:
            rec = get_sutra(sid)
            if is_blocked(sid, s):
                continue
            if asiddha_violates(sid, s):
                continue
            if is_frozen_by_nipatana(rec.sutra_type, s):
                continue
            if (sid, sig_before) in no_progress:
                continue
            if rec.cond is not None and rec.cond(s):
                candidates.append(sid)

        if not candidates:
            _annotate_itika_taddhitānta(s)
            return s

        winner = resolve(candidates, s)
        before_len = len(s.trace)
        s2 = apply_rule(winner, s)
        if len(s2.trace) > before_len:
            last = s2.trace[-1]
            if last.get("sutra_id") == winner and last.get("status") in TRACE_STATUSES_FIRED:
                if _sig(s2) == sig_before:
                    no_progress.add((winner, sig_before))
        s = s2

    raise RuntimeError(f"itika-phak taddhita scanner exceeded max_steps={max_steps}; last: {s.flat_slp1()!r}")


def derive_EtikAyana_subanta_from_state(s: State) -> State:
    """
    Continue as *subanta* (prathamā-ekavacana-puṃ) on the current state without
    flatten+rebuild.  Structural `pada` merge keeps the derivational memory in
    one continuous `State.trace`.
    """
    _pada_merge(s)
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    # Clear taddhita-phase śeṣe/ṣaṣṭhī eligibility so subanta preflight doesn't
    # overwrite nominative intent.
    s.meta.pop("2_3_50_sheSa_shashthi_eligible", None)
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    s = apply_rule("6.1.72", s)
    s = apply_rule("8.1.16", s)
    s = run_subanta_post_4_1_2(s)
    return s


def derive_EtikAyana_subanta() -> State:
    """
    Backward-compatible wrapper: start from a fresh initial state for
    ``EtikAyana`` and derive ``EtikAyanaH``.
    """
    s = build_initial_state("EtikAyana", 1, 1, "pulliṅga")
    return derive_EtikAyana_subanta_from_state(s)


def derive_itika_EtikAyanaH() -> State:
    """Single continuous derivation: ``itika`` → ``EtikAyana`` → ``EtikAyanaH``."""
    s = derive_taddhita_itika_EtikAyana()
    return derive_EtikAyana_subanta_from_state(s)


def derive_full_itika_EtikAyanaH() -> tuple[State, State]:
    """
    Returns ``(taddhita_state, subanta_state)`` — two traces; *nom.* *sg.* *puṃ*
    ``EtikAyanaH`` is ``subanta_state.flat_slp1()``.
    """
    t = derive_taddhita_itika_EtikAyana()
    b = derive_EtikAyana_subanta()
    return t, b
