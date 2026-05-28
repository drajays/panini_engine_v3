"""
3.1.59  कृमृदृरुहिभ्यश्छन्दसि  —  VIDHI

Padaccheda: कृ-मृ-दृ-रुहिभ्यः छन्दसि

Krt suffix rule from dhatu: कृमृदृरुहिभ्यश्छन्दसि (59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_59_kfmfdfruhiBy_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_59_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfmfdfruhiByaSCandasi",
    text_dev              = "कृमृदृरुहिभ्यश्छन्दसि",
    padaccheda_dev        = "कृ-मृ-दृ-रुहिभ्यः छन्दसि",
    why_dev               = "धातोः [कृमृदृरुहिभ्यश्छन्दसि]-प्रत्ययः विहितः (३.१.59)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
