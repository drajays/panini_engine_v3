"""
3.1.121  युग्यं च पत्त्रे  —  VIDHI

Padaccheda: युग्यम् च पत्रे

Krt suffix rule from dhatu: युग्यं च पत्त्रे (121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_121_yugyaM_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_121_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yugyaM ca pattre",
    text_dev              = "युग्यं च पत्त्रे",
    padaccheda_dev        = "युग्यम् च पत्रे",
    why_dev               = "धातोः [युग्यं च पत्त्रे]-प्रत्ययः विहितः (३.१.121)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
