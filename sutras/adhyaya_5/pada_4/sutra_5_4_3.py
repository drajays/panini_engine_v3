"""
5.4.3  स्थूलादिभ्यः प्रकारवचने कन्  —  VIDHI

Padaccheda: स्थूल-आदिभ्यः प्रकारवचने कन्

स्थूलादिभ्यः प्रकारवचने कन् (5.4.3)
Pāṭha: ashtadhyayi.com data.txt row i=54003 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_3_sTUlAdiBya_3"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.3", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.3"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, all of one alternative together; what it says of the stem; the pratyaya or its readings)
    ((("taddhitArtha:prakAravacana", ),), dict(gana_name='sTUlAdiH'), 'kan'),
)


def _attach(state: State):
    said = {"taddhitArtha:prakAravacana": vivaksita(state, "taddhitArtha", "prakAravacana")}      # the senses are named by the sūtra itself: literals only
    for alts, kw, up in _RULES:
        if any(all(said[x] for x in alt) for alt in alts) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.3")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.3", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.4.3"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTUlAdiByaH prakAravacane kan",
    text_dev              = "स्थूलादिभ्यः प्रकारवचने कन्",
    samagra_slp1          = "sTUlAdiByaH prakAravacane kan",
    samagra_dev           = "स्थूलादिभ्यः प्रकारवचने कन्",
    padaccheda_dev        = "स्थूल-आदिभ्यः प्रकारवचने कन्",
    why_dev               = "(सूत्रम् 5.4.3) स्थूलादिभ्यः प्रकारवचने कन्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
