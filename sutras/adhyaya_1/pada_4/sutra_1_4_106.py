"""
1.4.106  प्रहासे च मन्योपपदे मन्यतेरुत्तम एकवच्च  —  VIDHI

*Padaccheda:* *prahāse* (सप्तमी-एकवचन) / *ca* (अव्यय)
/ *manya-upapade* (सप्तमी-एकवचन) / *manyateḥ* (षष्ठी-एकवचन)
/ *uttamaḥ* (प्रथमा-एकवचन) / *eka-vac* (अव्यय) / *ca* (अव्यय).

*Anuvṛtti:* puruṣa assignment from 1.4.105; tiṅ from 1.4.101.

*Content:* In a context of jest/mockery (*prahāsa*) when *manya* appears as
the upapada and the root is *manyate* (√man, to think), the verb takes
*uttama-puruṣa* (first person) and additionally is treated as *ekavacana*
(singular). This is an exceptional reassignment.

*Engine:* cond checks paribhasha_gates for idempotency.
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY     = "1_4_106_prAhAse_uttama"
_REGISTRY_KEY = "uttama_prAhAse"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = "manyopapade"
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.106",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="prahAse ca manyopapade manyateruttama ekavac ca",
    text_dev="प्रहासे च मन्योपपदे मन्यतेरुत्तम एकवच्च",
    padaccheda_dev=(
        "प्रहासे (सप्तमी-एकवचन) / च (अव्यय) / मन्य-उपापदे (सप्तमी-एकवचन) "
        "/ मन्यतेः (षष्ठी-एकवचन) / उत्तमः (प्रथमा-एकवचन) "
        "/ एकवच् (अव्यय) / च (अव्यय)"
    ),
    why_dev=(
        "प्रहासे मन्य-उपापद-विषये मन्यतेः उत्तम-पुरुषः एकवचनं च — "
        "अहं मन्ये (जेस्ट्-संदर्भे); १.४.१०५-अनुवृत्तिः।"
    ),
    anuvritti_from=("1.4.101", "1.4.105"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
