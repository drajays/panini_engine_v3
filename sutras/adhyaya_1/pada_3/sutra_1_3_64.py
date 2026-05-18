"""
1.3.64  प्रोपाभ्यां युजेरयज्ञपात्रेषु  —  VIDHI

*Padaccheda:* *pra-upābhyām* (पञ्चमी-द्विवचन) / *yujeḥ* (षष्ठी-एकवचन) /
*ayajñapātreṣu* (सप्तमी-बहुवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root yuj (to join/yoke; √yuj class 7) preceded by either pra or
upa takes ātmanepada endings — but only in contexts that are NOT yajña-pātra
(sacrificial vessel/implement contexts). In other words, when yuj with pra/upa
is used outside of ritual/sacrificial contexts, it takes ātmanepada.
For example: prayuṅkte — he employs/uses; upayuṅkte — he uses/enjoys.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_64" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _YUJ_ROOTS carries either "pra_prefix" or "upa_prefix" AND does NOT carry
"yajYapAtra_usage". No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_YUJ_ROOTS: frozenset[str] = frozenset({"yuj"})
_PREFIXES:  frozenset[str] = frozenset({"pra_prefix", "upa_prefix"})

_REGISTRY_KEY = "1_3_64_pra_upa_yuj_ayajYapAtra"
_STAMP_KEY    = "Atmanepada_1_3_64"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if (up in _YUJ_ROOTS
                and bool(_PREFIXES & t.tags)
                and "yajYapAtra_usage" not in t.tags):
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
    sutra_id="1.3.64",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="propAByAM yujeryajYapAtrezu",
    text_dev="प्रोपाभ्यां युजेरयज्ञपात्रेषु",
    padaccheda_dev=(
        "प्र-उपाभ्याम् (पञ्चमी-द्विवचन) / युजेः (षष्ठी-एकवचन) "
        "/ अयज्ञपात्रेषु (सप्तमी-बहुवचन)"
    ),
    why_dev=(
        "प्र/उप-पूर्वकस्य युज्-धातोः अयज्ञपात्र-विषये आत्मनेपदम् — "
        "prayuNkte, upayuNkte इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
