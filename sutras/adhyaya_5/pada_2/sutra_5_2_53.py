"""
5.2.53  वतोरिथुक्  —  VIDHI

Padaccheda: वतोः इथुक्

वतोरिथुक् (5.2.53)
Pāṭha: ashtadhyayi.com data.txt row i=52053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_53_vatoriTuk_53"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.53", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.53"
    return state


# SHORTCUT S43: saṃkhyā / saṃkhyādi are lex: tags from the caller (S33)
from engine.taddhita_attach import taddhita_site
from engine.luk import live_taddhita
from engine.state import Term
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    i = live_taddhita(state, only_from=("5.2.48",), upadesha=("qaw",))
    if i is None or i == 0 or state.meta.get("done:5.2.53") or not vivaksita(state, "taddhitArtha", "tasyapUraRa"):
        return None
    t = state.terms[i - 1]
    flat = "".join(v.slp1 for v in t.varnas)
    return i if flat.endswith("vat") else None


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.2.53"] = True
    state.terms.insert(i, Term(kind="agama", varnas=list(parse_slp1_upadesha_sequence("iTuk")), tags={"agama", "upadesha"}, meta={"upadesha_slp1": "iTuk"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vatoriTuk",
    text_dev              = "वतोरिथुक्",
    samagra_slp1          = "tasya pUraRe iti qawi vatoH iTuk",
    samagra_dev           = "'तस्य पूरणे' (इति) डटि वतोः इथुक्",
    padaccheda_dev        = "वतोः इथुक्",
    why_dev               = "(सूत्रम् 5.2.53) वतोरिथुक्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
