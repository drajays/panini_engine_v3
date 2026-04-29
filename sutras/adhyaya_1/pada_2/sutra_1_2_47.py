"""
1.2.47  ह्रस्वो नपुंसके प्रातिपदिकस्य  —  VIDHI

Narrow v3 slice used by the user's *adhistri* avyayībhāva derivation:
  - If a prātipadika is napuṃsaka, its final long vowel is shortened (hrasva).

We implement minimally:
  - I → i, U → u, A → a  (*simple* finals), and
  - *एच्* finals → *इक्* replacements via ``phonology.ec_ig_hrasva`` — the same
    resolver bundle used by **1.1.48** (*एच इग्घ्रस्वादेशे*) when another rule
    requests *hrasva* on an *एच्* vowel (अतिरै / अतिनौ demos).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.ec_ig_hrasva import ec_ig_replacement_slp1

_MAP = {"A": "a", "I": "i", "U": "u"}


def _find(state: State):
    for i, t in enumerate(state.terms):
        if "prātipadika" not in t.tags:
            continue
        if "napuṃsaka" not in t.tags:
            continue
        if not t.varnas:
            continue
        if t.meta.get("1_2_47_hrasva_done"):
            continue
        last = t.varnas[-1].slp1
        if last in _MAP:
            return i
        if ec_ig_replacement_slp1(last) is not None:
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    last = t.varnas[-1].slp1
    if last in _MAP:
        t.varnas[-1] = mk(_MAP[last])
    else:
        rep = ec_ig_replacement_slp1(last)
        if rep is None:
            return state
        t.varnas[-1] = mk(rep)
        t.meta["1_2_47_via_ec_ig_bundle"] = True
    t.meta["1_2_47_hrasva_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.47",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hrasvo napuMsake prAtipadikasya",
    text_dev       = "ह्रस्वो नपुंसके प्रातिपदिकस्य",
    padaccheda_dev = "ह्रस्वः / नपुंसके / प्रातिपदिकस्य",
    why_dev        = "नपुंसक-प्रातिपदिकस्य अन्त्य-दीर्घस्य ह्रस्वः।",
    anuvritti_from = ("1.2.45",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

