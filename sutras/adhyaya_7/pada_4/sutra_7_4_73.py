"""
7.4.73  भवतेरः  —  VIDHI

Padaccheda: भवतेः अः

For bhū (bhavateḥ), the abhyāsa vowel u (after 7.4.59 hrasva) → a.
This gives ba-bhū → ba-bhū-v... → after abhyāsa: bu-BU- → after 7.4.59 (U→u):
  abhyāsa has u (short) → 7.4.73 turns u → a → ba-BU-...

Engine:
  - cond: ``state.meta.get("7_4_73_arm") is True`` AND
    find abhyāsa term whose last vowel (or only vowel) is ``u`` (hrasva).
  - act: replace that ``u`` varna with ``a``.
  - state.samjna_registry["7_4_73_bhavatеra"] = True
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk


def _find_abhyasa_u(state: State):
    """Return (term_idx, varna_idx) of the last 'u' vowel in abhyāsa, or None."""
    for i, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_73_done"):
            continue
        # Find last vowel that is 'u'
        for j in range(len(t.varnas) - 1, -1, -1):
            if t.varnas[j].slp1 == "u":
                return (i, j)
    return None


def cond(state: State) -> bool:
    if not state.meta.get("7_4_73_arm"):
        return False
    if state.samjna_registry.get("7_4_73_bhavatеra"):
        return False
    return _find_abhyasa_u(state) is not None


def act(state: State) -> State:
    hit = _find_abhyasa_u(state)
    if hit is None:
        return state
    i, j = hit
    state.terms[i].varnas[j] = mk("a")
    state.terms[i].meta["7_4_73_done"] = True
    state.meta["7_4_73_arm"] = False
    state.samjna_registry["7_4_73_bhavatеra"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BavateraH",
    text_dev              = "भवतेरः",
    padaccheda_dev        = "भवतेः अः",
    why_dev               = "भू-धातोः अभ्यासे उ-वर्णस्य अ-आदेशः (७.४.५९ ह्रस्व-परे); ब-भू → ब-भू → बभू।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
