"""
6.1.89  एत्येधत्यूठ्सु  —  VIDHI  (apavāda of 6.1.94 / 6.1.88)

अवर्ण followed by the ए of ``eti`` (धातु इण्) / ``edhati`` (धातु एध्) or the ऊ of
``ūṭh`` (वह्-ādeśa) takes the vṛddhi ekādeśa:

    उप + एति → उपैति        उप + एधते → उपैधते        प्र + ऊह → प्रौह

Structural witness: the right Term is a dhātu whose upadeśa is ``iR`` or ``eDa~``
and which begins with ``e`` (guṇa already applied), or a ``vah`` dhātu beginning
with ``U`` (ūṭh).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_E_ROOTS = frozenset({"iR", "eDa~"})
_VRIDDHI = {"e": "E", "U": "O"}


def is_eti_edhati_uth(right) -> bool:
    """Shared with 6.1.94 so the apavāda is decided in one place."""
    if "dhatu" not in right.tags or not right.varnas:
        return False
    up = (right.meta.get("upadesha_slp1") or "").strip()
    first = right.varnas[0].slp1
    if first == "e":
        return up in _E_ROOTS
    if first == "U":
        return up.startswith("vah")
    return False


def _find(state: State):
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if left.varnas[-1].slp1 in ("a", "A") and is_eti_edhati_uth(right):
            return i, j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    i, j = hit
    old = state.terms[j].varnas[0].slp1
    del state.terms[i].varnas[-1]
    state.terms[j].varnas[0] = mk(_VRIDDHI[old])
    state.meta["__why_now_dev__"] = (
        "अवर्णात् परे एति-एधति-ऊठ्-अवयव-स्वरे वृद्धि-एकादेशः; "
        "यथा उप+एति → उपैति, प्र+ऊह → प्रौह। (६.१.८९)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.89",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "etyeDatyUWsu",
    text_dev       = "एत्येधत्यूठ्सु",
    padaccheda_dev = "एति-एधति-ऊठ्सु",
    why_dev        = "अवर्णात् परे एति/एधति/ऊठ् इत्येषु वृद्धि-एकादेशः।",
    apavada_of     = ("6.1.94", "6.1.88"),
    anuvritti_from = ("6.1.88",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
