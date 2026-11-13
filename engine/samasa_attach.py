"""engine/samasa_attach.py — what every samāsa-vidhāyaka sūtra does: read the two padas of the vākya (stem + sup each, the tape of
engine/tape_init/samasa.py) and make them members of one compound (docs/SAMASA_MACHINE.md, slice 2).

The meaning of the sup (the vibhakti the member stands in) is the sup Term's own saṃjñā tag ``vib:<name>`` (dvitīyā …), put there by the
speaker's vākya; the sūtras say "dvitīyā", "ṣaṣṭhī" … and read exactly that. Which stem is śrita, śauṇḍa, bhaya … is the stem's identity."""
from __future__ import annotations

from engine.gates import adhikara_in_effect
from engine.state import State

CAND = "samasa_cand"


def _stems(state: State) -> list[int]:
    return [i for i, t in enumerate(state.terms) if CAND in t.tags and t.kind == "prakriti"]


def name(t) -> str:
    return t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)


def pair(state: State, sutra_id: str, *, vib: str | None = None, uttara_vib: str | None = None, same_vib: bool = False,
         purva=None, uttara=None, uttara_names: frozenset[str] | None = None):
    """(i, j) of the two candidate stems when the sūtra's conditions hold, else None. ``vib``: the sup after the pūrvapada is of that vibhakti
    (the first term of the sūtra: dvitīyā, ṣaṣṭhī …); ``same_vib``: samānādhikaraṇa (both sups the same vibhakti); ``purva`` / ``uttara``:
    predicates on the stem Terms; ``uttara_names``: the sūtra lists its second member (śrita, atīta …)."""
    if not adhikara_in_effect(sutra_id, state, "2.1.3"):
        return None
    idx = _stems(state)
    if len(idx) != 2:
        return None
    i, j = idx
    if j != i + 2 or i + 1 >= len(state.terms) or "sup" not in state.terms[i + 1].tags:
        return None
    sp = state.terms[i + 1]
    if vib is not None and f"vib:{vib}" not in sp.tags:
        return None
    if uttara_vib is not None and not (j + 1 < len(state.terms) and f"vib:{uttara_vib}" in state.terms[j + 1].tags):
        return None
    if same_vib and not (j + 1 < len(state.terms) and any(x.startswith("vib:") and x in state.terms[j + 1].tags for x in sp.tags)):
        return None
    if purva is not None and not purva(state.terms[i]):
        return None
    if uttara is not None and not uttara(state.terms[j]):
        return None
    if uttara_names is not None and name(state.terms[j]) not in uttara_names:
        return None
    return i, j


def run(state: State, sutra_id: str, *, uttara_vib: str | None = None):
    """The indexes of all candidate stems (two or more) — for the compounds that take any number of members (dvandva, bahuvrīhi)."""
    if not adhikara_in_effect(sutra_id, state, "2.1.3"):
        return None
    idx = _stems(state)
    if len(idx) < 2 or any(b != a + 2 or "sup" not in state.terms[a + 1].tags for a, b in zip(idx, idx[1:])):
        return None
    return idx


def mark(state: State, idx: list[int], kind: str, sutra_id: str) -> State:
    """The members become one compound of this kind (a samāsa saṃjñā): pūrvapada(s) … uttarapada, in the order of the vākya."""
    vibs = {x for i in idx if i + 1 < len(state.terms) for x in state.terms[i + 1].tags if x.startswith("vib:")}
    for n, i in enumerate(idx):
        t = state.terms[i]
        t.tags.discard(CAND)
        t.tags |= {"samasa_member", kind} | ({"samAnADikaraRa"} if len(vibs) == 1 else set())      # the members' sups are of one vibhakti
        if n < len(idx) - 1:
            t.tags.add("samasa_purvapada")
        else:
            t.tags.add("samasa_uttarapada")
    state.meta["samasa_kind"] = kind
    state.meta["samasa_vidhi"] = sutra_id
    return state
