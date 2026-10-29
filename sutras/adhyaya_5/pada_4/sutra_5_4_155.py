"""
5.4.155  न संज्ञायाम्  —  VIDHI

Padaccheda: न संज्ञायाम्

न संज्ञायाम् (5.4.155)
Pāṭha: ashtadhyayi.com data.txt row i=54155 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_155_na_155"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.155", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.155"
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

_RX = re.compile(r"[a-zA-Z]+$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.155", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('bahuvrIhi',)):
        return None
    if not vivaksita(state, "arthaViSeSa", "saMjYA"):
        return None
    return "bar"


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("done:5.4.155")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    state.meta["kap_barred"] = True        # kap does not follow in a name
    state.meta["done:5.4.155"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.155",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na saMjYAyAm",
    text_dev              = "न संज्ञायाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA na saMjYAyAm bahuvrIhO kap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा न संज्ञायाम् बहुव्रीहौ कप्",
    padaccheda_dev        = "न संज्ञायाम्",
    why_dev               = "(सूत्रम् 5.4.155) न संज्ञायाम्।",
    anuvritti_from        = ('5.4.68',),
    apavada_of     = ('5.4.151', '5.4.153', '5.4.154'),
    also_vidhi     = True,          # no change of the tape: the loop must still offer it
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
