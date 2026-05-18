"""
1.3.83  व्याङ्परिभ्यो रमः  —  VIDHI

*Padaccheda:* *vi-āṅ-paribhyaḥ* (पञ्चमी-बहुवचन) / *ramaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root ram (√ram, to delight/enjoy) preceded by the prefixes vi,
ā, or pari takes ātmanepada endings. For example: viramate — he stops/desists;
āramate — he delights; pariramati/paramate — he enjoys.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_83" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _RAM_ROOTS carries any of "vi_prefix", "A_prefix", "pari_prefix".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_RAM_ROOTS: frozenset[str] = frozenset({"rama~", "ram"})
_PREFIXES:  frozenset[str] = frozenset({"vi_prefix", "A_prefix", "pari_prefix"})

_REGISTRY_KEY = "1_3_83_vi_A_pari_ram_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_83"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _RAM_ROOTS and _PREFIXES & t.tags:
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
    sutra_id="1.3.83",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="vyANpariByo ramaH",
    text_dev="व्याङ्परिभ्यो रमः",
    padaccheda_dev="वि-आङ्-परिभ्यः (पञ्चमी-बहुवचन) / रमः (षष्ठी-एकवचन)",
    why_dev=(
        "वि-आ-परि-पूर्वकस्य रम्-धातोः आत्मनेपदम् — "
        "viramate, Aramate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
