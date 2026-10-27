"""engine/taddhita_attach.py — what every taddhita-vidhāyaka sūtra does: put the pratyaya after the prātipadika that ends the tape, once.

The meaning is a frame an ADHIKARA opens (4.1.92 tasyāpatyam: artha ``apatya``, scope to 4.1.178): the pratyaya sūtras after it read that frame, as the
Aṣṭādhyāyī's anuvṛtti does. Which meaning the speaker intends is the vivakṣā ``taddhitArtha``."""
from __future__ import annotations

from engine import gana
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def stem_ends_tape(state: State) -> bool:
    return bool(state.terms) and "prātipadika" in state.terms[-1].tags and state.terms[-1].kind == "prakriti" \
        and not any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms)


def frame_open(state: State, artha: str | None = None) -> bool:
    return any(e.get("artha") and (artha is None or e.get("artha") == artha) for e in state.adhikara_stack)


def taddhita_site(state: State, artha: str | None = None, *, gana_name: str | None = None, final=None, origin: str | None = None):
    """The stem Term when the frame is open, the stem ends the tape and the sūtra's own condition on it holds: membership of a gaṇa, its final
    letters (a predicate on the SLP1 string), the pratyaya it already ends in (``origin``, for gotra-pratyayānta stems)."""
    if not (stem_ends_tape(state) and frame_open(state, artha)):
        return None
    t = state.terms[-1]
    flat = "".join(v.slp1 for v in t.varnas)
    name = t.meta.get("upadesha_slp1") or flat
    if gana_name is not None and not gana.in_gana(gana_name, name):
        return None
    if final is not None and not final(flat):
        return None
    if origin is not None and f"origin_pratyaya:{origin}" not in t.tags:
        return None
    return t


def attach_taddhita(state: State, upadesha_slp1: str) -> State:
    state.terms.append(Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(upadesha_slp1)),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": upadesha_slp1},
    ))
    return state
