"""
1.4.85  तृतीयार्थे  (tṛtīyārthe)  —  VIDHI

*Padaccheda:* *tṛtīyā-arthe* (saptamī-tatpuruṣa).

*Anuvṛtti:* *anuḥ* **1.4.84**; *karmapravacanīya* **1.4.83**.

*Śāstra:* *anu* (and by anuvrtti *prati*) is a *karmapravacanīya* also in
the instrumental (*tṛtīyā*) sense.

*Engine:* sets paribhāṣā gate for the *tṛtīyārtha* usage of *anu*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_85_tfwIyArTe"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.85",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "tfwIyArTe",
    text_dev             = "तृतीयार्थे",
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
