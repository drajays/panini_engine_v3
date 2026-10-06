"""
1.4.81  छन्दसि परेऽपि  —  SAMJNA

In the Vedic language (chandas), the gati may also follow (pare) the dhātu,
not only precede it.  This relaxes the positional requirement of 1.4.80 for
Vedic usage.

v3: registers samjna_registry["1_4_81_gati_pare_chandasi"] = True to mark
    that the chandas exception has been noted.
Pāṭha: ashtadhyayi.com data.txt row i=14081 (Art. 14).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("1_4_81_gati_pare_chandasi") is None


def act(state: State) -> State:
    state.samjna_registry["1_4_81_gati_pare_chandasi"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.81",
    sutra_type=SutraType.SAMJNA,
    text_slp1='Candasi parepi',
    text_dev='छन्दसि परेऽपि',
    samagra_slp1="AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH Candasi pare api te prAk DAtoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः छन्दसि परे अपि ते प्राक् धातोः",
    padaccheda_dev="छन्दसि / परे / अपि",
    why_dev="छन्दसि धातोः परेऽपि गतिर्भवति — छन्दसि-अपवाद-द्वारं स्थाप्यते।",
    anuvritti_from=("1.4.60", "1.4.80"),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
