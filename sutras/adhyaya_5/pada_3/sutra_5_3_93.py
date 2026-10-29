"""
5.3.93  वा बहूनां जातिपरिप्रश्ने डतमच्  —  VIDHI

Padaccheda: वा बहूनाम् जातिपरिप्रश्ने डतमच्

वा बहूनां जातिपरिप्रश्ने डतमच् (5.3.93)
Pāṭha: ashtadhyayi.com data.txt row i=53093 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_93_vA_93"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.93", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.93"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    # the vā leaves the plain pronoun (ka, ya, sa: 5.3.71 akac), which is not a taddhita derivation: only the ḍatamac reading is derived here
    ok = vivaksita(state, "taddhitArtha", "nirDAraRabahu") and vivaksita(state, "arthaViSeSa", "jAtiparipraSna")
    return "qatamac" if taddhita_site(state, None, ok=ok, stems=frozenset({"kim", "yad", "tad"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.93")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.93", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.93"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA bahUnAM jAtiparipraSne qatamac",
    text_dev              = "वा बहूनां जातिपरिप्रश्ने डतमच्",
    samagra_slp1          = "bahUnAm ekasya jAtiparipraSne nirDAraRe kim-yat-tadoH qatamac vA",
    samagra_dev           = "बहूनाम् एकस्य जातिपरिप्रश्ने निर्धारणे किम्-यत्-तदोः डतमच् वा",
    padaccheda_dev        = "वा बहूनाम् जातिपरिप्रश्ने डतमच्",
    why_dev               = "(सूत्रम् 5.3.93) वा बहूनां जातिपरिप्रश्ने डतमच्।",
    anuvritti_from        = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
