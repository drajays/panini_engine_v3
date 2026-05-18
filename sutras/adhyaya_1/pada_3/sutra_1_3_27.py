"""
1.3.27  उद्विभ्यां तपः  —  VIDHI

*Padaccheda:* *ut-vibhyām* (पञ्चमी) / *tapaḥ* (षष्ठी).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for tap (to heat/do austerities) after ud or vi.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) any dhātu Term
whose upadesha_slp1 is in _TAP_ROOTS, (c) that dhātu carries at least one tag
from _UD_VI, and (d) idempotency guard "Atmanepada_1_3_27" is absent from meta.
No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_TAP_ROOTS: frozenset[str] = frozenset({"tap", "tapa"})
_UD_VI: frozenset[str] = frozenset({"ud_prefix", "vi_prefix"})
_REGISTRY_KEY = "1_3_27_ud_vi_tap"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_27"):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _TAP_ROOTS
        and bool(_UD_VI & t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_27"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.27",
    sutra_type=SutraType.VIDHI,
    text_slp1="udviBhyAM tapaH",
    text_dev="उद्विभ्यां तपः",
    padaccheda_dev="उत्-विभ्याम् (पञ्चमी) / तपः (षष्ठी)",
    why_dev=(
        "उद्-वि-पूर्वकस्य तप्-धातोः आत्मनेपदं भवति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
