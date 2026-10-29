"""
5.1.89  चित्तवति नित्यम्  —  VIDHI

Padaccheda: चित्तवति नित्यम्

चित्तवति नित्यम् (5.1.89)
Pāṭha: ashtadhyayi.com data.txt row i=51089 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_89_cittavati_89"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.89", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.89"
    return state


from engine.taddhita_attach import sense_in
from engine.vivaksha import vivaksita
from engine.luk import live_taddhita, take_away


def _luk_site(state: State):
    i = live_taddhita(state)
    if i is None or i == 0 or not sense_in(state, "5.1.79", "5.1.80"):
        return None
    t = state.terms[i - 1]
    flat = "".join(v.slp1 for v in t.varnas)
    return i if "lex:dvigu" in t.tags and flat.endswith("varza") else None


def _new_cond(state: State) -> bool:
    return _luk_site(state) is not None and vivaksita(state, "arthaViSeSa", "cittavat") and not state.meta.get("done:5.1.89")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    i = _luk_site(state)
    if i is None or not _new_cond(state):
        return _legacy_act(state)
    state.meta["done:5.1.89"] = True
    return take_away(state, i, "luk")      # nityam: no vā


SUTRA = SutraRecord(
    sutra_id              = "5.1.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cittavati nityam",
    text_dev              = "चित्तवति नित्यम्",
    samagra_slp1          = "tam BUtaH iti varzAt dvigoH cittavati nityam luk",
    samagra_dev           = "'तम् भूतः' (इति) वर्षात् द्विगोः चित्तवति नित्यम् लुक्",
    padaccheda_dev        = "चित्तवति नित्यम्",
    why_dev               = "(सूत्रम् 5.1.89) चित्तवति नित्यम्।",
    anuvritti_from        = ('5.1.78',),
    apavada_of            = ('5.1.88',),   # nityam: the luk of 5.1.88 is vā, this one is not
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
