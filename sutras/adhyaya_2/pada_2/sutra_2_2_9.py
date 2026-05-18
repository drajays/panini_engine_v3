"""
2.2.9  याजकादिभिश्च  —  VIDHI

पदच्छेदः  याजक-आदिभिः / च

अनुवृत्तिः  षष्ठी 2.2.8

Kāśikā summary: the *yājaka* group (*yājaka*, *sthapati*, etc.) also compound
with a genitive (*ṣaṣṭhī*) subanta — this extends the ṣaṣṭhī-tatpuruṣa to
certain agent-nouns.  Examples: *brāhmaṇasya yājakaḥ* → *brāhmaṇayājakaḥ*.

Engine (narrow, mechanically blind):
  Gate key ``2_2_9_yajaka_gate``.  Recipe arms ``state.meta['2_2_9_arm']``
  and tags a Term with ``yajaka_adi`` indicating a *yājaka*-group compound.
  Extends the ṣaṣṭhī gate context (*ca* in the sūtra).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_YAJAKA_ADI = frozenset({"yAjaka", "sTapati", "purohita", "AcArya"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_9_yajaka_gate") is True:
        return False
    if not state.meta.get("2_2_9_arm"):
        return False
    return any(
        "yajaka_adi" in t.tags or t.meta.get("upadesha_slp1") in _YAJAKA_ADI
        for t in state.terms
    )


def act(state: State) -> State:
    if not cond(state):
        return state
    state.paribhasha_gates["2_2_9_yajaka_gate"] = True
    state.samjna_registry["2_2_9_yajaka_adi_samasa"] = True
    state.meta.pop("2_2_9_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.9",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="yAjakAdiBiS ca",
    text_dev="याजकादिभिश्च",
    padaccheda_dev="याजक-आदिभिः / च",
    why_dev=(
        "याजकादयः षष्ठ्यन्तेन च समस्यन्ते — ब्राह्मणयाजकः इत्यादि।"
    ),
    anuvritti_from=("2.2.8",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
