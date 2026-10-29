"""
5.2.25  पक्षात्तिः  —  VIDHI

Padaccheda: पक्षात् तिः

पक्षात्तिः (5.2.25)
Pāṭha: ashtadhyayi.com data.txt row i=52025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_25_pakzAttiH_25"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.25", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.25"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, what it says of the stem, the pratyaya or its readings)
    (('mUla',), dict(stems=frozenset({"pakza"})), 'ti'),
)


def _attach(state: State):
    said = {"mUla": vivaksita(state, "taddhitArtha", "mUla")}      # the senses are named by the sūtra itself: literals only
    for senses, kw, up in _RULES:
        if any(said[v] for v in senses) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.25")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.25", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pakzAttiH",
    text_dev              = "पक्षात्तिः",
    samagra_slp1          = "tasya mUle iti pakzAt tiH",
    samagra_dev           = "'तस्य मूले' (इति) पक्षात् तिः",
    padaccheda_dev        = "पक्षात् तिः",
    why_dev               = "(सूत्रम् 5.2.25) पक्षात्तिः।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
