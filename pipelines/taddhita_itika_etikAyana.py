"""
pipelines/taddhita_itika_etikAyana.py — *itika* + *Ṣaṣ* (*Nas*) + *phak* → *EtikAyana* / *EtikAyanaH*.

**Scope (user *adhikāra* + *whitelist*):** ``ADHIKARAS`` and ``WHITELIST`` below
match the engine-optimized *prakriyā* prompt; *optional* ``validate_trace_against_whitelist``
filters *APPLIED* *sūtra* rows to that set (UI / tests).

**Taddhita phase:** *itika* (prātipadika) + internal *sup* **6-1** (*Nas*), *samarthā*
**4.1.82** + **4.1.92** *apatya*, **4.1.99** *naḍādibhyaḥ phak* (ANUVADA trace;
*phak* is **kit**), **1.2.46**, **2.4.71** *luk*; then **7.1.2** *ph*→*Āyana*, **7.2.118**
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

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

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
WHITELIST: frozenset[str] = frozenset(
    {
        "4.1.1", "4.1.2", "4.1.76", "4.1.82", "4.1.92", "4.1.99",
        "1.2.45", "1.2.46", "2.4.71", "1.1.60", "1.1.62",
        "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8", "1.3.9",
        "1.4.13", "3.1.1", "3.1.2", "3.1.3", "7.1.2", "1.3.10", "7.2.118", "1.1.1", "1.1.50",
        "1.4.18", "6.4.1", "6.4.129", "6.4.148", "8.1.16", "8.2.1", "8.2.66", "8.3.15",
    }
)


def validate_trace_against_whitelist(
    s: State,
    *,
    allowed: frozenset[str] | set[str] | None = None,
) -> list[str]:
    """
    Return *sūtra* ids that appear *APPLIED* in ``s.trace`` but are *not* in
    ``allowed`` (default: ``WHITELIST``).  Empty list ⇒ all *APPLIED* rows are
    in the set (structural / ``__MERGE__`` steps ignored).
    """
    allow = WHITELIST if allowed is None else allowed
    bad: list[str] = []
    for row in s.trace:
        if row.get("status") != "APPLIED":
            continue
        sid = row.get("sutra_id")
        if not sid or sid == "__MERGE__":
            continue
        if sid not in allow:
            bad.append(sid)
    return bad


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
    s.meta["vibhakti_vacana"] = "6-1"
    return s


def _append_taddhita_Pak(s: State) -> None:
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Pak"),
        tags={"pratyaya", "taddhita", "upadesha", "kit"},
        meta={"upadesha_slp1": "Pak"},
    )
    s.terms.append(pr)


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
    s = apply_rule("4.1.1", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("4.1.2", s)
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.92", s)
    s.meta["4_1_99_prayoga"] = "naDAdi_Pak"
    s = apply_rule("4.1.99", s)
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.50", s)
    s = apply_rule("3.1.1", s)
    s = apply_rule("3.1.2", s)
    s = apply_rule("3.1.3", s)
    s = apply_rule("4.1.76", s)
    _append_taddhita_Pak(s)
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)
    s = apply_rule("1.1.62", s)
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)
    s = apply_rule("7.1.2", s)
    s = apply_rule("1.3.10", s)
    s = apply_rule("7.2.118", s)
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = apply_rule("1.1.60", s)
    _annotate_itika_taddhitānta(s)
    return s


def derive_EtikAyana_subanta() -> State:
    """
    *Subanta* on ``EtikAyana``: *prathama* *eka* *puṃ*; includes **6.1.72** and
    **8.1.16** before the standard post-**4.1.2** block (so **8.2.1** is under
    *pada* / *saṃhitā* *adhikāra* as in the user *śikṣā*).
    """
    s = build_initial_state("EtikAyana", 1, 1, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    s = apply_rule("6.1.72", s)
    s = apply_rule("8.1.16", s)
    s = run_subanta_post_4_1_2(s)
    return s


def derive_full_itika_EtikAyanaH() -> tuple[State, State]:
    """
    Returns ``(taddhita_state, subanta_state)`` — two traces; *nom.* *sg.* *puṃ*
    ``EtikAyanaH`` is ``subanta_state.flat_slp1()``.
    """
    t = derive_taddhita_itika_EtikAyana()
    b = derive_EtikAyana_subanta()
    return t, b
