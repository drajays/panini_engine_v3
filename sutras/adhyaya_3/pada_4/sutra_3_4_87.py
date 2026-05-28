"""
3.4.87  सेर्ह्यपिच्च  —  VIDHI (*loṭ* *sip* → *hi*)

In *loṭ*, *madhyamaika* *sip* (2sg parasmaipada) is replaced by *hi* (*apit*).

Structural trigger: the loṭ lakāra-placeholder term (``upadesha_slp1 == "loT"``
and ``"lakAra_pratyaya_placeholder" in tags``) is still on tape, AND a tiṅ term
with ``upadesha_slp1 == "sip"`` is present.  "sip" occurs in eight lakāras
(laT/liT/luT/lRT/laṅ/luṅ/lṛṅ/leT) — the loṭ placeholder is the disambiguator;
no arm key needed.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sip":
            continue
        # 3.4.78 records source_lakara_upadesha on tin-adesha terms; "loT" is loṭ.
        if t.meta.get("source_lakara_upadesha") != "loT":
            continue
        if t.meta.get("P031_3_4_87_hi_done"):
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
    t.varnas = list(parse_slp1_upadesha_sequence("hi"))
    t.meta["upadesha_slp1"] = "hi"
    t.tags.add("tin_adesha_3_4_78")
    t.meta["P031_3_4_87_hi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.87",
    sutra_type=SutraType.VIDHI,
    text_slp1="ser hyapic ca",
    text_dev="सेर्ह्यपिच्च",
    padaccheda_dev="सेः / हि / अपि / च",
    why_dev="लोटि सिप्-स्थाने हि-आदेशः; लोट्-प्लेसहोल्डर-पद-संज्ञया निर्धारणम् (Art.13)।",
    anuvritti_from=("3.4.86",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
