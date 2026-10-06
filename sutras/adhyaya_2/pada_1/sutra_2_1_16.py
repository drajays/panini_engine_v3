"""
2.1.16  यस्य चायामः  (yasya ca āyāmaḥ)  —  VIDHI

**Pāṭha:** Used in avyayībhāva contexts where *āyāma* (length/extent)
is the meaning — typically with *anu* continued from 2.1.15 (anuvṛtti).

Example: *doṣam anu* → *anudoṣam* ("throughout the night",
  where the night's *āyāma*/extent is the sense).

v3 narrow slice: gate-marks the compound with key
``2_1_16_yasya_ayama``.
Pāṭha: ashtadhyayi.com data.txt row i=21016 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_16_yasya_ayama"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Fire when the pipeline marks an āyāma (extent/length) avyayībhāva context.


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yasya cAyAmaH",
    text_dev              = "यस्य चायामः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA avyayIBAvaH yasya ca AyAmaH lakzaRena anuH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा अव्ययीभावः यस्य च आयामः लक्षणेन अनुः",
    padaccheda_dev        = "यस्य / च / आयामः",
    why_dev               = "आयामार्थे यस्य-शब्दस्य च अव्ययीभावः (२.१.१६)।",
    anuvritti_from        = ("2.1.5", "2.1.15"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
