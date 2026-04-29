"""
2.4.82  अव्ययादाप्सुपः  —  VIDHI

Narrow v3 slice: if a *sup* pratyaya follows an *avyaya* (indeclinable) block,
the *sup* takes **luk**.

This implementation follows the v3.1 “zero-width ghost” contract:
  - do not delete the *sup* ``Term`` object
  - clear its ``varnas`` in-place and add ``luk_lopa``
  - keep the ``sup``/``pratyaya`` tags so pratyayalakṣaṇam scans remain possible

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only tags/meta (``avyaya`` tag, ``upadesha_slp1`` for *sup* id).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG, term_is_sup_luk_ghost
from engine.state import State


def _find(state: State):
    for i in range(1, len(state.terms)):
        pr = state.terms[i]
        if "sup" not in pr.tags:
            continue
        if term_is_sup_luk_ghost(pr):
            continue
        # Find nearest non-ghost term to the left.
        k = i - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        left = state.terms[k]
        if "avyaya" not in left.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    pr = state.terms[i]
    pr.varnas.clear()
    pr.tags.add(LUK_LOPA_GHOST_TAG)
    state.meta["2_4_82_luk"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.82",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1      = "avyayAd Ap-supoH",
    text_dev       = "अव्ययादाप्सुपः",
    padaccheda_dev = "अव्ययात् / आप्-सुपोः",
    why_dev        = "अव्ययात् परस्य सुपः लुक् (अव्यय-शब्दाः अव्ययवत् तिष्ठन्ति)।",
    anuvritti_from = ("2.4.58",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

