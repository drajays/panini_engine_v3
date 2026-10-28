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


def taddhita_site(state: State, artha: str | None = None, *, gana_name: str | None = None, final=None, origin: str | None = None,
                  ok: bool | None = None, stems: frozenset[str] | None = None, tag: str | None = None, gana_of: str | None = None,
                  has_tag: str | None = None, lacks: tuple[str, ...] = ()):
    """The stem Term when the frame is open, the stem ends the tape and the sūtra's own condition on it holds: membership of a gaṇa, its final
    letters (a predicate on the SLP1 string), the pratyaya it already ends in (``origin``, for gotra-pratyayānta stems)."""
    if ok is None:
        ok = frame_open(state, artha)         # the frame an ADHIKARA opened (4.1.92 …) — or, when the sūtra names its meaning itself, the vivakṣā it asked (``ok``)
    if not (stem_ends_tape(state) and ok):
        return None
    t = state.terms[-1]
    flat = "".join(v.slp1 for v in t.varnas)
    name = t.meta.get("upadesha_slp1") or flat
    if gana_name is not None and not gana.in_gana(gana_name, name):
        return None
    if stems is not None and name not in stems:
        return None
    if tag is not None and f"lex:{tag}" not in t.tags:
        return None            # a lexical category of the stem (rāga, nakṣatra …): the caller's Lexicon fact, never derived
    if has_tag is not None and has_tag not in t.tags:
        return None            # a saṃjñā the loop itself gave the stem (vṛddha 1.1.73 …)
    if any(f"lex:{x}" in t.tags for x in lacks):
        return None            # the stem must NOT carry these lexical facts (asamāse: a compound is lex:samAsa)
    if gana_of is not None and not gana.in_gana_of_sutra(gana_of, name):
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


def _only_ok(only: dict | None, t: Term) -> bool:
    """The stems a default pratyaya (4.4.1 ṭhak …) is taught for in a sense whose opener names them: any one of the listed stems, a final, a gaṇa, a lexical tag."""
    if not only:
        return True
    flat = "".join(v.slp1 for v in t.varnas)
    name = t.meta.get("upadesha_slp1") or flat
    return (name in only.get("stems", ()) or any(flat.endswith(f) for f in only.get("final", ()))
            or any(gana.in_gana_of_sutra(g, name) for g in only.get("gana", ())) or any(f"lex:{x}" in t.tags for x in only.get("tag", ())))


def open_default_frame(state: State, sid: str, artha: str, dflt: str, group_end: str, only: dict | None = None) -> State:
    """A sense of the 4.4.1 – 74 group (ṭhak) or 4.4.75 – 117 (yat): the sense frame, with the stems its opener limits the default to, and the default's own marker."""
    state.adhikara_stack.append({"id": sid, "scope_end": group_end, "artha": artha, "dflt": dflt, "only": only})
    if not any(e.get("id") == dflt for e in state.adhikara_stack):
        state.adhikara_stack.append({"id": dflt, "scope_end": group_end, "text_dev": dflt})
    return state


def _sid(s: str) -> tuple[int, ...]:
    return tuple(int(x) for x in s.split("."))


def frame_in(state: State, dflt: str, ids: tuple[str, str]) -> bool:
    """Some sense frame of the ``dflt`` group was opened by a sūtra in the range ``ids`` (the ārhīya senses 5.1.37 – 63 of the ṭhañ group)."""
    return any(e.get("dflt") == dflt and e.get("artha") and _sid(ids[0]) <= _sid(e["id"]) <= _sid(ids[1]) for e in state.adhikara_stack)


def default_site(state: State, dflt: str, ids: tuple[str, str] | None = None):
    """The stem Term when some sense frame of the group admits it: the default pratyaya of the group (ṭhak, yat) attaches.
    ``ids``: only frames whose opener lies in this sūtra range (5.1.19 ṭhak reaches the senses 5.1.37 – 63 of the ṭhañ group)."""
    if not stem_ends_tape(state):
        return None
    t = state.terms[-1]
    return t if any(e.get("dflt") == dflt and _only_ok(e.get("only"), t) and (ids is None or _sid(ids[0]) <= _sid(e["id"]) <= _sid(ids[1]))
                    for e in state.adhikara_stack) else None


def group_open(state: State, dflt: str) -> bool:
    """Some sense frame of the group whose default is ``dflt`` is open: its specials apply in every one of its senses (5.1.2 – 4 in the cha group)."""
    return any(e.get("dflt") == dflt and e.get("artha") for e in state.adhikara_stack)
