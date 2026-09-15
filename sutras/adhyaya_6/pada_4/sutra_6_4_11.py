"""
6.4.11  अप्तृन्तृच्…  —  VIDHI

Narrow v3:
  • ``…an`` + ``s``-initial *sup* (``cetan`` → ``cetAn`` before ``su``).
  • ``prakriya_21`` — ``hotar``-shaped *tṛc* stem (``…a`` + ``r`` finale) before
    ``am`` *sarvanāmasthāna*: penultimate hrasa ``a`` → **dīrgha** (``hotAr``).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64011 · अप्तृन्तृच्स्वसृनप्तृनेष्टृत्वष्टृक्षत्तृहोतृपोतृप्रशास्तॄणाम्
              padaccheda: अप्-तृन्-तृच्-स्वसृ-नप्तृ-नेष्टृ-त्वष्टृ-क्षत्तृ-होतृ-पोतॄ-प्रशास्तॄणाम्
              anuvṛtti:   63111: दीर्घः | 64001: अङ्गस्य | 64007: उपधायाः | 64008: सर्वनामस्थाने असम्बुद्धौ
  Source #2 — Kāśikā 6.4.11 udāharaṇa:
                अप् — आपः
                बह्वाम्पि तडागानीति केचिदिच्छन्ति
                तत्र  (परि० ८४) इति समासान्तो न क्रियते
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_trc.py, tests/unit/test_akurvAtAm_laG_tanadi_kf.py, tests/unit/test_avaDIt_luN_han.py
  Reference record: sutra_ref_out/6_4_11.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_hrasva


def _eligible_cetan_path(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ang = state.terms[0]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return False
    if ang.meta.get("upadha_dirgha_6_4_11_done"):
        return False
    vs = ang.varnas
    if len(vs) < 3:
        return False
    if vs[-1].slp1 != "n":
        return False
    penult_v = vs[-2].slp1
    if not is_hrasva(penult_v):
        return False
    if not sup.varnas or sup.varnas[0].slp1 != "s":
        return False
    return True


def _eligible_hotr_prakriya_21(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ang = state.terms[-2]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags:
        return False
    if "sup" not in sup.tags:
        return False
    if (sup.meta.get("upadesha_slp1") or "").strip() != "am":
        return False
    if ang.meta.get("upadha_dirgha_6_4_11_hotr_done"):
        return False
    vs = ang.varnas
    if len(vs) < 2:
        return False
    if vs[-1].slp1 != "r":
        return False
    penult_v = vs[-2].slp1
    if penult_v != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _eligible_cetan_path(state) or _eligible_hotr_prakriya_21(state)


def act(state: State) -> State:
    if _eligible_cetan_path(state):
        ang = state.terms[0]
        i = len(ang.varnas) - 2
        v = ang.varnas[i].slp1
        long_map = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
        rep = long_map.get(v, v)
        ang.varnas[i] = mk(rep)
        ang.meta["upadha_dirgha_6_4_11_done"] = True
        return state
    if _eligible_hotr_prakriya_21(state):
        ang = state.terms[-2]
        i = len(ang.varnas) - 2
        v = ang.varnas[i].slp1
        long_map = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
        rep = long_map.get(v, v)
        ang.varnas[i] = mk(rep)
        ang.meta["upadha_dirgha_6_4_11_hotr_done"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.11",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "aptfntfc svf... (narrow)",
    text_dev       = "अप्तृन्तृच्…",
    padaccheda_dev = "अप्तृन्-तृच्-…",
    why_dev        = "तृण्-विषये उपधा-दीर्घः सर्वनामस्थाने (चेता-पथ)।",
    anuvritti_from = ("6.4.10",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
