"""
3.3.174  (कृवादिभ्य उण् — narrow *glass-box* for ``prakriya_24``)

Śāstra anchor: *kṛvāpājimi…* row supplies *uṇ* after *√vā* (गतिगन्धनयोः) in the
*uṇādi* tradition folded into this engine slice (full *uṇādi* inventory is out of
band; this file is the *vidhi* hook only).

Engine:
  When ``state.meta['prakriya_24_uR_arm']`` is True and the tape is exactly one
  ``dhātu`` ``Term`` with ``meta['upadesha_slp1'] == 'vA'``, append ``uR`` (*uṇ*
  *upadeśa*) as a ``kṛt`` *pratyaya* ``Term`` and stamp ``meta['prakriya_24_uR_source']``
  for downstream **7.3.33**.

``cond`` does not read *vibhakti* / gold surface.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_24_uR_arm"):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "vA":
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    uR = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("uR")),
        tags={"pratyaya", "upadesha", "krt"},
        meta={"upadesha_slp1": "uR", "prakriya_24_uR_source": True},
    )
    state.terms.append(uR)
    state.meta.pop("prakriya_24_uR_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.174",
    sutra_type=SutraType.VIDHI,
    text_slp1="kRvAdibhyo uR",
    text_dev="कृवादिभ्य उण्",
    padaccheda_dev="कृवादिभ्यः / उण्",
    why_dev="वा-धातोः उण्-प्रत्ययः (*prakriya_24*, ग्लास-बॉक्स्)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
