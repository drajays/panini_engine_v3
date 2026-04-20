"""
6.4.148  यस्येति च  —  VIDHI

"Of an aṅga whose final is 'a' or 'i' (+ long variants), before an
 it-initial pratyaya, the final vowel is elided (lopa)."

Reading after anuvṛtti from 6.4.1 (aṅgasya): the *final* vowel of an
aṅga is deleted when the following pratyaya starts with 'i' / 'I'.

Representative logic here — full Pāṇinian nuance (all ā-stem vs.
i-stem distinctions) is handled by additional conditions in a
production file.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State


_FINAL_OK  = frozenset({"A", "I"})      # only dīrgha a/i — hrasva-a goes via guṇa
_NEXT_OK   = frozenset({"i", "I"})


def _find_target(state: State):
    """Return (term_idx, varna_idx) of the aṅga-final vowel to delete,
    or None.

    v3.1 correction: hrasva 'a' is EXCLUDED from this rule — when
    hrasva-a meets i/ī the correct output is guṇa 'e' via 6.1.87,
    not lopa.  6.4.148 applies to dīrgha stems (ā/ī) where the
    vowel is dropped wholesale before the i-pratyaya.
    """
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        anga = state.terms[i]
        nxt  = state.terms[i + 1]
        if "anga" not in anga.tags:
            continue
        if not anga.varnas or not nxt.varnas:
            continue
        last = anga.varnas[-1]
        first = nxt.varnas[0]
        if last.slp1 in _FINAL_OK and first.slp1 in _NEXT_OK:
            return (i, len(anga.varnas) - 1)
    return None


def cond(state: State) -> bool:
    if not adhikara_in_effect("6.4.148", state, "6.4.1"):
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    del state.terms[ti].varnas[vi]
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.148",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yasyeti ca (aNgasya)",
    text_dev       = "यस्येति च (अङ्गस्य)",
    padaccheda_dev = "यस्य इति च — अङ्गस्य",
    why_dev        = "इ-आदि-प्रत्यये परे अङ्गस्य अन्त्यस्य अ/इ-वर्णस्य लोपः।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
