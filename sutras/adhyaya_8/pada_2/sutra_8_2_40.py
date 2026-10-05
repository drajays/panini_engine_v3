"""
8.2.40  झषस्तथोर्धोऽधः  —  VIDHI

Any झष् (voiced aspirate — घ्/झ्/ढ्/ध्/भ्) immediately before त्/थ् turns
that त्/थ् into ध् — general across the whole झष् class (लब्ध, दुग्ध+ति→
दुग्ध्+धि both go through this same branch), not just a ध्+त् literal.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82040 · झषस्तथोर्धोऽधः
              padaccheda: झषः त-थोः धः अ-धः
  Source #2 — Kāśikā 8.2.40 udāharaṇa:
                लब्धा
                लब्धुम्
                लब्धव्यम्
  Cross-check — surface pinned by: tests/unit/test_corrected_prakriyas_v2_bundle.py, tests/unit/test_iddhaH_kta_YiinDI.py
  Reference record: sutra_ref_out/8_2_40.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

# झष् (4th/voiced-aspirate letter of each varga) — the trigger consonant.
_JHASH = frozenset({"G", "J", "Q", "D", "B"})
_TA_THA = frozenset({"t", "T"})


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_2_40_jhas_tatho_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 in _JHASH and vs[i + 1].slp1 in _TA_THA:
            if t.meta.get("dhatu_upadesha") == "quDAY" and vs[i].slp1 == "D" and "abhyasa_v" not in vs[i].tags:
                continue                                  # अधः: dhā is excepted (धत्तः, not दधद्धः)
            return i + 1
    return None


def _find_p001_d_pre_tripadi(state: State):
    """
    **P001-D** (*iddhaḥ*): merged *pada* ``iD``+``ta`` → ``iDta``; apply **8.2.40**
    **before** **8.2.1** so **4.1.2** is not *asiddha*-blocked (Tripāḍī firewall).
    """
    if not state.meta.get("corrected_v2_P001_D_pre_tripadi_cluster_arm"):
        return None
    if state.tripadi_zone:
        return None
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("corrected_v2_P001_D_pre_8240_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "D" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def _find_p033_Gta(state: State):
    """P033 **8.2.40**: *jhazi* *t*→*d* (द्) after **G** (घ्).

    Scoped to its own pipeline's recipe key (``P033_agda_recipe``, set only
    by ``pipelines/agda_lit_ghas.py`` — NOT ``jhalo_jhali_recipe``, which
    8.2.26 pops after its own use and would already be gone by the time this
    rule runs) now that the general branch below also matches G+t — without
    this gate a generalized caller (e.g. दुह्→दुघ्+ति) would collide with
    this one-word legacy demo and get द् instead of the real ध् the general
    झषस्तथोर्धः text gives.
    """
    if not state.meta.get("P033_agda_recipe"):
        return None
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags or t.meta.get("P033_8_2_40_Gta_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "G" and vs[i + 1].slp1 == "t":
            return i + 1
    return None


def cond(state: State) -> bool:
    if _find_p001_d_pre_tripadi(state) is not None:
        return True
    if not state.tripadi_zone:
        return False
    return _find_p033_Gta(state) is not None or _find(state) is not None


def act(state: State) -> State:
    j_pre = _find_p001_d_pre_tripadi(state)
    if j_pre is not None:
        t = state.terms[0]
        t.varnas[j_pre] = mk("D")
        t.meta["corrected_v2_P001_D_pre_8240_done"] = True
        return state
    j3 = _find_p033_Gta(state)
    if j3 is not None:
        t = state.terms[0]
        t.varnas[j3] = mk("d")
        t.meta["P033_8_2_40_Gta_done"] = True
        return state
    j = _find(state)
    if j is None:
        return state
    t = state.terms[0]
    t.varnas[j] = mk("D")
    t.meta["8_2_40_jhas_tatho_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.40",
    sutra_type=SutraType.VIDHI,
    text_slp1='JazastaTorDoDaH',
    text_dev='झषस्तथोर्धोऽधः',
    padaccheda_dev="झषः / त-थोः / (र्धः) / अधः",
    why_dev="झष्-पूर्वे त्/थ् का ध्-आदेशः (डेमो: रुणद्धि; प००१-डि पूर्व-त्रिपादी)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

