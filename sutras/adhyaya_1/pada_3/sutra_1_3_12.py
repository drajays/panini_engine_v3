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
    if state.meta.get("pada") == "Atmanepada":
        return False
    if not any("dhatu" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
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

