"""
1.1.28  विभाषा दिक्समासे बहुव्रीहौ  —  VIBHASHA

पदच्छेदः  विभाषा / दिक्समासे / बहुव्रीहौ

अनुवृत्तिः  सर्वादीनि 1.1.27, सर्वनामानि 1.1.27

अनुवृत्तिसहितं सूत्रम्  दिक्समासे बहुव्रीहौ सर्वादीनि विभाषा सर्वनामानि

One-line (EN): Words from the sarvādi-gaṇa inside a dik-compound bahuvrīhi are
optionally treated as sarvanāma.

Engine note (glass-box, mechanically blind):
This sūtra is optional (“विभाषा”), so we model it as SutraType.VIBHASHA.
Its condition is purely structural: a term is tagged to indicate that the
current prātipadika is a **dik-samāsa bahuvrīhi** context and that a sarvādi
member is present. The rule then optionally adds the `sarvanama` tag.

Together with **2.2.26**’s Kāśikā-vārttika *sarvanāmno vṛtti-mātre puṃ-vad-bhāvaḥ*
and ``meta['vartika_sarvanAma_puMvat_vrtti']`` on the merged dik stem, this
models the traditional link between **puṃ-vat** in *vṛtti* and optional
sarvanāma-saṃjñā for declension-class behaviour (not full *subanta* here).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Set

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


_SARVADI: Optional[Set[str]] = None


def _load_sarvadi() -> Set[str]:
    global _SARVADI
    if _SARVADI is not None:
        return _SARVADI
    path = Path(__file__).parents[3] / "data" / "inputs" / "sarvadi_slp1.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _SARVADI = set(data.get("sarvadi", []))
    return _SARVADI


def _eligible_terms(state: State):
    for t in state.terms:
        # Must be a prātipadika aṅga in a dik-samāsa bahuvrīhi context.
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "diksamasa" not in t.tags or "bahuvrihi" not in t.tags:
            continue
        # This flag is structural: the pipeline that creates a dik-samāsa
        # bahuvrīhi must set it when a sarvādi member is present.
        if t.meta.get("contains_sarvadi") is not True:
            continue
        if "sarvanama" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    # Register inventory for audit; then tag eligible terms.
    state.samjna_registry["sarvanama"] = frozenset(_load_sarvadi())
    for t in _eligible_terms(state):
        t.tags.add("sarvanama")
        t.meta["sarvanama_1_1_28_vibhasha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.28",
    sutra_type     = SutraType.VIBHASHA,
    text_slp1      = "diksamAse bahuvrIhau sarvAdIni vibhasA sarvanAmAni",
    text_dev       = "दिक्समासे बहुव्रीहौ सर्वादीनि विभाषा सर्वनामानि",
    padaccheda_dev = "विभाषा / दिक्समासे / बहुव्रीहौ",
    why_dev        = "दिक्समास-बहुव्रीहौ सर्वादि-शब्दाः विकल्पेन सर्वनाम-संज्ञकाः।",
    anuvritti_from = ("1.1.27",),
    vibhasha_default = True,
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

