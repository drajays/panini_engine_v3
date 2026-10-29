"""
5.3.88  कुटीशमीशुण्डाभ्यो रः  —  VIDHI

Padaccheda: कुटी-शमी-शुण्डाभ्यः रः

कुटीशमीशुण्डाभ्यो रः (5.3.88)
Pāṭha: ashtadhyayi.com data.txt row i=53088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_88_kuwISamISu_88"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.88", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.88"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    return 'ra' if taddhita_site(state, None, ok=sense_in(state, "5.3.86"), stems=frozenset({"kuwI", "SamI", "SuRqA"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.88")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.88", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.88"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kuwISamISuRqAByo raH",
    text_dev              = "कुटीशमीशुण्डाभ्यो रः",
    samagra_slp1          = "hrasve kuwI-SamI-SuRqAByaH raH",
    samagra_dev           = "ह्रस्वे कुटी-शमी-शुण्डाभ्यः रः",
    padaccheda_dev        = "कुटी-शमी-शुण्डाभ्यः रः",
    why_dev               = "(सूत्रम् 5.3.88) कुटीशमीशुण्डाभ्यो रः।",
    anuvritti_from        = ('5.3.70',),
    apavada_of     = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
