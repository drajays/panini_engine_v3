"""
Support for **1.1.63** *na lumatā … pratyayalope … aṅgasya pratyayalakṣaṇam* —
not a sūtra file.

Sets ``state.paribhasha_gates[NA_LUMATANGASYA_GATE]`` when **1.1.63** fires
(after **1.1.62** is already active).  *Vidhi* rules that must block
*lukta*/*śluta*/*lupta*-*pratyaya*-driven *aṅga-kārya* may consult
``na_lumatangasya_paribhasha_is_active``.
"""
from __future__ import annotations

from typing import Final

from engine.state import State

NA_LUMATANGASYA_GATE: Final[str] = "1.1.63_na_lumatangasya"


def na_lumatangasya_paribhasha_is_active(state: State) -> bool:
    return bool(state.paribhasha_gates.get(NA_LUMATANGASYA_GATE))
