"""
5.3.100  देवपथादिभ्यश्च  —  VIDHI

Padaccheda: देवपथ-आदिभ्यः च

देवपथादिभ्यश्च (5.3.100)
Pāṭha: ashtadhyayi.com data.txt row i=53100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_100_devapaTAdi_100"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.100", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.100"
    return state


from engine.taddhita_attach import sense_in
from engine import gana
from engine.luk import live_taddhita, take_away
from engine.vivaksha import vivaksita


def _site(state: State):
    i = live_taddhita(state, only_from=("5.3.96", "5.3.97"))
    return i if i is not None and i > 0 and vivaksita(state, "taddhitArtha", "iva") else None


def _ok(state: State) -> bool:
    i = _site(state)
    return i is not None and gana.in_gana("devapaTAdiH", "".join(v.slp1 for v in state.terms[i - 1].varnas))


def _new_cond(state: State) -> bool:
    return _ok(state) and not state.meta.get("done:5.3.100")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    state.meta["done:5.3.100"] = True
    return take_away(state, _site(state), "lup")      # the kan after the devapathādi stems


SUTRA = SutraRecord(
    sutra_id              = "5.3.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devapaTAdiByaSca",
    text_dev              = "देवपथादिभ्यश्च",
    samagra_slp1          = "ive kanaH devapaTAdiByaH lup",
    samagra_dev           = "इवे कनः देवपथादिभ्यः लुप्",
    padaccheda_dev        = "देवपथ-आदिभ्यः च",
    why_dev               = "(सूत्रम् 5.3.100) देवपथादिभ्यश्च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
