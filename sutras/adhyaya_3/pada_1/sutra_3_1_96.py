"""
3.1.96  तव्यत्तव्यानीयरः  —  VIDHI

**Pāṭha (ashtadhyayi-com data.txt i=30196):** tavyat-tavyānīyaraḥ — kṛtya affixes
**tavyat**, **tavya**, **anīyar** in the dhātu context (3.1.91 anuvṛtti).

3.1.96 enumerates three kṛtya options; all three are equally valid for any
dhātu.  Selection is made via the **krtya_recipe** coordination key:

  state.meta["krtya_recipe"] = "anIyar"   →  anīyar attached
  state.meta["krtya_recipe"] = "tavyat"   →  tavyat attached
  state.meta["krtya_recipe"] = "tavya"    →  tavya  attached  (not yet implemented)

This is a recipe coordination key (like ``3_1_68_kartari_recipe``), not an arm
flag: it selects among the grammatically equivalent options; it does not bypass
any linguistic check.

Backward-compat: the old ``3_1_96_anIyar_arm`` key is still accepted so
existing pipelines that have not yet migrated continue to work.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _wants_aniyar(state: State) -> bool:
    if state.meta.get("krtya_recipe") == "anIyar":
        return True
    # backward-compat: legacy arm flag
    return bool(state.meta.get("3_1_96_anIyar_arm"))


def _matches_aniyar(state: State) -> bool:
    if not _wants_aniyar(state):
        return False
    if not state.terms:
        return False
    if state.meta.get("3_1_96_anIyar_done"):
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "anIyar" for t in state.terms):
        return False
    return True


def _matches_tavyat(state: State) -> bool:
    recipe = state.meta.get("krtya_recipe")
    if recipe == "tavyat":
        pass  # new coordination key path
    elif not state.meta.get("prakriya_P002_3_1_96_tavyat_arm"):
        return False
    if not state.terms:
        return False
    if state.meta.get("prakriya_P002_3_1_96_tavyat_done"):
        return False
    # For the legacy arm path, require the P002 demo tag
    if not recipe and not any("prakriya_P002_Bavitavyam_demo" in t.tags for t in state.terms):
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "tavyat" for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches_aniyar(state) or _matches_tavyat(state)


def act(state: State) -> State:
    if _matches_aniyar(state):
        pr = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("anIyar")),
            tags={"pratyaya", "upadesha", "krt", "ardhadhatuka"},
            meta={
                "upadesha_slp1": "anIyar",
                "krit_pratyaya": "anIyar",
                "anit_ardhadhatuka": True,
            },
        )
        state.terms.append(pr)
        state.meta["3_1_96_anIyar_done"] = True
        state.meta.pop("3_1_96_anIyar_arm", None)
        state.meta.pop("krtya_recipe", None)
        return state
    if _matches_tavyat(state):
        pr = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("tavyat")),
            tags={"pratyaya", "upadesha", "krt", "ardhadhatuka"},
            meta={
                "upadesha_slp1": "tavyat",
                "upadesha_slp1_original": "tavyat",
                "krit_pratyaya": "tavyat",
            },
        )
        state.terms.append(pr)
        state.meta["prakriya_P002_3_1_96_tavyat_done"] = True
        state.meta.pop("prakriya_P002_3_1_96_tavyat_arm", None)
        state.meta.pop("krtya_recipe", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.96",
    sutra_type=SutraType.VIDHI,
    text_slp1="tavyat-tavyA-nIyar",
    text_dev="तव्यत्तव्यानीयरः",
    padaccheda_dev="तव्यत्-तव्य-अनीयर्",
    why_dev=(
        "कृत्य-प्रत्ययाः तव्यत्/तव्य/अनीयर् — 'krtya_recipe' संयोजन-कुञ्जिकया चित्यते।"
    ),
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
