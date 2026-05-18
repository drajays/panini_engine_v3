"""
1.3.21  क्रीडोऽनुसम्परिभ्यश्च  —  VIDHI

*Padaccheda:* *krīḍaḥ* (षष्ठी) / *anu-sam-pari-bhyaḥ* (पञ्चमी) / *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* For the root krīḍ (to play/sport) preceded by any of the prefixes
anu, sam, or pari, ātmanepada endings are prescribed.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) a dhātu Term whose
upadesha_slp1 is in _KRIDA_ROOTS, (c) any tag from _KRIDA_PREFIXES present on
that dhātu, and (d) idempotency guard "Atmanepada_1_3_21" absent from meta.
No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_KRIDA_ROOTS: frozenset[str] = frozenset({"krIq", "krIqf"})
_KRIDA_PREFIXES: frozenset[str] = frozenset({"anu_prefix", "sam_prefix", "pari_prefix"})
_REGISTRY_KEY = "1_3_21_krIqa_anu_sam_pari"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_21"):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _KRIDA_ROOTS
        and bool(_KRIDA_PREFIXES & t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_21"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.21",
    sutra_type=SutraType.VIDHI,
    text_slp1="krIqo'nusaMpariBya(S)ca",
    text_dev="क्रीडोऽनुसम्परिभ्यश्च",
    padaccheda_dev="क्रीडः (षष्ठी) / अनु-सम्-परि-भ्यः (पञ्चमी) / च",
    why_dev=(
        "अनु-सम्-परि-पूर्वकस्य क्रीड्-धातोः आत्मनेपदं भवति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
