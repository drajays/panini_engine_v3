"""
4.1.105  गर्गादिभ्यो यञ्  —  VIDHI (narrow: **P042** *gārgya*)

*Śāstra (laghu):* from a *gargādi* stem *garga-*, the *taddhita* **yañ** (*yaY*
*upadeśa*) marks *apatya* in the *gotra* line.

Engine (recipe-armed only):
  - **P042:** ``state.meta['P042_4_1_105_yaY_arm']`` + ``garga`` stem (+ demo tag).
  - **corrected-v2 P004-A:** ``state.meta['corrected_v2_P004_A_stage2_yaY_arm']``
    + merged stem ``upadesha_slp1 == 'kauYjAyana'`` (*Kauñjāyana*).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 41105 · गर्गादिभ्यो यञ्
              padaccheda: गर्ग-आदिभ्यः यञ्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 41092: तस्यापत्यम् | 41098: गोत्रे
  Source #2 — Kāśikā 4.1.105 udāharaṇa:
                गर्गादिभ्यो गोत्रापत्ये यञ् प्रत्ययो भवति
                गार्ग्यः
                वात्स्यः
  Cross-check — surface pinned by: tests/unit/test_gArgyAH_garga_yaY_luk.py
  Reference record: sutra_ref_out/4_1_105.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_META_P004_A_STAGE2 = "corrected_v2_P004_A_stage2_yaY_arm"
_UPA_KAU_YJ_AYANA = "kauYjAyana"


def _site_p042(state: State) -> int | None:
    if not state.meta.get("P042_4_1_105_yaY_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags:
            continue
        if "P042_garga_demo" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "garga":
            continue
        return i
    return None


def _site_p004_a(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != _UPA_KAU_YJ_AYANA:
            continue
        return i
    return None


def _site(state: State) -> int | None:
    i = _site_p042(state)
    if i is not None:
        return i
    return _site_p004_a(state)


def _has_yaY(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == "yaY" for t in state.terms)


def cond(state: State) -> bool:
    return _site(state) is not None and not _has_yaY(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    yaY = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("yaY")),
        tags={"pratyaya", "upadesha", "taddhita", "krt"},
        meta={"upadesha_slp1": "yaY"},
    )
    state.terms.insert(i + 1, yaY)
    state.meta.pop("P042_4_1_105_yaY_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.105",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "gargAdibhyaH yaY (narrow P042 / P004-A)",
    text_dev       = "गर्गादिभ्यो यञ् — P042 / प००४-अ",
    padaccheda_dev = "गर्गादिभ्यः / यञ्",
    why_dev        = "गर्गादि-गणात् यञ् — P042; कौञ्जायनाद् युवापत्ये प००४-अ।",
    anuvritti_from = ("4.1.76",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
