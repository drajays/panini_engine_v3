"""
1.3.81  प्राद्वहः  —  VIDHI

*Padaccheda:* *prāt* (पञ्चमी-एकवचन) / *vahaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root vah (√vah, to carry/bear) preceded by the prefix pra
takes ātmanepada endings. For example: pravahate — he carries forward.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_81" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _VAH_ROOTS carries the tag "pra_prefix".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_VAH_ROOTS: frozenset[str] = frozenset({"vaha~", "vah"})

_REGISTRY_KEY = "1_3_81_pra_vah_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_81"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _VAH_ROOTS and "pra_prefix" in t.tags:
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
    sutra_id="1.3.81",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="prAdvAhaH",
    text_dev="प्राद्वहः",
    padaccheda_dev="प्रात् (पञ्चमी-एकवचन) / वहः (षष्ठी-एकवचन)",
    why_dev=(
        "प्र-पूर्वकस्य वह्-धातोः आत्मनेपदम् — "
        "pravahate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
