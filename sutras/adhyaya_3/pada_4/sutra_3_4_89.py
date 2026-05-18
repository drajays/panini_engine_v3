"""
3.4.89  मेर्निः  —  VIDHI (narrow: loṭ mip → ni)

In loṭ context (arm ``3_4_89_loT_arm``): replaces the 1sg tiṅ ādeśa 'mi'
(mip after IT-lopa) with 'ni' ("niḥ"):
  mip → mi (IT-lopa: p drops) → ni  (3.4.89)
  Then 7.3.101 (ato dīrgho yañi) lengthens the preceding śap-a to ā before
  the 'n' of 'ni' (yañ), giving: bhav + ā + ni = bhavāni.

Apavāda to 3.4.101 (which would give mi→am for laṅ) — call 3.4.89 first.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State) -> int | None:
    if not state.meta.get("3_4_89_loT_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_89_done"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up != "mip":
            continue
        cur = "".join(v.slp1 for v in t.varnas)
        if cur != "mi":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas = [mk("n"), mk("i")]
    t.meta["upadesha_slp1"] = "ni"
    t.meta["3_4_89_done"] = True
    t.tags.discard("upadesha")
    state.samjna_registry["3.4.89_me_ni"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.89",
    sutra_type=SutraType.VIDHI,
    text_slp1="merniH",
    text_dev="मेर्निः",
    padaccheda_dev="मेः / निः",
    why_dev=(
        "लोटि उत्तम-एकवचन-तिङ् मि-स्थाने नि-आदेशः; "
        "तदनन्तरं ७.३.१०१ (यञि दीर्घः): अ→आ → भवानि।"
    ),
    anuvritti_from=("3.4.85",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
