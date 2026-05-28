"""
3.1.137  पाघ्राध्माधेट्दृशः शः  —  VIDHI

Padaccheda: पा-घ्रा-ध्मा-धेट्-दृशः शः

Krt suffix rule from dhatu: पाघ्राध्माधेट्दृशः शः (137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_137_pAGrADmADewd_137"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_137_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAGrADmADewdfSaH SaH",
    text_dev              = "पाघ्राध्माधेट्दृशः शः",
    padaccheda_dev        = "पा-घ्रा-ध्मा-धेट्-दृशः शः",
    why_dev               = "धातोः [पाघ्राध्माधेट्दृशः शः]-प्रत्ययः विहितः (३.१.137)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
