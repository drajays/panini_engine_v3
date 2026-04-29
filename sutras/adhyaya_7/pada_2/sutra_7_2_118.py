"""
7.2.118  ङिति च  (kiti ca)  —  VIDHI (narrow: *aṅgā* *ādi*-*vṛddhi* before *kit* *taddhite*)

**Narrow v3 glass-box (``pipelines/taddhita_itika_etikAyana`` only):** when
``State.meta['prakriya_itika_phak']`` and the *taddhite* *pratyaya* carries
``'kit'`` in ``Term.tags`` (*P* *a* *k* in *upadeśa*; *kit* = *k* it) and
**7.1.2** *phadi* has *already* applied (*Āyana* *pratyaya*; **1.3.10**), then
the first *i* in the *aṅga* (*itika* …) is replaced by *E* (SLP1 *vṛddhi* of *i*).

*Scope:* *not* the full **7.2.118** *śāstra* — only this *yoga*; does not
compete with **7.2.116** (ṇit *upadhā*) or **7.2.117** (ñit).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State
from phonology     import mk


def _adi_i_to_E(anga) -> int | None:
    """Index of the first SLP1 ``i`` in ``anga.varnas`` to *vṛddhi*, else ``None``."""
    for j, v in enumerate(anga.varnas):
        if v.slp1 == "i":
            return j
    return None


def _itika_kit_taddhita_index(state: State) -> int | None:
    for j in range(len(state.terms) - 1, -1, -1):
        pr = state.terms[j]
        if term_is_sup_luk_ghost(pr):
            continue
        if "taddhita" in pr.tags and "kit" in pr.tags:
            return j
    return None


def _anga_index_before(state: State, pr_index: int) -> int | None:
    k = pr_index - 1
    while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
        k -= 1
    if k < 0 or "anga" not in state.terms[k].tags:
        return None
    return k


def _matches(state: State) -> bool:
    if not state.meta.get("prakriya_itika_phak"):
        return False
    if not adhikara_in_effect("7.2.118", state, "6.4.1"):
        return False
    if len(state.terms) < 2:
        return False
    pj = _itika_kit_taddhita_index(state)
    if pj is None:
        return False
    aj = _anga_index_before(state, pj)
    if aj is None:
        return False
    anga, pr = state.terms[aj], state.terms[pj]
    if "taddhita" not in pr.tags or "kit" not in pr.tags:
        return False
    if not pr.meta.get("7_1_2_phadi_done"):
        return False
    if anga.meta.get("7_2_118_adi_vrddhi_done"):
        return False
    return _adi_i_to_E(anga) is not None


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pj = _itika_kit_taddhita_index(state)
    aj = _anga_index_before(state, pj) if pj is not None else None
    if pj is None or aj is None:
        return state
    anga = state.terms[aj]
    j = _adi_i_to_E(anga)
    if j is None:
        return state
    anga.varnas[j] = mk("E")
    anga.meta["7_2_118_adi_vrddhi_done"] = True
    anga.meta["upadesha_slp1"] = "Etika"
    return state


SUTRA = SutraRecord(
    sutra_id        = "7.2.118",
    sutra_type      = SutraType.VIDHI,
    text_slp1       = "Niti ca (aNge taddhite~kiti~ parize)",
    text_dev        = "ङिति च (अङ्गे तद्धिते-कि-तद्धित-परिक्षे)।",
    padaccheda_dev  = "ङिति / च (अङ्गे किति)",
    why_dev         = "तद्धित-कि-तद्धित-परिक्षे *इतिक* आदौ *इ*→*E* (वृद्धि)।",
    anuvritti_from  = ("6.4.1", "6.1.1"),
    cond            = cond,
    act             = act,
    adhikara_scope  = None,
)

register_sutra(SUTRA)
