"""
5.3.116  दामन्यादित्रिगर्तषष्ठाच्छः  —  VIDHI

Padaccheda: दामनि-आदि-त्रिगर्तषष्ठात् छः

दामन्यादित्रिगर्तषष्ठाच्छः (5.3.116)
Pāṭha: ashtadhyayi.com data.txt row i=53116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_116_dAmanyAdit_116"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.116", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.116"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    return "Ca" if taddhita_site(state, None, ok=True, tag="AyuDajIvisaNGa", gana_name="dAmanyAdiH") is not None or taddhita_site(state, None, ok=True, tag="AyuDajIvisaNGa", stems=frozenset({"kORqoparaTa", "dARqaki", "krORwaki", "jAlamAni", "brAhmagupta", "jAnaki"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.116")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.116", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.116"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dAmanyAditrigartazazWAcCaH",
    text_dev              = "दामन्यादित्रिगर्तषष्ठाच्छः",
    samagra_slp1          = "AyuDajIvisaNGAt dAmanyAdi-trigartazazWAt CaH",
    samagra_dev           = "आयुधजीविसङ्घात् दामन्यादि-त्रिगर्तषष्ठात् छः",
    padaccheda_dev        = "दामनि-आदि-त्रिगर्तषष्ठात् छः",
    why_dev               = "(सूत्रम् 5.3.116) दामन्यादित्रिगर्तषष्ठाच्छः।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
