"""
8.2.28  इडादेशे  —  VIDHI (narrow: delete sic 's' after iṭ)

Engine scope: in luṅ glass-box spines, when an iṭ-āgama 'i' has been inserted
immediately before the sic marker 's', delete that 's'. This models the
classical rule that sic disappears in the presence of iṭ (as described in the
user's अलावीत् notes).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.savarna import is_savarna, dirgha_of


def _find(state: State) -> tuple[int, int] | None:
    if not state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    # After structural merge, varṇa tags may be normalized away; so we key off
    # the phonemic neighborhood directly. In our luṅ glass-box spines the sic
    # residue is "si" (after halantyam removes final 'c'), and Īṭ adds leading I
    # to the following apṛkta t, giving "... i + s + i + I + t ...".
    for i in range(1, len(t.varnas) - 1):
        if t.varnas[i].slp1 == "s" and t.varnas[i - 1].slp1 == "i" and t.varnas[i + 1].slp1 in {"i", "I"}:
            return (0, i)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    _ti, i = hit
    t = state.terms[0]
    # Delete the sic 's' after iṭ, then collapse any resulting savarṇa vowel pairs
    # (i+i → I, I+I → I, etc.) locally inside tripāḍī.
    del t.varnas[i]
    # Try up to two local collapses around the deletion site.
    for _ in range(2):
        if not (0 < i < len(t.varnas)):
            break
        v1 = t.varnas[i - 1].slp1
        v2 = t.varnas[i].slp1
        if v1 in {"a", "A", "i", "I", "u", "U", "f", "F", "x", "X"} and v2 in {
            "a", "A", "i", "I", "u", "U", "f", "F", "x", "X",
        } and is_savarna(v1, v2):
            t.varnas[i - 1] = mk(dirgha_of(v1))
            del t.varnas[i]
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.28",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "iD-AdeSe (sici~ s-lopaH)",
    text_dev       = "इडादेशे",
    padaccheda_dev = "इडादेशे",
    why_dev        = "इट्-आगमे सति सिच्-स्थ-सकारस्य लोपः (लुङ्-प्रक्रिया, अलावीत्)।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

