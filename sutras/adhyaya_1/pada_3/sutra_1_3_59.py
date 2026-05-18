"""
1.3.59  प्रत्याङ्भ्यां श्रुवः  —  VIDHI

*Padaccheda:* *prati-āṅbhyām* (तृतीया/पञ्चमी-द्विवचन) / *śruvaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root śru (to hear) preceded by either prati or ā (āṅ) takes
ātmanepada endings (unconditionally, not just in san). For example:
pratiśṛṇute — he hears back / he promises; āśṛṇute — he hears.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_59" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _SRU_ROOTS carries either "prati_prefix" or "A_prefix". No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_SRU_ROOTS: frozenset[str] = frozenset({"Sru"})
_PREFIXES:  frozenset[str] = frozenset({"prati_prefix", "A_prefix"})

_REGISTRY_KEY = "1_3_59_prati_A_Sru"
_STAMP_KEY    = "Atmanepada_1_3_59"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _SRU_ROOTS and bool(_PREFIXES & t.tags):
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
    sutra_id="1.3.59",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="pratyANByAM SruvaH",
    text_dev="प्रत्याङ्भ्यां श्रुवः",
    padaccheda_dev="प्रति-आङ्भ्याम् (पञ्चमी-द्विवचन) / श्रुवः (षष्ठी-एकवचन)",
    why_dev=(
        "प्रति/आ-पूर्वकस्य श्रु-धातोः आत्मनेपदम् — "
        "pratiSfRute, ASfRute इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
