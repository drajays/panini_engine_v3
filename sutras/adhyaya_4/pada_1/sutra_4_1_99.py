"""
4.1.99  नडादिभ्यः फक्  —  VIDHI (glass-box narrow)

In a zero-patchwork engine, *phak* must be appended by the sūtra's own `act()`,
not by an external pipeline helper.

This implementation is intentionally *narrow* (glass-box recipe support): it
fires when:
- the *apatya* adhikāra (**4.1.92**) is in effect, and
- the current *aṅga* belongs to a small *naḍādi* membership set (v3.0: minimal
  lexicon, starting with ``itika``).

This avoids pipeline-level “arming” meta and keeps the suffix insertion inside
the sūtra's own `act()`.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.gates import adhikara_in_effect
from phonology.varna import parse_slp1_upadesha_sequence


_NADADI_BASES = frozenset({"itika"})


def _site(state: State) -> int | None:
    # Require *apatya* scope; otherwise 4.1.99 should be invisible.
    if not adhikara_in_effect("4.1.99", state, "4.1.92"):
        return None
    if not state.terms:
        return None
    # Lexical membership (minimal v3.0): only specific naḍādi bases.
    t0 = state.terms[0]
    base = (t0.meta.get("upadesha_slp1") or "").replace("~", "").strip()
    if base not in _NADADI_BASES:
        return None
    # If a taddhita pratyaya is already present, do nothing.
    if any(("taddhita" in t.tags and "pratyaya" in t.tags) for t in state.terms):
        return None
    return len(state.terms) - 1


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Pak"),
        tags={"pratyaya", "taddhita", "upadesha", "kit"},
        meta={"upadesha_slp1": "Pak"},
    )
    state.terms.append(pr)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.99",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "naDAdibhyaH Pak",
    text_dev       = "नडादिभ्यः फक्",
    padaccheda_dev = "नड-आदिभ्यः / फक्",
    why_dev        = "नडादि-गण-आधारेण (अपत्याधिकारः ४.१.९२) *फक्* तद्धित-प्रत्यय-विधानम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

