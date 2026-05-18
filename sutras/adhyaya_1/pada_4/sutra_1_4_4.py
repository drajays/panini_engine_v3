"""
1.4.4  नेयङुवङ्स्थानावस्त्री  (neyaṅuvaṅsthānāv astri)  —  NIYAMA

**Pāṭha:** The substitutions *iyaṅ* (*iy*) and *uvaṅ* (*uv*) — or a
non-feminine nominal — do NOT receive the *nadī* saṃjñā from 1.4.3.

v3: removes the *nadi* tag from any Term that already has it but is either
tagged *iyaN_sub*, *uvaN_sub*, or lacks *stri*, and records a done-marker
in ``term.meta`` to prevent re-firing.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _eligible(state: State):
    for t in state.terms:
        if "nadi" not in t.tags:
            continue
        if t.meta.get("1_4_4_done"):
            continue
        if "iyaN_sub" in t.tags or "uvaN_sub" in t.tags or "stri" not in t.tags:
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["nadi_exception_iyaN_uvaN"] = frozenset({"iyaN_sub", "uvaN_sub"})
    for t in _eligible(state):
        t.tags.discard("nadi")
        t.meta["1_4_4_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.4",
    sutra_type             = SutraType.NIYAMA,
    text_slp1              = "na iyaNuvaNsTAnAv astri",
    text_dev               = "नेयङुवङ्स्थानावस्त्री",
    padaccheda_dev         = "न / इयङ्-उवङ्-स्थानौ / अस्त्री",
    why_dev                = "इयङ्-उवङ्-स्थानभूतस्य अथवा स्त्री-भिन्नस्य नदीसंज्ञा न।",
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
