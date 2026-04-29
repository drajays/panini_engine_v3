"""
7.1.2  प्रत्ययादीनां फढखछघाम् आयन्-एय्-ईन्-ईय्-इयः  —  VIDHI

**Padaccheda:** *āyan*-*ey*-*īn*-*īy*-*iyaḥ* (prathamā bahuvacanam),
*pha-ḍha-kha-cha-ghām* (ṣaṣṭhī bahuvacanam), *pratyayādīnām* (ṣaṣṭhī bahuvacanam).

**Anuvṛtti:** none baked in the short *pāṭha* line below (full *pāṭha* lists all
items as in the user's *anuvṛtti*-sahita reading).

**Adhikāra:** *aṅgasya* **6.4.1** (same thread as neighbouring **7.1.x** in this repo).

**Śāstra (laghu):** the initial **P** (फ्), **Q** (ढ्), **K** (ख्), **C** (छ्), **G** (घ्)
of a **taddhita** (non-*kṛt*, non-*sup*, non-*tiṅ*) *pratyaya* is replaced — *yathāsaṅkhyam*
**1.3.10** — by **Ayana**, **eya**, **Ina**, **Iya**, **iya** respectively (*Pak* →
*Ayana*, *Qak* → *eya*, *K* → *Ina*, *Ca* / *CaH* → *Iya*, *G* → *iya*).  **1.3.7**
*cuṭū* does not give *it* to **Q** / **C** here because **7.1.2** applies first; **1.3.8**
*laśakvataddhite* does not attach to **K** / **G** in the *taddhita* domain, so these
affixes are in scope.  *Kṛt* affixes beginning with **K** / **G** (*kha*, *khaś*,
*ghinuṇ*, …) are **out of scope** (*na* *prasaṅgaḥ*).

**Engine:** rewrites the last ``Term``'s ``varnas`` when the shape matches; sets
``meta['7_1_2_phadi_done']`` and updates ``upadesha_slp1`` to the substitute stem.

**English (one line):** the consonants **Ph–Ḍh–Kh–Ch–Gh** at the start of a qualifying
*taddhita* *pratyaya* are replaced, in order, by **āyan–ey–īn–īy–iy** respectively.
"""
from __future__ import annotations

from typing import List, Optional, Tuple

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term, Varna
from phonology.varna import parse_slp1_upadesha_sequence


_META_DONE = "7_1_2_phadi_done"


def _pratyaya_in_scope(pr: Term) -> bool:
    if pr.kind != "pratyaya":
        return False
    if "krt" in pr.tags:
        return False
    if "sup" in pr.tags or "tin" in pr.tags:
        return False
    return True


def _phadi_replacement(varnas: List[Varna]) -> Optional[Tuple[str, List[Varna]]]:
    """
    If leading shape matches Ph/Ḍh/Kh/Ch/Gh opener, return
    (new_upadesha_slp1, new_varna_list).  Else None.
    """
    if not varnas:
        return None
    c0 = varnas[0].slp1
    # phak
    if (
        c0 == "P"
        and len(varnas) >= 3
        and varnas[1].slp1 == "a"
        and varnas[2].slp1 == "k"
    ):
        return ("Ayana", parse_slp1_upadesha_sequence("Ayana"))
    # ḍhak (vinatā + Ḍhak)
    if (
        c0 == "Q"
        and len(varnas) >= 3
        and varnas[1].slp1 == "a"
        and varnas[2].slp1 == "k"
    ):
        return ("eya", parse_slp1_upadesha_sequence("eya"))
    # kh (kulāt khah)
    if c0 == "K" and len(varnas) == 1:
        return ("Ina", parse_slp1_upadesha_sequence("Ina"))
    # chah (vṛddhāc chaḥ) — Ca or CaH
    if c0 == "C":
        if (
            len(varnas) >= 3
            and varnas[1].slp1 == "a"
            and varnas[2].slp1 == "H"
        ):
            return ("Iya", parse_slp1_upadesha_sequence("Iya"))
        if len(varnas) >= 2 and varnas[1].slp1 == "a":
            return ("Iya", parse_slp1_upadesha_sequence("Iya"))
    # gh (kṣatrād ghah)
    if c0 == "G" and len(varnas) == 1:
        return ("iya", parse_slp1_upadesha_sequence("iya"))
    return None


def _rightmost_phadi_pratyaya_index(state: State) -> int | None:
    for j in range(len(state.terms) - 1, -1, -1):
        pr = state.terms[j]
        if _pratyaya_in_scope(pr):
            return j
    return None


def _anga_index_left_of_phadi(state: State, pr_index: int) -> int | None:
    k = pr_index - 1
    while k >= 0 and term_is_sup_luk_ghost(state.terms[k]):
        k -= 1
    if k < 0 or "anga" not in state.terms[k].tags:
        return None
    return k


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    pj = _rightmost_phadi_pratyaya_index(state)
    if pj is None:
        return False
    aj = _anga_index_left_of_phadi(state, pj)
    if aj is None:
        return False
    pr = state.terms[pj]
    if pr.meta.get(_META_DONE):
        return False
    if _phadi_replacement(pr.varnas) is None:
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pj = _rightmost_phadi_pratyaya_index(state)
    if pj is None:
        return state
    pr = state.terms[pj]
    rep = _phadi_replacement(pr.varnas)
    if rep is None:
        return state
    new_id, new_varnas = rep
    pr.meta["upadesha_slp1_original"] = pr.meta.get(
        "upadesha_slp1_original", pr.meta.get("upadesha_slp1")
    )
    pr.varnas = [v.clone() for v in new_varnas]
    pr.meta["upadesha_slp1"] = new_id
    pr.meta[_META_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.2",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "pratyayAdInAm PaQaKacaGAm AyaneyInIyiyaH",
    text_dev       = "प्रत्ययादीनां फढखछघाम् आयन्-एय्-ईन्-ईय्-इयः",
    padaccheda_dev = (
        "आयन्-एय्-ईन्-ईय्-इयः (प्रथमा-बहुवचनम्) / "
        "फ-ढ-ख-छ-घाम् (षष्ठी-बहुवचनम्) / प्रत्ययादीनाम् (षष्ठी-बहुवचनम्)"
    ),
    why_dev        = (
        "तद्धित-प्रत्ययस्य आदौ फ्-ढ्-ख्-छ्-घ्-क्रमेण आयन्-एय्-ईन्-ईय्-इय्-आदेशाः (१.३.१० यथासङ्ख्यम्)। "
        "कृत्-सुप्-तिङ्-प्रत्ययेषु न।"
    ),
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
