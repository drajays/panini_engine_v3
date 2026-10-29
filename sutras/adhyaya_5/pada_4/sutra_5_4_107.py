"""
5.4.107  अव्ययीभावे शरत्प्रभृतिभ्यः  —  VIDHI

Padaccheda: अव्ययीभावे शरत्-प्रभृतिभ्यः

अव्ययीभावे शरत्प्रभृतिभ्यः (5.4.107)
Pāṭha: ashtadhyayi.com data.txt row i=54107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_107_avyayIBAve_107"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.107", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.107"
    return state


import re
from engine import gana
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_MEMBERS = gana.members("SaradAdiH")      # SHORTCUT S62: the compound is one Term; its last member is read off the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.107", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: any(f.endswith(m) and f != m for m in _MEMBERS))
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('avyayIBAva',)):
        return None
    return 'wac'


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.107")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.107", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.107"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyayIBAve SaratpraBftiByaH",
    text_dev              = "अव्ययीभावे शरत्प्रभृतिभ्यः",
    samagra_slp1          = "SaratpraBftiByaH avyayIBAve wac",
    samagra_dev           = "शरत्प्रभृतिभ्यः अव्ययीभावे टच्",
    padaccheda_dev        = "अव्ययीभावे शरत्-प्रभृतिभ्यः",
    why_dev               = "(सूत्रम् 5.4.107) अव्ययीभावे शरत्प्रभृतिभ्यः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
