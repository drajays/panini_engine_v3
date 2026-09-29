"""
7.3.33  आतो युक् चिण्कृतोः  —  VIDHI (narrow *glass-box* for ``prakriya_24``)

Śāstra: after a stem-final long **ā**, the augment **yuk** appears before a *kṛt*
affix bearing indicatory **ṇ** or **ñ** (here *uṇ* → **ṇ-it**).

Engine (*vā* + *uṇ* residue):
  After *it*-lopa leaves ``[vA, u]`` with the second ``Term`` still marked
  ``meta['prakriya_24_uR_source']``, and ``state.meta['prakriya_24_7_3_33_arm']``,
  insert semivowel ``y`` immediately after the stem-final ``A`` on the *dhātu*
  ``Term`` (tape ``vA`` + ``y`` + ``u`` → ``vAyu`` after merge).

``cond`` does not read *vibhakti* / paradigm coordinates.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73033 · आतो युक् चिण्कृतोः
              padaccheda: आतः युक् चिण्-कृतोः
              anuvṛtti:   64001: अङ्गस्य | 72115: ञ्णिति
  Source #2 — Kāśikā 7.3.33 udāharaṇa:
                अदायि
                अधायि
                कृति — दायः
  Cross-check — surface pinned by: tests/unit/test_vAyavaH.py
  Reference record: sutra_ref_out/7_3_33.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _matches(state: State) -> bool:
    if len(state.terms) != 2:
        return False
    anga, pr = state.terms[0], state.terms[1]
    if "dhatu" not in anga.tags:
        return False
    if not anga.varnas or anga.varnas[-1].slp1 != "A":
        return False
    if "pratyaya" not in pr.tags:
        return False
    if not pr.meta.get("prakriya_24_uR_source"):
        return False
    if not pr.varnas or pr.varnas[0].slp1 != "u":
        return False
    if anga.meta.get("7_3_33_yuk_inserted"):
        return False
    return True


def _cin_krt_after_A(state: State) -> int | None:
    """आतो युक् चिण्कृतोः: an ā-final aṅga before ciṇ or a ñit/ṇit kṛt (अग्लायि, दायक)."""
    for i, t in enumerate(state.terms[:-1]):
        nxt = state.terms[i + 1]
        itm = nxt.meta.get("it_markers") or set()
        if ("dhatu" in t.tags and t.varnas and t.varnas[-1].slp1 == "A"
                and not t.meta.get("7_3_33_yuk_inserted")
                and ("Y" in itm or "R" in itm) and ("c" in itm or "krt" in nxt.tags)):
            return i
    return None


def cond(state: State) -> bool:
    return _matches(state) or _cin_krt_after_A(state) is not None


def act(state: State) -> State:
    if not _matches(state):
        i = _cin_krt_after_A(state)
        if i is not None:
            state.terms[i].varnas.append(mk("y"))
            state.terms[i].meta["7_3_33_yuk_inserted"] = True
        return state
    anga = state.terms[0]
    anga.varnas.append(mk("y"))
    anga.meta["7_3_33_yuk_inserted"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.33",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ato yuk ciNkRtoH",
    text_dev="आतो युक् चिण्कृतोः",
    padaccheda_dev="आतः / युक् / चिण्-कृतोः",
    why_dev="आकारान्ताद् उणादौ युक्-आगमः (*prakriya_24*, ग्लास-बॉक्स्)।",
    anuvritti_from=("7.3.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
