"""
1.3.93  लुटि च कॢपः  —  VIDHI

*Padaccheda:* *luṭi* (सप्तमी-एकवचन) / *ca* / *kḷpaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12; sya-sanoḥ from 1.3.92 extended by ca.

*Content:* Also, the root kḷp (√kḷp, to be fit/to ordain) takes ātmanepada
endings when the luṭ (periphrastic future) lakāra is used. For example:
kalptā — he will be fit. The ca extends from 1.3.92.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_93" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _KLP_ROOTS carries the tag "luT_lakAra".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KLP_ROOTS: frozenset[str] = frozenset({"kFpa~", "kFp", "kxpa~", "klp", "kxp"})

_REGISTRY_KEY = "1_3_93_kFp_luT_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_93"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _KLP_ROOTS and "luT_lakAra" in t.tags:
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
    sutra_id="1.3.93",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="luTi ca kFpaH",
    text_dev="लुटि च कॢपः",
    padaccheda_dev="लुटि (सप्तमी-एकवचन) / च / कॢपः (षष्ठी-एकवचन)",
    why_dev=(
        "कॢप्-धातोः लुटि-लकारे आत्मनेपदम् — "
        "kalptA इत्यादि; "
        "१.३.९२ इत्यस्य विस्तारः (च); १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.92"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
