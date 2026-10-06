"""
5.3.52  एकादाकिनिच्चासहाये  —  VIDHI

Padaccheda: एकात् आकिनिच् च असहाये

एकादाकिनिच्चासहाये (5.3.52)
Pāṭha: ashtadhyayi.com data.txt row i=53052 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_52_ekAdAkinic_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.52", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAdAkiniccAsahAye",
    text_dev              = "एकादाकिनिच्चासहाये",
    samagra_slp1          = "ekAt asahAye Akinic kan lukO ca",
    samagra_dev           = "एकात् असहाये आकिनिच्, कन् लुकौ च",
    padaccheda_dev        = "एकात् आकिनिच् च असहाये",
    why_dev               = "(सूत्रम् 5.3.52) एकादाकिनिच्चासहाये।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
