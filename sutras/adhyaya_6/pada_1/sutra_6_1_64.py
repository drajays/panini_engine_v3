"""
6.1.64  धात्वादेः षः सः  —  VIDHI (narrow **corrected-v2 P001-C**)

Glass-box row for *ñiṣvidā̃* → *ṣvid* → *svid* before *kta* *niṣṭhā* (**8.2.42**).

General *dhātvādeḥ ṣaḥ saḥ* scope is **not** attempted here (CONSTITUTION Art. 7).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

META_ARM = "corrected_v2_P001_C_6_1_64_arm"


def cond(state: State) -> bool:
    if not state.meta.get(META_ARM):
        return False
    if len(state.terms) < 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if not t0.varnas:
        return False
    if t0.varnas[0].slp1 != "z":
        return False
    if t0.meta.get("corrected_v2_P001_C_6_1_64_done"):
        return False
    return True


def act(state: State) -> State:
    t0 = state.terms[0]
    t0.varnas[0] = mk("s")
    t0.meta["corrected_v2_P001_C_6_1_64_done"] = True
    state.meta.pop(META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.64",
    sutra_type=SutraType.VIDHI,
    text_slp1="dhAtvAdeH zaH saH",
    text_dev="धात्वादेः षः सः",
    padaccheda_dev="धात्वादेः / षः / सः",
    why_dev="धात्वादौ षकारस्य सकारः (P001-C ञिष्विदाँ → स्विद्, आर्म्-सीमितम्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
