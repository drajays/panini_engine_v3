"""
8.4.41  ष्टुना ष्टुः  —  VIDHI (narrow demos)

(A) Canonical shard: ``z`` + ``t`` → ``z`` + ``w`` (ट्) in Tripāḍī.

(B) **P031** (*viśiṇḍhi*): dental ``n`` before palatal ``S`` (श्) → ``R`` (ण्),
    recipe-armed only (JSON’s confused *ṣṭu*-row folded here).

(C) **corrected-v2 P001-B** (*dhṛṣṭaḥ*): ``z``+``t`` → ``z``+``w`` **before**
    **8.2.1** so **4.1.2** can attach *sup* (Tripāḍī firewall).

(निनाय's ``Nal``→``a`` it-lopa now runs through the real it-lopa channel —
**1.3.3**/**1.3.7**/**1.3.9** — not this sūtra; the former (B) *P036* branch
here was a fake home for that and has been removed.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84041 · ष्टुना ष्टुः
              padaccheda: ष्टुना · ष्टुः
              anuvṛtti:   82108: संहितायाम् | 84040: स्तोः
  Source #2 — Kāśikā 8.4.41 udāharaṇa:
                वृक्षष्षण्डे
                प्लक्षष्षण्डे
                वृक्षष्टीकते
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_adhyagIzwa.py, tests/unit/test_dhRSTaH_kta_YiDfzf.py
  Reference record: sutra_ref_out/8_4_41.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find_p031(state: State):
    if not state.meta.get("P031_8_4_41_n_R_before_S_arm"):
        return None
    if not state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("P031_8_4_41_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "n" and vs[i + 1].slp1 == "S":
            return i
    return None


def _find_p001_b_zt_pre_tripadi(state: State):
    """
    **P001-B**: merged *pada* ``Dfz``+``ta`` → ``Dfzta``; apply *ṣṭ* **before**
    ``state.tripadi_zone`` so ``4.1.2`` is not ASIDDHA-blocked.
    """
    if state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("corrected_v2_P001_B_zt_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "z" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def _find_zt(state: State):
    if not state.tripadi_zone:
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if "8_4_41_done" in t.meta:
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "z" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def cond(state: State) -> bool:
    return (
        _find_p031(state) is not None
        or _find_p001_b_zt_pre_tripadi(state) is not None
        or _find_zt(state) is not None
    )


def act(state: State) -> State:
    p = _find_p031(state)
    if p is not None:
        t = state.terms[0]
        t.varnas[p] = mk("R")
        t.meta["P031_8_4_41_done"] = True
        state.meta.pop("P031_8_4_41_n_R_before_S_arm", None)
        return state
    i_pre = _find_p001_b_zt_pre_tripadi(state)
    if i_pre is not None:
        t = state.terms[0]
        t.varnas[i_pre] = mk("w")
        t.meta["corrected_v2_P001_B_zt_done"] = True
        return state
    i = _find_zt(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("w")
    t.meta["8_4_41_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="zwunA zwuH",
    text_dev="ष्टुना ष्टुः",
    padaccheda_dev="ष्टुना / ष्टुः",
    why_dev="ष्-समीपे तकारस्य टकारादेशः; प०३१ न्→ण्; P001-B पूर्व-त्रिपादी ``z``+``t``।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
