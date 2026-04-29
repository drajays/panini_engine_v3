"""
3.2.115  परोक्षे लिट्  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  Introduce lakāra liṭ when the recipe marks parokṣa-bhūta context.

Engine:
  - recipe arms via ``state.meta['3_2_115_paroksha_lit_arm']``.
  - sets ``state.meta['lakara_liT'] = True`` and appends a placeholder pratyaya
    Term with ``upadesha_slp1 = 'liT'``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    return bool(state.meta.get("3_2_115_paroksha_lit_arm")) and not state.meta.get("lakara_liT")


def act(state: State) -> State:
    if not cond(state):
        return state
    state.meta["lakara_liT"] = True
    state.meta["3_2_115_paroksha_lit_arm"] = False
    lit = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("liT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "liT"},
    )
    # drop it-marker T (as in laT placeholder handling)
    if lit.varnas and lit.varnas[-1].slp1 == "T":
        del lit.varnas[-1]
    state.terms.append(lit)
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.115",
    sutra_type=SutraType.VIDHI,
    text_slp1="parokze liT",
    text_dev="परोक्षे लिट्",
    padaccheda_dev="परोक्षे / लिट्",
    why_dev="परोक्ष-भूते लिट्-लकार-प्रत्ययः विधीयते (विभिदतुः)।",
    anuvritti_from=("3.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

