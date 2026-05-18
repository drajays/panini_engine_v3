"""
1.4.105  युष्मद्युपपदे समानाधिकरणे स्थानिन्यपि मध्यमः  —  VIDHI

*Padaccheda:* *yuṣmadi* (सप्तमी-एकवचन) / *upapade* (सप्तमी-एकवचन)
/ *samānādhikaraṇe* (सप्तमी-एकवचन) / *sthānini* (सप्तमी-एकवचन)
/ *api* (अव्यय) / *madhyamaḥ* (प्रथमा-एकवचन).

*Anuvṛtti:* tiṅ-puruṣa assignment chain from 1.4.101.

*Content:* When *yuṣmad* (the second-person pronoun) appears as the upapada
in the same syntactic slot (samānādhikaraṇa) as the subject — even when a
substitute (sthānin) is present — the verb takes *madhyama-puruṣa* (second
person) endings.

*Engine:* cond checks paribhasha_gates for idempotency.
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY     = "1_4_105_yuzmad_maDyama"
_REGISTRY_KEY = "maDyama_puruzA"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = "yuzmad_upapade"
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.105",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="yuzmadyupapade samAnADikaraRe sTAninyapi maDyamaH",
    text_dev="युष्मद्युपपदे समानाधिकरणे स्थानिन्यपि मध्यमः",
    padaccheda_dev=(
        "युष्मदि (सप्तमी-एकवचन) / उपापदे (सप्तमी-एकवचन) "
        "/ समानाधिकरणे (सप्तमी-एकवचन) / स्थानिनि (सप्तमी-एकवचन) "
        "/ अपि (अव्यय) / मध्यमः (प्रथमा-एकवचन)"
    ),
    why_dev=(
        "युष्मद्-उपापदे समानाधिकरणे स्थानिन्यपि मध्यम-पुरुष-ग्रहणम् — "
        "त्वं पचसि इत्यत्र मध्यमः; १.४.१०१-अनुवृत्तिः।"
    ),
    anuvritti_from=("1.4.101",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
