"""
1.2.43  प्रथमानिर्दिष्टं समास उपसर्जनम्  —  SAMJNA (upasarjana)

Narrow v3 slice for avyayībhāva demos:
  - In avyayībhāva, the avyaya member is the prathamā-nirdiṣṭa component and
    receives upasarjana-saṃjñā.

Engine: when a term carries ``avyayibhava`` and looks like an avyaya (tag
``avyaya`` or kind ``nipata``), tag it ``upasarjana``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_2.pada_1.sutra_2_1_6 import TAG_AVYAYIBHAVA


def _eligible(state: State):
    for t in state.terms:
        if TAG_AVYAYIBHAVA not in t.tags:
            continue
        if "upasarjana" in t.tags:
            continue
        if "avyaya" in t.tags or t.kind == "nipata" or (t.meta.get("upadesha_slp1") in {"prati", "adhi"}):
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("upasarjana")
    state.samjna_registry["1.2.43_upasarjana"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.43",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "prathamAnirdizwam samAsa upasarjanam",
    text_dev       = "प्रथमानिर्दिष्टं समास उपसर्जनम्",
    padaccheda_dev = "प्रथमा-निर्दिष्टम् / समासे / उपसर्जनम्",
    why_dev        = "समासे प्रथमानिर्दिष्टं पदम् उपसर्जन-संज्ञकं (अव्ययीभावे अव्ययः)।",
    anuvritti_from = ("1.2.42",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

