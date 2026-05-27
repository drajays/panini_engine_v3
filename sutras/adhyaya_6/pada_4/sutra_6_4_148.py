"""
6.4.148  यस्येति च  —  VIDHI

Reading *aṅgasya* from **6.4.1** and *bhasya* from **6.4.129**: the *aṅga*'s
final vowel is elided before an affix whose onset is *i* / *ī* (SLP1 ``i`` /
``I``).

For **sup**-final pratyayas, the *aṅga* must carry the *bha* tag from **1.4.18**
(*yaci bham*) so this rule fires only in the *bhādhikāra* scope intended for
*svādi* (*ac* / *yaṭ*-onset *asarvanāmasthāna* affixes).  Non-**sup** affixes
keep the older engine slice (dīrgha *ā* / *ī* only) without a *bha* check, so
*taddhita* prakriyā examples can still schedule **6.4.148** when **6.4.129** is
open (without requiring the **1.4.18** *bha* tag on **sup**).

Recipe exclusions: **a**+short **i** (→ **6.1.87** *guṇa*); **i**+**i**; and
**a**+**ī** before *sarvanāmasthāna* / **O** / **Si**/**SI** surfaces so
napuṃsaka dual **O** paths stay **jñāne**-style, not *lopa*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State


_NEXT_OK = frozenset({"i", "I"})

META_P004_B_148 = "corrected_v2_P004_B_6_4_148_arm"

META_P004_A_CA_PHAYA = "prakriya_P004_A_caPhaya"
META_P004_A_STAGE2_148 = "corrected_v2_P004_A_stage2_6_4_148_arm"
_UPA_KAU_YJ_AYANA = "kauYjAyana"

META_P005_A_148 = "corrected_v2_P005_A_6_4_148_arm"


def _finals_for_pair(anga, pr) -> frozenset[str]:
    if "sup" in pr.tags:
        if "bha" not in anga.tags:
            return frozenset()
        return frozenset({"a", "A", "i", "I"})
    # Taddhita (non-sup): include short 'a' — e.g. dāśaratha + iñ → dāśarathi
    return frozenset({"a", "A", "I"})


def _p005_a_kurucara_final_a_before_I(state: State) -> tuple[int, int] | None:
    """**P005-A**: *kurucara* + *ṅīp* residue ``ī`` — *aṅgāntya* ``a`` *lopa*."""
    for j in range(1, len(state.terms)):
        nxt = state.terms[j]
        if term_is_sup_luk_ghost(nxt):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        anga = state.terms[k]
        if "anga" not in anga.tags or not anga.varnas or not nxt.varnas:
            continue
        if not anga.meta.get("corrected_v2_P005_A_kurucara_stem"):
            continue
        if anga.varnas[-1].slp1 != "a":
            continue
        if nxt.varnas[0].slp1 != "I":
            continue
        return (k, len(anga.varnas) - 1)
    return None


def _p004_a_caPhaya_ayana_anga_a_lopa(state: State) -> tuple[int, int] | None:
    """
    Same tape geometry as *itika*+*phak* (**Ayana** after **7.1.2**), keyed by
    ``prakriya_P004_A_caPhaya`` (corrected-v2 **P004-A**, च्फञ् cycle).
    """
    if not state.meta.get(META_P004_A_CA_PHAYA):
        return None
    for j in range(1, len(state.terms)):
        nxt = state.terms[j]
        if term_is_sup_luk_ghost(nxt):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        anga = state.terms[k]
        if "anga" not in anga.tags or "bha" not in anga.tags:
            continue
        if "taddhita" not in nxt.tags or not nxt.varnas:
            continue
        if not nxt.meta.get("7_1_2_phadi_done"):
            continue
        if nxt.meta.get("upadesha_slp1") != "Ayana":
            continue
        if not anga.varnas or anga.varnas[-1].slp1 != "a":
            continue
        if nxt.varnas[0].slp1 != "A":
            continue
        return (k, len(anga.varnas) - 1)
    return None


def _p004_a_stage2_kauYjAyana_before_ya(state: State):
    """**P004-A** stage 2: *kauYjAyana* + *yaY* residue ``ya`` (like **P004-B**)."""
    if not state.meta.get(META_P004_A_STAGE2_148):
        return None
    for j in range(1, len(state.terms)):
        nxt = state.terms[j]
        if term_is_sup_luk_ghost(nxt):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        anga = state.terms[k]
        if "anga" not in anga.tags or not anga.varnas or not nxt.varnas:
            continue
        if "taddhita" not in nxt.tags:
            continue
        if (anga.meta.get("upadesha_slp1") or "").strip() != _UPA_KAU_YJ_AYANA:
            continue
        if anga.varnas[-1].slp1 != "a":
            continue
        if len(nxt.varnas) < 2:
            continue
        if nxt.varnas[0].slp1 != "y" or nxt.varnas[1].slp1 != "a":
            continue
        return (k, len(anga.varnas) - 1)
    return None


def _itika_pha_ayana_anga_a_lopa(state: State) -> tuple[int, int] | None:
    """
    *Narrow:* ``prakriya_itika_phak`` + **1.4.18** *bha*; **7.1.2** has
    replaced *Pak* by *Āyana*; lopa of *aṅgāntya* *a* before initial *A*
    of *Āyana* (6.4.129 + *yacy* *bha* pedagogy; not the general *i* / *ī* pair).
    """
    if not state.meta.get("prakriya_itika_phak"):
        return None
    for j in range(1, len(state.terms)):
        nxt = state.terms[j]
        if term_is_sup_luk_ghost(nxt):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        anga = state.terms[k]
        if "anga" not in anga.tags or "bha" not in anga.tags:
            continue
        if "taddhita" not in nxt.tags or not nxt.varnas:
            continue
        if not nxt.meta.get("7_1_2_phadi_done"):
            continue
        if nxt.meta.get("upadesha_slp1") != "Ayana":
            continue
        if not anga.varnas or anga.varnas[-1].slp1 != "a":
            continue
        if nxt.varnas[0].slp1 != "A":
            continue
        return (k, len(anga.varnas) - 1)
    return None


def _p004_b_shandikya_final_a_before_initial_ya(state: State):
    """
    **corrected-v2 P004-B** (*śāṇḍikya*): *aṅgāntya* hrasa ``a`` before *ñya*
    residue ``ya`` (initial ``y`` + ``a``), under **6.4.129** + **6.4.148**.
    """
    for j in range(1, len(state.terms)):
        nxt = state.terms[j]
        if term_is_sup_luk_ghost(nxt):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        anga = state.terms[k]
        if "anga" not in anga.tags or not anga.varnas or not nxt.varnas:
            continue
        if "taddhita" not in nxt.tags:
            continue
        if anga.varnas[-1].slp1 != "a":
            continue
        if len(nxt.varnas) < 2:
            continue
        if nxt.varnas[0].slp1 != "y" or nxt.varnas[1].slp1 != "a":
            continue
        return (k, len(anga.varnas) - 1)
    return None


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    if not adhikara_in_effect("6.4.148", state, "6.4.1"):
        return None
    if not adhikara_in_effect("6.4.148", state, "6.4.129"):
        return None
    hit_b = _p004_b_shandikya_final_a_before_initial_ya(state)
    if hit_b is not None:
        return hit_b
    hit_p04_s2 = _p004_a_stage2_kauYjAyana_before_ya(state)
    if hit_p04_s2 is not None:
        return hit_p04_s2
    hit_p05 = _p005_a_kurucara_final_a_before_I(state)
    if hit_p05 is not None:
        return hit_p05
    # Narrow P018 arm: drop final short i before ika taddhita.
    if state.meta.get("prakriya_P018_6_4_148_i_lopa_before_ika_arm"):
        for j in range(1, len(state.terms)):
            nxt = state.terms[j]
            if term_is_sup_luk_ghost(nxt):
                continue
            k = j - 1
            while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
                k -= 1
            if k < 0:
                continue
            anga = state.terms[k]
            if "anga" not in anga.tags or not anga.varnas or not nxt.varnas:
                continue
            if anga.varnas[-1].slp1 != "i":
                continue
            if "taddhita" not in nxt.tags:
                continue
            if (nxt.meta.get("upadesha_slp1") or "").strip() != "ika":
                continue
            return (k, len(anga.varnas) - 1)
    hit_p04_1 = _p004_a_caPhaya_ayana_anga_a_lopa(state)
    if hit_p04_1 is not None:
        return hit_p04_1
    hit0 = _itika_pha_ayana_anga_a_lopa(state)
    if hit0 is not None:
        return hit0
    for j in range(1, len(state.terms)):
        nxt = state.terms[j]
        if term_is_sup_luk_ghost(nxt):
            continue
        k = j - 1
        while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
            k -= 1
        if k < 0:
            continue
        anga = state.terms[k]
        if "anga" not in anga.tags:
            continue
        if not anga.varnas or not nxt.varnas:
            continue
        finals_ok = _finals_for_pair(anga, nxt)
        if not finals_ok:
            continue
        last = anga.varnas[-1]
        first = nxt.varnas[0]
        if last.slp1 not in finals_ok or first.slp1 not in _NEXT_OK:
            continue
        # In sup context, a+i → guṇa e by 6.1.87 (e.g. rāma+ṭā → rāmeṇa); skip.
        # In taddhita context, 6.4.148 lopa applies (e.g. dāśaratha+iñ → dāśarathi).
        if last.slp1 == "a" and first.slp1 == "i" and "sup" in nxt.tags:
            continue
        # *ikārānta* + affix-initial short *i* (e.g. *hari* + *Ni* → *harau*) — not this lopa.
        if last.slp1 == "i" and first.slp1 == "i":
            continue
        # *a* + *ī* before *sarvanāmasthāna* / dual-*O* paths is not this *lopa*
        # (e.g. *jñāna* + dual → *jñāne*; meta may still read ``O`` or ``Si``).
        if last.slp1 == "a" and first.slp1 == "I":
            if "sarvanamasthana" in nxt.tags:
                continue
            if nxt.meta.get("upadesha_slp1") in ("O", "Si", "SI"):
                continue
        return (k, len(anga.varnas) - 1)
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    hit_s2 = _p004_a_stage2_kauYjAyana_before_ya(state)
    hit_p05 = _p005_a_kurucara_final_a_before_I(state)
    ti, vi = hit
    del state.terms[ti].varnas[vi]
    state.meta.pop("prakriya_P018_6_4_148_i_lopa_before_ika_arm", None)
    if hit_s2 is not None and hit_s2 == hit:
        state.meta.pop(META_P004_A_STAGE2_148, None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.148",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yasyeti ca (aNgasya)",
    text_dev       = "यस्येति च (अङ्गस्य)",
    padaccheda_dev = "यस्य इति च — अङ्गस्य",
    why_dev        = "भाधिकारे इत्यादौ परे अङ्गान्त्यस्य अ/इ-वर्णस्य लोपः।",
    anuvritti_from = ("6.4.1", "6.4.129"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
