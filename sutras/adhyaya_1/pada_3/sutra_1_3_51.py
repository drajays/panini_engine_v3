"""
1.3.51  अवाद्ग्रः  —  VIDHI

*Padaccheda:* *avāt* (पञ्चमी-एकवचन) / *graḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root grah (√grah / √grā, to seize/take) preceded by the
prefix ava takes ātmanepada endings. For example: avagraha — avagṛhīte
(he seizes/takes hold of).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_1_3_51" is absent, and (c) a dhātu Term
whose upadesha_slp1 is in _GRAH_ROOTS and which carries the tag "ava_prefix".
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_GRAH_ROOTS: frozenset[str] = frozenset({"gfhU", "graha", "grA", "grah"})

_REGISTRY_KEY = "1_3_51_ava_grah"
_STAMP_KEY    = "Atmanepada_1_3_51"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _GRAH_ROOTS and "ava_prefix" in t.tags:
            return True
    return False


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.51",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="avAdgraH",
    text_dev="अवाद्ग्रः",
    padaccheda_dev="अवात् (पञ्चमी-एकवचन) / ग्रः (षष्ठी-एकवचन)",
    why_dev=(
        "अव-पूर्वकस्य ग्रह्-धातोः प्रयोगे आत्मनेपदम् — "
        "avagfhIte इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
