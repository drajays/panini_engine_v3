"""
2.1.7  यथासादृश्ये  (yathā-sādṛśye)  —  VIDHI

**Pāṭha:** The avyaya *yathā* combines with a subanta to form an
avyayībhāva samāsa when the meaning is sādṛśya (resemblance).

Example: *yathā śakti* → *yathaśakti* ("according to one's strength").

v3 narrow slice: gate-marks the avyayībhāva samāsa with the key
``2_1_7_yatha_sadrshya`` so downstream rules can proceed.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_7_yatha_sadrshya"

_YATHA_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") == "yaTA" and _YATHA_TAGS & t.tags:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaTA sAdqSye",
    text_dev              = "यथासादृश्ये",
    padaccheda_dev        = "यथा / सादृश्ये",
    why_dev               = "यथा-अव्यय-पूर्वकः सादृश्यार्थे अव्ययीभावः (२.१.७)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
