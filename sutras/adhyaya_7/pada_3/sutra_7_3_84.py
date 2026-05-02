"""
7.3.84  सार्वधातुकार्धधातुकयोः  —  VIDHI

When the **first** affix **immediately after** the *dhātu* *Term* is *sārvadhātuka*
or *ārdhadhātuka* (``is_sarvadhatuka_upadesha_slp1``, ``sarvadhatuka_3_4_113`` tag,
or ``ardhadhatuka`` / ``sarvadhatuka`` tags — as with *kṛt* **tfc**), replace the
**final ``ik`` vowel** of that *dhātu* with its **guṇa** substitute.

Covers **kṛdanta** ``[dhātu, kṛt]`` and **tin**anta ``[dhātu, śap, tiṅ]`` (trigger
on *Sap* / *tip* *upadeśa*), not only ``terms[-1]`` *kṛt*.

Narrow **P040** (*juhoti*): when ``state.meta['P040_7_3_84_arm']``, *guṇa* targets the
**non-*abhyāsa*** *hu* *dhātu* before ``ti`` (not ``_first_dhatu_index``, which would
hit the *abhyāsa* copy).

ṛ/ṝ → ``a`` with **1.1.51** (उरण् रपरः) completing ``ar`` / ``ar``…
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import IK

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1
from sutras.adhyaya_1.pada_1.sutra_1_1_4 import ik_guna_vriddhi_blocked_by_1_1_4
from sutras.adhyaya_1.pada_1.sutra_1_1_5 import ik_guna_vriddhi_blocked_by_1_1_5
from sutras.adhyaya_1.pada_1.sutra_1_1_6 import dhatu_blocked_by_1_1_6


_IK_GUNA = {
    "i": "e", "I": "e",
    "u": "o", "U": "o",
    "f": "a", "F": "a",
    "x": "a", "X": "a",
}


def _ik_letter(ch: str) -> bool:
    return ch in IK or ch in ("I", "U", "F", "X")


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _p040_non_abhyasa_hu_dhatu_index(state: State) -> int | None:
    """**P040** *juhoti*: *guṇa* on the second *hu* (non-*abhyāsa*), not the first."""
    if not state.meta.get("P040_7_3_84_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "hu":
            continue
        return i
    return None


def _sarvadhatuka_or_ardhadhatuka_following_dhatu(state: State, di: int) -> bool:
    """True iff ``terms[di+1]`` is the *pare* *sārvadhātuka* / *ārdhadhātuka* trigger."""
    if di + 1 >= len(state.terms):
        return False
    nxt = state.terms[di + 1]
    up = (nxt.meta.get("upadesha_slp1") or "").strip()
    if is_sarvadhatuka_upadesha_slp1(up):
        return True
    if "ardhadhatuka" in nxt.tags or "sarvadhatuka" in nxt.tags:
        return True
    if "sarvadhatuka_3_4_113" in nxt.tags:
        return True
    return False


def _p040_eligible(state: State) -> bool:
    di = _p040_non_abhyasa_hu_dhatu_index(state)
    if di is None:
        return False
    d0 = state.terms[di]
    if dhatu_blocked_by_1_1_6(d0.meta.get("upadesha_slp1")):
        return False
    if not _sarvadhatuka_or_ardhadhatuka_following_dhatu(state, di):
        return False
    if d0.meta.get("anga_guna_7_3_84"):
        return False
    if not d0.varnas:
        return False
    last = d0.varnas[-1].slp1
    return _ik_letter(last)


def cond(state: State) -> bool:
    if ik_guna_vriddhi_blocked_by_1_1_4(state):
        return False
    if ik_guna_vriddhi_blocked_by_1_1_5(state):
        return False
    if state.meta.get("P040_7_3_84_arm"):
        return _p040_eligible(state)
    di = _first_dhatu_index(state)
    if di is None:
        return False
    d0 = state.terms[di]
    if "dhatu" not in d0.tags:
        return False
    if dhatu_blocked_by_1_1_6(d0.meta.get("upadesha_slp1")):
        return False
    if not _sarvadhatuka_or_ardhadhatuka_following_dhatu(state, di):
        return False
    if d0.meta.get("anga_guna_7_3_84"):
        return False
    if not d0.varnas:
        return False
    last = d0.varnas[-1].slp1
    return _ik_letter(last)


def act(state: State) -> State:
    if state.meta.get("P040_7_3_84_arm") and _p040_eligible(state):
        di = _p040_non_abhyasa_hu_dhatu_index(state)
        assert di is not None
        d0 = state.terms[di]
        last = d0.varnas[-1].slp1
        rep = _IK_GUNA.get(last, last)
        d0.varnas[-1] = mk(rep)
        d0.meta["anga_guna_7_3_84"] = True
        if last in ("f", "F"):
            d0.meta["urN_rapara_pending"] = "r"
        elif last in ("x", "X"):
            d0.meta["urN_rapara_pending"] = "l"
        state.meta.pop("P040_7_3_84_arm", None)
        return state
    di = _first_dhatu_index(state)
    assert di is not None
    d0 = state.terms[di]
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
    why_dev        = (
        "अङ्गान्तिकः गुणः — धातोः परतरं सार्वधातुके वा आर्धधातुके वा "
        "(तिङ्-शित्-सूची, तृच्-आदि)।"
    ),
    anuvritti_from = ("7.3.83",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
