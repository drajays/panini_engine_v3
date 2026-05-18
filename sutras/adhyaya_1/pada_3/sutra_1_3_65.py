"""
1.3.65  समः क्ष्णुवः  —  VIDHI

*Padaccheda:* *samaḥ* (पञ्चमी-एकवचन) / *kṣṇuvaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root kṣṇu (to sharpen; √kṣṇu class 2) preceded by the prefix
sam takes ātmanepada endings. For example: saṃkṣṇute — he sharpens (together).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_65" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _KSNU_ROOTS carries the tag "sam_prefix". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KSNU_ROOTS: frozenset[str] = frozenset({"kzRu", "kzRuv"})

_REGISTRY_KEY = "1_3_65_sam_kzRu"
_STAMP_KEY    = "Atmanepada_1_3_65"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _KSNU_ROOTS and "sam_prefix" in t.tags:
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
    sutra_id="1.3.65",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="samaH kzRuvaH",
    text_dev="समः क्ष्णुवः",
    padaccheda_dev="समः (पञ्चमी-एकवचन) / क्ष्णुवः (षष्ठी-एकवचन)",
    why_dev=(
        "सम्-पूर्वकस्य क्ष्णु-धातोः आत्मनेपदम् — "
        "saMkzRute इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
