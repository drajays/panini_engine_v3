"""
1.3.82  परेर्मृषः  —  VIDHI

*Padaccheda:* *pareḥ* (पञ्चमी-एकवचन) / *mṛṣaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root mṛṣ (√mṛṣā, to endure/tolerate) preceded by the prefix
pari takes ātmanepada endings. For example: parimṛṣate — he tolerates/endures.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_82" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _MRS_ROOTS carries the tag "pari_prefix".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_MRS_ROOTS: frozenset[str] = frozenset({"mfza~", "mfz", "mrzA"})

_REGISTRY_KEY = "1_3_82_pari_mfz_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_82"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _MRS_ROOTS and "pari_prefix" in t.tags:
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
    sutra_id="1.3.82",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="parerMfzaH",
    text_dev="परेर्मृषः",
    padaccheda_dev="परेः (पञ्चमी-एकवचन) / मृषः (षष्ठी-एकवचन)",
    why_dev=(
        "परि-पूर्वकस्य मृष्-धातोः आत्मनेपदम् — "
        "parimfzate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
