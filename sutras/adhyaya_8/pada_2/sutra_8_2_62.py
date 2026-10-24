"""
8.2.62  क्विन्प्रत्ययस्य कुः  —  VIDHI

Padaccheda: क्विन्-प्रत्ययस्य कुः

क्विन्प्रत्ययस्य कुः (8.2.62)
Pāṭha: ashtadhyayi.com data.txt row i=82062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import HAL

_KU = {"q": "g", "Q": "G", "w": "k", "W": "K", "d": "g", "D": "G", "t": "k", "T": "K", "b": "g", "B": "G", "p": "k", "P": "K",
       "j": "g", "J": "G", "c": "k", "C": "K", "z": "k", "S": "k", "s": "k"}


def _site(state: State):
    """क्विन्प्रत्ययस्य कुः — the pada-final letter of a stem made with kvin (दृश्, दिश्, स्पृश् …) becomes a ku-varga letter (k, then 8.2.39 / 8.4.55
    choose g / k): दृक्, दृग्, दिक्षु. The stem is a pada at its own end — at the end of the word or before a hal-initial sup."""
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "origin_pratyaya:kvin" not in t.tags or t.meta.get("8_2_62_done"):
        return None
    vs = t.varnas
    end = next((k for k in range(1, len(vs)) if "pratyaya_start_v" in vs[k].tags), len(vs))      # where the sup begins
    if end < len(vs) and vs[end].slp1 not in HAL:
        return None                      # a vowel-initial sup: the letter is not pada-final
    return (t, end - 1) if end >= 1 and vs[end - 1].slp1 in HAL and vs[end - 1].slp1 not in "kKgGN" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, k = _site(state)
    old = t.varnas[k].slp1
    t.varnas[k] = mk(_KU.get(old, "g"))           # the antaratama ku letter (same voicing / aspiration): ḍ → g, ṭ → k; 8.4.55 / 8.4.56 may devoice
    t.meta["8_2_62_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.62",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "kvinpratyayasya kuH",
    text_dev              = "क्विन्प्रत्ययस्य कुः",
    samagra_slp1          = "padasya kvinpratyayasya kuH",
    samagra_dev           = "पदस्य क्विन्प्रत्ययस्य कुः",
    padaccheda_dev        = "क्विन्-प्रत्ययस्य कुः",
    why_dev               = "(सूत्रम् 8.2.62) क्विन्प्रत्ययस्य कुः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
