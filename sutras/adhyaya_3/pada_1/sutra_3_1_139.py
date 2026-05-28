"""
3.1.139  ददातिदधात्योर्विभाषा  —  VIDHI

Padaccheda: ददाति-दधात्योः विभाषा

Krt suffix rule from dhatu: ददातिदधात्योर्विभाषा (139)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_139_dadAtidaDAty_139"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_139_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.139"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dadAtidaDAtyorviBAzA",
    text_dev              = "ददातिदधात्योर्विभाषा",
    padaccheda_dev        = "ददाति-दधात्योः विभाषा",
    why_dev               = "धातोः [ददातिदधात्योर्विभाषा]-प्रत्ययः विहितः (३.१.139)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
