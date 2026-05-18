"""
1.3.35  अकर्मकाच्च  —  VIDHI

*Padaccheda:* *akarmakāt* (पञ्चमी-एकवचन) / *ca* (अव्यय).

*Anuvṛtti:* ātmanepada from 1.3.34; vi-prefix context continues.

*Content:* And [Ātmanepada] for akarmaka (intransitive) roots when preceded
by the prefix vi (extension of the vi-śabdakarmaṇaḥ context of 1.3.34).
For example: viharate — he wanders/moves about (intransitive with vi).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries both the tag "akarmaka" (encoding intransitive usage)
and the tag "vi_prefix" (encoding prefix vi), and (c) the idempotency stamp
"Atmanepada_1_3_35" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_35_akarmaka_vi"
_STAMP_KEY    = "Atmanepada_1_3_35"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "akarmaka" in t.tags
        and "vi_prefix" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.35",
    sutra_type=SutraType.VIDHI,
    text_slp1="akarmakAc ca",
    text_dev="अकर्मकाच्च",
    padaccheda_dev="अकर्मकात् (पञ्चमी-एकवचन) / च (अव्यय)",
    why_dev=(
        "वि-पूर्वकस्य अकर्मकस्य धातोः प्रयोगे आत्मनेपदम् — "
        "viharate इत्यादि; "
        "१.३.३४ इत्यतः अनुवर्तते।"
    ),
    anuvritti_from=("1.3.34",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
