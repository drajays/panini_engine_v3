"""
6.1.185  तित्स्वरितम्  —  ANUVADA (narrow ``prakriya_34``)

**Pāṭha (cross-check: ``sutrANi.tsv``):** *tit-svaritam* — an affix bearing the indicatory
letter **त्** (*tit*) causes *svarita* accent on the relevant *pada* (*Ṛk-prātiśākhya* tier).

Narrow v3 (**अध्यापक क्व**):
  • ``kv`` with ``prakriya_34_kv_interrogative_demo`` after vocative ``aDyApaka``;
    ``prakriya_34_6_1_185_arm`` stamps ``meta['prakriya_34_kv_svarita_note']`` on ``terms[1]``.

No *svara* columns on ``Varna`` rows (accent is *śruti*-metadata only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_34_6_1_185_arm"):
        return False
    if len(state.terms) < 2:
        return False
    t1 = state.terms[1]
    if "prakriya_34_kv_interrogative_demo" not in t1.tags:
        return False
    if t1.meta.get("upadesha_slp1") != "kv":
        return False
    if t1.meta.get("prakriya_34_kv_svarita_note"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.terms[1].meta["prakriya_34_kv_svarita_note"] = True
    state.meta.pop("prakriya_34_6_1_185_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.185",
    sutra_type=SutraType.ANUVADA,
    text_slp1="titsvaritam",
    text_dev="तित्स्वरितम्",
    padaccheda_dev="तित्-स्वरितम्",
    why_dev="ति-प्रत्ययान्तस्य स्वरित-अनुवादः (*prakriya_34*, ``क्व``)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
