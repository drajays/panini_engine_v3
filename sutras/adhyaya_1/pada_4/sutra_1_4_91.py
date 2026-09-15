"""
1.4.91  अभिरभागे  (abhir abhāge)  —  VIDHI

*Padaccheda:* *abhiḥ* (prathamā), *abhāge* (saptamī).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *abhi* is a *karmapravacanīya* when used in the *abhāga*
(non-partitive / non-sharing) sense, i.e., when it does not denote partition.

*Engine:* sets paribhāṣā gate for *abhi-in-abhāga*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
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
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "aBir aBAGe",
    text_dev             = "अभिरभागे",
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
