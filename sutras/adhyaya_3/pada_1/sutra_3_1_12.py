"""
3.1.12  भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः  —  VIDHI

Padaccheda: भृश-आदिभ्यः भुवि अ-च्वेः लोपः च हलः

Krt suffix rule from dhatu: भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः (12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_12_BfSAdiByo_12"


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
    state.meta["krt_kind"] = "3.1.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BfSAdiByo BuvyacverlopaSca halaH",
    text_dev              = "भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः",
    padaccheda_dev        = "भृश-आदिभ्यः भुवि अ-च्वेः लोपः च हलः",
    why_dev               = "धातोः [भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः]-प्रत्ययः विहितः (३.१.12)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
