"""
3.2.76  क्विप् च  —  VIDHI (narrow *glass-box*)

Śāstra anchor: *kṛt* *kvip* after *upapada* *karman* in *śāstrīya* *prayoga*s such as
*ratnāni dadhāti* → *ratnadhā* (``prakriya_22`` JSON).

Engine (v3):
  When ``state.meta['3_2_76_kvip_arm']`` is True and the tape already bears a
  *dhātu* ``Term`` without a *kvip* ``Term``, append ``kvip`` as a ``krt`` *pratyaya*
  immediately after that *dhātu*.

Mechanical blindness:
  ``cond`` reads tags + ``state.meta`` only (never *vibhakti* / gold surface).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _already_has_kvip(state: State) -> bool:
    return any(t.meta.get("upadesha_slp1") == "kvip" for t in state.terms)


def cond(state: State) -> bool:
    if not state.meta.get("3_2_76_kvip_arm"):
        return False
    if _already_has_kvip(state):
        return False
    return _dhatu_index(state) is not None


def act(state: State) -> State:
    if not cond(state):
        return state
    di = _dhatu_index(state)
    if di is None:
        return state
    kvip = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("kvip")),
        tags={"pratyaya", "upadesha", "krt"},
        meta={"upadesha_slp1": "kvip"},
    )
    state.terms.insert(di + 1, kvip)
    state.meta.pop("3_2_76_kvip_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.76",
    sutra_type=SutraType.VIDHI,
    text_slp1="kvip ca",
    text_dev="क्विप् च",
    padaccheda_dev="क्विप् / च",
    why_dev="उपपद-कर्मणि धातोः क्विप्-प्रत्ययः (प्रक्रिया-२२, ग्लास-बॉक्स्)।",
    anuvritti_from=("3.2.84",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
