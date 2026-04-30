"""
6.3.25  (narrow) मातापितरौ — special dvandva base (glass-box)

The classical dvandva **mātā-pitarau** has special behavior in traditional
commentary; the JSON ``split_prakriyas_11/P013.json`` explicitly flags this as a
“listed/nipātana-like” outcome and does not provide the full micro-spine.

Engine (narrow v3):
  When the recipe arms ``state.meta['prakriya_P013_6_3_25_arm']`` and the state
  contains the two samāsa members ``mAtf`` and ``pitf`` (in that order), rewrite
  them to a single prātipadika base ``mAtApitar``.

This is kept as a single VIDHI step (not NIPATANA) so downstream sup attachment
is not frozen.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_P013_6_3_25_arm"):
        return False
    if len(state.terms) < 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if t0.kind != "prakriti" or t1.kind != "prakriti":
        return False
    if "samasa_member" not in t0.tags or "samasa_member" not in t1.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != "mAtf":
        return False
    if (t1.meta.get("upadesha_slp1") or "").strip() != "pitf":
        return False
    if state.samjna_registry.get("6.3.25_mAtApitar_base_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("mAtApitar")),
        tags={"anga", "prātipadika", "prakriya_P013_mAtApitarO_demo"},
        meta={"upadesha_slp1": "mAtApitar"},
    )
    # Drop both members and replace with the composite base.
    state.terms = [t] + state.terms[2:]
    state.samjna_registry["6.3.25_mAtApitar_base_done"] = True
    state.meta.pop("prakriya_P013_6_3_25_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.3.25",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "mAtA pitarO (narrow)",
    text_dev       = "मातापितरौ (नैपातिक-न्यायः; संक्षेपः)",
    padaccheda_dev = "माता / पितरौ",
    why_dev        = "विशिष्ट-द्वन्द्वे 'मातापितर-' आधारः (P013 narrow glass-box).",
    anuvritti_from = ("6.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

