"""
3.2.78  सुप्यजातौ णिनिस्ताच्छिल्ये  —  VIDHI

Padaccheda: सुपि अ-जातौ णिनिः ताच्छील्ये

krt-suffix rule: सुप्यजातौ णिनिस्ताच्छिल्ये (78)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_78_supyajAtO_78"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.78"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "supyajAtO RinistAcCilye",
    text_dev              = "सुप्यजातौ णिनिस्ताच्छिल्ये",
    padaccheda_dev        = "सुपि अ-जातौ णिनिः ताच्छील्ये",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुप्यजातौ णिनिस्ताच्छिल्ये] विहितः (३.२.78)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
