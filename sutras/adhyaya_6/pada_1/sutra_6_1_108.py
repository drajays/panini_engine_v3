"""
6.1.108  सम्प्रसारणाच्च  —  VIDHI

Operational role (v3.6, demo slice):
  After samprasāraṇa (1.1.45), if within the same dhātu term we have an IK
  vowel immediately followed by 'a' (e.g. u + a), collapse to the prior
  vowel (pūrvarūpa-ekādeśa) by deleting that 'a'.

Example (1145.md):
  u a c + t  → u c + t
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import IK


def _find(state: State):
    dh_i = next((i for i, t in enumerate(state.terms) if "dhatu" in t.tags), None)
    if dh_i is None:
        return None
    dh = state.terms[dh_i]
    if dh.meta.get("6_1_108_purvarupa_done"):
        return None
    vs = dh.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 in IK and vs[i + 1].slp1 == "a":
            return (dh_i, i + 1)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    dh_i, del_i = hit
    dh = state.terms[dh_i]
    dh.varnas.pop(del_i)
    dh.meta["6_1_108_purvarupa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.108",
    sutra_type=SutraType.VIDHI,
    text_slp1="saMprasAraNAcca",
    text_dev="सम्प्रसारणाच्च",
    padaccheda_dev="सम्प्रसारणात् च",
    why_dev="सम्प्रसारण-वर्णात् परस्य अचः पूर्वरूप-एकादेशः (उ+अ→उ इत्यादि)।",
    anuvritti_from=("6.1.84",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

