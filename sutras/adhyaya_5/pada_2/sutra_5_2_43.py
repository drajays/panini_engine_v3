"""
5.2.43  द्वित्रिभ्यां तयस्यायज्वा  —  VIDHI

Padaccheda: द्वि-त्रिभ्याम् तयस्य अयच् वा

द्वित्रिभ्यां तयस्यायज्वा (5.2.43)
Pāṭha: ashtadhyayi.com data.txt row i=52043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_43_dvitriByAM_43"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.43", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.43"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
# SHORTCUT S36: ayac as the substitute of tayap is attached as a second reading of the pratyaya (ādeśa folded), as in 5.2.44.

_RULES = (      # (the senses the sūtra names itself, what it says of the stem, the pratyaya or its readings)
    (('saMKyAvayava',), dict(stems=frozenset({"dvi", "tri"})), ('tayap', 'ayac')),
)


def _attach(state: State):
    said = {"saMKyAvayava": vivaksita(state, "taddhitArtha", "saMKyAvayava")}      # the senses are named by the sūtra itself: literals only
    for senses, kw, up in _RULES:
        if any(said[v] for v in senses) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.43")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.43", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitriByAM tayasyAyajvA",
    text_dev              = "द्वित्रिभ्यां तयस्यायज्वा",
    samagra_slp1          = "tat asya iti saNKyAyAH avayave dvitriByAm tayasya ayac vA",
    samagra_dev           = "द्वित्रिभ्याम् तयस्य अयच् वा",
    padaccheda_dev        = "द्वि-त्रिभ्याम् तयस्य अयच् वा",
    why_dev               = "(सूत्रम् 5.2.43) द्वित्रिभ्यां तयस्यायज्वा।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.42',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
