"""
3.1.15  कर्मणः रोमन्थतपोभ्यां वर्तिचरोः  —  VIDHI

Padaccheda: कर्मणः रोमन्थ-तपोभ्याम् वर्ति-चरोः

Krt suffix rule from dhatu: कर्मणः रोमन्थतपोभ्यां वर्तिचरोः (15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_15_karmaRaH_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRaH romanTatapoByAM varticaroH",
    text_dev              = "कर्मणः रोमन्थतपोभ्यां वर्तिचरोः",
    padaccheda_dev        = "कर्मणः रोमन्थ-तपोभ्याम् वर्ति-चरोः",
    why_dev               = "धातोः [कर्मणः रोमन्थतपोभ्यां वर्तिचरोः]-प्रत्ययः विहितः (३.१.15)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
