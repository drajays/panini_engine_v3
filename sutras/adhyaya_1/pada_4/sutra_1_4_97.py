"""
1.4.97  अधिरीश्वरे  —  VIDHI

*Padaccheda:* *adhiḥ* (prathamā), *īśvare* (saptamī).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *adhi* is a *karmapravacanīya* when used in the *īśvara*
(lord / master / controller) sense.  E.g. *adhi brāhmaṇāḥ kauśalāḥ*
("the brāhmaṇas are masters of Kauśala").

*Engine:* sets paribhāṣā gate for *adhi-in-īśvara*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
Pāṭha: ashtadhyayi.com data.txt row i=14097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import chandasi_gate_eligible

_GATE_KEY = "1_4_97_aDi_ISvare"


def cond(state: State) -> bool:
    return chandasi_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.97",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'aDirISvare',
    text_dev             = 'अधिरीश्वरे',
    samagra_slp1         = "AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH karmapravacanIyAH aDiH ISvare",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः कर्मप्रवचनीयाः अधिः ईश्वरे",
    padaccheda_dev       = "अधिः / ईश्वरे",
    why_dev              = (
        "ईश्वर-अर्थे वर्तमानः 'अधि' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
