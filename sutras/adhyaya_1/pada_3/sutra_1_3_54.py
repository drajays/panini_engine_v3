"""
1.3.54  समस्तृतीयायुक्तात्  —  VIDHI

*Padaccheda:* *samaḥ* (पञ्चमी-एकवचन) / *tṛtīyā-yuktāt* (पञ्चमी-एकवचन).

*Anuvṛtti:* ātmanepada (and caraḥ) from 1.3.53 → 1.3.12.

*Content:* The root car (√car) preceded by the prefix sam takes ātmanepada
endings when accompanied by a tṛtīyā (instrumental case) word — i.e., when the
verb means "to go along with" or "to travel together with" (someone expressed
in the instrumental). For example: saṃcarate devadattena — [he] travels with
Devadatta.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_54" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _CAR_ROOTS carries both the tag "sam_prefix" and the tag "tRtIyA_yukta_usage".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True because no
surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_CAR_ROOTS: frozenset[str] = frozenset({"cara", "car"})

_REGISTRY_KEY = "1_3_54_sam_cara_tRtIyA"
_STAMP_KEY    = "Atmanepada_1_3_54"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _CAR_ROOTS and "sam_prefix" in t.tags and "tRtIyA_yukta_usage" in t.tags:
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
    sutra_id="1.3.54",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="samastatRtIyAyuktAt",
    text_dev="समस्तृतीयायुक्तात्",
    padaccheda_dev="समः (पञ्चमी-एकवचन) / तृतीया-युक्तात् (पञ्चमी-एकवचन)",
    why_dev=(
        "सम्-पूर्वकस्य चर-धातोः तृतीया-युक्त-प्रयोगे आत्मनेपदम् — "
        "saṃcarate devadattena इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.53"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
