"""
2.4.45  इणो गा लुङि  —  VIDHI (narrow demo)

Demo slice (अध्यगीष्ट):
  When dhātu upadeśa is ``iN`` and lakāra is luṅ, replace the dhātu with the
  substitute ``gA`` (treated as ``gAN`` in the note’s prakriyā for 1.2.1).

Engine representation:
  - pipelines must arm via ``state.meta['2_4_45_iNo_ga_luG_arm']``.
  - we rewrite term[0] varṇas to SLP1 ``gAN`` (ga + A + N) and set
    meta['upadesha_slp1'] = 'gAN' so **1.2.1** can see it.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("2_4_45_iNo_ga_luG_arm"):
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "iN":
        return False
    if state.meta.get("lakara") != "luG":
        return False
    if dh.meta.get("2_4_45_iNo_ga_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh = state.terms[0]
    dh.varnas = list(parse_slp1_upadesha_sequence("gAN"))
    dh.meta["upadesha_slp1"] = "gAN"
    dh.meta["2_4_45_iNo_ga_done"] = True
    state.meta["2_4_45_iNo_ga_luG_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.45",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="iNo gA luGi",
    text_dev="इणो गा लुङि",
    padaccheda_dev="इणः / गा / लुङि",
    why_dev="लुङ्-लकारे इण्-धातोः स्थाने गा-आदेशः (अध्यगीष्ट-प्रक्रिया)।",
    anuvritti_from=("2.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

