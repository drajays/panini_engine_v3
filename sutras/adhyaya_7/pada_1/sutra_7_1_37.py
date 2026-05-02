"""
7.1.37  समासेऽनञ्पूर्वे क्त्वो ल्यप्  —  VIDHI (narrow: ktvā → lyap)

Engine (glass-box):
  When a ktvā-pratyaya is present and the recipe arms this substitution
  (typically because an upasarga precedes), replace it with ``lyap``.

Representation convention:
  - We model the upadeśa as ``lyap`` (initial l and final p are *it* via
    **1.3.8** / **1.3.3**, lopa by **1.3.9**), leaving surface ``ya``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_ktva(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        orig = (t.meta.get("upadesha_slp1_original") or "").strip()
        if orig == "ktvA":
            return i
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"ktvA", "itvA", "tvA"}:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("7_1_37_lyap_arm"):
        return False
    i = _find_ktva(state)
    if i is None:
        return False
    return not state.terms[i].meta.get("7_1_37_ktvA_to_lyap_done")


def act(state: State) -> State:
    i = _find_ktva(state)
    if i is None:
        return state
    pr = state.terms[i]
    pr.varnas = list(parse_slp1_upadesha_sequence("lyap"))
    pr.tags.add("upadesha")
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "ktvA")
    pr.meta["upadesha_slp1"] = "lyap"
    pr.meta["7_1_37_ktvA_to_lyap_done"] = True
    state.meta["7_1_37_lyap_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.37",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "samAse ananyapUrve ktvo lyap",
    text_dev       = "समासेऽनञ्पूर्वे क्त्वो ल्यप्",
    padaccheda_dev = "समासे / अनञ्-पूर्वे / क्त्वः / ल्यप्",
    why_dev        = "उपसर्गादि-पूर्वे क्त्वा-प्रत्ययस्य ल्यप्-आदेशः (नरूप्य-डेमो)।",
    anuvritti_from = ("7.1.12",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

