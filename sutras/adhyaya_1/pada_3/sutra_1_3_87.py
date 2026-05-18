"""
1.3.87  निगरणचलनार्थेभ्यश्च  —  VIDHI

*Padaccheda:* *nigaraṇa-calana-arthebhyaḥ* (पञ्चमी-बहुवचन) / *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12; ṇeḥ from 1.3.86; ca = "and also".

*Content:* Also, roots meaning swallowing (nigaraṇa) or movement (calana)
take ātmanepada endings when followed by the causative suffix ṇi.
This extends 1.3.86 to cover a semantic class.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_87" is absent, (c) a dhātu Term carries the tag
"NI_causative_context" AND either "nigaraNa_usage" or "calana_usage".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets for semantic usage tags (CONSTITUTION Art. 13.3)
_USAGE_TAGS: frozenset[str] = frozenset({"nigaraNa_usage", "calana_usage"})

_REGISTRY_KEY = "1_3_87_nigaraNa_calana_Ni_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_87"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if "NI_causative_context" in t.tags and _USAGE_TAGS & t.tags:
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
    sutra_id="1.3.87",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="nigaraNacalanArTeBYaSca",
    text_dev="निगरणचलनार्थेभ्यश्च",
    padaccheda_dev="निगरण-चलन-अर्थेभ्यः (पञ्चमी-बहुवचन) / च",
    why_dev=(
        "निगरण-चलन-अर्थक-धातूनां णि-प्रत्यये परे आत्मनेपदम् — "
        "१.३.८६ इत्यस्य विस्तारः; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.86"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
