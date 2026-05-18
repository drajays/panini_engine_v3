"""
1.3.14  कर्तरि कर्मव्यतिहारे  —  VIDHI

*Padaccheda:* *kartari* (सप्तमी) / *karma-vyatihāre* (सप्तमी).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* In kartari (agentive) construction where there is karma-vyatihāra
(reciprocal action — each subject acts on the other), the verb takes ātmanepada
endings.

*Engine:* cond checks that (a) pada is not already "Atmanepada" and (b) at least one
dhātu Term carries the tag "karmavyatihAra_usage" — set by the recipe to signal a
reciprocal construction.  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_14_kartari_karmavyatihAre"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    return any(
        "dhatu" in t.tags and "karmavyatihAra_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.14",
    sutra_type=SutraType.VIDHI,
    text_slp1="kartari karmavyatihAre",
    text_dev="कर्तरि कर्मव्यतिहारे",
    padaccheda_dev="कर्तरि (सप्तमी) / कर्म-व्यतिहारे (सप्तमी)",
    why_dev=(
        "कर्तरि प्रयोगे यदा कर्म-व्यतिहारः (परस्परक्रिया) अस्ति तदा "
        "आत्मनेपद-विभक्तयः भवन्ति; १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
