"""
3.1.7  धातोः कर्मणः समानकर्तृकादिच्छायां वा  —  VIDHI (narrow demo)

Demo slice (रुरुदिषति):
  In the sense of desire (icchā), add the sanādi pratyaya `san` (represented
  here as surface `is`) after the dhātu.

Engine:
  - recipe arms via ``state.meta['3_1_7_san_arm']``.
  - appends a pratyaya Term tagged ``sanadi`` with ``upadesha_slp1='is'``.
  - marks it ārdhadhātuka (desiderative base).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("3_1_7_san_arm"):
        return False
    # avoid duplicates
    return not any((t.meta.get("upadesha_slp1") or "").strip() in {"san", "is"} and "sanadi" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    san = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("is"),
        # Not marked as `upadesha` so 1.3.3 (halantyam) doesn't delete final `s`.
        tags={"pratyaya", "sanadi", "ardhadhatuka"},
        meta={"upadesha_slp1": "is"},
    )
    state.terms.append(san)
    state.meta["3_1_7_san_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.7",
    sutra_type=SutraType.VIDHI,
    text_slp1="DAtoH karmaNaH samAnakartfka-icchAyAm vA (narrow)",
    text_dev="धातोः कर्मणः समानकर्तृकादिच्छायां वा",
    padaccheda_dev="धातोः / कर्मणः / समानकर्तृकात् / इच्छायाम् / वा",
    why_dev="इच्छार्थे धातोः सन्-प्रत्ययः (रुरुदिषति)।",
    anuvritti_from=("3.1.1", "3.1.2"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

