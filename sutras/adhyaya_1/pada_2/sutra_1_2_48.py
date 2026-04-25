"""
1.2.48  गोस्त्रियोरुपसर्जनस्य  —  VIDHI

पदच्छेदः  गो-स्त्रियोः (षष्ठी-द्विवचनम्), उपसर्जनस्य (षष्ठी-एकवचनम्)

अनुवृत्तिः  ह्रस्वः 1.2.47, प्रातिपदिकस्य 1.2.47

अधिकारः  —

Kāśikā (summary): Of a *prātipadika*, there is *hrasva* when its final part is
an *upasarjana* member that is the word *go* (→ *gu*, e.g. *citraguḥ*) or is
*strī-pratyaya*-final (e.g. *atikhATvaḥ* from *khATvA*).  Counter-examples
(*rājakumārī*, *atitandrīḥ* …) are **not** encoded as phoneme rules here —
the recipe must **not** tag non-*upasarjana* bases.  Vārttika **īyaso
bahuvrīheḥ pratiṣedhaḥ**: no *hrasva* in *bahuvrīhi* + *īyasun* cases — modelled
by tag ``Iyas_bahuvrIhi_pratishedha``.

Engine (modular, mechanically blind):
  • Phoneme rewrites live in ``phonology/gostriyor_upasarjana.py``.
  • Recipe sets ``state.meta['1_2_48_arm'] = True`` and tags the target
    *prakṛti* Term with ``upasarjana`` plus **either** ``gostriyor_go`` **or**
    ``TAp_anta`` (ṭāp-anta / feminine-stem signal from **4.1.4** when *upasarjana*).
  • Tag ``Iyas_bahuvrIhi_pratishedha`` blocks application (vārttika).
"""
from __future__ import annotations

from typing import Optional, Tuple

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.gostriyor_upasarjana import (
    apply_go_hrasva,
    apply_strI_pratyaya_final_hrasva,
    ends_with_go_component,
    flat_slp1,
    strI_final_dirgha_applicable,
)


def _find_target(state: State) -> Optional[Tuple[int, str]]:
    if not state.meta.get("1_2_48_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "upasarjana" not in t.tags:
            continue
        if "Iyas_bahuvrIhi_pratishedha" in t.tags:
            continue
        flat = flat_slp1(t.varnas)
        if "gostriyor_go" in t.tags and ends_with_go_component(flat):
            return i, "go"
        if "TAp_anta" in t.tags and strI_final_dirgha_applicable(flat):
            return i, "strI"
    return None


def cond(state: State) -> bool:
    hit = _find_target(state)
    if hit is None:
        return False
    i, branch = hit
    t = state.terms[i]
    if branch == "go":
        return apply_go_hrasva(t.varnas) is not None
    return apply_strI_pratyaya_final_hrasva(t.varnas) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    i, branch = hit
    t = state.terms[i]
    new_varnas = (
        apply_go_hrasva(t.varnas)
        if branch == "go"
        else apply_strI_pratyaya_final_hrasva(t.varnas)
    )
    if new_varnas is None:
        return state
    nt = Term(
        kind=t.kind,
        varnas=new_varnas,
        tags=set(t.tags),
        meta=dict(t.meta),
    )
    nt.meta["hrasva_1_2_48"] = True
    nt.meta["upadesha_slp1"] = flat_slp1(new_varnas)
    state.terms[i] = nt
    state.meta["1_2_48_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.48",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "go-striyor upasarjanasya",
    text_dev       = "गोस्त्रियोरुपसर्जनस्य",
    padaccheda_dev = (
        "गो-स्त्रियोः (षष्ठी-द्विवचनम्) / उपसर्जनस्य (षष्ठी-एकवचनम्)"
    ),
    why_dev        = (
        "उपसर्जन-गोरुपसर्जनस्त्रीप्रत्ययान्तस्य च प्रातिपदिकस्य ह्रस्वः; "
        "ईयसो बहुव्रीहेः प्रतिषेधः (वार्तिक)।"
    ),
    anuvritti_from = ("1.2.47",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
