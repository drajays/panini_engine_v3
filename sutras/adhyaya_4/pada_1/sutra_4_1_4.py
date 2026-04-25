"""
4.1.4  अजाद्यतष्टाप्  —  VIDHI

पदच्छेदः  अजादि-अतः (पञ्चमी-एकवचनम्), टाप् (प्रथमा-एकवचनम्)

अनुवृत्तिः  ह्रस्वः 1.2.47, प्रातिपदिकस्य 1.2.47

अधिकारः  प्रत्ययः 3.1.1, परश्च 3.1.2, आद्युदात्तश्च 3.1.3, ङ्याप्प्रातिपदिकात् 4.1.1,
          स्त्रियाम् 4.1.3

अनुवृत्तिसहितं सूत्रम्  अजाद्यतः प्रातिपदिकात् स्त्रियाम् टाप् प्रत्ययः

Meaning (summary): To mark the feminine, **ṭāp** is added after a **prātipadika**
that is **hrasva-akārānta** (*at*-para on **ajādi**) or is listed in the
**ajādi**-gaṇa.  *Ākārānta* stems (long **ā**) are excluded by the **at** condition.

Engine (modular, mechanically blind):
  • Eligibility helpers: ``phonology/ajadi_tap_4_1_4.py`` + ``data/inputs/ajadi_gana_slp1.json``.
  • Requires **4.1.3** (*strī*) adhikāra on ``adhikara_stack`` and a **prakṛti**
    ``prātipadika`` tagged ``strīliṅga``.
  • Skips **tyadādi** stems (``tyadadi`` tag): those need **a**-stem substitution
    (e.g. 7.2.102) **before** ṭāp in the full prakriyā — not inserted at this slot
    in ``pipelines/subanta.py`` yet.
  • Inserts a **ṭāp** residue Term (single ``A`` varṇa) tagged ``stri_wAp`` between
    aṅga and **sup**; **6.1.101** then lengthens **a** + **A** across the boundary
    (*khawvā* type).
  • When the stem already carries ``upasarjana`` (e.g. dik-*bahuvrīhi* output),
    adds ``TAp_anta`` (+ ``strīliṅga`` if absent) as a general *ṭāp*-residue /
    feminine-stem signal for **1.2.48** *strī*-branch recipe alignment — not
    at bare compound time (**2.2.26**).  **1.2.48** application itself is still
    tracked via ``meta['1_2_48_hrasva_applied']`` / ``hrasva_1_2_48`` on the merged
    compound, not by this tag name.

This is a narrow slice: no full **wAp** it-lopa simulation here; ``meta`` records
the canonical upadeśa id ``wAp``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk
from phonology.ajadi_tap_4_1_4 import tap_4_1_4_applies


def _in_strI_adhikara(state: State) -> bool:
    return any(e.get("id") == "4.1.3" for e in state.adhikara_stack)


def _first_strI_prakriti(state: State):
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "prātipadika" not in t.tags:
            continue
        if "strīliṅga" not in t.tags:
            continue
        return i, t
    return None


def _already_has_tap(state: State) -> bool:
    return any("stri_wAp" in t.tags for t in state.terms)


def _has_sup(state: State) -> bool:
    return any(t.kind == "pratyaya" and "sup" in t.tags for t in state.terms)


def _insert_site(state: State):
    if not _in_strI_adhikara(state):
        return None
    if _already_has_tap(state) or _has_sup(state):
        return None
    hit = _first_strI_prakriti(state)
    if hit is None:
        return None
    idx, t = hit
    if "tyadadi" in t.tags:
        return None
    if "Iyas_bahuvrIhi_pratishedha" in t.tags:
        return None
    flat = "".join(v.slp1 for v in t.varnas)
    if not tap_4_1_4_applies(t.meta.get("upadesha_slp1"), flat):
        return None
    return idx, t


def cond(state: State) -> bool:
    return _insert_site(state) is not None


def act(state: State) -> State:
    site = _insert_site(state)
    if site is None:
        return state
    idx, stem = site
    tap = Term(
        kind="pratyaya",
        varnas=[mk("A")],
        tags={"upadesha", "pratyaya", "stri_wAp"},
        meta={"upadesha_slp1": "wAp"},
    )
    state.terms.insert(idx + 1, tap)
    stem.meta["stri_TAp_4_1_4"] = True
    if "upasarjana" in stem.tags:
        stem.tags.add("TAp_anta")
        stem.tags.add("strīliṅga")
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.4",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ajAdi ataH prAtipadikAt striyAm wAp pratyayaH",
    text_dev       = "अजाद्यतः प्रातिपदिकात् स्त्रियाम् टाप् प्रत्ययः",
    padaccheda_dev = (
        "अजादि-अतः (पञ्चमी-एकवचनम्) / टाप् (प्रथमा-एकवचनम्)"
    ),
    why_dev        = (
        "अजादिगण-शब्देभ्यः ह्रस्व-अकारान्तेभ्यश्च स्त्रियाम् टाप्; "
        "ईयसो बहुव्रीहेः प्रतिषेधो वार्तिकेन (अङ्गे 'Iyas_bahuvrIhi_pratishedha' इति)।"
    ),
    anuvritti_from = ("1.2.47",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
