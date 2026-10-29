"""
5.1.75  पथः ष्कन्  —  VIDHI

Padaccheda: पथः ष्कन्

पथः ष्कन् (5.1.75)
Pāṭha: ashtadhyayi.com data.txt row i=51075 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_75_paTaH_75"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.75", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.75"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from engine.taddhita_attach import taddhita_site


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "gacCati")
    return "zkan" if taddhita_site(state, None, ok=ok, stems=frozenset({"paTin"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.75")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.75", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.75"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paTaH zkan",
    text_dev              = "पथः ष्कन्",
    samagra_slp1          = "tat gacCati iti paTaH zkan",
    samagra_dev           = "'तत् गच्छति' (इति) पथः ष्कन्",
    padaccheda_dev        = "पथः ष्कन्",
    why_dev               = "(सूत्रम् 5.1.75) पथः ष्कन्।",
    anuvritti_from        = ('5.1.18',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
