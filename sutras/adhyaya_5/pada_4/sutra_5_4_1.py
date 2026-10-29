"""
5.4.1  पादशतस्य संख्यादेर्वीप्सायां वुन् लोपश्च  —  VIDHI

Padaccheda: पादशतस्य संख्या-आदेः वीप्सायाम् वुन् लोपः च

पादशतस्य संख्याऽऽदेर्वीप्सायां वुन् लोपश्च (5.4.1)
Pāṭha: ashtadhyayi.com data.txt row i=54001 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_1_pAdaSatasy_1"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.1", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.1"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RULES = (      # (the senses the sūtra names itself, all of one alternative together; what it says of the stem; the pratyaya or its readings)
    ((("arthaViSeSa:vIpsA", ),), dict(tag='saMKyAdi', final=lambda f: f.endswith("pAda")), 'vun'),
    ((("arthaViSeSa:vIpsA", ),), dict(tag='saMKyAdi', final=lambda f: f.endswith("Sata")), 'vun'),
)


def _attach(state: State):
    said = {"arthaViSeSa:vIpsA": vivaksita(state, "arthaViSeSa", "vIpsA")}      # the senses are named by the sūtra itself: literals only
    for alts, kw, up in _RULES:
        if any(all(said[x] for x in alt) for alt in alts) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.1")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.1", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.4.1"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'pAdaSatasya saMKyAdervIpsAyAM vun lopaSca',
    text_dev              = 'पादशतस्य संख्यादेर्वीप्सायां वुन् लोपश्च',
    samagra_slp1          = "saMKyAdeH pAda-Satasya vIpsAyAm vun lopaH ca",
    samagra_dev           = "संख्यादेः पाद-शतस्य वीप्सायाम् वुन् लोपः च",
    padaccheda_dev        = "पादशतस्य संख्या-आदेः वीप्सायाम् वुन् लोपः च",
    why_dev               = "(सूत्रम् 5.4.1) पादशतस्य संख्याऽऽदेर्वीप्सायां वुन् लोपश्च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
