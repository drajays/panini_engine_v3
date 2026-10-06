"""
7.3.80  प्वादीनां ह्रस्वः  —  VIDHI

Padaccheda: पू-आदीनाम् ह्रस्वः

प्वादीनां ह्रस्वः (7.3.80)
Pāṭha: ashtadhyayi.com data.txt row i=73080 (Art. 14).
"""
from __future__ import annotations
from phonology import mk

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_80_pvAdInAM_80"


_HRASVA = {"U": "u", "I": "i", "F": "f", "X": "x"}


def _find(state: State) -> int | None:
    """प्वादीनां ह्रस्वः (शिति, 7.3.75): a pvādi root's long final vowel shortens
    before a śit affix — लू + श्ना → लुनाति, स्तॄ → स्तृणाति."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("7_3_80_done"):
            continue
        if "प्वादिः" not in (t.meta.get("antarganas") or ()):
            return None
        if not t.varnas or t.varnas[-1].slp1 not in _HRASVA:
            return None
        nxt = next((u for u in state.terms[i + 1:] if u.varnas or u.meta.get("upadesha_slp1")), None)
        if nxt is not None and (nxt.meta.get("upadesha_slp1") or "").startswith("S"):
            return i                                      # śit: श्ना, शप् …
        return None
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk(_HRASVA[t.varnas[-1].slp1])
    t.meta["7_3_80_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.80",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "pvAdInAM hrasvaH",
    text_dev              = "प्वादीनां ह्रस्वः",
    samagra_slp1          = "aNgasya pvAdInAm hrasvaH Siti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य प्वादीनाम् ह्रस्वः शिति",
    padaccheda_dev        = "पू-आदीनाम् ह्रस्वः",
    why_dev               = "(सूत्रम् 7.3.80) प्वादीनां ह्रस्वः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
