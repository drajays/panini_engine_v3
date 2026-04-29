"""
3.4.107  सुट् तिथोः  —  VIDHI (narrow demo)

Demo slice (भित्सीष्ट / BitzIzwa):
  Insert the augment **suṭ** (surface ``s``) immediately before the *tiṅ*
  ādeśa ``ta`` in āśīr-liṅ.

Engine:
  - recipe arms via ``state.meta['3_4_107_suw_arm']``.
  - inserts a pratyaya Term ``s`` just before the final *tiṅ* term.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_tin_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"}:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("3_4_107_suw_arm"):
        return False
    if not state.meta.get("ashir_liG"):
        return False
    idx = _find_tin_index(state)
    if idx is None:
        return False
    # avoid duplicates: if there is already a suṭ marker just before tin.
    if idx - 1 >= 0 and "".join(v.slp1 for v in state.terms[idx - 1].varnas) == "s":
        return False
    return True


def act(state: State) -> State:
    idx = _find_tin_index(state)
    if idx is None:
        return state
    s = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("s"),
        tags={"pratyaya", "suw_agama"},
        meta={"upadesha_slp1": "s"},
    )
    state.terms.insert(idx, s)
    state.meta["3_4_107_suw_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.107",
    sutra_type=SutraType.VIDHI,
    text_slp1="suw tiToH",
    text_dev="सुट् तिथोः",
    padaccheda_dev="सुट् / तिथोः",
    why_dev="तिङ्-आदेशे (डेमो: त/ताम्) पुरः सुट्-आगमः — भित्सीष्ट।",
    anuvritti_from=("3.4.77",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

