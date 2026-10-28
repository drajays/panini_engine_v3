"""
4.4.22  संसृष्टे  —  VIDHI

Padaccheda: संसृष्टे

संसृष्टे (4.4.22)
Pāṭha: ashtadhyayi.com data.txt row i=44022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_22_saMsfzwe_22"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.22", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.22"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _sense(state: State):
    if not stem_ends_tape(state):
        return None
    if vivaksita(state, "taddhitArtha", "saMsfzwa") and not any(e.get("id") == "4.4.22" for e in state.adhikara_stack):
        return ('saMsfzwa', None)
    return None


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _sense(state) is not None:
        v, only = _sense(state)
        return open_default_frame(state, "4.4.22", v, "4.4.1", "4.4.74", only)
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMsfzwe",
    text_dev              = "संसृष्टे",
    samagra_slp1          = "tena saMsfzwe iti samarTAnAm praTamAt paraH Wak pratyayaH",
    samagra_dev           = "'तेन संसृष्टे' (इति) समर्थानाम् प्रथमात् परः ठक् प्रत्ययः",
    padaccheda_dev        = "संसृष्टे",
    why_dev               = "(सूत्रम् 4.4.22) संसृष्टे।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
