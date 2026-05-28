"""
3.1.42  अभ्युत्सादयांप्रजनयांचिकयांरमयामकः  —  VIDHI

Padaccheda: अभ्युत्सादयाम् प्रजनयाम् चिकयाम् रमयाम् अकः (तिङ्) पावयांक्रियात् (तिङ्) विदामक्रन् (तिङ्) इति छन्दसि

Krt suffix rule from dhatu: अभ्युत्सादयांप्रजनयांचिकयांरमयामकः (42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_42_aByutsAdayAM_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_42_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aByutsAdayAMprajanayAMcikayAMramayAmakaH",
    text_dev              = "अभ्युत्सादयांप्रजनयांचिकयांरमयामकः",
    padaccheda_dev        = "अभ्युत्सादयाम् प्रजनयाम् चिकयाम् रमयाम् अकः (तिङ्) पावयांक्रियात् (तिङ्) विदामक्रन् (तिङ्) इति छन्दसि",
    why_dev               = "धातोः [अभ्युत्सादयांप्रजनयांचिकयांरमयामकः]-प्रत्ययः विहितः (३.१.42)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
