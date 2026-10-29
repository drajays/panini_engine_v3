"""
5.2.26  तेन वित्तश्चुञ्चुप्चणपौ  —  VIDHI

Padaccheda: तेन वित्तः चुञ्चुप्-चणपौ

तेन वित्तश्चुञ्चुप्चणपौ (5.2.26)
Pāṭha: ashtadhyayi.com data.txt row i=52026 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_26_tena_26"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.26", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.26"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, what it says of the stem, the pratyaya or its readings)
    (('vitta',), dict(), ('cuYcup', 'caRap')),
)


def _attach(state: State):
    for senses, kw, up in _RULES:
        if any(vivaksita(state, "taddhitArtha", v) for v in senses) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.26")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.26", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena vittaScuYcupcaRapO",
    text_dev              = "तेन वित्तश्चुञ्चुप्चणपौ",
    samagra_slp1          = "tena vittaH iti cuYcup-caRapO",
    samagra_dev           = "'तेन वित्तः' (इति) चुञ्चुप्-चणपौ",
    padaccheda_dev        = "तेन वित्तः चुञ्चुप्-चणपौ",
    why_dev               = "(सूत्रम् 5.2.26) तेन वित्तश्चुञ्चुप्चणपौ।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
