"""
2.2.25  संख्ययाऽव्ययासन्नादूराधिकसंख्याः संख्येये  —  VIDHI

Padaccheda: संख्यया अव्यय-आसन्न-अदूर-अधिक-संख्याः संख्येये

Numeral + near/far/excess forms karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=22025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_25_samkhyaya_sankhyeye"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.2.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'saMKyayAvyayAsannAdUrADikasaMKyAH saMKyeye',
    text_dev              = 'संख्ययाऽव्ययासन्नादूराधिकसंख्याः संख्येये',
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA saMKyayA avyaya-Asanna-adUra-aDika-saMKyAH saMKyeye anekam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा संख्यया अव्यय-आसन्न-अदूर-अधिक-संख्याः संख्येये अनेकम्",
    padaccheda_dev        = "संख्यया अव्यय-आसन्न-अदूर-अधिक-संख्याः संख्येये",
    why_dev               = "संख्यया अव्यय-आसन्न-आदि-संख्याः संख्येये कर्मधारयः (२.२.२५)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
