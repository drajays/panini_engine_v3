"""
1.3.66  भुजोऽनवने  —  VIDHI

*Padaccheda:* *bhujaḥ* (षष्ठी-एकवचन) / *anavane* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root bhuj (to eat/enjoy; √bhuj class 7 — bhunakti/bhuṅkte) takes
ātmanepada endings in meanings other than "protecting" (avana = protecting/
nourishing). So bhuj meaning "to eat/enjoy" takes ātmanepada (bhuṅkte), but
bhuj meaning "to protect" takes parasmaipada. For example: bhuṅkte — he eats/
enjoys; but bhojati/bhunakti — he protects (rare usage).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_66" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _BHUJ_ROOTS does NOT carry the tag "avana_usage". No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_BHUJ_ROOTS: frozenset[str] = frozenset({"BuY", "BuJ", "Buj", "Buja"})

_REGISTRY_KEY = "1_3_66_Buj_anavana"
_STAMP_KEY    = "Atmanepada_1_3_66"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _BHUJ_ROOTS and "avana_usage" not in t.tags:
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
    sutra_id="1.3.66",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="BujoanavAne",
    text_dev="भुजोऽनवने",
    padaccheda_dev="भुजः (षष्ठी-एकवचन) / अनवने (सप्तमी-एकवचन)",
    why_dev=(
        "भुज्-धातोः अवन-अर्थव्यतिरिक्त-विषये आत्मनेपदम् — "
        "BuNkte (भोजनार्थे) इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
