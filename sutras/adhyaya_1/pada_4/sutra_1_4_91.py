"""
1.4.91  अभिरभागे  —  VIDHI

*Padaccheda:* *abhiḥ* (prathamā), *abhāge* (saptamī).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *abhi* is a *karmapravacanīya* when used in the *abhāga*
(non-partitive / non-sharing) sense, i.e., when it does not denote partition.

*Engine:* sets paribhāṣā gate for *abhi-in-abhāga*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
Pāṭha: ashtadhyayi.com data.txt row i=14091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import chandasi_gate_eligible

_GATE_KEY = "1_4_91_aBi_aBAge"


def cond(state: State) -> bool:
    return chandasi_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.91",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'aBiraBAge',
    text_dev             = 'अभिरभागे',
    samagra_slp1         = "AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH karmapravacanIyAH aBiH aBAge lakzaRa-itTamBUtAKyAna-BAga-vIpsAsu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः कर्मप्रवचनीयाः अभिः अभागे लक्षण-इत्थम्भूताख्यान-भाग-वीप्सासु",
    padaccheda_dev       = "अभिः / अभागे",
    why_dev              = (
        "अभाग-अर्थे वर्तमानः 'अभि' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
