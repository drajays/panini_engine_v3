"""
2.1.8  यावदवधारणे  (yāvad-avadhāraṇe)  —  VIDHI

**Pāṭha:** The avyaya *yāvat* combines with a subanta to form an
avyayībhāva samāsa when the meaning is avadhāraṇa (delimitation/extent).

Example: *yāvat jīvanam* → *yāvajjīvam* ("as long as life lasts").

v3 narrow slice: gate-marks the avyayībhāva samāsa with key
``2_1_8_yavad_avadhara``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_8_yavad_avadhara"

_YAVAT_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") in {"yAvat", "yAvad"} and _YAVAT_TAGS & t.tags:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yAvad avaDAraNe",
    text_dev              = "यावदवधारणे",
    padaccheda_dev        = "यावत् / अवधारणे",
    why_dev               = "यावत्-अव्यय-पूर्वकः अवधारणार्थे अव्ययीभावः (२.१.८)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
