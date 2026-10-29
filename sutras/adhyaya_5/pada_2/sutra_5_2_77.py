"""
5.2.77  तावतिथं ग्रहणमिति लुग्वा  —  VIDHI

Padaccheda: तावतिथम् ग्रहणम् इति लुक् वा

तावतिथं ग्रहणमिति लुग्वा (5.2.77)
Pāṭha: ashtadhyayi.com data.txt row i=52077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_77_tAvatiTaM_77"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.77", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.77"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.luk import live_taddhita, take_away
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _ok(state: State) -> bool:
    return vivaksita(state, "taddhitArtha", "grahaRa")


def _attach(state: State):
    return "kan" if taddhita_site(state, None, ok=_ok(state), stems=frozenset({"tAvatiTa"})) is not None else None


def _luk_site(state: State):
    i = live_taddhita(state, only_from=("5.2.77",), upadesha=("kan",))
    return i if i is not None and i > 0 and _ok(state) and not state.meta.get("done:5.2.77") else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None or _luk_site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state)
    if up is not None:
        return attach_taddhita(state, up)
    i = _luk_site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.2.77"] = True
    if policy_pick(state, "5.2.77.luk", 2) == 0:       # lug vā
        take_away(state, i, "luk")
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAvatiTaM grahaRamiti lugvA",
    text_dev              = "तावतिथं ग्रहणमिति लुग्वा",
    samagra_slp1          = "tAvatiTam grahaRam iti luk vA kan",
    samagra_dev           = "तावतिथम् ग्रहणम् इति लुक् वा, कन्",
    padaccheda_dev        = "तावतिथम् ग्रहणम् इति लुक् वा",
    why_dev               = "(सूत्रम् 5.2.77) तावतिथं ग्रहणमिति लुग्वा।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
