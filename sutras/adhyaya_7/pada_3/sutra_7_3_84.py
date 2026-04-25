"""
7.3.84  सार्वधातुकार्धधातुकयोः  —  VIDHI

When the **first** affix **immediately after** the *dhātu* *Term* is *sārvadhātuka*
or *ārdhadhātuka* (``is_sarvadhatuka_upadesha_slp1``, ``sarvadhatuka_3_4_113`` tag,
or ``ardhadhatuka`` / ``sarvadhatuka`` tags — as with *kṛt* **tfc**), replace the
**final ``ik`` vowel** of that *dhātu* with its **guṇa** substitute.

Covers **kṛdanta** ``[dhātu, kṛt]`` and **tin**anta ``[dhātu, śap, tiṅ]`` (trigger
on *Sap* / *tip* *upadeśa*), not only ``terms[-1]`` *kṛt*.

ṛ/ṝ → ``a`` with **1.1.51** (उरण् रपरः) completing ``ar`` / ``ar``…
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import IK

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1


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


def cond(state: State) -> bool:
    di = _first_dhatu_index(state)
    if di is None:
        return False
    d0 = state.terms[di]
    if "dhatu" not in d0.tags:
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
