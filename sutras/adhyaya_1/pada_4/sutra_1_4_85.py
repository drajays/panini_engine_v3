"""
1.4.85  तृतीयार्थे  —  VIDHI

*Padaccheda:* *tṛtīyā-arthe* (saptamī-tatpuruṣa).

*Anuvṛtti:* *anuḥ* **1.4.84**; *karmapravacanīya* **1.4.83**.

*Śāstra:* *anu* (and by anuvrtti *prati*) is a *karmapravacanīya* also in
the instrumental (*tṛtīyā*) sense.

*Engine:* sets paribhāṣā gate for the *tṛtīyārtha* usage of *anu*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
Pāṭha: ashtadhyayi.com data.txt row i=14085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import chandasi_gate_eligible

_GATE_KEY = "1_4_85_tfwIyArTe"


def cond(state: State) -> bool:
    return chandasi_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.85",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'tftIyArTe',
    text_dev             = 'तृतीयार्थे',
    samagra_slp1         = "AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH karmapravacanIyAH tftIyArTe anuH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः कर्मप्रवचनीयाः तृतीयार्थे अनुः",
    padaccheda_dev       = "तृतीया-अर्थे",
    why_dev              = (
        "तृतीया-अर्थे वर्तमानः 'अनु' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83", "1.4.84"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
