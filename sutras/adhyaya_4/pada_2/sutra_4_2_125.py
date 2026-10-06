"""
4.2.125  अवृद्धादपि बहुवचनविषयात्  —  VIDHI

Padaccheda: अ-वृद्धात् अपि बहुवचन-विषयात्

अवृद्धादपि बहुवचनविषयात् (4.2.125)
Pāṭha: ashtadhyayi.com data.txt row i=42125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_125_avfdDAdapi_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.125", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avfdDAdapi bahuvacanavizayAt",
    text_dev              = "अवृद्धादपि बहुवचनविषयात्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA a-vfdDAt api bahuvacana-vizayAt vfdDAt vuY janapada-tad-avaDyoH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा अ-वृद्धात् अपि बहुवचन-विषयात् वृद्धात् वुञ् जनपद-तद्-अवध्योः च",
    padaccheda_dev        = "अ-वृद्धात् अपि बहुवचन-विषयात्",
    why_dev               = "(सूत्रम् 4.2.125) अवृद्धादपि बहुवचनविषयात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
