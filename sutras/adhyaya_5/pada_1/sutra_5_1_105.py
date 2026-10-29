"""
5.1.105  ऋतोरण्  —  VIDHI

Padaccheda: ऋतोः अण्

ऋतोरण् (5.1.105)
Pāṭha: ashtadhyayi.com data.txt row i=51105 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_105_ftoraR_105"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.105", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.105"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return 'aR' if taddhita_site(state, None, ok=sense_in(state, "5.1.104"), stems=frozenset({"ftu"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.105")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.105", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ftoraR",
    text_dev              = "ऋतोरण्",
    samagra_slp1          = "tat asya prAptam iti ftoH aR",
    samagra_dev           = "'तत् अस्य प्राप्तम्' इति ऋतोः अण्",
    padaccheda_dev        = "ऋतोः अण्",
    why_dev               = "(सूत्रम् 5.1.105) ऋतोरण्।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
