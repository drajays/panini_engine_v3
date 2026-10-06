"""
1.4.89  आङ् मर्यादावचने  (āṅ maryādāvacane)  —  VIDHI

*Padaccheda:* *āṅ* (prathamā), *maryādā-vacane* (saptamī-tatpuruṣa).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *āṅ* (ā) is a *karmapravacanīya* when it expresses *maryādā*
(limit / boundary).  E.g. *ā mūlāt* ("up to the root").

*Engine:* sets paribhāṣā gate for *āṅ-in-maryādā*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
Pāṭha: ashtadhyayi.com data.txt row i=14089 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import chandasi_gate_eligible

_GATE_KEY = "1_4_89_AN_maryAdAvacane"


def cond(state: State) -> bool:
    return chandasi_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.89",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "AN maryAdAvacane",
    text_dev             = "आङ् मर्यादावचने",
    samagra_slp1         = "AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH karmapravacanIyAH AN maryAdAvacane",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev          = "आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः कर्मप्रवचनीयाः आङ् मर्यादावचने",
    padaccheda_dev       = "आङ् / मर्यादा-वचने",
    why_dev              = (
        "मर्यादा-अर्थे वर्तमानः 'आ' (आङ्) कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
