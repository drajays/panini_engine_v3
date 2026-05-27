"""
3.1.13  लोहितादिडाज्भ्यः क्यष्  —  VIDHI (narrow: *kyṣ* after *lohitādi*)

Teaching **corrected_prakriyas_v2**:

  • **P016** (*lohitāyati*): lone **``lohita``** *prātipadika*.
  • **P017** (*paṭapaṭāyati*): **``pawapawA``** (डाच्-पश्चात् पद) *prātipadika* —
    ``state.meta['corrected_v2_P017_3_1_13_arm']``.

Engine:
  • ``state.meta['corrected_v2_P016_3_1_13_arm']`` or **P017** arm (both cleared).
  • expects lone stem *prātipadika* (no separate *kyaz* ``Term`` yet).
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
    state.meta.pop("corrected_v2_P016_3_1_13_arm", None)
    state.meta.pop("corrected_v2_P017_3_1_13_arm", None)
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
