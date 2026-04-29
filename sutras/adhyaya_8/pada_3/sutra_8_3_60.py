"""
8.3.60  शासिवसिघसीनां च  —  VIDHI (narrow demo)

Demo slice (उषित्वा / uzitvA):
  For dhātu `vas`, after samprasāraṇa has produced initial `u`, change `s` → `z`
  (ṣatva) before the following `tvA` block.

Engine:
  - recipe arms via ``state.meta['8_3_60_shasi_vasi_ghasi_arm']``.
  - narrow: applies only when the primary dhātu upadeśa is `vas` and the dhātu
    term currently contains `s` as its final varṇa.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def cond(state: State) -> bool:
    if not state.meta.get("8_3_60_shasi_vasi_ghasi_arm"):
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "vas":
        return False
    if dh.meta.get("8_3_60_satva_done"):
        return False
    if not dh.varnas:
        return False
    return dh.varnas[-1].slp1 == "s"


def act(state: State) -> State:
    if not cond(state):
        return state
    dh = state.terms[0]
    dh.varnas[-1] = mk("z")
    dh.meta["8_3_60_satva_done"] = True
    state.meta["8_3_60_shasi_vasi_ghasi_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.60",
    sutra_type=SutraType.VIDHI,
    text_slp1="SAsi-vasi-Gasi-nAm ca (narrow)",
    text_dev="शासिवसिघसीनां च",
    padaccheda_dev="शासि-वसि-घसि-नाम् / च",
    why_dev="वसादौ (सम्प्रसारणोत्तरं) सस्य षत्वं (उषित्वा)।",
    anuvritti_from=("8.3.57",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

