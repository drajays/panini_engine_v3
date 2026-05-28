"""
3.2.48  अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः  —  VIDHI

Padaccheda: अन्त-अत्यन्त-अध्व-दूर-पार-सर्व-अनन्तेषु डः

krt-suffix rule: अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः (48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_48_antAtyantA_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antAtyantADvadUrapArasarvAnantezu qaH",
    text_dev              = "अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः",
    padaccheda_dev        = "अन्त-अत्यन्त-अध्व-दूर-पार-सर्व-अनन्तेषु डः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः] विहितः (३.२.48)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
