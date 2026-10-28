"""
5.1.12  तदर्थं विकृतेः प्रकृतौ  —  VIDHI

Padaccheda: तदर्थम् विकृतेः प्रकृतौ

तदर्थं विकृतेः प्रकृतौ (5.1.12)
Pāṭha: ashtadhyayi.com data.txt row i=51012 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_12_tadarTaM_12"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.12", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.12"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, group_open, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _sense(state: State):
    if not stem_ends_tape(state):
        return None
    if vivaksita(state, "taddhitArtha", "prakfti") and not any(e.get("id") == "5.1.12" for e in state.adhikara_stack):
        return ('prakfti', None)
    return None


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _sense(state) is not None:
        v, only = _sense(state)
        return open_default_frame(state, "5.1.12", v, "5.1.1", "5.1.17", only)
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "5.1.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadarTaM vikfteH prakftO",
    text_dev              = "तदर्थं विकृतेः प्रकृतौ",
    samagra_slp1          = "tadarTaM prakftO iti vikfteH CaH",
    samagra_dev           = "'तदर्थं प्रकृतौ' (इति) विकृतेः छः",
    padaccheda_dev        = "तदर्थम् विकृतेः प्रकृतौ",
    why_dev               = "(सूत्रम् 5.1.12) तदर्थं विकृतेः प्रकृतौ।",
    anuvritti_from        = ('5.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
