"""
5.1.88  वर्षाल्लुक् च  —  VIDHI

Padaccheda: वर्षात् लुक् च

वर्षाल्लुक् च (5.1.88)
Pāṭha: ashtadhyayi.com data.txt row i=51088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_88_varzAlluk_88"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.88", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.88"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita, sense_in
from engine.vikalpa import policy_pick
from engine.luk import live_taddhita, take_away


def _attach(state: State):
    return ("Ka", "-") if arhiya_site(state, "5.1.79", "5.1.80", tag="dvigu", final=lambda f: f.endswith("varza")) is not None else None      # kha, or the ṭhañ that stays

def _luk_site(state: State):
    i = live_taddhita(state)
    if i is None or i == 0 or not sense_in(state, "5.1.79", "5.1.80"):
        return None
    t = state.terms[i - 1]
    flat = "".join(v.slp1 for v in t.varnas)
    return i if "lex:dvigu" in t.tags and flat.endswith("varza") else None


def _attaching(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.88")


def _new_cond(state: State) -> bool:
    if _attaching(state):
        return True
    return _luk_site(state) is not None and not state.meta.get("done:5.1.88")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _attaching(state):
        up = _attach(state)
        up = up[policy_pick(state, "5.1.88", len(up))]
        if up == "-":
            state.meta["declined:5.1.88"] = True
            return state
        return attach_taddhita(state, up)
    i = _luk_site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.1.88"] = True
    if policy_pick(state, "5.1.88.luk", 2) == 1:       # vā: the pratyaya stays
        return state
    return take_away(state, i, "luk")


SUTRA = SutraRecord(
    sutra_id              = "5.1.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varzAlluk ca",
    text_dev              = "वर्षाल्लुक् च",
    samagra_slp1          = "tamaDIzwo Bfto BUto BAvI taTA tena nirvfttam iti varzAt dvigoH KaH WaY vA luk ca ",
    samagra_dev           = "'तमधीष्टो भृतो भूतो भावी' (तथा) 'तेन निर्वृत्तम्' (इति) वर्षात् द्विगोः खः ठञ् वा, लुक् च ।",
    padaccheda_dev        = "वर्षात् लुक् च",
    why_dev               = "(सूत्रम् 5.1.88) वर्षाल्लुक् च।",
    anuvritti_from        = ('5.1.78',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
