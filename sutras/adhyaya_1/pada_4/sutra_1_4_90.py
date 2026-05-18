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
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_90_prati_pary_anu_lakzaRAdau"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.90",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "lakzaRe-tTamBUtAKyAnaBAgavIpsAsu prati-pary-anavaH",
    text_dev             = "लक्षणेत्थम्भूताख्यानभागवीप्सासु प्रतिपर्यनवः",
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
