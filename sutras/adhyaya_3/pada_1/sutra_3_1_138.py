"""
3.1.138  अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च  —  VIDHI

Padaccheda: अन्-उपसर्गात् लिम्प-विन्द-धारि-पारि-वेदि-उदेजि-चेति-साति-साहिभ्यः च

Krt suffix rule from dhatu: अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च (138)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_138_anupasargAll_138"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_138_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupasargAllimpavindaDAripArivedyudejicetisAtisAhiByaSca",
    text_dev              = "अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च",
    padaccheda_dev        = "अन्-उपसर्गात् लिम्प-विन्द-धारि-पारि-वेदि-उदेजि-चेति-साति-साहिभ्यः च",
    why_dev               = "धातोः [अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च]-प्रत्ययः विहितः (३.१.138)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
