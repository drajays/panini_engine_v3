"""
5.3.99  जीविकार्थे चापण्ये  —  VIDHI

Padaccheda: जीविका-अर्थे च अपण्ये

जीविकाऽर्थे चापण्ये (5.3.99)
Pāṭha: ashtadhyayi.com data.txt row i=53099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_99_jIvikArTe_99"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.99", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.99"
    return state


from engine.taddhita_attach import sense_in
from engine.luk import live_taddhita, take_away
from engine.vivaksha import vivaksita


def _site(state: State):
    i = live_taddhita(state, only_from=("5.3.96", "5.3.97"))
    return i if i is not None and i > 0 and vivaksita(state, "taddhitArtha", "iva") else None


def _ok(state: State) -> bool:
    i = _site(state)
    return i is not None and vivaksita(state, "jIvikArTa", "jIvikArTa") and vivaksita(state, "abhiDeya", "apaRya")


def _new_cond(state: State) -> bool:
    return _ok(state) and not state.meta.get("done:5.3.99")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    state.meta["done:5.3.99"] = True
    return take_away(state, _site(state), "lup")      # the kan of an image made for a livelihood and not for sale


SUTRA = SutraRecord(
    sutra_id              = "5.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'jIvikArTe cApaRye',
    text_dev              = 'जीविकार्थे चापण्ये',
    samagra_slp1          = "ive kanaH jIvikArTe apaRye lup",
    samagra_dev           = "इवे कनः जीविकार्थे अपण्ये लुप्",
    padaccheda_dev        = "जीविका-अर्थे च अपण्ये",
    why_dev               = "(सूत्रम् 5.3.99) जीविकाऽर्थे चापण्ये।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
