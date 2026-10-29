"""
5.2.105  देशे लुबिलचौ च  —  VIDHI

Padaccheda: देशे लुप्-इलचौ च

देशे लुबिलचौ च (5.2.105)
Pāṭha: ashtadhyayi.com data.txt row i=52105 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_105_deSe_105"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.105", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.105"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State, **kw):
    return taddhita_site(state, None, ok=sense_in(state, "5.2.94"), **kw)



from engine.luk import live_taddhita, take_away


def _attach(state: State):
    return "ilac" if state.meta.get("hold:5.2.105") and _site(state, stems=frozenset({"sikatA", "SarkarA"})) is not None else None


def _lup_site(state: State):
    i = live_taddhita(state, only_from=("5.2.104",))
    return i if i is not None and vivaksita(state, "arthaViSeSa", "deSa") and sense_in(state, "5.2.94") and not state.meta.get("done:5.2.105") else None


def cond(state: State) -> bool:
    return _attach(state) is not None or _lup_site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state)
    if up is not None:
        state.meta["hold:5.2.105"] = False
        return attach_taddhita(state, up)
    i = _lup_site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.2.105"] = True
    return take_away(state, i, "lup")      # deśe lub: the aṇ of 5.2.104 is taken away in the sense of a place


SUTRA = SutraRecord(
    sutra_id              = "5.2.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "deSe lubilacO ca",
    text_dev              = "देशे लुबिलचौ च",
    samagra_slp1          = "tat asya asmin astIti iti sikatA-SarkarAByAm deSe aR ilac matu~p lup ca",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) सिकता-शर्कराभ्याम् देशे अण्, इलच्, मतुँप्, लुप् च",
    padaccheda_dev        = "देशे लुप्-इलचौ च",
    why_dev               = "(सूत्रम् 5.2.105) देशे लुबिलचौ च।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.94', '5.2.115'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
