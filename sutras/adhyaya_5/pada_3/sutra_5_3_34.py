"""
5.3.34  उत्तराधरदक्षिणादातिः  —  VIDHI

Padaccheda: उत्तर-अधर-दक्षिणात् आतिः

उत्तराधरदक्षिणादातिः (5.3.34)
Pāṭha: ashtadhyayi.com data.txt row i=53034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_34_uttarADara_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.34", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttarADaradakziRAdAtiH",
    text_dev              = "उत्तराधरदक्षिणादातिः",
    samagra_slp1          = "uttara-aDara-dakziRAt saptamI-paYcamI-praTamAByaH dig-deSa-kAlezu AtiH",
    samagra_dev           = "उत्तर-अधर-दक्षिणात् सप्तमी-पञ्चमी-प्रथमाभ्यः दिग्-देश-कालेषु आतिः",
    padaccheda_dev        = "उत्तर-अधर-दक्षिणात् आतिः",
    why_dev               = "(सूत्रम् 5.3.34) उत्तराधरदक्षिणादातिः।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
