"""
5.1.96  तत्र च दीयते कार्यं भववत्  —  VIDHI

Padaccheda: तत्र च दीयते (क्रियापदम्) कार्यम् भव-वत्

तत्र च दीयते कार्यं भववत् (5.1.96)
Pāṭha: ashtadhyayi.com data.txt row i=51096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_96_tatra_96"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.96", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.96"
    return state


_SENSES = ("kAladIyate", "kAlatatrakArya")


def _sense(state: State):
    from engine.taddhita_attach import open_sense
    return next((v for v in _SENSES if open_sense(state, "5.1.96", v)), None)


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    v = _sense(state)
    if v is None:
        return _legacy_act(state)
    state.adhikara_stack.append({"id": "5.1.96", "scope_end": "5.1.98", "artha": v})      # SHORTCUT S34: bhavavat names the pratyayas of the bhava sense (4.3.11 ff, not yet real); no default pratyaya opens here
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatra ca dIyate kAryaM Bavavat",
    text_dev              = "तत्र च दीयते कार्यं भववत्",
    samagra_slp1          = "tatra dIyate kAryam  iti kAlAt samarTAnAm praTamAt paraH Bavavat pratyayaH",
    samagra_dev           = "'तत्र दीयते, कार्यम् ' (इति) कालात् समर्थानाम् प्रथमात् परः भववत् प्रत्ययः",
    padaccheda_dev        = "तत्र च दीयते (क्रियापदम्) कार्यम् भव-वत्",
    why_dev               = "(सूत्रम् 5.1.96) तत्र च दीयते कार्यं भववत्।",
    anuvritti_from        = ('5.1.78',),
    also_vidhi     = True,          # the loop opens this sense-frame from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
