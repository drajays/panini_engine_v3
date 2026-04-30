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
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _matches(state: State) -> bool:
    if not state.meta.get("prakriya_24_7_3_33_arm"):
        return False
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


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[0]
    anga.varnas.append(mk("y"))
    anga.meta["7_3_33_yuk_inserted"] = True
    state.meta.pop("prakriya_24_7_3_33_arm", None)
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
