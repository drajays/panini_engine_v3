"""
5.3.79  घनिलचौ च  —  VIDHI

Padaccheda: घन्-इलचौ च

घनिलचौ च (5.3.79)
Pāṭha: ashtadhyayi.com data.txt row i=53079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_79_GanilacO_79"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.79", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.79"
    return state


_VOW = "aAiIuUfFxXeEoO"


def _bahvac(f: str) -> bool:      # bahvac: more than two vowels (ac)
    return sum(c in _VOW for c in f) > 2


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    return ("Gan", "ilac", "Wac", "-") if taddhita_site(state, None, ok=sense_in(state, "5.3.76", "5.3.77"), tag="manuzyanAman", final=_bahvac) is not None else None      # ca: the ṭhac of 5.3.78; vā: ka


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.79")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.79", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.79"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GanilacO ca",
    text_dev              = "घनिलचौ च",
    samagra_slp1          = "anukampAyAm nItO tadyuktAt bahvacaH manuzyanAmnaH Gan-ilacO vA",
    samagra_dev           = "अनुकम्पायाम् नीतौ तद्युक्तात् बह्वचः मनुष्यनाम्नः घन्-इलचौ वा",
    padaccheda_dev        = "घन्-इलचौ च",
    why_dev               = "(सूत्रम् 5.3.79) घनिलचौ च।",
    anuvritti_from        = ('5.3.70',),
    apavada_of     = ('5.3.70', '5.3.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
