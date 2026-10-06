"""
2.1.72  मयूरव्यंसकादयश्च  —  VIDHI

Padaccheda: मयूरव्यंसक-आदयः च

mayuravyamsaka etc. by nipatana form karmadharaya compound.
Pāṭha: ashtadhyayi.com data.txt row i=21072 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_72_mayura_vyamsaka"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mayUravyaMsakAdayaSca",
    text_dev              = "मयूरव्यंसकादयश्च",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH mayUravyaMsaka-AdayaH ca samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः मयूरव्यंसक-आदयः च समानाधिकरणेन",
    padaccheda_dev        = "मयूरव्यंसक-आदयः च",
    why_dev               = "मयूरव्यंसक-आदयश्च निपातनात् (२.१.७२)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
