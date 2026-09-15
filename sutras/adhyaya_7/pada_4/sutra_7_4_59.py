"""
7.4.59  ह्रस्वः  —  VIDHI (narrow: *abhyāsa* hrasva, P029 *yāyāvara*)

Teaching JSON **P029** step 7 / **P030** (*vivakṣaka*): the *abhyāsa* vowel is
first *hrasva* (here *A* → *a*, or *U* → *u*).

Teaching JSON **P034** (*jakṣatuḥ*): after **7.4.62**, the *abhyāsa* may be a lone
**j**; the JSON’s *hrasva* step is modelled as appending *hrasva* **a** so the
*abhyāsa* surface is **ja** before *pada* merge.

Teaching JSON **P035** (*papatuḥ*): *abhyāsa* **pā** → **pa** (*A* → *a*).

Teaching JSON **P036** (*nināya*): *abhyāsa* **ne** → **ni** (*e* → *i*, lit *hrasva*
row).

Narrow v3:
  • **P029** / **P030** / **P035**: ``…_abhyasa_hrasva_arm`` on the first ``abhyasa``-
    tagged ``Term`` with a *dīrgha* *ak* vowel → replace the **leftmost** such vowel
    with its *hrasva* mate.
  • **P034**: abhyāsa is exactly **j** (single varṇa) → append **a**.
  • **P036**: abhyāsa is exactly **ne** → **ni**.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74059 · ह्रस्वः
              padaccheda: ह्रस्वः
              anuvṛtti:   64001: अङ्गस्य | 74058: अभ्यासस्य | 12028: अचः
  Source #2 — Kāśikā 7.4.59 udāharaṇa:
                दुढौकिषते
                तुत्रौकिषते
                डुढौके
  Cross-check — surface pinned by: tests/unit/test_jakzatuH_lit_ad_gas.py, tests/unit/test_juhoti_hu_lat_tip_Slu.py, tests/unit/test_kf_lit_karmani_bhave.py
  Reference record: sutra_ref_out/7_4_59.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha

_D2H: dict[str, str] = {"A": "a", "I": "i", "U": "u", "F": "f", "X": "x"}


def _abhyasa_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "abhyasa" in t.tags:
            return i
    return None


def _first_dirgha_ak_index(t) -> int | None:
    for j, v in enumerate(t.varnas):
        if is_dirgha(v.slp1) and v.slp1 in _D2H:
            return j
    return None


def _site_dirgha(state: State) -> bool:
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("7_4_59_hrasva_done"):
        return False
    return _first_dirgha_ak_index(t) is not None


def _site_p034(state: State) -> bool:
    """Abhyāsa is exactly ``j`` (single varṇa) — structural; j-abhyāsa only in jakzatuḥ."""
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P034_7_4_59_hrasva_done"):
        return False
    return len(t.varnas) == 1 and t.varnas[0].slp1 == "j"


def _site_p036(state: State) -> bool:
    """Abhyāsa is exactly ``ne`` — structural; ne-abhyāsa only in nināya."""
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P036_7_4_59_ne_to_ni_done"):
        return False
    return len(t.varnas) == 2 and t.varnas[0].slp1 == "n" and t.varnas[1].slp1 == "e"


def _site_p037(state: State) -> bool:
    """Abhyāsa is exactly ``Aw`` — structural; Aw-abhyāsa only in āṭ context."""
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P037_7_4_59_hrasva_done"):
        return False
    return len(t.varnas) == 2 and t.varnas[0].slp1 == "A" and t.varnas[1].slp1 == "w"


def _site(state: State) -> bool:
    return _site_dirgha(state) or _site_p034(state) or _site_p036(state) or _site_p037(state)


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if _site_p034(state):
        i = _abhyasa_index(state)
        assert i is not None
        t = state.terms[i]
        t.varnas.append(mk("a"))
        t.meta["P034_7_4_59_hrasva_done"] = True
        return state
    if _site_p037(state):
        i = _abhyasa_index(state)
        assert i is not None
        t = state.terms[i]
        t.varnas[0] = mk("a")
        t.meta["P037_7_4_59_hrasva_done"] = True
        return state
    if _site_p036(state):
        i = _abhyasa_index(state)
        assert i is not None
        t = state.terms[i]
        t.varnas[1] = mk("i")
        t.meta["P036_7_4_59_ne_to_ni_done"] = True
        return state
    if not _site_dirgha(state):
        return state
    i = _abhyasa_index(state)
    assert i is not None
    t = state.terms[i]
    j = _first_dirgha_ak_index(t)
    if j is None:
        return state
    t.varnas[j] = mk(_D2H[t.varnas[j].slp1])
    t.meta["7_4_59_hrasva_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.59",
    sutra_type=SutraType.VIDHI,
    text_slp1="hrasvaH",
    text_dev="ह्रस्वः",
    padaccheda_dev="ह्रस्वः",
    why_dev="अभ्यासे दीर्घस्य ह्रस्वः (P०२९/P०३०/P०३५/P०३६) अथवा प०३४ अभ्यास-पदार्थम् तथा प०३७।",
    anuvritti_from=("7.4.58",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
