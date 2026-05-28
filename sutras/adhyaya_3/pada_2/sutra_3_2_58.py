"""
3.2.58  स्पृशोऽनुदके क्विन्  —  VIDHI

Padaccheda: स्पृशः अनुदके क्विन्

krt-suffix rule: स्पृशोऽनुदके क्विन् (58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_58_spfSonuda_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_58_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "spfSo'nudake kvin",
    text_dev              = "स्पृशोऽनुदके क्विन्",
    padaccheda_dev        = "स्पृशः अनुदके क्विन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्पृशोऽनुदके क्विन्] विहितः (३.२.58)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
