"""
7.3.84  सार्वधातुकार्धधातुकयोः  —  VIDHI

Narrow v3: before a following **sārvadhātuka** or **ārdhadhātuka** affix,
replace the **final ``ik`` vowel** of the dhātu *aṅga* with its **guṇa**
substitute (1.1.2 / इको गुणवृद्धी operational slice).

ṛ/ṝ → ``a`` with **1.1.51** (उरण् रपरः) completing ``ar`` / ``ar``…
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import IK


_IK_GUNA = {
    "i": "e", "I": "e",
    "u": "o", "U": "o",
    "f": "a", "F": "a",
    "x": "a", "X": "a",
}


def _ik_letter(ch: str) -> bool:
    return ch in IK or ch in ("I", "U", "F", "X")


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    d0 = state.terms[0]
    pr = state.terms[-1]
    if "dhatu" not in d0.tags or "krt" not in pr.tags:
        return False
    if not (("ardhadhatuka" in pr.tags) or ("sarvadhatuka" in pr.tags)):
        return False
    if d0.meta.get("anga_guna_7_3_84"):
        return False
    if not d0.varnas:
        return False
    last = d0.varnas[-1].slp1
    return _ik_letter(last)


def act(state: State) -> State:
    d0 = state.terms[0]
    last = d0.varnas[-1].slp1
    rep = _IK_GUNA.get(last, last)
    d0.varnas[-1] = mk(rep)
    d0.meta["anga_guna_7_3_84"] = True
    if last in ("f", "F"):
        d0.meta["urN_rapara_pending"] = "r"
    elif last in ("x", "X"):
        d0.meta["urN_rapara_pending"] = "l"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.84",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sArvaDAtukArDaDAtukayoH",
    text_dev       = "सार्वधातुकार्धधातुकयोः",
    padaccheda_dev = "सार्वधातुक-आर्धधातुकयोः",
    why_dev        = "अङ्गान्त्यिकः गुण आर्धधातुके/सार्वधातुके परे (तृच्-पथ)।",
    anuvritti_from = ("7.3.83",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
