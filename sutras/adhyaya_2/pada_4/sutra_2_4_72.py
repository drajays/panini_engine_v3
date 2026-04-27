"""
2.4.72  अदिप्रभृतिभ्यः शपः  —  VIDHI (narrow: luk of Sap for adādi)

Glass-box scope for `mArzwi`:
  When a recipe arms adādi-luk and a `Sap` vikaraṇa term is present, delete it.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _sap_indexes(state: State) -> list[int]:
    return [
        i
        for i, t in enumerate(state.terms)
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "Sap"
    ]


def cond(state: State) -> bool:
    return bool(state.meta.get("2_4_72_sap_luk_arm")) and bool(_sap_indexes(state))


def act(state: State) -> State:
    idxs = _sap_indexes(state)
    for i in reversed(idxs):
        del state.terms[i]
    state.meta["2_4_72_sap_luk_arm"] = False
    state.meta["2_4_72_sap_luk"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.72",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "adiprabhftibhyaH SapaH",
    text_dev       = "अदिप्रभृतिभ्यः शपः",
    padaccheda_dev = "अदिप्रभृतिभ्यः / शपः",
    why_dev        = "अदादिगणीय-धातोः परे शप्-विकरणस्य लुक् (ग्लास-बॉक्स् आर्म्ड)।",
    anuvritti_from = ("2.4.58",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

