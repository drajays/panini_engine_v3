"""
1.4.97  अधिरीश्वरे  (adhir īśvare)  —  VIDHI

*Padaccheda:* *adhiḥ* (prathamā), *īśvare* (saptamī).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *adhi* is a *karmapravacanīya* when used in the *īśvara*
(lord / master / controller) sense.  E.g. *adhi brāhmaṇāḥ kauśalāḥ*
("the brāhmaṇas are masters of Kauśala").

*Engine:* sets paribhāṣā gate for *adhi-in-īśvara*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_97_aDi_ISvare"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.97",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "aDir ISvare",
    text_dev             = "अधिरीश्वरे",
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
