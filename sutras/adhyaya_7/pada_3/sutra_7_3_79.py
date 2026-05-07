"""
7.3.79  ज्ञाजनोर्जा  —  VIDHI (narrow)

*Śāstra (laghu):* **ज्ञा** / **जनि** roots show **जा** before a following *śit*
(here: **श्ना** vikaraṇa).

Engine: ``corrected_v2_P012_7_3_79_arm`` — dhātu tape **``jYA``** immediately
before **``SnA``** → **``jA``** (corrected-v2 **P012** *apajānīte*).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_META_ARM = "corrected_v2_P012_7_3_79_arm"


def _hit(state: State) -> int | None:
    if not state.meta.get(_META_ARM):
        return None
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags:
            continue
        if "".join(v.slp1 for v in dh.varnas) != "jYA":
            continue
        nxt = state.terms[i + 1]
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up == "SnA" or "SnA_vikaraṇa" in nxt.tags:
            return i
    return None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    i = _hit(state)
    if i is None:
        return state
    state.terms[i].varnas = list(parse_slp1_upadesha_sequence("jA"))
    state.samjna_registry["7.3.79_P012_jYA_to_jA"] = True
    state.meta.pop(_META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="jYAjanoH jA",
    text_dev="ज्ञाजनोर्जा",
    padaccheda_dev="ज्ञा-जनोः / जा",
    why_dev="शिति परे ज्ञा-कार्यम् → जा (प०१२ संक्षिप्तम्)।",
    anuvritti_from=("7.3.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
