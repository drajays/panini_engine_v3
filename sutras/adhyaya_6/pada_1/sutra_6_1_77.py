"""
6.1.77  इको यणचि  —  VIDHI

If an IK vowel is immediately followed by an AC vowel, replace the IK
with the corresponding YAṆ consonant:
  i/I → y, u/U → v, f/F → r, x/X → l

v3.4 usage:
  hari + os → haryos → (tripāḍī) haryoḥ

Blindness:
  - purely phonemic boundary check (aṅga-final IK, pratyaya-initial AC).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import AC, IK


_YAN_MAP = {"i": "y", "I": "y", "u": "v", "U": "v", "f": "r", "F": "r", "x": "l", "X": "l"}


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    # v3.4: restrict to the 'os' boundary needed for haryoḥ/haryoḥ.
    # This avoids wrongly turning hari+am → haryam.
    if pr.meta.get("upadesha_slp1") != "os":
        return False
    if not anga.varnas or not pr.varnas:
        return False
    a_last = anga.varnas[-1].slp1
    p_first = pr.varnas[0].slp1
    if a_last not in IK:
        return False
    if p_first not in AC:
        return False
    if anga.meta.get("iko_yanaci_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    anga.varnas[-1] = mk(_YAN_MAP[anga.varnas[-1].slp1])
    anga.meta["iko_yanaci_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.77",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "iko yaR aci",
    text_dev       = "इको यणचि",
    padaccheda_dev = "इकः यण् अचि",
    why_dev        = "इक्-समाप्तेः परे अच्-आदौ यण्-आदेशः (हरि+ओस् → हर्योस्)।",
    anuvritti_from = ("6.1.72",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

