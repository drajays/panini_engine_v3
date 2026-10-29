"""
5.4.20  विभाषा बहोर्धाविप्रकृष्टकाले  —  VIDHI

Padaccheda: विभाषा बहोः धा अविप्रकृष्टकाले

विभाषा बहोर्धाऽविप्रकृष्टकाले (5.4.20)
Pāṭha: ashtadhyayi.com data.txt row i=54020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_20_viBAzA_20"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.20", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.20"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, all of one alternative together; what it says of the stem; the pratyaya or its readings)
    ((("taddhitArtha:kriyAaByAvftti", "arthaViSeSa:aviprakfzwakAla", ),), dict(stems=frozenset(['bahu'])), ('DA', '-')),
)


def _attach(state: State):
    said = {"taddhitArtha:kriyAaByAvftti": vivaksita(state, "taddhitArtha", "kriyAaByAvftti"), "arthaViSeSa:aviprakfzwakAla": vivaksita(state, "arthaViSeSa", "aviprakfzwakAla")}      # the senses are named by the sūtra itself: literals only
    for alts, kw, up in _RULES:
        if any(all(said[x] for x in alt) for alt in alts) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.20")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.20", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.4.20"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'viBAzA bahorDAviprakfzwakAle',
    text_dev              = 'विभाषा बहोर्धाविप्रकृष्टकाले',
    samagra_slp1          = "bahoH aviprakfzwakAle kriyA-aByAvfttigaRane viBAzA DA",
    samagra_dev           = "बहोः अविप्रकृष्टकाले क्रिया-अभ्यावृत्तिगणने विभाषा धा",
    padaccheda_dev        = "विभाषा बहोः धा अविप्रकृष्टकाले",
    why_dev               = "(सूत्रम् 5.4.20) विभाषा बहोर्धाऽविप्रकृष्टकाले।",
    anuvritti_from        = ('4.1.76',),
    apavada_of     = ('5.4.17',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
