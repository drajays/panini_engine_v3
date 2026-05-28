"""
3.1.17  शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे  —  VIDHI

Padaccheda: शब्द-वैर-कलह-अभ्र-कण्व-मेघेभ्यः करणे

Krt suffix rule from dhatu: शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे (17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_17_SabdavErakal_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_17_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SabdavErakalahABrakaRvameGeByaH karaRe",
    text_dev              = "शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे",
    padaccheda_dev        = "शब्द-वैर-कलह-अभ्र-कण्व-मेघेभ्यः करणे",
    why_dev               = "धातोः [शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे]-प्रत्ययः विहितः (३.१.17)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
