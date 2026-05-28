"""
3.2.178  अन्येभ्योऽपि दृश्यते  —  VIDHI

Padaccheda: अन्येभ्यः अपि दृश्यते (क्रियापदम्)

krt-suffix rule: अन्येभ्योऽपि दृश्यते (178)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_178_anyeByopi_178"


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
    state.meta["krt_kind"] = "3.2.178"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.178",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anyeByo'pi dfSyate",
    text_dev              = "अन्येभ्योऽपि दृश्यते",
    padaccheda_dev        = "अन्येभ्यः अपि दृश्यते (क्रियापदम्)",
    why_dev               = "धातोः कृत्-प्रत्ययः [अन्येभ्योऽपि दृश्यते] विहितः (३.२.178)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
