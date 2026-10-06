"""
1.4.84  अनुर्लक्षणे  —  VIDHI

*Padaccheda:* *anuḥ* (prathamā), *lakṣaṇe* (saptamī).

*Śāstra (adhikāra 1.4.83):* The nipāta *anu* is a *karmapravacanīya* when
used in the *lakṣaṇa* (marking / signifying) sense.

*Engine:* sets a paribhāṣā gate once to signal that *anu-in-lakṣaṇa* has
been recognised.  ``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
Pāṭha: ashtadhyayi.com data.txt row i=14084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import chandasi_gate_eligible

_GATE_KEY = "1_4_84_anu_lakzaRe"


def cond(state: State) -> bool:
    return chandasi_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.84",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'anurlakzaRe',
    text_dev             = 'अनुर्लक्षणे',
    samagra_slp1         = "AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH karmapravacanIyAH anuH lakzaRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः कर्मप्रवचनीयाः अनुः लक्षणे",
    padaccheda_dev       = "अनुः / लक्षणे",
    why_dev              = (
        "लक्षण-अर्थे वर्तमानः 'अनु' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
