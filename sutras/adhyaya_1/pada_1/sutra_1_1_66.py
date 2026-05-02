"""
1.1.66  तस्मिन्निति निर्दिष्टे पूर्वस्य  —  PARIBHASHA (narrow **P044**)

*Sūtra:* when a rule uses **saptamī** (*tasmin* “in that”), the operation is
understood on the **preceding** (*pūrva*) element — contrast **1.1.67**
(*pañcamī* → *uttara*).

Engine: installs ``paribhasha_gates['1.1.66_tasminniti_nirdiste_purvasya']`` when
``state.meta['prakriya_P044_paribhasha_note']`` is set (recipe-scoped demo).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1.1.66_tasminniti_nirdiste_purvasya"


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_P044_paribhasha_note"):
        return False
    return _GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = {
        "mode": "saptami_purva",
        "why_dev": "सप्तम्यर्थे निर्दिष्टे कार्यं पूर्व-पदे — १.१.६६ (P044)।",
    }
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.66",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="tasmmin iti nirdizwe pUrvasya",
    text_dev="तस्मिन्निति निर्दिष्टे पूर्वस्य",
    padaccheda_dev="तस्मिनि / इति / निर्दिष्टे / पूर्वस्य",
    why_dev="परिभाषा-गेट: सप्तमी-निर्देशे पूर्व-ग्रहणम् (१.१.६६) — P044।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
