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

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 41004 · अजाद्यतष्टाप्
              padaccheda: अच्-आदि-अतः टाप्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: प्रातिपदिकात् | 41003: स्त्रियाम्
  Source #2 — Kāśikā 4.1.4 udāharaṇa:
                पकारः सामान्यग्रहणार्थः
                टकारः सामान्यग्रहणाविघातार्थः
                अजा
  Cross-check — surface pinned by: tests/unit/test_dyukAmA_bahuvrihi_paribhasha.py, tests/unit/test_sutra_4_1_4_ajadyataSTAp.py, tests/unit/test_taddhita_salIya.py
  Reference record: sutra_ref_out/4_1_4.json
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


def _fem_sarvanama_site(t) -> bool:
    """Feminine sarvanāma whose stem is a-final (after 7.2.102 for tyadādi: ida, ta, ka …)."""
    return "sarvanama" in t.tags and bool(t.varnas) and t.varnas[-1].slp1 == "a"


def _insert_site(state: State):
    if not _in_strI_adhikara(state):
        return None
    hit = _first_strI_prakriti(state)
    if _already_has_tap(state):
        # ṭāp already stands as its own Term (inserted before the sup): for a feminine sarvanāma its a + ā → ā
        # is the antaraṅga step the sarvanāma ādeśas (7.3.114 …) need done first.
        if hit is None or not _has_sup(state) or not _fem_sarvanama_site(hit[1]):
            return None
        i, st = hit
        return (i, st) if i + 1 < len(state.terms) and "stri_wAp" in state.terms[i + 1].tags else None
    if hit is None:
        return None
    idx, t = hit
    sup_present = _has_sup(state)
    if sup_present and not _fem_sarvanama_site(t):
        return None   # a ṭāp *after* sup attachment is only the feminine sarvanāma case below
    if "tyadadi" in t.tags and not sup_present:
        return None
    if "Iyas_bahuvrIhi_pratishedha" in t.tags:
        return None
    flat = "".join(v.slp1 for v in t.varnas)
    # After 7.2.102 the tyadādi stem is a-final (ida, ta, ka): match the tape, not the upadeśa (idam, tad).
    if not tap_4_1_4_applies(None if sup_present else t.meta.get("upadesha_slp1"), flat):
        return None
    return idx, t


def cond(state: State) -> bool:
    return _insert_site(state) is not None


def act(state: State) -> State:
    site = _insert_site(state)
    if site is None:
        return state
    idx, stem = site
    if idx + 1 < len(state.terms) and "stri_wAp" in state.terms[idx + 1].tags:
        before = state.flat_slp1()          # pending ṭāp Term: join it to the prakṛti (a + ā → ā)
        del state.terms[idx + 1]
        stem.varnas[-1] = mk("A")
        stem.tags |= {"TAp_anta", "strīliṅga", "stri_wAp", "anga"}  # the merged prakṛti is the aṅga of the sup
        state.emit_structural("__TAP_SAVARNA__", form_before=before, form_after=state.flat_slp1(),
                              why_dev="ṭāप् + प्रकृति — अ + आ → आ (६.१.१०१ अकः सवर्णे दीर्घः, अङ्ग के भीतर, सुप्-आदेश से पहले)।",
                              type_label="टाप्-सन्धिः", event="MERGE")
        return state
    if _has_sup(state):
        # Feminine sarvanāma: the sup is already on the tape. ṭāp joins the *prakṛti* (antaraṅga) and
        # a + ā → ā (6.1.101 akaḥ savarṇe dīrghaḥ) inside the aṅga, before any sup ādeśa: ida → idā.
        before = state.flat_slp1()
        stem.varnas[-1] = mk("A")
        stem.tags |= {"TAp_anta", "strīliṅga", "stri_wAp"}
        stem.meta["stri_TAp_4_1_4"] = True
        state.emit_structural("__TAP_SAVARNA__", form_before=before, form_after=state.flat_slp1(),
                              why_dev="ṭāप् + प्रकृति — अ + आ → आ (६.१.१०१ अकः सवर्णे दीर्घः, अङ्ग के भीतर, सुप्-आदेश से पहले)।",
                              type_label="टाप्-सन्धिः", event="MERGE")
        return state
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
    text_slp1      = 'ajAdyatazwAp',
    text_dev       = 'अजाद्यतष्टाप्',
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
