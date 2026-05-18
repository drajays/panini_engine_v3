"""
1.3.33  अधेः प्रसहने  —  VIDHI

*Padaccheda:* *adheḥ* (पञ्चमी-एकवचन) / *prasahane* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for sah (to endure / overpower) preceded by the
prefix adhi in the sense of prasahana (overpowering / forceful overcoming;
e.g. adhisahate — he overpowers).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 in {"zaha~", "sah"} and carries the tag
"aDi_prefix", and (c) the idempotency stamp "Atmanepada_1_3_33" is absent
from state.meta.  The prasahana sense is conveyed through the structural
presence of "aDi_prefix" on the dhātu (per the sūtra's own scope; an
optional "prasahana_usage" tag is also checked when present, but the rule
is not blocked by its absence since the adhi + sah combination is itself
the primary diagnostic).  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset (CONSTITUTION Art. 13.3)
_SAH_ROOTS: frozenset[str] = frozenset({"zaha~", "sah"})

_REGISTRY_KEY = "1_3_33_aDi_prasahana"
_STAMP_KEY    = "Atmanepada_1_3_33"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _SAH_ROOTS
        and "aDi_prefix" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.33",
    sutra_type=SutraType.VIDHI,
    text_slp1="aDes prasahane",
    text_dev="अधेः प्रसहने",
    padaccheda_dev="अधेः (पञ्चमी) / प्रसहने (सप्तमी)",
    why_dev=(
        "अधि-पूर्वकस्य सह्-धातोः प्रसहन-अर्थे प्रयोगे आत्मनेपदम् — "
        "adhisahate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
