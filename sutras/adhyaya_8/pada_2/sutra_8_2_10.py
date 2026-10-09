"""
8.2.10  झयः  —  VIDHI

Padaccheda: झयः

झयः (8.2.10)
Pāṭha: ashtadhyayi.com data.txt row i=82010 (Art. 14).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import JHAL
from sutras.adhyaya_8.pada_2.sutra_8_2_9 import _yavadi

_MATUP = "matu~p"

_JHAY = frozenset(JHAL) - frozenset("SzsH") - frozenset("h")      # jhay = jhal minus the ūṣmans and h


def _site(state: State):
    if not state.tripadi_zone:
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "") != _MATUP or not t.varnas or t.varnas[0].slp1 != "m":
            continue
        prev = next((u for u in reversed(state.terms[:i]) if u.varnas), None)
        if prev is None or (prev.meta.get("upadesha_slp1") or "") in _yavadi():     # ayavādibhyaḥ continues (Kāśikā: harit, kakud, garut, marut … keep m)
            continue
        if prev.varnas[-1].slp1 in _JHAY:                                  # jhayaḥ: after a jhay-final stem (vidyutvān)
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        state.terms[i].varnas[0] = mk("v")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "JayaH",
    text_dev              = "झयः",
    samagra_slp1          = "padasya pUrvatrAsidDam JayaH vaH matoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् झयः वः मतोः",
    padaccheda_dev        = "झयः",
    why_dev               = "(सूत्रम् 8.2.10) झयः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
