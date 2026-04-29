"""
1.1.39  कृन्मेजन्तः  —  SAMJNA

User note (``कृन्मेजन्तः.md``): a kṛdanta whose kṛt suffix is
  - **m-anta** (ends in ``m``; e.g. kṛ + ṇamul → … + ``am``), or
  - **ec-anta / ej-anta** (ends in ``e/E/o/O``),
is treated as *avyaya* for downstream operations such as **2.4.82** (*sup*-luk).

Engine (glass-box):
  - When an aṅga is immediately followed by a **kṛt** pratyaya Term whose surface
    (current ``varnas`` on tape) ends in ``m`` or an EC vowel, tag the block as
    ``avyaya`` (aṅga + that pratyaya).
  - This is a metadata assignment only; no surface change.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only Term tags + current varṇas.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import iter_anga_to_following_pratyaya_pairs
from engine.state import State

_EC_LAST = frozenset({"e", "E", "o", "O"})

META_1_1_39_DONE: str = "1_1_39_kRnmejanta_avyaya_done"


def _is_krt_pratyaya(pr) -> bool:
    return pr.kind == "pratyaya" and "krt" in pr.tags


def _eligible_pairs(state: State):
    for ai, pi in iter_anga_to_following_pratyaya_pairs(state):
        anga = state.terms[ai]
        pr = state.terms[pi]
        if "anga" not in anga.tags or "prātipadika" not in anga.tags:
            continue
        if not _is_krt_pratyaya(pr):
            continue
        if pr.meta.get(META_1_1_39_DONE):
            continue
        if not pr.varnas:
            continue
        last = pr.varnas[-1].slp1
        if last != "m" and last not in _EC_LAST:
            continue
        yield ai, pi


def cond(state: State) -> bool:
    return next(_eligible_pairs(state), None) is not None


def act(state: State) -> State:
    for ai, pi in _eligible_pairs(state):
        anga = state.terms[ai]
        pr = state.terms[pi]
        anga.tags.add("avyaya")
        pr.tags.add("avyaya")
        pr.meta[META_1_1_39_DONE] = True
    state.samjna_registry["1_1_39_kRnmejanta"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.39",
    sutra_type     = SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1      = "kRnmejantaH",
    text_dev       = "कृन्मेजन्तः",
    padaccheda_dev = "कृन्-मे-जन्तः (अव्ययवत्)",
    why_dev        = "कृदन्ते मकारान्ते वा एचन्ते (मे-जन्ते) अव्यय-संज्ञा; ततो २.४.८२ सुप्-लुक्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]

