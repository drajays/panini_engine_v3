"""
1.3.22  समवप्रविभ्यः स्थः  —  VIDHI

*Padaccheda:* *sam-ava-pra-vi-bhyaḥ* (पञ्चमी) / *sthaḥ* (षष्ठी).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* For the root sthā (to stand/be established) preceded by any of the
prefixes sam, ava, pra, or vi, ātmanepada endings are prescribed.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) a dhātu Term whose
upadesha_slp1 is in _STHA_ROOTS, (c) any tag from _STHA_PREFIXES present on
that dhātu, and (d) idempotency guard "Atmanepada_1_3_22" absent from meta.
No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_STHA_ROOTS: frozenset[str] = frozenset({"zwA"})
_STHA_PREFIXES: frozenset[str] = frozenset({"sam_prefix", "ava_prefix", "pra_prefix", "vi_prefix"})
_REGISTRY_KEY = "1_3_22_sam_ava_pra_vi_zwA"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_22"):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _STHA_ROOTS
        and bool(_STHA_PREFIXES & t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_22"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.22",
    sutra_type=SutraType.VIDHI,
    text_slp1="samavapraviBya(H) sTaH",
    text_dev="समवप्रविभ्यः स्थः",
    padaccheda_dev="सम्-अव-प्र-वि-भ्यः (पञ्चमी) / स्थः (षष्ठी)",
    why_dev=(
        "सम्-अव-प्र-वि-पूर्वकस्य स्था-धातोः आत्मनेपदं भवति; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
