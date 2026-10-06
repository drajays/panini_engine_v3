"""
2.2.36  निष्ठा  —  VIDHI

Padaccheda: निष्ठा

Nistha-suffix form in bahuvrihi compound.
Pāṭha: ashtadhyayi.com data.txt row i=22036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_36_nistha_bahuvrihi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("bahuvrIhi" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["bahuvrihi_kind"]             = "2.2.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWA",
    text_dev              = "निष्ठा",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA nizWA pUrvam bahuvrIhO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा निष्ठा पूर्वम् बहुव्रीहौ",
    padaccheda_dev        = "निष्ठा",
    why_dev               = "निष्ठा-अन्तं बहुव्रीहौ (२.२.३६)।",
    anuvritti_from        = ('2.2.23',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
