"""
7.3.110  ऋतो ङिसर्वनामस्थानयोः  —  VIDHI (narrow)

**Pāṭha:** *ṛtaḥ ṅi-sarvanāmasthānayoḥ* — *guṇa* of stem-final **ṛ** before a
*ṅit* or *sarvanāmasthāna* affix.

Narrow v3 (``prakriya_21`` *hotāram*):
  • ``state.meta['prakriya_21_7_3_110_arm']``; penultimate ``Term`` *aṅga* with
    ``krt_tfc`` whose last Varṇa is ``f`` (ऋ); final ``Term`` *sup* bears
    ``sarvanamasthana`` (from **1.1.43**).
  • ``act`` — replace final ``f``/``F`` with short ``a`` and arm **1.1.51**
    *uraṇ-rapara* (same hook as **7.3.84**).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73110 · ऋतो ङिसर्वनामस्थानयोः
              padaccheda: ऋतः ङि-सर्वनामस्थानयोः
              anuvṛtti:   64001: अङ्गस्य | 73108: गुणः
  Source #2 — Kāśikā 7.3.110 udāharaṇa:
                ङौ — मातरि
                पितरि
                भ्रातरि
  Cross-check — surface pinned by: tests/unit/test_hotAram.py, tests/unit/test_sutra_7_3_110_hotf_am.py
  Reference record: sutra_ref_out/7_3_110.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

from sutras.adhyaya_1.pada_1.sutra_1_1_43 import TAG as SARVANAMASTHANA_TAG


def _eligible(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ang = state.terms[-2]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags:
        return False
    if SARVANAMASTHANA_TAG not in sup.tags:
        return False
    if not ang.varnas:
        return False
    if ang.varnas[-1].slp1 not in ("f", "F"):
        return False
    if ang.meta.get("Rta_guna_7_3_110_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    ang = state.terms[-2]
    ang.varnas[-1] = mk("a")
    ang.meta["urN_rapara_pending"] = "r"
    ang.meta["urN_rapara_after_index"] = len(ang.varnas) - 1
    ang.meta["Rta_guna_7_3_110_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.110",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "fto Ngi-sarvanAmasthAnayoH",
    text_dev       = "ऋतो ङिसर्वनामस्थानयोः",
    padaccheda_dev = "ऋतः / ङि-सर्वनामस्थानयोः",
    why_dev        = "सर्वनामस्थाने ऋकारस्य गुणः → अ + रपरः (प्रक्रिया-२१)।",
    anuvritti_from = ("7.3.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
