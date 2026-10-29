"""
5.4.98  उत्तरमृगपूर्वाच्च सक्थ्नः  —  VIDHI

Padaccheda: उत्तर-मृग-पूर्वात् च सक्थ्‍नः

उत्तरमृगपूर्वाच्च सक्थ्नः (5.4.98)
Pāṭha: ashtadhyayi.com data.txt row i=54098 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_98_uttaramfga_98"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.98", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.98"
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_RX = re.compile(r"[a-zA-Z]*sakTi$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.98", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('tatpuruza',)):
        return None
    if not any(f"lex:{x}" in t.tags for x in ('upamAna', 'uttaramfgapUrva')):
        return None
    return 'wac'


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.98")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.98", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.98"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttaramfgapUrvAcca sakTnaH",
    text_dev              = "उत्तरमृगपूर्वाच्च सक्थ्नः",
    samagra_slp1          = "uttara-mfga-pUrvAt upamAnAt ca sakTnaH",
    samagra_dev           = "उत्तर-मृग-पूर्वात् उपमानात् च सक्थ्नः",
    padaccheda_dev        = "उत्तर-मृग-पूर्वात् च सक्थ्‍नः",
    why_dev               = "(सूत्रम् 5.4.98) उत्तरमृगपूर्वाच्च सक्थ्नः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
