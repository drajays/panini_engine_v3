"""
1.3.24  उदोऽनूर्ध्वकर्मणि  —  VIDHI

*Padaccheda:* *udaḥ* (पञ्चमी) / *anu* (समाहृत) / *ūrdhva-karmaṇi* (सप्तमी).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* For [roots] preceded by the prefix ud (or anu) when the karma
(object) is "ūrdhva" (upward/elevated action), ātmanepada endings are
prescribed.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) any dhātu Term
carries "ud_prefix" or "anu_prefix" in its tags, (c) that dhātu carries the
semantic usage tag "UrDva_karma_usage", and (d) idempotency guard
"Atmanepada_1_3_24" is absent from meta.  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_UD_ANU_PREFIXES: frozenset[str] = frozenset({"ud_prefix", "anu_prefix"})
_REGISTRY_KEY = "1_3_24_ud_UrDva_karma"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_24"):
        return False
    return any(
        "dhatu" in t.tags
        and bool(_UD_ANU_PREFIXES & t.tags)
        and "UrDva_karma_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_24"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.24",
    sutra_type=SutraType.VIDHI,
    text_slp1="udo'nUrDvakarmaRi",
    text_dev="उदोऽनूर्ध्वकर्मणि",
    padaccheda_dev="उदः (पञ्चमी) / अनु / ऊर्ध्व-कर्मणि (सप्तमी)",
    why_dev=(
        "उद्-अनु-पूर्वकस्य धातोः ऊर्ध्व-कर्म-विषये आत्मनेपदं भवति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
