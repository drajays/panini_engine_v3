"""
1.1.49  षष्ठी स्थानेयोगा  —  PARIBHASHA

Operational role (v3):
  - Registers the fundamental substitution-locus paribhāṣā gate.
  - Whenever Pāṇini uses the 6th vibhakti (ṣaṣṭhī) in a sūtra text,
    it means "in place of" (sthāne = substitution locus), i.e. the
    item in the genitive is replaced by what the sūtra prescribes.
  - This interpretive gate underpins all ādeśa (substitution) rules.

Blindness:
  - cond() reads only state.paribhasha_gates — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_49_zasTI_sTAneyogA"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id            = "1.1.49",
    sutra_type          = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1           = "zasTI sTAneyogA",
    text_dev            = "षष्ठी स्थानेयोगा",
    padaccheda_dev      = "षष्ठी / स्थाने-योगा",
    why_dev             = "सूत्रे षष्ठी-विभक्तिः \"स्थाने\" (आदेश-लक्ष्य) अर्थे — यस्य स्थाने आदेशः तस्य ग्रहणम्।",
    anuvritti_from      = (),
    cond                = cond,
    act                 = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
