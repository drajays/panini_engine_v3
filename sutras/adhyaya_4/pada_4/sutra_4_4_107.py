"""
4.4.107  समानतीर्थे वासी  —  VIDHI

Padaccheda: समानतीर्थे वासी

समानतीर्थे वासी (4.4.107)
Pāṭha: ashtadhyayi.com data.txt row i=44107 (Art. 14).
"""
# DEFERRED: not yet real — reason, missing feature and the stage that finishes it are in docs/DEFERRED_SUTRAS.md
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_107_samAnatIrT_107"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.107", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.107"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _sense(state: State):
    if not stem_ends_tape(state):
        return None
    if vivaksita(state, "taddhitArtha", "vAsI") and not any(e.get("id") == "4.4.107" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('vAsI', {'stems': ['samAnatIrTa']})
    return None


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _sense(state) is not None:
        v, only = _sense(state)
        return open_default_frame(state, "4.4.107", v, "4.4.75", "5.1.4", only)
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAnatIrTe vAsI",
    text_dev              = "समानतीर्थे वासी",
    samagra_slp1          = "vAsI iti saMjYAyAm samAnatIrTe yat",
    samagra_dev           = "'वासी' (इति) संज्ञायाम् समानतीर्थे यत्",
    padaccheda_dev        = "समानतीर्थे वासी",
    why_dev               = "(सूत्रम् 4.4.107) समानतीर्थे वासी।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
