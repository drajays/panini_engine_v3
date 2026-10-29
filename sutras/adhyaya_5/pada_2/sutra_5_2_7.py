"""
5.2.7  तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति  —  VIDHI

Padaccheda: तत् सर्व-आदेः पथ्यङ्ग-कर्म-पत्र-पात्रम् व्याप्नोति (क्रियापदम्)

तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति (5.2.7)
Pāṭha: ashtadhyayi.com data.txt row i=52007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_7_tatsarvAde_7"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.7", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.7"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from engine import gana

_TAILS = ("paTin", "aNga", "karman", "patra", "pAtra")


def _sarvadi_final(f: str) -> bool:      # SHORTCUT S36: the compound is one lex:samAsa Term; the sarvādi pūrvapada is read off its letters
    return any(f.endswith(x) and gana.in_gana("sarvAdiH", f[:-len(x)]) for x in _TAILS) or (f.endswith("ANga") and gana.in_gana("sarvAdiH", f[:-4] + "a"))      # sarva + aṅga = sarvāṅga


_RULES = (      # (the senses the sūtra names itself, what it says of the stem, the pratyaya or its readings)
    (('vyApnoti',), dict(tag="samAsa", final=_sarvadi_final), 'Ka'),
)


def _attach(state: State):
    said = {"vyApnoti": vivaksita(state, "taddhitArtha", "vyApnoti")}      # the senses are named by the sūtra itself: literals only
    for senses, kw, up in _RULES:
        if any(said[v] for v in senses) and taddhita_site(state, None, ok=True, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.7")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.7", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatsarvAdeH paTyaNgakarmapatrapAtraM vyApnoti",
    text_dev              = "तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति",
    samagra_slp1          = "tat vyApnoti iti sarvAdeH paTi-aNga-karma-patra-pAtram KaH",
    samagra_dev           = "'तत् व्याप्नोति' (इति) सर्वादेः पथि-अङ्ग-कर्म-पत्र-पात्रम् खः",
    padaccheda_dev        = "तत् सर्व-आदेः पथ्यङ्ग-कर्म-पत्र-पात्रम् व्याप्नोति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.2.7) तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
