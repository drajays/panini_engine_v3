"""
1.3.48  व्यक्तवाचां समुच्चारणे  —  VIDHI

*Padaccheda:* *vyakta-vācām* (षष्ठी-बहुवचन) / *samuccāraṇe* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12; vad (vadaḥ) from 1.3.47.

*Content:* [The root vad takes ātmanepada] in the context of samuccāraṇa
(distinct/clear joint utterance) of vyaktavāc (distinct/articulate speech).
This covers pronouncing or articulating words/sounds distinctly in unison or
in sequence — e.g., a teacher and student chanting together.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_1_3_48" is absent, and (c) a dhātu Term
whose upadesha_slp1 is in _VAD_ROOTS and which carries the tag
"samuccArana_usage" (indicating the samuccāraṇa context).
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_VAD_ROOTS: frozenset[str] = frozenset({"vada~", "vad"})

_REGISTRY_KEY = "1_3_48_vad_samuccArana"
_STAMP_KEY    = "Atmanepada_1_3_48"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _VAD_ROOTS and "samuccArana_usage" in t.tags:
            return True
    return False


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.48",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="vyaktavAcAM samuccArane",
    text_dev="व्यक्तवाचां समुच्चारणे",
    padaccheda_dev="व्यक्त-वाचाम् (षष्ठी-बहुवचन) / समुच्चारणे (सप्तमी-एकवचन)",
    why_dev=(
        "व्यक्तवाचां समुच्चारणे वद्-धातोः आत्मनेपदम् — "
        "वाचां सम्यक् स्पष्टोच्चारणे वदते इत्यादि; "
        "१.३.४७ इत्यतः वदः, १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.47"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
