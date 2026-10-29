"""
5.4.157  वन्दिते भ्रातुः  —  VIDHI

Padaccheda: वन्दिते भ्रातुः

वन्दिते भ्रातुः (5.4.157)
Pāṭha: ashtadhyayi.com data.txt row i=54157 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_157_vandite_157"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.157", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.157"
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RX = re.compile(r"[a-zA-Z]+BrAtf$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.157", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('bahuvrIhi',)):
        return None
    if not vivaksita(state, "arthaViSeSa", "vandita"):
        return None
    return "bar"


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("done:5.4.157")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    state.meta["kap_barred"] = True        # kap does not follow BrAtf in vandita
    state.meta["done:5.4.157"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vandite BrAtuH",
    text_dev              = "वन्दिते भ्रातुः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA vandite BrAtuH bahuvrIhO kap na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा वन्दिते भ्रातुः बहुव्रीहौ कप् न",
    padaccheda_dev        = "वन्दिते भ्रातुः",
    why_dev               = "(सूत्रम् 5.4.157) वन्दिते भ्रातुः।",
    anuvritti_from        = ('5.4.68',),
    apavada_of     = ('5.4.151', '5.4.153', '5.4.154'),
    also_vidhi     = True,          # no change of the tape: the loop must still offer it
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
