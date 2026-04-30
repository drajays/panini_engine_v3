"""
3.1.96  तव्यत्तव्यानीयरः  —  VIDHI (narrow demos)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=30196):** *tavyat-tavyānīyaraḥ* — kṛtya affixes
**tavyat**, **tavya**, **anīyar** (context from **3.1.91** *ṛṇ* … *dhātoḥ*).

**Engine (disjoint recipe arms — never both in one step):**

1. **anīyar** — ``meta['3_1_96_anIyar_arm']`` (existing ``hiqanIya_heq_nic_anIyar_demo``).
2. **tavyat** — ``meta['prakriya_P002_3_1_96_tavyat_arm']`` + witness ``prakriya_P002_Bavitavyam_demo``
   (``split_prakriyas_11`` **P002**, **भवितव्यम्**).

Each arm appends one ``Term`` and clears its arm flag; **R1**-visible phonetic change on the tape.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches_aniyar(state: State) -> bool:
    if not state.meta.get("3_1_96_anIyar_arm"):
        return False
    if not state.terms:
        return False
    if state.meta.get("3_1_96_anIyar_done"):
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "anIyar" for t in state.terms):
        return False
    return True


def _matches_tavyat(state: State) -> bool:
    if not state.meta.get("prakriya_P002_3_1_96_tavyat_arm"):
        return False
    if not state.terms:
        return False
    if state.meta.get("prakriya_P002_3_1_96_tavyat_done"):
        return False
    if not any("prakriya_P002_Bavitavyam_demo" in t.tags for t in state.terms):
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
        state.meta["3_1_96_anIyar_arm"] = False
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
        state.meta["prakriya_P002_3_1_96_tavyat_arm"] = False
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.96",
    sutra_type=SutraType.VIDHI,
    text_slp1="tavyat-tavyA-nIyar",
    text_dev="तव्यत्तव्यानीयरः",
    padaccheda_dev="तव्यत्-तव्य-अनीयर्",
    why_dev="कृत्य-प्रत्ययाः — **अनीयर्** (recipe ``3_1_96_anIyar_arm``), **तव्यत्** (**P002** ``prakriya_P002_*``)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
