"""
1.3.17  नेर्विशः  —  VIDHI

*Padaccheda:* *neḥ* (पञ्चमी-एकवचन) / *viśaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for the dhātu viś (to enter) when preceded by the
prefix ni (ni + viś → niviśate).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 == "viS" and also carries the tag
"ni_prefix" (set by the recipe to signal the presence of upasarga ni), and
(c) the idempotency stamp "Atmanepada_1_3_17" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_17_ni_viS"
_STAMP_KEY    = "Atmanepada_1_3_17"
_DHATU_SLP1   = "viS"
_PREFIX_TAG   = "ni_prefix"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() == _DHATU_SLP1
        and _PREFIX_TAG in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.17",
    sutra_type=SutraType.VIDHI,
    text_slp1="ner viSaH",
    text_dev="नेर्विशः",
    padaccheda_dev="नेः (पञ्चमी) / विशः (षष्ठी)",
    why_dev=(
        "नि-पूर्वस्य विश्-धातोः प्रयोगे आत्मनेपदम् — niviśate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
