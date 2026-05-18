"""
1.3.80  अभिप्रत्यतिभ्यः क्षिपः  —  VIDHI

*Padaccheda:* *abhi-prati-atibhyaḥ* (पञ्चमी-बहुवचन) / *kṣipaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root kṣip (√kṣip, to throw/cast) preceded by the prefixes abhi,
prati, or ati takes ātmanepada endings. For example: abhikṣipate — he throws
towards; pratikṣipate — he throws back; atikṣipate — he throws beyond.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_80" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _KSIP_ROOTS carries any of "aBi_prefix", "prati_prefix", "ati_prefix".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KSIP_ROOTS: frozenset[str] = frozenset({"kzip", "kzipu~"})
_PREFIXES:   frozenset[str] = frozenset({"aBi_prefix", "prati_prefix", "ati_prefix"})

_REGISTRY_KEY = "1_3_80_aBi_prati_ati_kzip_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_80"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _KSIP_ROOTS and _PREFIXES & t.tags:
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
    sutra_id="1.3.80",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="aBipratyatiBYaH kzipaH",
    text_dev="अभिप्रत्यतिभ्यः क्षिपः",
    padaccheda_dev="अभि-प्रति-अतिभ्यः (पञ्चमी-बहुवचन) / क्षिपः (षष्ठी-एकवचन)",
    why_dev=(
        "अभि-प्रति-अति-पूर्वकस्य क्षिप्-धातोः आत्मनेपदम् — "
        "aBikzipate, pratikzipate, atikzipate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
