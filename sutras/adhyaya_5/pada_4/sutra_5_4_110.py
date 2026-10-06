"""
5.4.110  नदीपौर्णमास्याग्रहायणीभ्यः  —  VIDHI

Padaccheda: नदी-पौर्णमासी-आग्रहायणीभ्यः

नदीपौर्णमास्याग्रहायणीभ्यः (5.4.110)
Pāṭha: ashtadhyayi.com data.txt row i=54110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_110_nadIpOrRam_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.110", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nadIpOrRamAsyAgrahAyaRIByaH",
    text_dev              = "नदीपौर्णमास्याग्रहायणीभ्यः",
    samagra_slp1          = "nadI-pOrRamAsI-AgrahAyaRIByaH avyayIBAve anyatarasyAm wac",
    samagra_dev           = "नदी-पौर्णमासी-आग्रहायणीभ्यः अव्ययीभावे अन्यतरस्याम् टच्",
    padaccheda_dev        = "नदी-पौर्णमासी-आग्रहायणीभ्यः",
    why_dev               = "(सूत्रम् 5.4.110) नदीपौर्णमास्याग्रहायणीभ्यः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
