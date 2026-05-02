"""
4.4.135  (narrow) दधि-आदि-प्रसङ्गे ठक्  —  VIDHI (P018)

The JSON ``split_prakriyas_11/P018.json`` uses sūtra id **4.4.135** to attach
the taddhita pratyaya **ठक्** (*Tak*) in the sense “prepared with / by means of”.

This repository currently implements only a narrow, recipe-armed attachment:
  - recipe sets ``state.meta['prakriya_P018_4_4_135_Tak_arm'] = True``
  - state must contain an ``anga``+``prātipadika`` witness tagged
    ``prakriya_P018_dADikam_demo``.

We model *Tak* as a taddhita ``Term`` with:
  - ``meta['upadesha_slp1'] = 'Tak'``
  - ``meta['it_markers']`` includes `'N'` so **7.2.117** (ñ/ṇit) can trigger.

No semantic selection beyond the explicit arming.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("prakriya_P018_4_4_135_Tak_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "prakriya_P018_dADikam_demo" not in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    idx = _site(state)
    if idx is None:
        return False
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "Tak" for t in state.terms)


def act(state: State) -> State:
    idx = _site(state)
    if idx is None:
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Tak")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "Tak", "it_markers": {"N"}},
    )
    state.terms.insert(idx + 1, pr)
    state.meta["prakriya_P018_4_4_135_Tak_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.4.135",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tena saMskftam (Tak) (narrow)",
    text_dev       = "तेन संस्कृतम् (ठक्) — संक्षेपः",
    padaccheda_dev = "तेन / संस्कृतम्",
    why_dev        = "दध्ना संस्कृतम् इत्याद्यर्थे ठक्-प्रत्ययः (P018 narrow demo).",
    anuvritti_from = ("4.1.76",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

