"""
6.4.143  टेः  —  VIDHI (two narrow *corpus* *loci*)

**(A)** *luṭ* + *ḍit*: when a *tāsi* *vikaraṇa* ``Term`` (``tAsi_vikaraṇa``) ends in ``…A`` + ``s``
(*ṭi*), and the following ``Term`` is a *ḍit* residue beginning with ``a``,
delete the final ``A`` + ``s`` from the *vikaraṇa* ``Term``.

Gate: ``6_4_143_lut_tasi_arm``; completion ``6_4_143_lut_tasi_done``.

**(B)** *kim* + *ḍati* → *kati*: when ``6_4_143_kim_qati_arm`` and ``[kim, qati]``,
replace with a single *prātipadika* ``kati`` (``6_4_143_kim_qati_done``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import parse_slp1_upadesha_sequence


def _find_lut(state: State) -> int | None:
    if not state.meta.get("6_4_143_lut_tasi_arm"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if not t.meta.get("tAsi_vikaraṇa"):
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        if vs[-2].slp1 != "A" or vs[-1].slp1 != "s":
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        if not nxt.meta.get("dit_pratyaya"):
            continue
        return i
    return None


def _find_kim_qati(state: State) -> bool:
    if not state.meta.get("6_4_143_kim_qati_arm"):
        return False
    if len(state.terms) != 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if t0.kind != "prakriti" or t1.kind != "pratyaya":
        return False
    u0 = (t0.meta.get("upadesha_slp1") or "").strip()
    f0 = "".join(v.slp1 for v in t0.varnas)
    if u0 != "kim" and f0 != "kim":
        return False
    u1 = (t1.meta.get("upadesha_slp1") or "").strip()
    if u1 != "qati":
        return False
    if "dit_pratyaya" not in t1.tags:
        return False
    return True


def cond(state: State) -> bool:
    if not state.meta.get("6_4_143_lut_tasi_done"):
        if _find_lut(state) is not None:
            return True
    if not state.meta.get("6_4_143_kim_qati_done"):
        if _find_kim_qati(state):
            return True
    return False


def act(state: State) -> State:
    if not state.meta.get("6_4_143_lut_tasi_done"):
        i = _find_lut(state)
        if i is not None:
            vs = state.terms[i].varnas
            state.terms[i].varnas = vs[:-2]
            state.meta["6_4_143_lut_tasi_done"] = True
            return state
    if not state.meta.get("6_4_143_kim_qati_done") and _find_kim_qati(state):
        kati = Term(
            kind="prakriti",
            varnas=parse_slp1_upadesha_sequence("kati"),
            tags={"prātipadika", "anga"},
            meta={"upadesha_slp1": "kati"},
        )
        state.terms = [kati]
        state.meta.pop("6_4_143_kim_qati_arm", None)
        state.meta["6_4_143_kim_qati_done"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.143",
    sutra_type=SutraType.VIDHI,
    text_slp1="weH DiTi pare Ti-lopa (narrow lut | kim-qati)",
    text_dev="टेः (डिति परे टि-लोपः)",
    padaccheda_dev="टेः / डिति / परे / टि-लोपः",
    why_dev="डित्-परे टि-लोपः — *luṭ*-*vikaraṇ* अथवा *kim*+*qati*→*kati* (आर्म्ड)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
