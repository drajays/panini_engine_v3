"""
3.4.59  अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ  —  VIDHI

Padaccheda: अव्यये अयथाभिप्रेताख्याने कृञः क्त्वा-णमुँल्ौ

krt-suffix rule: अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ
Pāṭha: ashtadhyayi.com data.txt row i=34059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_59_avyayeyaT_59"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.59", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'avyayeyaTABipretAKyAne kfYaH ktvARamulO',
    text_dev              = 'अव्ययेऽयथाभिप्रेताख्याने कृञः क्त्वाणमुलौ',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH avyaye ayaTABipretAKyAne kfYaH ktvA-RamulO kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अव्यये अयथाभिप्रेताख्याने कृञः क्त्वा-णमुलौ कृत्",
    padaccheda_dev        = "अव्यये अयथाभिप्रेताख्याने कृञः क्त्वा-णमुँल्ौ",
    why_dev               = "धातोः प्रत्ययः (३.4.59)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
