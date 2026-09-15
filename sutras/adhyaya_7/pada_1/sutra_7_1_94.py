"""
7.1.94  ऋदुशनस्पुरुदंसोऽनेहसां च  —  VIDHI

Narrow v3: for a **tṛc** prātipadika (``krt_tfc`` on the aṅga) whose final
is **f** (vocalic ṛ), substitute **an** for that **f** before **su**
(single ``s`` after it-prakaraṇa).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71094 · ऋदुशनस्पुरुदंसोऽनेहसां च
              padaccheda: ऋत्-उशनस्-पुरुदंस्-अनेहसाम् च
              anuvṛtti:   64001: अङ्गस्य | 71092: असम्बुद्धौ | 71093: अनङ् सौ
  Source #2 — Kāśikā 7.1.94 udāharaṇa:
                कर्ता
                हर्ता
                माता
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_trc.py, tests/unit/test_vaktA_split_prakriyas.py
  Reference record: sutra_ref_out/7_1_94.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ang = state.terms[0]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return False
    if ang.meta.get("anaN_7_1_94_done"):
        return False
    if not ang.varnas or ang.varnas[-1].slp1 != "f":
        return False
    if not sup.varnas or sup.varnas[0].slp1 != "s":
        return False
    return True


def act(state: State) -> State:
    ang = state.terms[0]
    ang.varnas[-1] = mk("a")
    ang.varnas.append(mk("n"))
    ang.meta["anaN_7_1_94_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.94",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "fdUSanaspurudaMso anehasAM ca",
    text_dev       = "ऋदुशनस्पुरुदंसोऽनेहसां च",
    padaccheda_dev = "ऋत्-उशनस्-पुरुदंसोः अनेहसां च",
    why_dev        = "ऋकारान्ते अनङ्-आदेशः (तृच् + सु)।",
    anuvritti_from = ("7.1.93",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
