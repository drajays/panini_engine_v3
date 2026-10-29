"""
5.4.95  ग्रामकौटाभ्यां च तक्ष्णः  —  VIDHI

Padaccheda: ग्राम-कौटाभ्याम् च तक्ष्णः

ग्रामकौटाभ्यां च तक्ष्णः (5.4.95)
Pāṭha: ashtadhyayi.com data.txt row i=54095 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_95_grAmakOwAB_95"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.95", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.95"
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_RX = re.compile(r"(grAma|kowa)takzan$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.95", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('tatpuruza',)):
        return None
    return 'wac'


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.95")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.95", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.95"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmakOwAByAM ca takzRaH",
    text_dev              = "ग्रामकौटाभ्यां च तक्ष्णः",
    samagra_slp1          = "grAmakOwAByAm takzRaH tatpuruzasya wac",
    samagra_dev           = "ग्रामकौटाभ्याम् तक्ष्णः तत्पुरुषस्य टच्",
    padaccheda_dev        = "ग्राम-कौटाभ्याम् च तक्ष्णः",
    why_dev               = "(सूत्रम् 5.4.95) ग्रामकौटाभ्यां च तक्ष्णः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
