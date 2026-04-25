"""
1.4.16  सिति च  —  SAMJNA (*pada* on *prakṛti*)

*Anuvṛtti* from **1.4.14** (*suptiṅantam padam*) + **1.4.1**.

Before an *asarvanāmasthāna* *svādi* affix whose raw upadeśa is in **siti**
(operational: ends in *it*‑marker dental ``s``, with **yaṭ**/**ac**-type onset
``y/v/r/l`` or vowel — excluding **ś/ṣ** so **śas** does not block **bha**),
the *prakṛti* / *aṅga* receives *pada* technical tagging ``pada_1_4_16``.

This *pada* **bādhate** *bha* from **1.4.18** (e.g. *ūrṇā* + *yus*).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_4.samjna_sup_prakriti_1_4 import is_siti_pada_context


_REGISTRY = "1.4.16_pada_anga_indices"


def _eligible(state: State):
    for i in range(len(state.terms) - 1):
        anga, pr = state.terms[i], state.terms[i + 1]
        if not is_siti_pada_context(pr, anga):
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
        anga = state.terms[i]
        anga.tags.add("pada_1_4_16")
        anga.tags.discard("pada_1_4_17")
        new_idx.add(i)
    state.samjna_registry[_REGISTRY] = frozenset(new_idx)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.16",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "siti ca",
    text_dev       = "सिति च",
    padaccheda_dev = "सिति च",
    why_dev        = "सिति परे प्रातिपदिकस्य पदसंज्ञा; भसंज्ञां बाधते।",
    anuvritti_from = ("1.4.1", "1.4.14"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
