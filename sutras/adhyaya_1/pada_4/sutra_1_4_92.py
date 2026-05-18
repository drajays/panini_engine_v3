"""
1.4.92  प्रतिः प्रतिनिधिप्रतिदानयोः  (pratiḥ pratinidhipradānayoḥ)  —  VIDHI

*Padaccheda:* *pratiḥ* (prathamā), *pratinidhi-pratidānayoḥ* (saptamī-dvivacana).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *prati* is a *karmapravacanīya* in the senses of *pratinidhi*
(substitute / representative) and *pratidāna* (return-gift / giving back).

*Engine:* sets paribhāṣā gate for *prati-in-pratinidhi/pratidāna*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_92_prati_pratiniDi_pratidAna"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.92",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "pratiH pratiniDi-pratidAnayoH",
    text_dev             = "प्रतिः प्रतिनिधिप्रतिदानयोः",
    padaccheda_dev       = "प्रतिः / प्रतिनिधि-प्रतिदानयोः",
    why_dev              = (
        "प्रतिनिधि-प्रतिदान-अर्थयोः वर्तमानः 'प्रति' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
