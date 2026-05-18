"""
1.3.79  अनुपराभ्यां कृञः  —  VIDHI

*Padaccheda:* *anu-parābhyām* (पञ्चमी-द्विवचन) / *kṛñaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root kṛ (√kṛñ, to do/make) preceded by the prefixes anu or parā
takes ātmanepada endings. For example: anukurute — he imitates; parākurute —
he does surpassingly.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_79" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _KR_ROOTS carries either "anu_prefix" or "parA_prefix" tag.
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KR_ROOTS: frozenset[str] = frozenset({"qukf~Y", "kf", "kfY", "kara"})
_PREFIXES: frozenset[str] = frozenset({"anu_prefix", "parA_prefix"})

_REGISTRY_KEY = "1_3_79_anu_parA_kf_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_79"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _KR_ROOTS and _PREFIXES & t.tags:
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
    sutra_id="1.3.79",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="anuparAByAM kfYaH",
    text_dev="अनुपराभ्यां कृञः",
    padaccheda_dev="अनु-पराभ्याम् (पञ्चमी-द्विवचन) / कृञः (षष्ठी-एकवचन)",
    why_dev=(
        "अनु-पूर्वकस्य पर-पूर्वकस्य च कृञ्-धातोः आत्मनेपदम् — "
        "anukurute, parAkurute इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
