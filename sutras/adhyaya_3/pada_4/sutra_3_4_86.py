"""
3.4.86  एरुः  —  VIDHI (narrow: loṭ tiṅ i → u)

In loṭ context (arm ``3_4_86_loT_arm``): replaces the final 'i' (ikaraḥ = "eḥ")
of a tiṅ ādeśa with 'u' ("uḥ"):
  • tip → ti → tu  (3sg: bhavatu)
  • jhi → anti (via 7.1.3) → antu  (3pl: bhavantu)

Guards: skip if upadesha_slp1 is "hi" (from 3.4.87 sip→hi) or "ni" (from 3.4.89
mi→ni) — those substitutions are apavāda and their 'i' must not become 'u'.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_SKIP_UPADESHA = frozenset({"hi", "ni"})


def _find(state: State) -> int | None:
    if not state.meta.get("3_4_86_loT_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_86_done"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _SKIP_UPADESHA:
            continue
        if not t.varnas or t.varnas[-1].slp1 != "i":
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
    t.varnas[-1] = mk("u")
    t.meta["3_4_86_done"] = True
    state.samjna_registry["3.4.86_e_u"] = (
        state.samjna_registry.get("3.4.86_e_u", 0) + 1
    )
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.86",
    sutra_type=SutraType.VIDHI,
    text_slp1="eruH",
    text_dev="एरुः",
    padaccheda_dev="एः / उः",
    why_dev=(
        "लोटि तिङ्-अन्त्य-इकारस्य उकार-आदेशः: "
        "ति→तु (भवतु), अन्ति→अन्तु (भवन्तु)।"
    ),
    anuvritti_from=("3.4.85",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
