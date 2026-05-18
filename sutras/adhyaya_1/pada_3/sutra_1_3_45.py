"""
1.3.45  अकर्मकाच्च  —  VIDHI

*Padaccheda:* *akarmakāt* (पञ्चमी-एकवचन) / *ca* (अव्यय).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* And [ātmanepada applies] for an akarmaka (intransitive) root
[following on from 1.3.44]. The "ca" picks up the prior context; any dhātu
that is akarmaka (carries no direct object, tagged "akarmaka") takes
ātmanepada endings.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_1_3_45" is absent, and (c) a dhātu Term
carries the tag "akarmaka".
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_45_akarmaka"
_STAMP_KEY    = "Atmanepada_1_3_45"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags and "akarmaka" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.45",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="akarmakAcca",
    text_dev="अकर्मकाच्च",
    padaccheda_dev="अकर्मकात् (पञ्चमी-एकवचन) / च (अव्यय)",
    why_dev=(
        "अकर्मक-धातोः प्रयोगे आत्मनेपदम् — "
        "च-शब्देन पूर्वसूत्रस्य अनुवृत्तिः; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.44"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
