"""
7.2.115  अचो ञ्णिति  —  VIDHI

When a following pratyaya is **ñit** or **ṇit**, the **final vowel** (*ac*)
of the *aṅga* receives *vṛddhi* (operational mapping to ``A`` / ``E`` / ``O``
in SLP1).

Narrow use: kṛt ``Nvul`` path where upadhā-vṛddhi (**7.2.116**) does not
apply (e.g. ``nI`` + ``ak`` → ``nE`` + ``ak`` for नायक).
"""
from __future__ import annotations

from typing import Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _vrddhi_vowel(ch: str, state: State) -> Optional[str]:
    """Map final ``ac`` to vṛddhi letter (SLP1), using optional sthānāntara gate."""
    st = state.paribhasha_gates.get("sthanantara_vrddhi") or {}
    if ch in st:
        return st[ch]
    if ch in ("a",):
        return "A"
    if ch in ("i", "I"):
        return "E"
    if ch in ("u", "U"):
        return "O"
    if ch in ("f", "F", "x", "X"):
        return None
    if ch in ("e", "E", "o", "O"):
        return ch
    return None


def _find(state: State):
    if len(state.terms) < 2:
        return None
    dhatu = next((t for t in state.terms if "dhatu" in t.tags), None)
    if dhatu is None:
        return None
    pr = state.terms[-1]
    if "krt" not in pr.tags:
        return None
    if dhatu.meta.get("aco_nniti_vrddhi_done"):
        return None
    if dhatu.meta.get("dIdhIvevI_guna_vrddhi_nishedha"):
        return None
    itm = pr.meta.get("it_markers", set())
    if not isinstance(itm, set):
        return None
    if not (("Y" in itm) or ("N" in itm) or ("R" in itm)):
        return None
    if not dhatu.varnas:
        return None
    last = dhatu.varnas[-1].slp1
    # Paninian ``ac`` (अच्) — hrasva + dīrgha; ``AC`` pratyāhāra here is short-only.
    if not (is_hrasva(last) or is_dirgha(last)):
        return None
    rep = _vrddhi_vowel(last, state)
    if rep is None:
        return None
    di = state.terms.index(dhatu)
    return (di, len(dhatu.varnas) - 1, rep)


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi, rep = hit
    state.terms[ti].varnas[vi] = mk(rep)
    state.terms[ti].meta["aco_nniti_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.115",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "acaH YRiti",
    text_dev       = "अचो ञ्णिति",
    padaccheda_dev = "अचः ञ्-णिति",
    why_dev        = "ञित्/णिति-परे अङ्गान्त्यचः वृद्धिः (णीञ्+ण्वुल् → नै/नायक)।",
    anuvritti_from = ("7.2.114",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
