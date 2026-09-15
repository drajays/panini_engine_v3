"""
6.2.42  कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूःपण्यकम्बलो दासीभाराणां च  —  VIDHI

Padaccheda: कुरुगार्हपत (षष्ठ्याः सौत्रः लुक्) रिक्तगुरु (षष्ठ्याः सौत्रः लुक्) असूतजरती अश्लीलदृढरूपा पारेवडवा तैतिलकद्रूः पण्यकम्बलः (सर्वत्र सुब्व्यत्ययेन षष्ठीस्थाने प्रथमा वेदितया) दासीभाराणाम् च

कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूःपण्यकम्बलो दासीभाराणां च (6.2.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_42_kurugArhap_42"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.42", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kurugArhapatariktagurvasUtajaratyaSlIladfQarUpApArevaqavAtEtilakadrUHpaRyakambalo dAsIBArARAM ca",
    text_dev              = "कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूःपण्यकम्बलो दासीभाराणां च",
    padaccheda_dev        = "कुरुगार्हपत (षष्ठ्याः सौत्रः लुक्) रिक्तगुरु (षष्ठ्याः सौत्रः लुक्) असूतजरती अश्लीलदृढरूपा पारेवडवा तैतिलकद्रूः पण्यकम्बलः (सर्वत्र सुब्व्यत्ययेन षष्ठीस्थाने प्रथमा वेदितया) दासीभाराणाम् च",
    why_dev               = "(सूत्रम् 6.2.42) कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूःपण्यकम्बलो दासीभाराणां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
