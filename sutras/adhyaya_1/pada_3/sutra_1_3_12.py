"""
1.3.12  अनुदात्तङित आत्मनेपदम्  —  PARIBHASHA (narrow demo)

Demo slice (वन्दे .md):
  For the dhātu `vad` in this note, force ātmanepada and select the 1sg ending
  `i` (iT placeholder collapsed to `i`).

Engine:
  - recipe-armed by ``state.meta['1_3_12_arm']``.
  - records `state.meta['pada']='Atmanepada'` and `state.meta['tin_adesha_slp1']='i'`.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("1_3_12_arm"):
        return False
    if state.meta.get("pada") == "Atmanepada":
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    up = (state.terms[0].meta.get("upadesha_slp1") or "").strip()
    target = (state.meta.get("1_3_12_target_upadesha_slp1") or "").strip()
    if target:
        return up == target
    return up == "vad"


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    # Keep vande-demo behaviour when not overridden.
    if not (state.meta.get("1_3_12_target_upadesha_slp1") or "").strip():
        # 1sg ātmanepada in our tin inventory is `iw`; its hal (`w`) will be removed
        # by 1.3.3 + 1.3.9, leaving `i`, then 3.4.79 (demo) yields `e`.
        state.meta["tin_adesha_for_vande"] = "iw"
    state.paribhasha_gates["1.3.12_anudatta_nit_atmanepada"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.12",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="anudAtta-Nit Atmanepadam (demo)",
    text_dev="अनुदात्तङित आत्मनेपदम्",
    padaccheda_dev="अनुदात्त-ङित् / आत्मनेपदम्",
    why_dev="अनुदात्तङित्-धातोः आत्मनेपदः (डेमो: वन्दे)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

