"""
5.1.103  कर्मण उकञ्  —  VIDHI

Padaccheda: कर्मणः उकञ्

कर्मण उकञ् (5.1.103)
Pāṭha: ashtadhyayi.com data.txt row i=51103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_103_karmaRa_103"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.103", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.103"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return 'ukaY' if taddhita_site(state, None, ok=sense_in(state, "5.1.101"), stems=frozenset({'karman'})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.103")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.103", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRa ukaY",
    text_dev              = "कर्मण उकञ्",
    samagra_slp1          = "tasmE praBavati iti karmaRaH ukaY",
    samagra_dev           = "'तस्मै प्रभवति' (इति) कर्मणः उकञ्",
    padaccheda_dev        = "कर्मणः उकञ्",
    why_dev               = "(सूत्रम् 5.1.103) कर्मण उकञ्।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
