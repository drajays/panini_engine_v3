"""
2.4.28  हेमन्तशिशिरावहोरात्रे च च्छन्दसि  —  VIDHI

Padaccheda: हेमन्तशिशिरौ अहोरात्रे च छन्दसि

hemanta and sisira in ahoraatra and chandas context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_28_hemanta_sisira"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(
        "dvandva_samasa" in t.tags or "samasa_member" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hemantaSiSirAvahorAtre ca cCandasi",
    text_dev              = "हेमन्तशिशिरावहोरात्रे च च्छन्दसि",
    padaccheda_dev        = "हेमन्तशिशिरौ अहोरात्रे च छन्दसि",
    why_dev               = "हेमन्त-शिशिरौ अहोरात्रे च छन्दसि (२.४.२८)।",
    anuvritti_from        = ('2.4.26',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
