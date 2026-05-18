"""
1.4.86  हीने  (hīne)  —  VIDHI

*Padaccheda:* *hīne* (saptamī).

*Anuvṛtti:* *anuḥ* **1.4.84**; *karmapravacanīya* **1.4.83**.

*Śāstra:* *anu* is a *karmapravacanīya* when used in the *hīna*
(inferior / deficient) sense.

*Engine:* sets paribhāṣā gate for *anu-in-hīna*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_86_hIne"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.86",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "hIne",
    text_dev             = "हीने",
    padaccheda_dev       = "हीने",
    why_dev              = (
        "हीन-अर्थे (न्यून-अर्थे) वर्तमानः 'अनु' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83", "1.4.84"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
