"""
3.1.45  शल इगुपधादनिटः क्सः  —  VIDHI

Padaccheda: शलः इक्-उपधात् अन्-इटः क्सः

Krt suffix rule from dhatu: शल इगुपधादनिटः क्सः (45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_45_Sala_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_45_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Sala igupaDAdaniwaH ksaH",
    text_dev              = "शल इगुपधादनिटः क्सः",
    padaccheda_dev        = "शलः इक्-उपधात् अन्-इटः क्सः",
    why_dev               = "धातोः [शल इगुपधादनिटः क्सः]-प्रत्ययः विहितः (३.१.45)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
