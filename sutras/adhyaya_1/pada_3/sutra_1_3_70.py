"""
1.3.70  लियः सम्माननशालीनीकरणयोश्च  —  VIDHI

*Padaccheda:* *liyaḥ* (षष्ठी-एकवचन) / *sammānana-śālīnīkaraṇayoḥ* (सप्तमी-द्विवचन)
/ *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root lī (to dissolve/cling/adhere; √lī class 9 or 4) takes
ātmanepada endings in the meanings of sammānana (honouring/respecting) and
śālīnīkaraṇa (making humble/causing to hide/making modest). The "ca" includes
other meanings already established. For example: līyate (he hides himself/
becomes modest).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_70" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _LI_ROOTS carries either "sammAnana_usage" or "SAlinIkaraNa_usage" tag.
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_LI_ROOTS:  frozenset[str] = frozenset({"lI", "li", "lIN"})
_USAGES:    frozenset[str] = frozenset({"sammAnana_usage", "SAlinIkaraNa_usage"})

_REGISTRY_KEY = "1_3_70_lI_sammAnana_SAlinI"
_STAMP_KEY    = "Atmanepada_1_3_70"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _LI_ROOTS and bool(_USAGES & t.tags):
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
    sutra_id="1.3.70",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="liyaH sammAnanaZAlInIkaraNayoSca",
    text_dev="लियः सम्माननशालीनीकरणयोश्च",
    padaccheda_dev=(
        "लियः (षष्ठी-एकवचन) / सम्मानन-शालीनीकरणयोः (सप्तमी-द्विवचन) / च"
    ),
    why_dev=(
        "ली-धातोः सम्मानन/शालीनीकरण-अर्थयोः आत्मनेपदम् — "
        "lIyate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
