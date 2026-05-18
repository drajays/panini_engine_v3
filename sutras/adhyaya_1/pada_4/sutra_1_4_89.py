"""
1.4.89  आङ् मर्यादावचने  (āṅ maryādāvacane)  —  VIDHI

*Padaccheda:* *āṅ* (prathamā), *maryādā-vacane* (saptamī-tatpuruṣa).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *āṅ* (ā) is a *karmapravacanīya* when it expresses *maryādā*
(limit / boundary).  E.g. *ā mūlāt* ("up to the root").

*Engine:* sets paribhāṣā gate for *āṅ-in-maryādā*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_89_AN_maryAdAvacane"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.89",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "AN maryAdAvacane",
    text_dev             = "आङ् मर्यादावचने",
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
