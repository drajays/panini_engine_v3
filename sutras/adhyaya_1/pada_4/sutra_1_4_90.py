"""
1.4.90  लक्षणेत्थम्भूताख्यानभागवीप्सासु प्रतिपर्यनवः  —  VIDHI

*Padaccheda:* *lakṣaṇa-ittham-bhūta-ākhyāna-bhāga-vīpsāsu* (saptamī-bahuvacanam),
*prati-pary-anavaḥ* (prathamā-bahuvacanam).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *prati*, *pari*, and *anu* are *karmapravacanīya* in six senses:
*lakṣaṇa* (marking), *ittham-bhūta* (being-such), *ākhyāna* (narrating),
*bhāga* (sharing), *vīpsā* (distributive / each-and-every).

*Engine:* sets paribhāṣā gate for *prati/pari/anu* in these six senses.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
Pāṭha: ashtadhyayi.com data.txt row i=14090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import chandasi_gate_eligible

_GATE_KEY = "1_4_90_prati_pary_anu_lakzaRAdau"


def cond(state: State) -> bool:
    return chandasi_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.90",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = 'lakzaRetTamBUtAKyAnaBAgavIpsAsu pratiparyanavaH',
    text_dev             = 'लक्षणेत्थम्भूताख्यानभागवीप्सासु प्रतिपर्यनवः',
    samagra_slp1         = "AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH karmapravacanIyAH lakzaRa-itTamBUtAKyAna-BAga-vIpsAsu prati-pari-anavaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः कर्मप्रवचनीयाः लक्षण-इत्थम्भूताख्यान-भाग-वीप्सासु प्रति-परि-अनवः",
    padaccheda_dev       = "लक्षण-इत्थम्भूत-आख्यान-भाग-वीप्सासु / प्रति-परि-अनवः",
    why_dev              = (
        "लक्षण-इत्थम्भूत-आख्यान-भाग-वीप्सा-अर्थेषु 'प्रति' 'परि' 'अनु' "
        "कर्मप्रवचनीय-संज्ञकाः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
