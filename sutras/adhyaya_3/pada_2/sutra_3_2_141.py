"""
3.2.141  शमित्यष्टाभ्यो घिनुण्  —  VIDHI

Padaccheda: शम्-इति (लुप्तपञ्चम्यन्तनिर्देशः) अष्टाभ्यः घिनुँण्

krt-suffix rule: शमित्यष्टाभ्यो घिनुण् (141)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_141_SamityazwA_141"


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
    state.meta["krt_kind"] = "3.2.141"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SamityazwAByo GinuR",
    text_dev              = "शमित्यष्टाभ्यो घिनुण्",
    padaccheda_dev        = "शम्-इति (लुप्तपञ्चम्यन्तनिर्देशः) अष्टाभ्यः घिनुँण्",
    why_dev               = "धातोः कृत्-प्रत्ययः [शमित्यष्टाभ्यो घिनुण्] विहितः (३.२.141)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
