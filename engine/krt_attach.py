"""engine/krt_attach.py — the one operation every kṛt-vidhāyaka sūtra performs: put the upadeśa of the pratyaya after the dhātu.

DAtoH … paraH (3.1.91, 3.1.2): the dhātu must end the tape, so the affix is attached once. Its it-letters are left to the it-prakaraṇa
(1.3.2–1.3.9) and its ārdhadhātuka-saṃjñā to 3.4.114, exactly as for ktvā (3.4.21)."""
from __future__ import annotations

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def dhatu_ends_tape(state: State) -> bool:
    return bool(state.terms) and "dhatu" in state.terms[-1].tags and not any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms)


def attach_krt(state: State, upadesha_slp1: str) -> State:
    state.terms.append(Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(upadesha_slp1)),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": upadesha_slp1},
    ))
    return state


# --- the kṛtya family (3.1.95–3.1.132): each sūtra offers its affix beside the others; the reading takes one -------------

def kftya_stem(state: State) -> str:
    """The dhātu as it stands on the tape (it-letters gone), slp1."""
    return "".join(v.slp1 for v in state.terms[-1].varnas) if state.terms else ""


def kftya_open(state: State, sutra_id: str) -> bool:
    """The speaker means a kṛtya (vivakṣā), the dhātu ends the tape, and this sūtra has not already been declined."""
    from engine.vivaksha import vivaksita
    return not state.meta.get(f"kftya_declined:{sutra_id}") and vivaksita(state, "krt", "kftya") and dhatu_ends_tape(state)


def kftya_attach(state: State, sutra_id: str, upadesha_slp1: str, *, bars: tuple[str, ...] = (), nitya: bool = False) -> State:
    """Attach ``upadesha_slp1`` or decline (engine.vikalpa.choose({sutra_id: 1})). An apavāda (``bars``) takes its utsarga's
    site away whether it attaches or the speaker prefers a sibling kṛtya, so its decline closes those sūtras too."""
    from engine.vikalpa import policy_pick
    if nitya or policy_pick(state, sutra_id, 2) == 0:
        return attach_krt(state, upadesha_slp1)
    state.meta[f"kftya_declined:{sutra_id}"] = True
    for b in bars:
        state.meta[f"kftya_declined:{b}"] = True
    return state
