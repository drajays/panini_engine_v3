"""
6.1.77  इको यणचि  —  VIDHI

If an IK vowel is immediately followed by an AC vowel, replace the IK
with the corresponding YAṆ consonant:
  i/I → y, u/U → v, f/F → r, x/X → l

v3.4 usage:
  hari + os → haryos → (tripāḍī) haryoḥ

Blindness:
  - purely phonemic boundary check (aṅga-final IK, pratyaya-initial AC).

The narrow *hari*+*os* path and the armed cross-*Term* path both skip when the
left *aṅga* carries **1.1.11** ``pragrahya`` (e.g. *amū* + *atra*).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import AC, IK

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


_YAN_MAP = {"i": "y", "I": "y", "u": "v", "U": "v", "f": "r", "F": "r", "x": "l", "X": "l"}

# Recipe-only general *iko yaṇ aci* across adjacent ``Term``s (e.g. *nu* + *anti*).
_META_IK_YAN_ACI_GENERAL: str = "6_1_77_ik_yan_aci_general_arm"


def _find_armed_ik_yan_aci(state: State) -> int | None:
    """
    Return index ``i`` such that ``terms[i]`` ends in *ik* and ``terms[i+1]``
    begins with *ac*, when ``6_1_77_ik_yan_aci_general_arm`` is set.
    """
    if not state.meta.get(_META_IK_YAN_ACI_GENERAL):
        return None
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if not left.varnas or not right.varnas:
            continue
        if left.meta.get("iko_yanaci_done"):
            continue
        if PRAGHYA_TERM_TAG in left.tags:
            continue
        la = left.varnas[-1].slp1
        rf = right.varnas[0].slp1
        # Armed path: allow dīrgha ``I``/``U``/… (``_YAN_MAP``), not only ``IK``.
        if la not in _YAN_MAP or rf not in AC:
            continue
        return i
    return None


def _find_krt_ak_boundary(state: State) -> int | None:
    """
    Universal kṛdanta boundary: dhātu-final IK/dīrgha followed by kṛt 'ak' (7.1.1).
    Example: āṅ + dīdhīṅ + ṇvul → ... dIDhI + ak → dIDhyak ...
    """
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if "dhatu" not in left.tags:
            continue
        if "krt" not in right.tags:
            continue
        if (right.meta.get("upadesha_slp1") or "").strip() != "ak":
            continue
        if not left.varnas or not right.varnas:
            continue
        if left.meta.get("iko_yanaci_done"):
            continue
        if PRAGHYA_TERM_TAG in left.tags:
            continue
        la = left.varnas[-1].slp1
        rf = right.varnas[0].slp1
        if la not in _YAN_MAP or rf not in AC:
            continue
        return i
    return None


def _find_iti_boundary(state: State) -> int | None:
    """
    Sentence boundary with the nipāta ``iti``: allow *iko yaṇ aci* to be
    *considered* without recipe arming, but still respect pragṛhya.

    This supports demos like ``vAyU iti`` where 6.1.125 (prakṛti-bhāva) blocks yaṇ.
    """
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if not left.varnas or not right.varnas:
            continue
        if left.meta.get("iko_yanaci_done"):
            continue
        if PRAGHYA_TERM_TAG in left.tags:
            continue
        if (right.meta.get("upadesha_slp1") or "").strip() != "iti":
            continue
        la = left.varnas[-1].slp1
        rf = right.varnas[0].slp1
        if la not in _YAN_MAP or rf not in AC:
            continue
        return i
    return None


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr   = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if PRAGHYA_TERM_TAG in anga.tags:
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
    return (
        _matches(state)
        or _find_armed_ik_yan_aci(state) is not None
        or _find_krt_ak_boundary(state) is not None
        or _find_iti_boundary(state) is not None
    )


def act(state: State) -> State:
    j = _find_iti_boundary(state)
    if j is not None:
        left = state.terms[j]
        la = left.varnas[-1].slp1
        left.varnas[-1] = mk(_YAN_MAP[la])
        left.meta["iko_yanaci_done"] = True
        return state
    j = _find_krt_ak_boundary(state)
    if j is not None:
        left = state.terms[j]
        la = left.varnas[-1].slp1
        left.varnas[-1] = mk(_YAN_MAP[la])
        left.meta["iko_yanaci_done"] = True
        return state
    j = _find_armed_ik_yan_aci(state)
    if j is not None:
        left = state.terms[j]
        la = left.varnas[-1].slp1
        left.varnas[-1] = mk(_YAN_MAP[la])
        left.meta["iko_yanaci_done"] = True
        return state
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
    why_dev        = (
        "इक्-समाप्तेः परे अच्-आदौ यण्-आदेशः (हरि+ओस् → हर्योस्; "
        "अथवा रेसिपि-मेटा ६.१.७७-इक्-यण्-अचि-सामान्यम्)।"
    ),
    anuvritti_from = ("6.1.72",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

