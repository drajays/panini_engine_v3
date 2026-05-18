"""
1.3.46  सम्प्रतिभ्यामनाध्याने  —  VIDHI

*Padaccheda:* *sam-pratibhyām* (पञ्चमी-द्विवचन) / *anādhyāne* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada applies] after the prefixes sam and prati when the
sense is NOT one of learning/studying (anādhyāna). When sam or prati precede
a root but the action is not the ādhyāna (study/recitation) sense,
ātmanepada is mandated.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_1_3_46" is absent, and (c) a dhātu Term
carries one of _SAM_PRATI_PREFIXES and also carries the tag "anADyAna_usage"
(indicating the action is in the non-learning sense).
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_SAM_PRATI_PREFIXES: frozenset[str] = frozenset({"sam_prefix", "prati_prefix"})

_REGISTRY_KEY = "1_3_46_sam_prati_anADyAna"
_STAMP_KEY    = "Atmanepada_1_3_46"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and not _SAM_PRATI_PREFIXES.isdisjoint(t.tags)
        and "anADyAna_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.46",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="sampratiByAmanADyAne",
    text_dev="सम्प्रतिभ्यामनाध्याने",
    padaccheda_dev="सम्-प्रतिभ्याम् (पञ्चमी-द्विवचन) / अनाध्याने (सप्तमी-एकवचन)",
    why_dev=(
        "सम्-पूर्वकस्य प्रति-पूर्वकस्य वा धातोः अनाध्यान-अर्थे आत्मनेपदम् — "
        "saMpaThate, pratipaThate (न अध्ययन-अर्थे) इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
