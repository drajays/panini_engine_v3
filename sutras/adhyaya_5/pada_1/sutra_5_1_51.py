"""
5.1.51  वस्नद्रव्याभ्यां ठन्कनौ  —  VIDHI

Padaccheda: वस्न-द्रव्याभ्याम् ठन्-कनौ

वस्नद्रव्याभ्यां ठन्कनौ (5.1.51)
Pāṭha: ashtadhyayi.com data.txt row i=51051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_51_vasnadravy_51"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.51", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.51"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    for stem, up in (("vasna", "Wan"), ("dravya", "kan")):      # in the sense of 5.1.50
        if arhiya_site(state, "5.1.50", stems=frozenset({stem})) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.51")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.51", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.51"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasnadravyAByAM WankanO",
    text_dev              = "वस्नद्रव्याभ्यां ठन्कनौ",
    samagra_slp1          = "tad harati vahati Avahati iti vasna-dravyAByAm Wan-kanO",
    samagra_dev           = "'तद् हरति, वहति, आवहति' (इति) वस्न-द्रव्याभ्याम् ठन्-कनौ",
    padaccheda_dev        = "वस्न-द्रव्याभ्याम् ठन्-कनौ",
    why_dev               = "(सूत्रम् 5.1.51) वस्नद्रव्याभ्यां ठन्कनौ।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
