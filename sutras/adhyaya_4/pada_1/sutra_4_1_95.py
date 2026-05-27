"""
4.1.95  अत इञ्  —  VIDHI

Padaccheda: अतः इञ्

In the apatya adhikāra (4.1.92), an a-final prātipadika takes the taddhita
suffix iñ (SLP1: iY).  The ñ (Y) is the it-marker (1.3.3 hal-antyam);
1.3.9 will lope it, leaving 'i' and recording 'Y' in `it_markers`.
7.2.117 then applies vṛddhi to the first vowel of the aṅga (ñit context).
6.4.148 then lopos the final 'a' before the 'i' onset.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "4_1_95_ata_iY"


def _site(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.95", state, "4.1.92"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "anga" not in t0.tags:
        return False
    if not t0.varnas or t0.varnas[-1].slp1 != "a":
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["taddhita_kind"] = "4.1.95"
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("iY"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "iY"},
    )
    state.terms.append(pr)
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ata iY",
    text_dev              = "अत इञ्",
    padaccheda_dev        = "अतः इञ्",
    why_dev               = "(सूत्रम् 4.1.95) अत इञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
