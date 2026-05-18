"""
1.3.58  नानोर्ज्ञः  —  VIDHI

*Padaccheda:* *na* / *anoḥ* (पञ्चमी-एकवचन) / *jñaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada (san) from 1.3.57 → 1.3.12.

*Content:* Exception to 1.3.57 — the root jñā (to know) preceded by the
prefix anu does NOT take ātmanepada in the desiderative (san). So anujijñāsati
(not *anujijñāsate). This sūtra uses "na" to block the previous rule.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_58" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _JNA_ROOTS carries the tag "san_pratyaya" AND "anu_prefix" — in which case
we set a blocker flag to prevent 1.3.57 from firing for this combination.
Actually implemented as VIDHI that sets a negative gate. No arm flags.
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_JNA_ROOTS: frozenset[str] = frozenset({"jYA", "jYa"})

_REGISTRY_KEY = "1_3_58_anu_jYA_san_nAtmanepada"
_STAMP_KEY    = "Atmanepada_1_3_58"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _JNA_ROOTS and "san_pratyaya" in t.tags and "anu_prefix" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    if t is None:
        return state
    # Block ātmanepada for anu+jñā+san — set Parasmaipada explicitly
    state.meta["pada"]     = "Parasmaipada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.58",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="nAnorjYaH",
    text_dev="नानोर्ज्ञः",
    padaccheda_dev="न / अनोः (पञ्चमी-एकवचन) / ज्ञः (षष्ठी-एकवचन)",
    why_dev=(
        "अनु-पूर्वकस्य ज्ञा-धातोः सन्-प्रत्यये परे आत्मनेपदं न भवति — "
        "anujijYAsati (न anujijYAsate); "
        "१.३.५७ अपवादः; १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.57"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
