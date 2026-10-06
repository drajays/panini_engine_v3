"""
5.3.51  मानपश्वङ्गयोः कन्लुकौ च  —  VIDHI

Padaccheda: मान-पश्वङ्गयोः कन्-लुकौ च

मानपश्वङ्गयोः कन्लुकौ च (5.3.51)
Pāṭha: ashtadhyayi.com data.txt row i=53051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_51_mAnapaSvaN_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.51", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAnapaSvaNgayoH kanlukO ca",
    text_dev              = "मानपश्वङ्गयोः कन्लुकौ च",
    samagra_slp1          = "BAge zazWa-azwamAByAm mAna-paSvaNgayoH sandarBe kan-lukO ca",
    samagra_dev           = "भागे षष्ठ-अष्टमाभ्याम् मान-पश्वङ्गयोः (सन्दर्भे) कन्-लुकौ च",
    padaccheda_dev        = "मान-पश्वङ्गयोः कन्-लुकौ च",
    why_dev               = "(सूत्रम् 5.3.51) मानपश्वङ्गयोः कन्लुकौ च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
