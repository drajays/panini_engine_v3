"""
3.1.126  आसुयुवपिरपिलपित्रपिचमश्च  —  VIDHI

Padaccheda: आसु-यु-वपि-रपि-लपि-त्रपि-चमः च

Krt suffix rule from dhatu: आसुयुवपिरपिलपित्रपिचमश्च (126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_126_Asuyuvapirap_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AsuyuvapirapilapitrapicamaSca",
    text_dev              = "आसुयुवपिरपिलपित्रपिचमश्च",
    padaccheda_dev        = "आसु-यु-वपि-रपि-लपि-त्रपि-चमः च",
    why_dev               = "धातोः [आसुयुवपिरपिलपित्रपिचमश्च]-प्रत्ययः विहितः (३.१.126)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
