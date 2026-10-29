"""
5.2.103  अण् च  —  VIDHI

Padaccheda: अण् च

अण् च (5.2.103)
Pāṭha: ashtadhyayi.com data.txt row i=52103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_103_aR_103"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.103", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.103"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State, **kw):
    return taddhita_site(state, None, ok=sense_in(state, "5.2.94"), **kw)


def _attach(state: State):
    return "aR" if state.meta.get("hold:5.2.103") and _site(state, stems=frozenset({"tapas", "sahasra"})) is not None else None


def cond(state: State) -> bool:
    return _attach(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state)
    if up is None:
        return _legacy_act(state)
    state.meta["hold:5.2.103"] = False
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aR ca",
    text_dev              = "अण् च",
    samagra_slp1          = "tat asya asmin astIti iti tapaH-sahasrAByAmaR",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) तपः-सहस्राभ्यामण्",
    padaccheda_dev        = "अण् च",
    why_dev               = "(सूत्रम् 5.2.103) अण् च।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.94', '5.2.115'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
