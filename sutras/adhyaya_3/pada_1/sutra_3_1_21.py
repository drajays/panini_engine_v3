"""
3.1.21  मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो  —  VIDHI

Padaccheda: मुण्ड-मिश्र-श्लक्ष्ण-लवण-व्रत-वस्त्र-हल-कल-कृत-तूस्तेभ्यः णिच्

Krt suffix rule from dhatu: मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो (21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_21_muRqamiSraSl_21"


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
    state.meta["krt_kind"] = "3.1.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "muRqamiSraSlakzRalavaRavratavastrahalakalakftatUsteByo",
    text_dev              = "मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो",
    padaccheda_dev        = "मुण्ड-मिश्र-श्लक्ष्ण-लवण-व्रत-वस्त्र-हल-कल-कृत-तूस्तेभ्यः णिच्",
    why_dev               = "धातोः [मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो]-प्रत्ययः विहितः (३.१.21)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
