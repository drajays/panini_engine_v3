"""Shared locus for 1.2.11 लिङ्सिचावात्मनेपदेषु and 1.2.12 उश्च.

In ātmanepada, a jhal-ādi liṅ (āśīr: sīyuṭ) or sic after the dhātu is kit —
1.2.11 when the dhātu ends in hal with ik next to it (भिद् → भित्सीष्ट),
1.2.12 when it ends in ṛ (कृ → कृषीष्ट, अकृत). Kit blocks guṇa via 1.1.5.
"""
from __future__ import annotations

from engine.state import State

_IK = frozenset("iIuUfFxX")
_VOWELS = frozenset("aAiIuUfFxXeEoO")
_NOT_JHAL = _VOWELS | frozenset("yvrlYmGRnM")


def ling_sic_after(state: State, dhatu_ok) -> int | None:
    """Index of the jhalādi ātmanepada liṅ/sic term right after a dhātu passing ``dhatu_ok``."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        nxt = state.terms[i + 1]
        if "kngiti" in nxt.tags or not nxt.varnas or nxt.varnas[0].slp1 in _NOT_JHAL:
            continue
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        is_ling = "ling_sIyuw" in nxt.tags or (nxt.meta.get("source_lakara_upadesha") == "liG"
                                              and "ardhadhatuka" in nxt.tags)
        is_sic = up == "sic" or "sic_s" in nxt.varnas[0].tags
        atmane = any("atmanepada" in u.tags for u in state.terms[i + 1:])
        if (is_ling or is_sic) and atmane and dhatu_ok([v.slp1 for v in t.varnas]):
            return i + 1
    return None


def hal_ik(vs: list[str]) -> bool:          # 1.2.11 (इको झल् 1.2.9, हलन्ताच्च 1.2.10)
    return len(vs) >= 2 and vs[-1] not in _VOWELS and vs[-2] in _IK


def r_final(vs: list[str]) -> bool:         # 1.2.12 उः = ऋवर्णात्
    return vs[-1] == "f"
