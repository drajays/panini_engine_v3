"""
7.3.71  ओतः श्यनि  —  VIDHI

Padaccheda: ओतः श्यनि

ओतः श्यनि (7.3.71)
Pāṭha: ashtadhyayi.com data.txt row i=73071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State


def _site(state: State) -> int | None:
    """An aṅga ending in o (do, so, Co, Do, Co …) before śyan."""
    if not adhikara_in_effect("7.3.71", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "anga" not in t.tags or "dhatu" not in t.tags or not t.varnas or t.varnas[-1].slp1 != "o":
            continue
        nxt = state.terms[i + 1]
        if (nxt.meta.get("upadesha_slp1") or "").strip() == "Syan" or "Syan_vikaraṇa" in nxt.tags:
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        state.terms[i].varnas.pop()                     # lopaḥ of the final o
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.71",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "otaH Syani",
    text_dev              = "ओतः श्यनि",
    samagra_slp1          = "aNgasya otaH Syani lopaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ओतः श्यनि लोपः",
    padaccheda_dev        = "ओतः श्यनि",
    why_dev               = "(सूत्रम् 7.3.71) ओतः श्यनि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
