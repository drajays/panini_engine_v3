"""
3.2.158  स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्  —  VIDHI

Padaccheda: स्पृहि-गृहि-पति-दयि-निद्रा-तन्द्रा-श्रद्धाभ्यः आलुच्

krt-suffix rule: स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच् (158)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_158_spfhigfhip_158"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_158_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.158"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.158",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "spfhigfhipatidayinidrAtandrASradDABya Aluc",
    text_dev              = "स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्",
    padaccheda_dev        = "स्पृहि-गृहि-पति-दयि-निद्रा-तन्द्रा-श्रद्धाभ्यः आलुच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्] विहितः (३.२.158)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
