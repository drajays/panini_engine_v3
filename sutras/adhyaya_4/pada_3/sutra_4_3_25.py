"""
4.3.25  तत्र भवः  —  VIDHI (narrow: **aṇ** on *viśākhā* stem) — P039

JSON ``split_prakriyas_11/P039.json``: *tatra bhavaḥ* licenses **aṇ** after the
nakṣatra stem *viśākhā-* in the *jāta* sense (“born there / under that
constellation”).

Engine (recipe-armed only):
  - ``state.meta['P039_4_3_25_arm']``
  - witness ``prakriti`` tagged ``anga``, ``prātipadika``, ``P039_viSAKA_demo``.
  - inserts taddhita ``aR`` (``a`` + ``R`` per upadeśa parsing; **1.3** *it* path
    is left to the usual *prakriyā* hooks if the recipe fires **1.3.2**/**1.3.9**).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("P039_4_3_25_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "P039_viSAKA_demo" not in t.tags:
            continue
        return i
    return None


def _has_aR(state: State) -> bool:
    for t in state.terms:
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "aR":
            return True
    return False


def cond(state: State) -> bool:
    return _site(state) is not None and not _has_aR(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("aR")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "aR"},
    )
    state.terms.insert(i + 1, pr)
    state.meta.pop("P039_4_3_25_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.3.25",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tatra BavaH (aR) (narrow P039)",
    text_dev       = "तत्र भवः (अण्) — P039 संक्षेपः",
    padaccheda_dev = "तत्र / भवः",
    why_dev        = "विशाखायां जात इति प्रसङ्गे अण् (४.३.२५) — P039।",
    anuvritti_from = ("4.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
