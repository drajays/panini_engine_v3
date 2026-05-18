"""
1.3.73  अपाद्वदः  —  NIYAMA

*Padaccheda:* *apāt* (पञ्चमी-एकवचन) / *vadaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root vad (to speak; √vad class 1) preceded by the prefix apa
does NOT take ātmanepada endings — even when the general ātmanepada rules
(e.g., 1.3.72 kartrabhiprāya) would otherwise apply. This is a niyama
(restriction) that blocks ātmanepada for apa+vad. The form is apavadati
(not *apavadate). "Apāt" = from the prefix apa; "vadaḥ" = of the root vad.

*Engine (NIYAMA):* cond checks (a) pada is not already "Parasmaipada",
(b) idempotency stamp "Niyama_1_3_73" is absent, (c) a dhātu Term whose
upadesha_slp1 is in _VAD_ROOTS carries the tag "apa_prefix". act sets
pada = "Parasmaipada" and writes to niyama_gates. No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_VAD_ROOTS: frozenset[str] = frozenset({"vada~", "vad", "vada"})

_REGISTRY_KEY = "1_3_73_apa_vad_nAtmanepada"
_STAMP_KEY    = "Niyama_1_3_73"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Parasmaipada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _VAD_ROOTS and "apa_prefix" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    if t is None:
        return state
    # Niyama: restrict ātmanepada — force Parasmaipada for apa+vad
    state.meta["pada"]  = "Parasmaipada"
    state.meta[_STAMP_KEY] = True
    state.niyama_gates[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.73",
    sutra_type=SutraType.NIYAMA,
    r1_form_identity_exempt=True,
    text_slp1="apAdvadaH",
    text_dev="अपाद्वदः",
    padaccheda_dev="अपात् (पञ्चमी-एकवचन) / वदः (षष्ठी-एकवचन)",
    why_dev=(
        "अप-पूर्वकस्य वद्-धातोः आत्मनेपदं न भवति — apavadati (न *apavadate); "
        "१.३.७२ इत्यादेः अपवादः; १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते नियमेन निषिध्यते।"
    ),
    anuvritti_from=("1.3.12", "1.3.72"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
