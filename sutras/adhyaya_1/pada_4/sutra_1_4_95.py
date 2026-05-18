"""
1.4.95  अतिरतिक्रमणे च  (atir atikramaṇe ca)  —  VIDHI

*Padaccheda:* *atiḥ* (prathamā), *atikramaṇe* (saptamī), *ca* (avyaya).

*Anuvṛtti:* *karmapravacanīya* **1.4.83**; *pūjāyām* **1.4.94** (by *ca*).

*Śāstra:* *ati* is a *karmapravacanīya* in the *atikramaṇa* (transgression /
surpassing) sense, and also in the *pūjā* sense (by *ca* from **1.4.94**).

*Engine:* sets paribhāṣā gate for *ati-in-atikramaṇa*.
``cond`` never reads vibhakti/vacana/lakāra/surface.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_4_95_ati_atikramaRe"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.95",
    sutra_type           = SutraType.VIDHI,
    text_slp1            = "atir atikramaRe ca",
    text_dev             = "अतिरतिक्रमणे च",
    padaccheda_dev       = "अतिः / अतिक्रमणे / च",
    why_dev              = (
        "अतिक्रमण-अर्थे (पूजायां च) वर्तमानः 'अति' कर्मप्रवचनीय-संज्ञकः (१.४.८३-अधिकार)।"
    ),
    anuvritti_from       = ("1.4.83", "1.4.94"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
