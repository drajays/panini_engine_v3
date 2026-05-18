"""
1.3.74  णिचश्च  —  VIDHI

*Padaccheda:* *ṇicaḥ* (षष्ठी-एकवचन) / *ca*.

*Anuvṛtti:* ātmanepada (apāt vadaḥ — of root vad after apa) from 1.3.73.
Also: ātmanepada from 1.3.12.

*Content:* In the causative (ṇic / ṇi suffix) construction also, the rule of
1.3.73 (apa+vad = parasmaipada) applies — "ca" extends the previous niyama to
the causative. So apavādayati (he causes to speak-against) also takes
parasmaipada, not ātmanepada. More broadly, this sūtra establishes that ṇic
(causative) forms follow the same pada assignment as established in the prior
context.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_74" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _VAD_ROOTS carries both "apa_prefix" and "Nic_pratyaya". act sets
pada = "Parasmaipada" (extending niyama). No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_VAD_ROOTS: frozenset[str] = frozenset({"vada~", "vad", "vada"})

_REGISTRY_KEY = "1_3_74_apa_vad_Nic_parasmai"
_STAMP_KEY    = "Atmanepada_1_3_74"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Parasmaipada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _VAD_ROOTS and "apa_prefix" in t.tags and "Nic_pratyaya" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    if t is None:
        return state
    state.meta["pada"]     = "Parasmaipada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.74",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="RicaSca",
    text_dev="णिचश्च",
    padaccheda_dev="णिचः (षष्ठी-एकवचन) / च",
    why_dev=(
        "अप-पूर्वकस्य वद्-धातोः णिच्-प्रत्यये परे अपि आत्मनेपदं न भवति — "
        "apavAdayati (न *apavAdate); "
        "१.३.७३ अनुसारेण; १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.73"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
