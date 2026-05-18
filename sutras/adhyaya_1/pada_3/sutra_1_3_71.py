"""
1.3.71  मिथ्योपपदात् कृञोऽभ्यासे  —  VIDHI

*Padaccheda:* *mithyā-upapadāt* (पञ्चमी-एकवचन) / *kṛñaḥ* (षष्ठी-एकवचन) /
*abhyāse* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root kṛ (√kṛ, to do/make) preceded by the upapada (accompanying
word) mithyā (falsely/wrongly/in vain) takes ātmanepada endings when the
meaning involves abhyāsa (practice/repetition/habituation). For example:
mithyā kurvīta — he practises doing falsely / he habitually does wrong.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_71" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _KR_ROOTS carries the tag "miTyA_upapada" and "AByAsa_usage". No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KR_ROOTS: frozenset[str] = frozenset({"qukf~Y", "kf", "kfY"})

_REGISTRY_KEY = "1_3_71_miTyA_kf_AByAsa"
_STAMP_KEY    = "Atmanepada_1_3_71"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _KR_ROOTS and "miTyA_upapada" in t.tags and "AByAsa_usage" in t.tags:
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
    sutra_id="1.3.71",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="miTyopapadAtkfYoByAse",
    text_dev="मिथ्योपपदात् कृञोऽभ्यासे",
    padaccheda_dev=(
        "मिथ्या-उपपदात् (पञ्चमी-एकवचन) / कृञः (षष्ठी-एकवचन) / अभ्यासे (सप्तमी-एकवचन)"
    ),
    why_dev=(
        "मिथ्या-उपदपदपूर्वकस्य कृञ्-धातोः अभ्यास-विषये आत्मनेपदम् — "
        "miTyA kurvIta इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
