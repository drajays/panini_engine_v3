"""
1.3.31  स्पर्द्धायामाङः  —  VIDHI

*Padaccheda:* *spardhāyām* (सप्तमी-एकवचन) / *āṅaḥ* (पञ्चमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] in a competitive / rivalry (spardhā) sense when
the prefix ā (āṅ) is present (e.g. āspardhate — he competes with).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries the tag "A_prefix" (encoding prefix āṅ) and also
the tag "sparDA_usage" (encoding the competitive semantic context), and
(c) the idempotency stamp "Atmanepada_1_3_31" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_31_A_sparDA"
_STAMP_KEY    = "Atmanepada_1_3_31"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "A_prefix" in t.tags
        and "sparDA_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.31",
    sutra_type=SutraType.VIDHI,
    text_slp1="sparDAyAm ANaH",
    text_dev="स्पर्द्धायामाङः",
    padaccheda_dev="स्पर्द्धायाम् (सप्तमी) / आङः (पञ्चमी)",
    why_dev=(
        "स्पर्द्धा-अर्थे आङ्-पूर्वकस्य धातोः प्रयोगे आत्मनेपदम् — "
        "āspardhate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
