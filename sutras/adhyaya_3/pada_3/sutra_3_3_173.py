"""
3.3.173  आशिषि लिङ्लोटौ  —  VIDHI (narrow demo)

Demo slice (भित्सीष्ट / BitzIzwa):
  In the sense of benediction (*āśīḥ*), introduce **liṅ** (here, upadeśa SLP1
  ``liG``) as the lakāra placeholder.

Engine:
  - recipe arms via ``state.meta['3_3_173_ashishi_ling_arm']``.
  - appends a lakāra *pratyaya* Term with ``upadesha_slp1='liG'``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("3_3_173_ashishi_ling_arm"):
        return False
    # Avoid duplicates if a lakāra placeholder is already present.
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "liG" for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    liG = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("liG"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "liG"},
    )
    state.terms.append(liG)
    state.meta["ashir_liG"] = True
    state.meta["3_3_173_ashishi_ling_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.173",
    sutra_type=SutraType.VIDHI,
    text_slp1="ASizi liG-loTow",
    text_dev="आशिषि लिङ्लोटौ",
    padaccheda_dev="आशिषि / लिङ्-लोटौ",
    why_dev="आशीः-अर्थे लिङ्-लकारः (डेमो: भित्सीष्ट)।",
    anuvritti_from=("3.3.157",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

