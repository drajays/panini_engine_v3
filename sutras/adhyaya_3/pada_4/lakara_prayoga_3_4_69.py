"""
3.4.69 — modular helpers: *lac*-prayoga licencing (kartari / karmaṇi / bhāve).

Not a sūtra file.  Used by ``sutra_3_4_69.py`` and (later) tíṅanta / *lac* recipes.

*Śāstra (one line):* for *sakarmaka* roots, *lac* in kartari and karmaṇi; for *akarmaka*
roots, in kartari and bhāve.  *Sakarmaka* used without a *karman* (*avivakṣita-karman*)
is classed *akarmaka* for this purpose (Kāś. on 3.4.69).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from engine.state import State, Term

# Stable gate prefix so downstream sūtras can consult without string typos.
GATE_PFX = "prayoga_3_4_69"


def effective_karmakatva_for_lac(term: Term) -> Optional[str]:
    """
    Return an internal label used only to compute paribhāṣā gates:

    - ``sakarmaka`` — *dvy-artha* / *sakarmaka* in full sense → kartari + karmaṇi
    - ``akarmaka`` — *nityākarmaka* / *akarmaka* → kartari + bhāve, not karmaṇi
    - ``sakarmaka_candra`` — *sakarmaka* with *anādarita-karman* (teaching: treat like
      *akarmaka* for prayoga: kartari + bhāve, not karmaṇi locus in the same way)
    """
    if "dhatu" not in term.tags:
        return None
    raw = term.meta.get("karmakatva")
    if raw is None:
        return None
    if raw == "dvyarma":
        raw = "sakarmaka"
    if raw not in ("sakarmaka", "akarmaka"):
        return None
    if raw == "sakarmaka" and bool(term.meta.get("avivakshita_karma")):
        return "sakarmaka_candra"
    return raw


def dhatu_slp1_snapshot(term: Term) -> str:
    m = (term.meta.get("upadesha_slp1") or "").strip()
    if m:
        return m
    return "".join(v.slp1 for v in term.varnas)


def build_gates(eff: str, dhatu_slp1: str) -> Dict[str, Any]:
    """
    Boolean licences (downstream *prayoga* / *lakāra* logic may read these only).

    For *sakarmaka*: *kartari* + *karmaṇi* (not the *bhāve* distribution of 3.4.69
    in the *akarmaka* half).

    For *akarmaka* and *sakarmaka* with *anādarita-karman*: *kartari* + *bhāve*.
    """
    g: Dict[str, Any] = {
        f"{GATE_PFX}_dhatu_upadesha": dhatu_slp1,
        f"{GATE_PFX}_effective_karmakatva": eff,
    }
    if eff == "sakarmaka":
        g[f"{GATE_PFX}_licenses_kartari"] = True
        g[f"{GATE_PFX}_licenses_karmani"] = True
        g[f"{GATE_PFX}_licenses_bhave"] = False
    elif eff in ("akarmaka", "sakarmaka_candra"):
        g[f"{GATE_PFX}_licenses_kartari"] = True
        g[f"{GATE_PFX}_licenses_karmani"] = False
        g[f"{GATE_PFX}_licenses_bhave"] = True
    else:
        g[f"{GATE_PFX}_licenses_kartari"] = False
        g[f"{GATE_PFX}_licenses_karmani"] = False
        g[f"{GATE_PFX}_licenses_bhave"] = False
    return g


def find_lac_prayoga_terms(state: State) -> List[Tuple[int, Term]]:
    """(index, term) for terms tagged *dhatu* with usable *karmakatva*."""
    out: list[Tuple[int, Term]] = []
    for i, t in enumerate(state.terms):
        if effective_karmakatva_for_lac(t) is not None:
            out.append((i, t))
    return out
