"""
6.1.45  आदेच उपदेशेऽशिति  —  VIDHI

Padaccheda: आत् एचः उपदेशे अ-शिति

A dhātu whose upadeśa ends in an ec (ए ऐ ओ औ) takes ā for it before a pratyaya
that is not śit: ग्लै + ता → ग्लाता, ग्लै + स्य → ग्लास्यति, ग्लै + यासुट् → ग्लायात्.
Before a śit (śap: ग्लायति) the ec stays and meets 6.1.78.
"उपदेशे": only the root's own ec (``mula_dhatu_v``), never a guṇa product (भो).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_EC = frozenset("eEoO")


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        last = t.varnas[-1]
        if last.slp1 not in _EC or "mula_dhatu_v" not in last.tags:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or "pratyaya" not in nxt.tags:
            continue
        if (nxt.meta.get("upadesha_slp1") or "").strip().startswith("S"):
            continue                                   # śit (śap, śyan, śnu, śnā, śa)
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is not None:
        v = mk("A")
        v.tags.add("mula_dhatu_v")
        state.terms[i].varnas[-1] = v
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.45",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'Adeca upadeSeSiti',
    text_dev              = 'आदेच उपदेशेऽशिति',
    padaccheda_dev        = "आत् एचः उपदेशे अ-शिति",
    why_dev               = "उपदेशे एजन्तस्य धातोः आत्वम् अशिति प्रत्यये परे (ग्लै → ग्ला)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
