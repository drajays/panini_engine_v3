"""
1.3.63  आम्प्रत्ययवत् कृञोऽनुप्रयोगस्य  —  VIDHI

*Padaccheda:* *ām-pratyayavat* / *kṛñaḥ* (षष्ठी-एकवचन) / *anuprayogasya*
(षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root kṛ (√kṛ, to do) when used as an anuprayoga (an auxiliary
verb following another verbal form ending in the ām-pratyaya) takes ātmanepada
endings in the same way as the main verb (ām-pratyayavat). The ām-pratyaya is
the nominal verbal form. The kṛ in anuprayoga follows the pada of the main
verb. For example: gambhīrīkāñcakre — he has made deep (causative periphrastic
perfect). If the main verb is ātmanepada, kṛ also takes ātmanepada.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_63" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _KR_ROOTS carries the tag "anuprayoga_usage" and "Am_pratyaya". No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KR_ROOTS: frozenset[str] = frozenset({"qukf~Y", "kf", "kfY"})

_REGISTRY_KEY = "1_3_63_kf_anuprayoga_Am"
_STAMP_KEY    = "Atmanepada_1_3_63"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _KR_ROOTS and "anuprayoga_usage" in t.tags and "Am_pratyaya" in t.tags:
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
    sutra_id="1.3.63",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="AmpratyayavatkfYonuprayogasya",
    text_dev="आम्प्रत्ययवत् कृञोऽनुप्रयोगस्य",
    padaccheda_dev=(
        "आम्-प्रत्ययवत् / कृञः (षष्ठी-एकवचन) / अनुप्रयोगस्य (षष्ठी-एकवचन)"
    ),
    why_dev=(
        "आम्-प्रत्ययान्तक्रियाऽनुप्रयोगे कृञ्-धातोः आम्-प्रत्ययवत् आत्मनेपदम् — "
        "gambhIrIkAYcakre इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
