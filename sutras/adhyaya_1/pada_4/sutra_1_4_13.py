"""
1.4.13  यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्  —  SAMJNA

The *ādi* of what follows from a pratyaya-ādeśa whose cause is a given
element — that element is called *aṅga* with respect to that affix.

Operational (kṛdanta): when a dhātu Term precedes a pratyaya Term, the dhātu
is the *aṅga* for that pratyaya (registry key for trace / downstream gates).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if "dhatu" not in state.terms[0].tags:
        return False
    if "pratyaya" not in state.terms[1].tags:
        return False
    return state.samjna_registry.get(("1.4.13_anga", 0)) is None


def act(state: State) -> State:
    state.samjna_registry[("1.4.13_anga", 0)] = frozenset({"active"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.13",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "yasmAt pratyayavidhis tadAdi pratyaye~Nga",
    text_dev       = "यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्",
    padaccheda_dev = "यस्मात् प्रत्यय-विधिः तदादि प्रत्यये अङ्गम्",
    why_dev        = "प्रत्यय-विधेर् यस्मात् तदादि प्रत्यये यत् तद् अङ्गम्।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
