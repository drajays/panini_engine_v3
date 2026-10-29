"""
5.3.48  पूरणाद्भागे तीयादन्  —  VIDHI

Padaccheda: पूरणात् भागे तीयात् अन्

पूरणाद्भागे तीयादन् (5.3.48)
Pāṭha: ashtadhyayi.com data.txt row i=53048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_48_pUraRAdBAg_48"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.48", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.48"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (
    ({'stems': ['dvitIya', 'tftIya']}, 'an'),
)      # (the stems the sūtra names, the pratyaya or its readings)


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "BAga")
    if not ok:
        return None
    for kw, up in _RULES:
        if taddhita_site(state, None, ok=True, **{k: (frozenset(v) if k == "stems" else v) for k, v in kw.items()}) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.48")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.48", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.3.48"] = True
        return state
    state = attach_taddhita(state, up)
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUraRAdBAge tIyAdan",
    text_dev              = "पूरणाद्भागे तीयादन्",
    samagra_slp1          = "tIyAt pUraRAt BAge an",
    samagra_dev           = "तीयात् पूरणात् भागे अन्",
    padaccheda_dev        = "पूरणात् भागे तीयात् अन्",
    why_dev               = "(सूत्रम् 5.3.48) पूरणाद्भागे तीयादन्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
