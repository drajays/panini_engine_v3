"""
1.3.50  विभाषा विप्रलापे  —  VIBHASHA

*Padaccheda:* *vibhāṣā* (अव्यय) / *vipralāpe* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Optionally (vibhāṣā) [ātmanepada applies] in the sense of
vipralāpa (deceptive speech / talking falsely / misleading talk).
When a root is used in the sense of deceptive or misleading speech,
ātmanepada is optionally available — the speaker may choose either
ātmanepada or parasmaipada.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_vibhASA_1_3_50" is absent, and (c) a dhātu
Term carries the tag "vipralApa_usage".
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
vibhasha_default=True: the optional ātmanepada form is taken by default.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_50_vipralApa_vibhASA"
_STAMP_KEY    = "Atmanepada_vibhASA_1_3_50"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags and "vipralApa_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.50",
    sutra_type=SutraType.VIBHASHA,
    vibhasha_default=True,
    r1_form_identity_exempt=True,
    text_slp1="vibhASA viprAlApe",
    text_dev="विभाषा विप्रलापे",
    padaccheda_dev="विभाषा (अव्यय) / विप्रलापे (सप्तमी-एकवचन)",
    why_dev=(
        "विप्रलाप-अर्थे धातोः प्रयोगे विभाषा आत्मनेपदम् — "
        "vipralApate / vipralApati इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
