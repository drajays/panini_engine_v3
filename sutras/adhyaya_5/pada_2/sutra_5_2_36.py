"""
5.2.36  तदस्य संजातं तारकादिभ्य इतच्  —  VIDHI

Padaccheda: तत् अस्य संजातम् तारका-आदिभ्यः इतच्

तदस्य संजातं तारकाऽऽदिभ्य इतच् (5.2.36)
Pāṭha: ashtadhyayi.com data.txt row i=52036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_36_tadasya_36"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.36", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.36"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, what it says of the stem, the pratyaya or its readings)
    (('saMjAta',), dict(gana_name="tArakAdiH"), 'itac'),
)


def _attach(state: State):
    for senses, kw, up in _RULES:
        if any(vivaksita(state, "taddhitArtha", v) for v in senses) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.36")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.36", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'tadasya saMjAtaM tArakAdiBya itac',
    text_dev              = 'तदस्य संजातं तारकादिभ्य इतच्',
    samagra_slp1          = "saMjAtam tat asya iti tArakAdiByaH itac",
    samagra_dev           = "'संजातम् तत् अस्य' (इति) तारकादिभ्यः इतच्",
    padaccheda_dev        = "तत् अस्य संजातम् तारका-आदिभ्यः इतच्",
    why_dev               = "(सूत्रम् 5.2.36) तदस्य संजातं तारकाऽऽदिभ्य इतच्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
