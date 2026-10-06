"""
4.4.125  तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः  —  VIDHI

Padaccheda: तद्वान् आसाम् उपधानः मन्त्रः इति इष्टकासु लुक् च मतोः

तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः (4.4.125)
Pāṭha: ashtadhyayi.com data.txt row i=44125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_125_tadvAnAsAm_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.125", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadvAnAsAmupaDAno mantra itIzwakAsu luk ca matoH",
    text_dev              = "तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः",
    samagra_slp1          = "upaDAnaH mantraH AsAm iti tadvAn iti izwakAsu yat matoH ca luk",
    samagra_dev           = "'उपधानः मन्त्रः आसाम्' (इति) 'तद्वान्' इति इष्टकासु यत्, मतोः च लुक्",
    padaccheda_dev        = "तद्वान् आसाम् उपधानः मन्त्रः इति इष्टकासु लुक् च मतोः",
    why_dev               = "(सूत्रम् 4.4.125) तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
