"""
1.3.84  उपाच्च  —  VIDHI

*Padaccheda:* *upāt* (पञ्चमी-एकवचन) / *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12; ram from 1.3.83; ca = "also".

*Content:* The root ram (√ram, to delight/enjoy) preceded by the prefix upa
also takes ātmanepada endings — extending 1.3.83. For example: uparamate —
he rests/desists.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_84" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _RAM_ROOTS carries the tag "upa_prefix".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_RAM_ROOTS: frozenset[str] = frozenset({"rama~", "ram"})

_REGISTRY_KEY = "1_3_84_upa_ram_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_84"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _RAM_ROOTS and "upa_prefix" in t.tags:
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
    sutra_id="1.3.84",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="upAcca",
    text_dev="उपाच्च",
    padaccheda_dev="उपात् (पञ्चमी-एकवचन) / च",
    why_dev=(
        "उप-पूर्वकस्य रम्-धातोः अपि आत्मनेपदम् — "
        "uparamate इत्यादि; "
        "१.३.८३ इत्यस्य विस्तारः; १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.83"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
