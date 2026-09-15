"""
3.1.13  लोहितादिडाज्भ्यः क्यष्  —  VIDHI (narrow: *kyṣ* after *lohitādi*)

Teaching **corrected_prakriyas_v2**:

  • **P016** (*lohitāyati*): lone **``lohita``** *prātipadika*.
  • **P017** (*paṭapaṭāyati*): **``pawapawA``** (डाच्-पश्चात् पद) *prātipadika* —
    ``state.meta['corrected_v2_P017_3_1_13_arm']``.

Engine:
  • ``state.meta['corrected_v2_P016_3_1_13_arm']`` or **P017** arm (both cleared).
  • expects lone stem *prātipadika* (no separate *kyaz* ``Term`` yet).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31013 · लोहितादिडाज्भ्यः क्यष्।
              padaccheda: लोहित-आदि-डाज्भ्यः क्यष्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31007: वा | 31012: भुवि अच्वेः
  Source #2 — Kāśikā 3.1.13 udāharaṇa:
                लोहितायति
                लोहितायते
                डाजन्तेभ्यः — पटपटायति
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_pacaka.py, tests/unit/test_cayanam_ciY_lyuw.py, tests/unit/test_devam_krt.py
  Reference record: sutra_ref_out/3_1_13.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> bool:
    if len(state.terms) != 1:
        return False
    t = state.terms[0]
    if "prātipadika" not in t.tags or "dhatu" in t.tags:
        return False
    stem = "".join(v.slp1 for v in t.varnas)
    return stem in {"pawapawA", "lohita"}


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    ky = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("kyaz")),
        tags={"pratyaya", "upadesha", "sanadi"},
        meta={"upadesha_slp1": "kyaz"},
    )
    state.terms.append(ky)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.13",
    sutra_type=SutraType.VIDHI,
    text_slp1="lohitAdiDAjByaH kyaz",
    text_dev="लोहितादिडाज्भ्यः क्यष्",
    padaccheda_dev="लोहितादि-डाज्भ्यः / क्यष्",
    why_dev="लोहितादि-प्रातिपदिकात् क्यष्-प्रत्ययः (P016)।",
    anuvritti_from=("3.1.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
