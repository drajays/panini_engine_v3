"""
4.4.1  प्राग्वहतेष्ठक्  —  VIDHI

Padaccheda: प्राक् वहतेः ठक्

प्राग्वहतेष्ठक् (4.4.1)
Pāṭha: ashtadhyayi.com data.txt row i=44001 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_1_prAgvahate_1"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.1", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.1"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _new_cond(state: State) -> bool:
    return default_site(state, "4.4.1") is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        return attach_taddhita(state, "Wak")
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.1",
    sutra_type            = SutraType.ADHIKARA,
    adhikara_scope = ("4.4.1", "4.4.74"),   # the pāṭha's extent
    r1_form_identity_exempt = True,
    text_slp1             = "prAgvahatezWak",
    text_dev              = "प्राग्वहतेष्ठक्",
    samagra_slp1          = "prAk-vahateH Wak",
    samagra_dev           = "प्राक्-वहतेः ठक्",
    padaccheda_dev        = "प्राक् वहतेः ठक्",
    why_dev               = "(सूत्रम् 4.4.1) प्राग्वहतेष्ठक्।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
