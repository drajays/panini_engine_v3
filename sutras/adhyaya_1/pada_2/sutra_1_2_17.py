"""
1.2.17  (narrow demo: *stAdgor ic ca* spine for **gha** + luṅ **sic** → **इच्**)

After **gha** (**1.1.20**) in luṅ, **sic** (**सिच्**, modelled as ``s`` after **3.1.44** ITs) is
substituted by **इच्** — phonemic ``i`` + hal **c** (it). Re-tag **``upadesha``** so
**1.3.3**/**1.3.9** can drop ``c``, and mark **kṅiti** via ``kngiti`` for **6.4.64**.

Demo path for *da~da* + luṅ: ``sic`` Term still has ``upadesha_slp1='sic'`` for lookup;
recipe arms ``meta['1_2_17_ghu_sici_ic_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_20 import GHU_DHATU_UPADESHA_SLP1, ghu_samjna_is_registered


def _primary_dhatu_upadesha(state: State) -> str:
    for t in state.terms:
        if "dhatu" in t.tags:
            return (t.meta.get("upadesha_slp1") or "").strip()
    return ""


def _find_sic_term(state: State):
    if not state.meta.get("1_2_17_ghu_sici_ic_arm"):
        return None
    if not ghu_samjna_is_registered(state):
        return None
    up0 = _primary_dhatu_upadesha(state)
    if up0 not in GHU_DHATU_UPADESHA_SLP1:
        return None
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        if t.meta.get("1_2_17_ic_adesha_done"):
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _find_sic_term(state) is not None


def act(state: State) -> State:
    t = _find_sic_term(state)
    if t is None:
        return state
    t.varnas = parse_slp1_upadesha_sequence("ic")
    t.meta["upadesha_slp1"] = "ic"
    t.tags.add("upadesha")
    t.tags.add("kngiti")
    t.meta["1_2_17_ic_adesha_done"] = True
    state.meta["1_2_17_ghu_sici_ic_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.17",
    sutra_type=SutraType.VIDHI,
    text_slp1="stAdgoH ric ca",
    text_dev="स्थाद्वो रिच्च",
    padaccheda_dev="स्थाद्वोः / रिच्च",
    why_dev="गु-स्थानिके सिचोऽपेक्षया इच्संनिधानं (लुङ्-डेमो: सिच् आदेशश्च)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
