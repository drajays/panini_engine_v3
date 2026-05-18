"""
1.3.69  गृधिवञ्च्योः प्रलम्भने  —  VIDHI

*Padaccheda:* *gṛdhi-vañcyoḥ* (षष्ठी-द्विवचन) / *pralambhane* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The roots gṛdh (to covet/be greedy; √gṛdh) and vañc (to deceive/
cheat; √vañc) take ātmanepada endings in the meaning of pralambhana (cheating/
deceiving/deluding). For example: gṛdhyate (he covets/is deluded);
vañcate (he deceives).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_69" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _ROOTS carries the tag "prAlambhana_usage". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_ROOTS: frozenset[str] = frozenset({"gfDu", "gfD", "vaYca~", "vaYc", "vaYj"})

_REGISTRY_KEY = "1_3_69_gfDu_vaYc_prAlambhana"
_STAMP_KEY    = "Atmanepada_1_3_69"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _ROOTS and "prAlambhana_usage" in t.tags:
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
    sutra_id="1.3.69",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="gfDivaYcyoH prAlambhane",
    text_dev="गृधिवञ्च्योः प्रलम्भने",
    padaccheda_dev="गृधि-वञ्च्योः (षष्ठी-द्विवचन) / प्रलम्भने (सप्तमी-एकवचन)",
    why_dev=(
        "गृध्/वञ्च्-धात्वोः प्रलम्भन-अर्थे आत्मनेपदम् — "
        "gfDyate, vaYcate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
