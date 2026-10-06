"""
8.3.65  उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्  —  VIDHI

Padaccheda: उपसर्गात् सुनोति-सुवति-स्यति-स्तौति-स्तोभति-स्था-सेनय-सेध-सिच-सञ्ज-स्वञ्जाम्

उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम् (8.3.65)
Pāṭha: ashtadhyayi.com data.txt row i=83065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_65_upasargAt_65"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.65", gate_key=_GATE_KEY)


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
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH upasargAt sunoti-suvati-syati-stOti-stoBati-sTA-senaya-seDa-sica-saYja-svaYjAm saH api aqvyavAye ca aByAsasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः उपसर्गात् सुनोति-सुवति-स्यति-स्तौति-स्तोभति-स्था-सेनय-सेध-सिच-सञ्ज-स्वञ्जाम् सः अपि अड्व्यवाये च अभ्यासस्य",
    padaccheda_dev        = "उपसर्गात् सुनोति-सुवति-स्यति-स्तौति-स्तोभति-स्था-सेनय-सेध-सिच-सञ्ज-स्वञ्जाम्",
    why_dev               = "(सूत्रम् 8.3.65) उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
