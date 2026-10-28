"""
5.1.41  सर्वभूमिपृथिवीभ्यामणञौ  —  VIDHI

Padaccheda: सर्वभूमि-पृथिवीभ्याम् अण्-अञौ

सर्वभूमिपृथिवीभ्यामणञौ (5.1.41)
Pāṭha: ashtadhyayi.com data.txt row i=51041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_41_sarvaBUmip_41"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.41", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.41"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick


def _attach(state: State):
    for stem, up in (("sarvaBUmi", "aR"), ("pfTivI", "aY")):      # in the senses 5.1.38, 42, 43 (the anuvṛtti of 42 and 43)
        if arhiya_site(state, "5.1.38", "5.1.42", "5.1.43", stems=frozenset({stem})) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.41")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.41", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.41"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvaBUmipfTivIByAmaRaYO",
    text_dev              = "सर्वभूमिपृथिवीभ्यामणञौ",
    samagra_slp1          = "tasya nimittaM saMyogotpAtO iti sarvaBUmi-pfTivIByAmaR-aYO",
    samagra_dev           = "'तस्य निमित्तं संयोगोत्पातौ' इति सर्वभूमि-पृथिवीभ्यामण्-अञौ",
    padaccheda_dev        = "सर्वभूमि-पृथिवीभ्याम् अण्-अञौ",
    why_dev               = "(सूत्रम् 5.1.41) सर्वभूमिपृथिवीभ्यामणञौ।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
