"""
8.3.65  उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्  —  VIDHI

Padaccheda: उपसर्गात् सुनोति-सुवति-स्यति-स्तौति-स्तोभति-स्था-सेनय-सेध-सिच-सञ्ज-स्वञ्जाम्

उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम् (8.3.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_65_upasargAt_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_65_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAt sunotisuvatisyatistOtistoBatisTAsenayaseDasicasaYjasvaYjAm",
    text_dev              = "उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्",
    padaccheda_dev        = "उपसर्गात् सुनोति-सुवति-स्यति-स्तौति-स्तोभति-स्था-सेनय-सेध-सिच-सञ्ज-स्वञ्जाम्",
    why_dev               = "(सूत्रम् 8.3.65) उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
