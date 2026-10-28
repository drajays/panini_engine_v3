"""
5.1.55  कुलिजाल्लुक्खौ च  —  VIDHI

Padaccheda: कुलिजात् लुक्-खौ च

कुलिजाल्लुक्खौ च (5.1.55)
Pāṭha: ashtadhyayi.com data.txt row i=51055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_55_kulijAlluk_55"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.55", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.55"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita, sense_in
from engine.vikalpa import policy_pick
from engine.luk import live_taddhita, take_away

_FROM = ("5.1.18", "5.1.19", "5.1.20", "5.1.21", "5.1.22", "5.1.23", "5.1.24", "5.1.25", "5.1.26", "5.1.27")     # the ārhīya pratyayas that luk takes away (5.1.28 – 31)


def _attach(state: State):
    return ("Ka", "-") if arhiya_site(state, "5.1.52", stems=frozenset({"kulija"})) is not None else None      # kha, or the ṭhañ whose luk is vā (below)


def _luk_site(state: State):
    i = live_taddhita(state, only_from=_FROM)
    if i is None or i == 0 or not sense_in(state, "5.1.52"):
        return None
    t = state.terms[i - 1]
    return i if (t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)) == "kulija" else None


def _new_cond(state: State) -> bool:
    if state.meta.get("declined:5.1.55") is None and _attach(state) is not None:
        return True
    return _luk_site(state) is not None and not state.meta.get("done:5.1.55")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if state.meta.get("declined:5.1.55") is None and _attach(state) is not None:
        up = _attach(state)
        up = up[policy_pick(state, "5.1.55", len(up))]
        if up == "-":                                  # anyatarasyām: the general pratyaya stays
            state.meta["declined:5.1.55"] = True
            return state
        return attach_taddhita(state, up)
    i = _luk_site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.1.55"] = True
    if policy_pick(state, "5.1.55.luk", 2) == 1:       # anyatarasyām: the pratyaya stays
        return state
    return take_away(state, i, "luk")


SUTRA = SutraRecord(
    sutra_id              = "5.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kulijAllukKO ca",
    text_dev              = "कुलिजाल्लुक्खौ च",
    samagra_slp1          = "tat samBavati avaharati pacati iti kulijAt dvigoH anyatarasyAm luk-KO zWan ca",
    samagra_dev           = "'तत् सम्भवति, अवहरति, पचति' (इति) कुलिजात् द्विगोः अन्यतरस्याम्  लुक्-खौ, ष्ठन्  च",
    padaccheda_dev        = "कुलिजात् लुक्-खौ च",
    why_dev               = "(सूत्रम् 5.1.55) कुलिजाल्लुक्खौ च।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
