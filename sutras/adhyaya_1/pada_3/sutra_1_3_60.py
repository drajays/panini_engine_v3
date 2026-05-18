"""
1.3.60  शदेः शितः  —  VIDHI

*Padaccheda:* *śadeḥ* (षष्ठी-एकवचन) / *śitaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root śad (to fall, perish; √śad class 1/6) takes ātmanepada
endings when followed by a śit suffix (a suffix marked with the anubandha ś).
For example: śīyate (from śad + yak = śīyate, the passive is śit).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_60" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _SAD_ROOTS carries the tag "Sit_pratyaya". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_SAD_ROOTS: frozenset[str] = frozenset({"Sad", "Sada"})

_REGISTRY_KEY = "1_3_60_Sad_Sit"
_STAMP_KEY    = "Atmanepada_1_3_60"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _SAD_ROOTS and "Sit_pratyaya" in t.tags:
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
    sutra_id="1.3.60",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="SadeH SitaH",
    text_dev="शदेः शितः",
    padaccheda_dev="शदेः (षष्ठी-एकवचन) / शितः (षष्ठी-एकवचन)",
    why_dev=(
        "शद्-धातोः शित्-प्रत्यये परे आत्मनेपदम् — "
        "SIyate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
