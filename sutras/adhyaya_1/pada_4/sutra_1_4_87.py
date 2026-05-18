"""
1.4.87  उपोऽधिके च  (upo 'dhike ca)  —  VIDHI

*Padaccheda:* *upaḥ* (prathamā), *adhike* (saptamī), *ca* (avyaya).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**; *hīne* **1.4.86** (by *ca*).

*Śāstra:* *upa* is a *karmapravacanīya* in the *adhika* (superior/excess) sense
and also in the *hīna* sense (by *ca*).

*Engine:* sets paribhāṣā gate for *upa-in-adhika*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_87_upa_aDike"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.87",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "upo aDike ca",
    text_dev             = "उपोऽधिके च",
    padaccheda_dev       = "उपः / अधिके / च",
    why_dev              = (
        "अधिक-अर्थे (हीन-अर्थे च) वर्तमानः 'उप' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83", "1.4.86"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
