"""
3.1.87  कर्मवत् कर्मणा तुल्यक्रियः  —  VIDHI

Padaccheda: कर्म-वत् कर्मणा तुल्यक्रियः

Krt suffix rule from dhatu: कर्मवत् कर्मणा तुल्यक्रियः (87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_87_karmavat_87"


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
    state.meta["krt_kind"] = "3.1.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmavat karmaRA tulyakriyaH",
    text_dev              = "कर्मवत् कर्मणा तुल्यक्रियः",
    padaccheda_dev        = "कर्म-वत् कर्मणा तुल्यक्रियः",
    why_dev               = "धातोः [कर्मवत् कर्मणा तुल्यक्रियः]-प्रत्ययः विहितः (३.१.87)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
