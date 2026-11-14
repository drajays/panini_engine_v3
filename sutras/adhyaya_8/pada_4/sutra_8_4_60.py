"""
8.4.60  तोर्लि  —  VIDHI

Padaccheda: तोः । लि

Sources consulted:
- ashtadhyayi.com data.txt row i=84060 (samagra: तोः लि परसवर्णः संहितायाम्; परसवर्णः ← 8.4.58)
- Kāśikā: "तवर्गस्य लकारे परतः परसवर्णादिशो भवति। अग्निचिल्लुनाति। सोमसुल्लुनाति। भवाँल्लुनाति। महाँल्लुनाति॥"
- SK: "तवर्गस्य लकारे परे परसवर्णः स्यात् । तल्लयः । विद्वाँल्लिखति । नकारस्याऽनुनासिको लकारः ॥"
- Cross-validation: LK cases tests/fixtures/lk_cases/a8.json (8.4.60: tallayaH, agnicillunAti).

A tavarga letter right before ल on the saṃhitā tape becomes the savarṇa of that ल: a stop becomes ल; न, being nasal, becomes the
anunāsika ल (sthāne'ntaratamaḥ; SK "नकारस्याऽनुनासिको लकारः"), carried as the varṇa tag `anunasika`.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_TU = frozenset("tTdDn")


def _site(state: State):
    if not state.tripadi_zone:
        return None
    flat = [(t, i, v.slp1) for t in state.terms for i, v in enumerate(t.varnas)]
    for (t, i, a), (_, _, b) in zip(flat, flat[1:]):
        if a in _TU and b == "l":
            return t, i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, i = _site(state)
    nasal = t.varnas[i].slp1 == "n"
    t.varnas[i] = mk("l", "anunasika") if nasal else mk("l")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.60",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "torli",
    text_dev              = "तोर्लि",
    samagra_slp1          = "toH li parasavarRaH saMhitAyAm",
    samagra_dev           = "तोः लि परसवर्णः संहितायाम्",
    padaccheda_dev        = "तोः । लि",
    why_dev               = "(सूत्रम् 8.4.60) तवर्गस्य लकारे परे परसवर्णः — तल्लयः, अग्निचिल्लुनाति।",
    anuvritti_from        = ('8.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
