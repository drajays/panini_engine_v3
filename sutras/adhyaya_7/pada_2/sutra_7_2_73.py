"""
7.2.73  यमरमनमातां सक् च  —  VIDHI

Padaccheda: यम-रम-नम-आताम् सक् च

यमरमनमातां सक् च (7.2.73)
Pāṭha: ashtadhyayi.com data.txt row i=72073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_73_yamaramana_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.73", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yamaramanamAtAM sak ca",
    text_dev              = "यमरमनमातां सक् च",
    samagra_slp1          = "aNgasya yamaramanamAtAm sak ca valAdeH iw ArDaDAtukasya sici parasmEpadezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य यमरमनमाताम् सक् च वलादेः इट् आर्धधातुकस्य सिचि परस्मैपदेषु",
    padaccheda_dev        = "यम-रम-नम-आताम् सक् च",
    why_dev               = "(सूत्रम् 7.2.73) यमरमनमातां सक् च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
