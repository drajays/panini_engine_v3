"""
1.3.77  विभाषोपपदेन प्रतीयमाने  —  VIDHI (VIBHASHA)

*Padaccheda:* *vibhāṣā* (प्रथमा-एकवचन) / *upapadeana* (तृतीया-एकवचन)
/ *pratīyamāne* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Optionally, ātmanepada is used when the sense is inferred
(pratīyamāna) from the upapada (accompanying word) context — i.e. the
syntactic neighbour implies that the fruit benefits the agent even without
an explicit marker. The vibhāṣā (option) means parasmaipada is also valid.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_vibhASA_1_3_77" is absent, (c) any dhātu Term carries the
tag "upapada_pratIyamAne_usage". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_TRIGGER_TAG  = "upapada_pratIyamAne_usage"
_STAMP_KEY    = "Atmanepada_vibhASA_1_3_77"
_REGISTRY_KEY = "1_3_77_upapada_vibhASA"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if _TRIGGER_TAG in t.tags:
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
    sutra_id="1.3.77",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    vibhasha_default=True,
    text_slp1="vibhAzOpapadeana pratIyamAne",
    text_dev="विभाषोपपदेन प्रतीयमाने",
    padaccheda_dev=(
        "विभाषा (प्रथमा-एकवचन) / उपापदेन (तृतीया-एकवचन) "
        "/ प्रतीयमाने (सप्तमी-एकवचन)"
    ),
    why_dev=(
        "उपापद-संनिधौ प्रतीयमाने विषये विभाषया आत्मनेपदम् — "
        "परस्मैपदम् अपि साधु; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
