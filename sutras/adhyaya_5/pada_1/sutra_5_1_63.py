"""
5.1.63  तद् अर्हति  —  VIDHI

Padaccheda: तत् अर्हति (क्रियापदम्)

तद् अर्हति (5.1.63)
Pāṭha: ashtadhyayi.com data.txt row i=51063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_63_tad_63"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.63", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.63"
    return state


from engine.taddhita_attach import open_sense, open_default_frame

_SENSES = ('arhati',)


def _sense(state: State):
    return next((v for v in _SENSES if open_sense(state, "5.1.63", v)), None)


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    v = _sense(state)
    if v is None:
        return _legacy_act(state)
    return open_default_frame(state, "5.1.63", v, "5.1.18", "5.1.114")      # ṭhañ (5.1.18) is the default to 5.1.114, ṭhak (5.1.19) to 5.1.63


SUTRA = SutraRecord(
    sutra_id              = "5.1.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tad arhati",
    text_dev              = "तद् अर्हति",
    samagra_slp1          = "tad arhati iti samarTAnAM praTamAt paraH WaY-pratyayaH",
    samagra_dev           = "'तद् अर्हति' (इति) समर्थानां प्रथमात् परः ठञ्-प्रत्ययः",
    padaccheda_dev        = "तत् अर्हति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.1.63) तद् अर्हति।",
    anuvritti_from        = ('5.1.19',),
    also_vidhi     = True,          # the loop opens this sense-frame from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
