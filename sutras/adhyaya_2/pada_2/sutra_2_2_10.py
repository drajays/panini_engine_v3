"""
2.2.10  न निर्धारणे  —  VIDHI (PRATISHEDHA scope)

पदच्छेदः  न / निर्धारणे

अनुवृत्तिः  षष्ठी 2.2.8

Kāśikā summary: a genitive (*ṣaṣṭhī*) used for *nirdhāraṇa* (specification /
singling-out from a class) does NOT compound in tatpuruṣa.  This is a
restriction (*niyama* / *pratiṣedha*) on the scope of 2.2.8.
Examples: *kṛṣṇānāṃ śreṣṭhaḥ* — "best among the Kṛṣṇas" — stays uncompounded.

Engine (narrow, mechanically blind):
  Gate key ``2_2_10_nirdhaarana_gate``.  Recipe arms
  ``state.meta['2_2_10_arm']`` and tags a Term with ``nirdhaarana``
  indicating the singling-out genitive context.  When this gate fires, the
  ṣaṣṭhī-tatpuruṣa gate (2.2.8) is NOT set for this derivation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_10_nirdhaarana_gate") is True:
        return False
    if not state.meta.get("2_2_10_arm"):
        return False
    return any("nirdhaarana" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    state.paribhasha_gates["2_2_10_nirdhaarana_gate"] = True
    state.samjna_registry["2_2_10_nirdhaarana_blocked"] = True
    # Block the ṣaṣṭhī-tatpuruṣa gate for nirdhāraṇa contexts.
    state.paribhasha_gates["2_2_8_sasthi_gate"] = True
    state.meta.pop("2_2_10_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.10",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="na nirDAraRe",
    text_dev="न निर्धारणे",
    padaccheda_dev="न / निर्धारणे",
    why_dev=(
        "निर्धारणे षष्ठी न समस्यते — कृष्णानां श्रेष्ठः न समस्यते।"
    ),
    anuvritti_from=("2.2.8",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
