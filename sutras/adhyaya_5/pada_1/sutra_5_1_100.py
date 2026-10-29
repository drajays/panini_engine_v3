"""
5.1.100  कर्मवेषाद्यत्  —  VIDHI

Padaccheda: कर्म-वेषात् यत्

कर्मवेषाद्यत् (5.1.100)
Pāṭha: ashtadhyayi.com data.txt row i=51100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_100_karmavezAd_100"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.100", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.100"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return 'yat' if taddhita_site(state, None, ok=sense_in(state, "5.1.99"), stems=frozenset({'karmaveza'})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.100")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.100", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmavezAdyat",
    text_dev              = "कर्मवेषाद्यत्",
    samagra_slp1          = "tena sampAdini iti karma-vezAt yat",
    samagra_dev           = "'तेन सम्पादिनि' (इति) कर्म-वेषात् यत्",
    padaccheda_dev        = "कर्म-वेषात् यत्",
    why_dev               = "(सूत्रम् 5.1.100) कर्मवेषाद्यत्।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
