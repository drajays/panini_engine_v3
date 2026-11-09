"""
8.3.28  ङ्णोः कुक्टुक् शरि  —  VIDHI

Padaccheda: ङ्‍-णोः कुक्-ट्टुक् शरि

ङ्णोः कुक्टुक् शरि (8.3.28)
Pāṭha: ashtadhyayi.com data.txt row i=83028 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site(state: State):
    """ङ्णोः कुक्टुक् शरि: after a pada-final ṅ (kuk = k) or ṇ (ṭuk = ṭ), before a śar (the ś/ṣ/s of su): प्राङ्क्षु / प्राङ्षु."""
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    t = state.terms[0]
    for k in range(len(t.varnas) - 1):
        if (t.varnas[k].slp1 in ("N", "R") and t.varnas[k + 1].slp1 in ("S", "z", "s")
                and "pratyaya_start_v" in t.varnas[k + 1].tags and not t.meta.get("8_3_28_done")):
            return t, k
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, k = _site(state)
    v = mk("k" if t.varnas[k].slp1 == "N" else "w")
    v.tags.add("kuk_tuk_agama")
    t.varnas.insert(k + 1, v)
    t.meta["8_3_28_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.28",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "NRoH kukwuk Sari",
    text_dev              = "ङ्णोः कुक्टुक् शरि",
    samagra_slp1          = "padasya NRoH Sari kuk wuk vA",
    samagra_dev           = "पदस्य ङ्णोः शरि कुक् टुक् वा",
    padaccheda_dev        = "ङ्‍-णोः कुक्-ट्टुक् शरि",
    why_dev               = "(सूत्रम् 8.3.28) ङ्णोः कुक्टुक् शरि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
