"""
1.4.17  स्वादिष्वसर्वनामस्थाने  —  SAMJNA (*pada* on *prakṛti*)

*Anuvṛtti* **1.4.1** (*ā kaḍārād ekā saṃjñā*); reading: *svādiṣv asarvanāmasthāne*
— before a non-*sarvanāmasthāna* *svādi* affix, the *prātipadika* / *aṅga*
receives *pada* tagging ``pada_1_4_17``.

This *pada* is **bādhyate** by *bha* from **1.4.18** when **1.4.18** also
applies (e.g. *rājan* + *śas* — *bha* blocks unwanted *pada*-driven **8.2.7**
*n*-lopa in fuller Tripāḍī scope).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_4.samjna_sup_prakriti_1_4 import (
    is_asarvanamasthana_svadi_sup,
)


_REGISTRY = "1.4.17_pada_anga_indices"


def _eligible(state: State):
    for i in range(len(state.terms) - 1):
        anga, pr = state.terms[i], state.terms[i + 1]
        if not is_asarvanamasthana_svadi_sup(pr, anga):
            continue
        if "pada_1_4_17" in anga.tags:
            continue
        if "pada_1_4_16" in anga.tags:
            continue
        yield i


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    prev = state.samjna_registry.get(_REGISTRY)
    if not isinstance(prev, frozenset):
        prev = frozenset()
    new_idx: set[int] = set(prev)
    for i in _eligible(state):
        state.terms[i].tags.add("pada_1_4_17")
        new_idx.add(i)
    state.samjna_registry[_REGISTRY] = frozenset(new_idx)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.17",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "svAdizvasarvanAmasthAne",
    text_dev       = "स्वादिष्वसर्वनामस्थाने",
    padaccheda_dev = "स्वादिषु असर्वनामस्थाने",
    why_dev        = "असर्वनामस्थान-स्वादि-प्रत्यये परे प्रातिपदिकस्य पदसंज्ञा।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
