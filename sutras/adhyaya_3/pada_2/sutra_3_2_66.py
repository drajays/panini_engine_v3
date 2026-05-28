"""
3.2.66  हव्येऽनन्तः पादम्  —  VIDHI

Padaccheda: हव्येः अनन्तःपादम्

krt-suffix rule: हव्येऽनन्तः पादम् (66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_66_havyenant_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_66_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "havye'nantaH pAdam",
    text_dev              = "हव्येऽनन्तः पादम्",
    padaccheda_dev        = "हव्येः अनन्तःपादम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [हव्येऽनन्तः पादम्] विहितः (३.२.66)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
