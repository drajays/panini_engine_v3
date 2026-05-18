"""
1.3.75  समुदाङ्भ्यो यमोऽग्रन्थे  —  VIDHI

*Padaccheda:* *sam-ud-āṅbhyaḥ* (पञ्चमी-बहुवचन) / *yamaḥ* (षष्ठी-एकवचन) /
*agrantha* (सप्तमी-एकवचन — *na grantha* = not the Vedic text recitation).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root yam (to restrain/hold; √yam class 1) preceded by any of
the prefixes sam, ud, or ā (āṅ) takes ātmanepada endings — but only outside
the context of grantha (text/Vedic recitation). For example: samyacchate —
he restrains himself; udyacchate — he lifts himself up; āyacchate — he
restrains/pulls toward himself.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_75" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _YAM_ROOTS carries one of {sam_prefix, ut_prefix, A_prefix} and does NOT
carry "granTa_usage". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_YAM_ROOTS: frozenset[str] = frozenset({"yam", "yama"})
_PREFIXES:  frozenset[str] = frozenset({"sam_prefix", "ut_prefix", "A_prefix"})

_REGISTRY_KEY = "1_3_75_sam_ud_A_yam_agrantha"
_STAMP_KEY    = "Atmanepada_1_3_75"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if (up in _YAM_ROOTS
                and bool(_PREFIXES & t.tags)
                and "granTa_usage" not in t.tags):
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
    sutra_id="1.3.75",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="samudANByoyamogrante",
    text_dev="समुदाङ्भ्यो यमोऽग्रन्थे",
    padaccheda_dev=(
        "सम्-उत्-आङ्भ्यः (पञ्चमी-बहुवचन) / यमः (षष्ठी-एकवचन) "
        "/ अग्रन्थे (सप्तमी-एकवचन)"
    ),
    why_dev=(
        "सम्/उत्/आ-पूर्वकस्य यम्-धातोः अग्रन्थ-विषये आत्मनेपदम् — "
        "samyacchate, udyacchate, Ayacchate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
