"""
1.3.25  उपान्मन्त्रकरणे  —  VIDHI

*Padaccheda:* *upāt* (पञ्चमी) / *mantra-karaṇe* (सप्तमी).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] when the prefix upa is used before certain roots in
the "mantra-making/reciting" (mantra-karaṇa) sense.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) any dhātu Term
carries "upa_prefix" in its tags, (c) that dhātu carries the semantic usage
tag "mantrakaraNa_usage", and (d) idempotency guard "Atmanepada_1_3_25" is
absent from meta.  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_25_upa_mantrakaraNa"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_25"):
        return False
    return any(
        "dhatu" in t.tags
        and "upa_prefix" in t.tags
        and "mantrakaraNa_usage" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_25"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.25",
    sutra_type=SutraType.VIDHI,
    text_slp1="upAnmantrakaraNe",
    text_dev="उपान्मन्त्रकरणे",
    padaccheda_dev="उपात् (पञ्चमी) / मन्त्र-करणे (सप्तमी)",
    why_dev=(
        "उप-पूर्वकस्य धातोः मन्त्र-करण-अर्थे आत्मनेपदं भवति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
