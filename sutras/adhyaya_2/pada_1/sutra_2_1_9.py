"""
2.1.9  सुप्प्रतिना मात्रार्थे  (sup + prati in mātrārtha)  —  VIDHI

**Pāṭha:** A subanta (*sup*-ending) combines with the avyaya *prati*
when the sense is mātrārtha (mere measure / proportion).

Example: *mukham prati* → *pratimukham* ("face to face / proportional to the face").

v3 narrow slice: gate-marks the avyayībhāva samāsa (prati-mātrārtha
usage) with key ``2_1_9_sup_prati_matra``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_9_sup_prati_matra"

_PRATI_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") == "prati" and _PRATI_TAGS & t.tags:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suB pratinA mAtrArTe",
    text_dev              = "सुप्प्रतिना मात्रार्थे",
    padaccheda_dev        = "सुप् / प्रतिना / मात्रार्थे",
    why_dev               = "सुप्-प्रति-योगे मात्रार्थे अव्ययीभावः (२.१.९)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
