"""
1.3.61  म्रियतेर्लुङ्लिङोश्च  —  VIDHI

*Padaccheda:* *mriyateḥ* (षष्ठी-एकवचन) / *luṅ-liṅoḥ* (सप्तमी-द्विवचन) / *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root mṛ (to die; √mṛ class 6) takes ātmanepada endings also in
the luṅ (aorist) and liṅ (optative/potential) lākāras, in addition to the
other lākāras already covered. The word "ca" includes the other lākāras
already given by the general rule (śit context from 1.3.60 etc). In practice
mṛ always takes ātmanepada. For example: amṛta (luṅ), mriyeta (liṅ).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_61" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _MR_ROOTS carries either "luN_lakara" or "liN_lakara" tag. No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_MR_ROOTS: frozenset[str] = frozenset({"mf", "mfY", "mriya"})
_LAKARA:   frozenset[str] = frozenset({"luN_lakara", "liN_lakara"})

_REGISTRY_KEY = "1_3_61_mf_luN_liN"
_STAMP_KEY    = "Atmanepada_1_3_61"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _MR_ROOTS and bool(_LAKARA & t.tags):
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
    sutra_id="1.3.61",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="mriyaterlufNliNgoSca",
    text_dev="म्रियतेर्लुङ्लिङोश्च",
    padaccheda_dev="म्रियतेः (षष्ठी-एकवचन) / लुङ्-लिङोः (सप्तमी-द्विवचन) / च",
    why_dev=(
        "मृ-धातोः लुङ्-लिङ्-लकारयोः आत्मनेपदम् — "
        "amfta, mriyeta इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
