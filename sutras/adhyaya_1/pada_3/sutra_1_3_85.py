"""
1.3.85  विभाषाऽकर्मकात्  —  VIDHI (vibhāṣā)

*Padaccheda:* *vibhāṣā* / *akarmakāt* (पञ्चमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Optionally, an intransitive (akarmaka) root takes ātmanepada
endings. The word vibhāṣā indicates optionality — both ātmanepada and
parasmaipada are allowed. For example: śete / śayate (to lie down).

*Engine:* vibhasha_default=True to indicate optional rule. cond checks
(a) pada is not already "Atmanepada", (b) idempotency stamp "Atmanepada_1_3_85"
is absent, (c) a dhātu Term carries the tag "akarmaka".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_85_akarmaka_vibhAzA_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_85"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if "akarmaka" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    if t is None:
        return state
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.85",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    vibhasha_default=True,
    text_slp1="viBazAkarmakAt",
    text_dev="विभाषाऽकर्मकात्",
    padaccheda_dev="विभाषा / अकर्मकात् (पञ्चमी-एकवचन)",
    why_dev=(
        "अकर्मक-धातोः विकल्पेन आत्मनेपदम् — "
        "Sete / Sayate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते; विभाषा = विकल्पः।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
