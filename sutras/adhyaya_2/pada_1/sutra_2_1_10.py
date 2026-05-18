"""
2.1.10  अक्षशलाकासंख्याः परिणा  (akṣa-śalākā-saṃkhyāḥ pariṇā)  —  VIDHI

**Pāṭha:** The words *akṣa* (die), *śalākā* (stick/splinter), and
*saṃkhyā* (number) combine with the avyaya *pari* to form an
avyayībhāva samāsa.

Example: *akṣān pari* → *paryakṣam* ("around/through dice").

v3 narrow slice: gate-marks the compound with key
``2_1_10_aksha_salaka_pari``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_10_aksha_salaka_pari"

_PARI_BASES: frozenset[str] = frozenset({"akza", "SalAkA", "saMKyA"})

_PARI_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    has_pari  = any(t.meta.get("upadesha_slp1") == "pari" and _PARI_TAGS & t.tags
                    for t in state.terms)
    has_base  = any(t.meta.get("upadesha_slp1") in _PARI_BASES for t in state.terms)
    return has_pari and has_base


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akzaSalAkAsaMKyAH pariNA",
    text_dev              = "अक्षशलाकासंख्याः परिणा",
    padaccheda_dev        = "अक्ष-शलाका-संख्याः / परिणा",
    why_dev               = "अक्ष-शलाका-संख्या-शब्दानां परि-अव्ययेन सह अव्ययीभावः (२.१.१०)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
