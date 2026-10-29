"""
5.4.10  स्थानान्ताद्विभाषा सस्थानेनेति चेत्  —  VIDHI

Padaccheda: स्थान-अन्तात् विभाषा सस्थानेन इति चेत्

स्थानान्ताद्विभाषा सस्थानेनेति चेत् (5.4.10)
Pāṭha: ashtadhyayi.com data.txt row i=54010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_10_sTAnAntAdv_10"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.10", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.10"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, all of one alternative together; what it says of the stem; the pratyaya or its readings)
    ((("taddhitArtha:sasTAna", ),), dict(final=lambda f: f.endswith("sTAna")), ('Ca', '-')),
)


def _attach(state: State):
    said = {"taddhitArtha:sasTAna": vivaksita(state, "taddhitArtha", "sasTAna")}      # the senses are named by the sūtra itself: literals only
    for alts, kw, up in _RULES:
        if any(all(said[x] for x in alt) for alt in alts) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.10")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.10", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.4.10"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTAnAntAdviBAzA sasTAneneti cet",
    text_dev              = "स्थानान्ताद्विभाषा सस्थानेनेति चेत्",
    samagra_slp1          = "sTAnAntAt sasTAnena cet iti viBAzA CaH",
    samagra_dev           = "स्थानान्तात् 'सस्थानेन चेत्' इति विभाषा छः",
    padaccheda_dev        = "स्थान-अन्तात् विभाषा सस्थानेन इति चेत्",
    why_dev               = "(सूत्रम् 5.4.10) स्थानान्ताद्विभाषा सस्थानेनेति चेत्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
