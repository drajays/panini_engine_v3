"""
1.4.93  अधिपरी अनर्थकौ  (adhi-parī anarthakau)  —  VIDHI

*Padaccheda:* *adhi-parī* (prathamā-dvivacana), *anarthakau* (prathamā-dvivacana).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *adhi* and *pari* are *karmapravacanīya* when they are *anarthaka*
(semantically empty / redundant — used for emphasis without adding meaning).

*Engine:* sets paribhāṣā gate for *adhi/pari-anarthaka*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_93_aDi_pari_anarTakau"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.93",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "aDi-parI anarTakau",
    text_dev             = "अधिपरी अनर्थकौ",
    padaccheda_dev       = "अधि-परी / अनर्थकौ",
    why_dev              = (
        "अनर्थक-रूपेण वर्तमानौ 'अधि' 'परि' कर्मप्रवचनीय-संज्ञकौ (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
