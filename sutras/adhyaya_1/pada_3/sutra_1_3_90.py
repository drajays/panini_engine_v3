"""
1.3.90  वा क्यषः  —  VIDHI (vibhāṣā)

*Padaccheda:* *vā* / *kyaṣaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Optionally, a root followed by the kyaṣ suffix (denominative)
takes ātmanepada endings. The word vā indicates optionality — both
ātmanepada and parasmaipada are allowed. For example: putrakāmyate /
putrakāmyati — he desires a son.

*Engine:* vibhasha_default=True. cond checks (a) pada is not already
"Atmanepada", (b) idempotency stamp "Atmanepada_1_3_90" is absent,
(c) a dhātu Term carries the tag "kyaz_pratyaya" or "kyaS_suffix".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets for kyaṣ-related tags (CONSTITUTION Art. 13.3)
_KYAZ_TAGS: frozenset[str] = frozenset({"kyaz_pratyaya", "kyaS_suffix", "kyaz_suffix"})

_REGISTRY_KEY = "1_3_90_kyaz_vibhAzA_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_90"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if _KYAZ_TAGS & t.tags:
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
    sutra_id="1.3.90",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    vibhasha_default=True,
    text_slp1="vA kyazaH",
    text_dev="वा क्यषः",
    padaccheda_dev="वा / क्यषः (षष्ठी-एकवचन)",
    why_dev=(
        "क्यष्-प्रत्यये परे विकल्पेन आत्मनेपदम् — "
        "putrakAmyate / putrakAmyati इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते; वा = विकल्पः।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
