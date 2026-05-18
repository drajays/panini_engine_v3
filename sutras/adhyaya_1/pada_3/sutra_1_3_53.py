"""
1.3.53  उदश्चरः सकर्मकात्  —  VIDHI

*Padaccheda:* *udaḥ* (पञ्चमी-एकवचन) / *caraḥ* (षष्ठी) / *sakarmakāt* (पञ्चमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root car (√car, to move/go) preceded by the prefix ud takes
ātmanepada endings — but only when the root is sakarmaka (transitive, i.e.,
accompanied by an object). For example: udcarate devadattaḥ gāḥ — Devadatta
drives the cows out.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_53" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _CAR_ROOTS carries both the tag "ut_prefix" and the tag "sakarmaka_usage".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True because no
surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_CAR_ROOTS: frozenset[str] = frozenset({"cara", "car"})

_REGISTRY_KEY = "1_3_53_ut_cara_sakarmaka"
_STAMP_KEY    = "Atmanepada_1_3_53"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _CAR_ROOTS and "ut_prefix" in t.tags and "sakarmaka_usage" in t.tags:
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
    sutra_id="1.3.53",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="udaScaraH sakarmakAt",
    text_dev="उदश्चरः सकर्मकात्",
    padaccheda_dev="उदः (पञ्चमी-एकवचन) / चरः (षष्ठी) / सकर्मकात् (पञ्चमी-एकवचन)",
    why_dev=(
        "उत्-पूर्वकस्य चर-धातोः सकर्मक-प्रयोगे आत्मनेपदम् — "
        "udcarate devadattaH gAH इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
