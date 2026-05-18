"""
1.4.88  अपपरी वर्जने  (apa-parī varjane)  —  VIDHI

*Padaccheda:* *apa-parī* (prathamā *dvivacana*), *varjane* (saptamī).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**.

*Śāstra:* *apa* and *pari* are *karmapravacanīya* when used in the
*varjana* (exclusion / exception) sense.

*Engine:* sets paribhāṣā gate for *apa/pari-in-varjana*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_88_apa_pari_varjane"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.88",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "apa-parI varjane",
    text_dev             = "अपपरी वर्जने",
    padaccheda_dev       = "अप-परी / वर्जने",
    why_dev              = (
        "वर्जन-अर्थे वर्तमानौ 'अप' 'परि' कर्मप्रवचनीय-संज्ञकौ (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
