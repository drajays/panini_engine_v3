"""
1.4.98  विभाषा कृञि  (vibhāṣā kṛñi)  —  VIDHI

*Padaccheda:* *vibhāṣā* (prathamā), *kṛñi* (saptamī).

*Anuvṛtti:* *adhi* + *īśvare* **1.4.97**; *karmapravacanīya* **1.4.83**.

*Śāstra:* optionally (*vibhāṣā*) *adhi* is a *karmapravacanīya* when
combined with *kṛ* (kṛñ) in the *īśvara* sense.  The option means it may
also function as a regular *upasarga*.  This closes the **1.4.83** adhikāra.

*Engine:* sets paribhāṣā gate for the optional *adhi-kṛñ* usage.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_98_viBazA_kfYi"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.98",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "viBazA kfYi",
    text_dev             = "विभाषा कृञि",
    padaccheda_dev       = "विभाषा / कृञि",
    why_dev              = (
        "विभाषा — कृञ्-योगे 'अधि' ऐच्छिकरूपेण कर्मप्रवचनीय-संज्ञकः (१.४.८३-१.४.९८-अधिकार-अन्तः)।"
    ),
    anuvritti_from       = ("1.4.83", "1.4.97"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
