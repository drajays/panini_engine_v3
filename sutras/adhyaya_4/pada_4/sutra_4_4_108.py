"""
4.4.108  समानोदरे शयित ओ चोदात्तः  —  VIDHI

Padaccheda: समानोदरे शयितः ओ (लुप्तप्रथमान्तनिर्देशः) च उदात्तः

समानोदरे शयित ओ चोदात्तः (4.4.108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_108_samAnodare_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.108", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAnodare Sayita o codAttaH",
    text_dev              = "समानोदरे शयित ओ चोदात्तः",
    padaccheda_dev        = "समानोदरे शयितः ओ (लुप्तप्रथमान्तनिर्देशः) च उदात्तः",
    why_dev               = "(सूत्रम् 4.4.108) समानोदरे शयित ओ चोदात्तः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
