"""
1.3.91  द्युद्भ्यो लुङि  —  VIDHI

*Padaccheda:* *dyu-dbhyaḥ* (पञ्चमी-बहुवचन) / *luṅi* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The roots of the dyu group (dyu etc.) take ātmanepada endings
when the luṅ (aorist) lakāra is used. For example: adyota — aorist of dyut.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_91" is absent, (c) a dhātu Term carries the tag
"dyu_usage" AND the tag "lUN_lakAra".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets for dyu-group roots (CONSTITUTION Art. 13.3)
_DYU_ROOTS: frozenset[str] = frozenset({
    "dyu", "dyuta~", "dyut",
    "snu", "snuta~",
    "kzu", "kzuta~",
})

_REGISTRY_KEY = "1_3_91_dyu_lUN_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_91"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        # Match either explicit dyu roots or the dyu_usage tag
        if (up in _DYU_ROOTS or "dyu_usage" in t.tags) and "lUN_lakAra" in t.tags:
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
    sutra_id="1.3.91",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="dyudByolUNi",
    text_dev="द्युद्भ्यो लुङि",
    padaccheda_dev="द्युद्भ्यः (पञ्चमी-बहुवचन) / लुङि (सप्तमी-एकवचन)",
    why_dev=(
        "द्यु-गण-धातूनां लुङि-लकारे आत्मनेपदम् — "
        "adyota इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
