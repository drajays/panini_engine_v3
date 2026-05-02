"""
4.1.105  गर्गादिभ्यो यञ्  —  VIDHI (narrow: **P042** *gārgya*)

*Śāstra (laghu):* from a *gargādi* stem *garga-*, the *taddhita* **yañ** (*yaY*
*upadeśa*) marks *apatya* in the *gotra* line.

Engine (recipe-armed only):
  - ``state.meta['P042_4_1_105_yaY_arm']``
  - witness ``prakriti`` ``anga`` with ``upadesha_slp1`` ``garga`` and tag ``P042_garga_demo``.
  - inserts ``yaY`` immediately after that stem (``taddhita``, ``krt``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("P042_4_1_105_yaY_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags:
            continue
        if "P042_garga_demo" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "garga":
            continue
        return i
    return None


def _has_yaY(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == "yaY" for t in state.terms)


def cond(state: State) -> bool:
    return _site(state) is not None and not _has_yaY(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    yaY = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("yaY")),
        tags={"pratyaya", "upadesha", "taddhita", "krt"},
        meta={"upadesha_slp1": "yaY"},
    )
    state.terms.insert(i + 1, yaY)
    state.meta.pop("P042_4_1_105_yaY_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.105",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "gargAdibhyaH yaY (narrow P042)",
    text_dev       = "गर्गादिभ्यो यञ् — P042 संक्षेपः",
    padaccheda_dev = "गर्गादिभ्यः / यञ्",
    why_dev        = "गर्गादि-गणात् यञ्-तद्धितः (४.१.१०५) — P042।",
    anuvritti_from = ("4.1.76",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
