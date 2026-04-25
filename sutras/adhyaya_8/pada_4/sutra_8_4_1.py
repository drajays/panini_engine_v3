"""
8.4.1  रषाभ्यां नो णः समानपदे संहितायाम्  —  VIDHI

"Of 'na' and 'ṇa' (standing for the repha / ṣa-letters), in *samānapada*,
*saṃhitāyāṃ*, *ṇ* replaces the *n* (that follows) *r* or *ṣ*; (the *ṛ* extension
in the *śāstra* is read as the same class as *r* in this engine, one varṇa back)."

*Vyavaccheda:* 8.4.2 (अट्कुप्वाङ्नुम् … अपि) is the *vyāya* extension.  This
sūtra is the *ādhya* *saṃnikarṣa* (immediately following varṇa) case within
one *Term* — which models *samānapada* in our linear *State* (see 8.4.2
docstring: cross-*Term* *r* … *n* must not ṅ).

Implementation:  within a single *Term*, if the varṇa immediately before *n* is
*r*, *z* (ष्), *f* or *F* (ऋ-वर्ण, *vārttika*), and *n* is not the absolute
final varṇa of the *State* (8.4.2-style *pada-final* opt-out for *n*), *n* → *R*
(ण्) and tag *natva_done* so 8.4.2 will not re-apply.

*Anuvṛtti (metadata):* *pūrvatrāsiddham* 8.2.1; 8.2.108 *saṃhitā* *adhikāra*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk

# Repha / ṣa, plus ऋ-वर्ण (*ṛ* / *ṝ*) from the *ṛ*-*vārttika* in the *prakriyā* trad.
_RASHA_RI = frozenset({"r", "z", "f", "F"})


def _last_flat_index(state: State) -> tuple[int, int] | None:
    if not state.terms:
        return None
    ti = len(state.terms) - 1
    t = state.terms[ti]
    if not t.varnas:
        return None
    return (ti, len(t.varnas) - 1)


def _find_adjacent_natva(state: State) -> tuple[int, int] | None:
    """
    Return (term_idx, varna_idx) of the *n* to replace, or None.
    *n* must follow *r* / *z* / *f* / *F* in the *same* *Term* with *no* intervening
    *varṇa* (8.4.1 only; 8.4.2 is non-adjacent *vyavāya*).
    """
    for ti, t in enumerate(state.terms):
        for vi in range(1, len(t.varnas)):
            v_prev = t.varnas[vi - 1]
            v_n = t.varnas[vi]
            if v_n.slp1 != "n":
                continue
            if "natva_done" in v_n.tags:
                continue
            if v_prev.slp1 not in _RASHA_RI:
                continue
            last = _last_flat_index(state)
            if last is not None and (ti, vi) == last:
                continue
            return (ti, vi)
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find_adjacent_natva(state) is not None


def act(state: State) -> State:
    hit = _find_adjacent_natva(state)
    if hit is None:
        return state
    ti, vi = hit
    new_varna = mk("R")
    new_varna.tags.add("natva_done")
    state.terms[ti].varnas[vi] = new_varna
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.1",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "samAnapade raSAByAm no RaH saMhitAyAm",
    text_dev       = "समानपदे रषाभ्यां नो णः संहितायाम्",
    padaccheda_dev = "समानपदे / रषाभ्याम् / नो / णः / संहितायाम्",
    why_dev        = "समानपदे रेफ-ष-वर्णाभ्यां (ऋवर्णाद् अपि) ऋणे परस्य न-कारस्य "
                     "सन्निहिते णादेशः (१०८ संहितायाम्, त्रिपादी)।",
    anuvritti_from = ("8.2.1", "8.2.108"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
