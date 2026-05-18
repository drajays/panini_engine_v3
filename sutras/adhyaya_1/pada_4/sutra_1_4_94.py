"""
1.4.94  सुः पूजायाम्  (suḥ pūjāyām)  —  VIDHI

*Padaccheda:* *suḥ* (prathamā), *pūjāyām* (saptamī).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *su* is a *karmapravacanīya* when used in the *pūjā*
(honour / respect) sense.  E.g. *su brāhmaṇam* ("honour to the brāhmaṇa").

*Engine:* sets paribhāṣā gate for *su-in-pūjā*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_94_su_pUjAyAm"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.94",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "suH pUjAyAm",
    text_dev             = "सुः पूजायाम्",
    padaccheda_dev       = "सुः / पूजायाम्",
    why_dev              = (
        "पूजा-अर्थे वर्तमानः 'सु' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
