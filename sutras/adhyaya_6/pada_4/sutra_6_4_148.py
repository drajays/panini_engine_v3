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


def _finals_for_pair(anga, pr) -> frozenset[str]:
    if "sup" in pr.tags:
        if "bha" not in anga.tags:
            return frozenset()
        return frozenset({"a", "A", "i", "I"})
    return frozenset({"A", "I"})


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


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    if not adhikara_in_effect("6.4.148", state, "6.4.1"):
        return None
    if not adhikara_in_effect("6.4.148", state, "6.4.129"):
        return None
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
        # Hrasva-a + short *i* is **6.1.87** *guṇa* (e.g. *rāma* + *ṭā* → *rāmeṇa*), not
        # this *lopa*.  Keep *a* + long *ī* (*I*) for *deva* + *ṅīp* → *dev* + *ī*.
        if last.slp1 == "a" and first.slp1 == "i":
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
    ti, vi = hit
    del state.terms[ti].varnas[vi]
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
