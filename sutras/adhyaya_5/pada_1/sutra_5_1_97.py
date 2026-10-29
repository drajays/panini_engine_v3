"""
5.1.97  व्युष्टादिभ्योऽण्  —  VIDHI

Padaccheda: व्युष्ट-आदिभ्यः अण्

व्युष्टादिभ्योऽण् (5.1.97)
Pāṭha: ashtadhyayi.com data.txt row i=51097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_97_vyuzwAdiBy_97"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.97", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.97"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    return 'aR' if taddhita_site(state, None, ok=sense_in(state, "5.1.96"), gana_name="vyuzwAdiH") is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.97")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.97", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'vyuzwAdiByoR',
    text_dev              = 'व्युष्टादिभ्योऽण्',
    samagra_slp1          = "tatra dIyate kAryam iti vyuzwAdiByaH aR",
    samagra_dev           = "'तत्र दीयते, कार्यम्' (इति) व्युष्टादिभ्यः अण्",
    padaccheda_dev        = "व्युष्ट-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 5.1.97) व्युष्टादिभ्योऽण्।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
