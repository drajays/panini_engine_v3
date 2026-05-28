"""
3.1.129  पाय्यसान्नाय्यनिकाय्यधाय्या मानहविर्निवाससामिधेनीषु  —  VIDHI

Padaccheda: पाय्य-सान्नाय्य-निकाय्य-धाय्याः मान-हविः-निवास-सामिधेनीषु

Krt suffix rule from dhatu: पाय्यसान्नाय्यनिकाय्यधाय्या मानहविर्निवाससामिधेनीषु (129)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_129_pAyyasAnnAyy_129"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_129_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.129"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAyyasAnnAyyanikAyyaDAyyA mAnahavirnivAsasAmiDenIzu",
    text_dev              = "पाय्यसान्नाय्यनिकाय्यधाय्या मानहविर्निवाससामिधेनीषु",
    padaccheda_dev        = "पाय्य-सान्नाय्य-निकाय्य-धाय्याः मान-हविः-निवास-सामिधेनीषु",
    why_dev               = "धातोः [पाय्यसान्नाय्यनिकाय्यधाय्या मानहविर्निवाससामिधेनीषु]-प्रत्ययः विहितः (३.१.129)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
