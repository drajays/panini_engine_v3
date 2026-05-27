"""
2.4.72  अदिप्रभृतिभ्यः शपः  —  VIDHI (luk of śap for adādi)

*Padaccheda:* *adi-prabhṛtibhyaḥ* (pañcamī) / *śapaḥ* (ṣaṣṭhī).

*Śāstra:* *adādi* (gaṇa 2) *dhātu* + *śap* *vikaraṇa* → *luk* (delete *śap*).

*Engine:* ``cond`` reads *dhātu* ``gana`` meta (gaṇa 2) and a following ``Sap`` *Term*;
no demo ``_arm`` (Art. 13).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _sap_indexes(state: State) -> list[int]:
    return [
        i
        for i, t in enumerate(state.terms)
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "Sap"
    ]


def _adadi_dhatu_present(state: State) -> bool:
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("gana") == 2:
            return True
    return False


def cond(state: State) -> bool:
    if state.meta.get("2_4_72_sap_luk"):
        return False
    if not _adadi_dhatu_present(state):
        return False
    return bool(_sap_indexes(state))


def act(state: State) -> State:
    idxs = _sap_indexes(state)
    for i in reversed(idxs):
        del state.terms[i]
    state.meta["2_4_72_sap_luk"] = True
    state.meta.pop("2_4_72_sap_luk_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.72",
    sutra_type=SutraType.VIDHI,
    text_slp1="adiprabhftibhyaH SapaH",
    text_dev="अदिप्रभृतिभ्यः शपः",
    padaccheda_dev="अदिप्रभृतिभ्यः / शपः",
    why_dev="अदादिगणीय-धातोः परे शप्-विकरणस्य लुक् (P008 आस्ते)।",
    anuvritti_from=("2.4.58",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
