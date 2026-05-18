"""
1.3.44  विभाषा स्मरतिहृद्यभावयोः  —  VIBHASHA

*Padaccheda:* *vibhāṣā* (अव्यय) / *smarati-hṛdyabhāvayoḥ* (सप्तमी-द्विवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Optionally (vibhāṣā) [ātmanepada applies] in the sense of
smaraṇa (remembering / √smṛ) and hṛdyabhāva (pleasing / dear to the heart).
That is, the root smṛ and roots expressing hṛdyabhāva may take ātmanepada
optionally.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_vibhASA_1_3_44" is absent, and (c) a dhātu
Term whose upadesha_slp1 is in _SMARA_ROOTS or which carries the tag
"hfdyaBAvA_usage".
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
vibhasha_default=True: the optional form is taken by default.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_SMARA_ROOTS: frozenset[str] = frozenset({"smf", "smara"})

_REGISTRY_KEY = "1_3_44_smarati_hfdyaBAvA_vibhASA"
_STAMP_KEY    = "Atmanepada_vibhASA_1_3_44"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _SMARA_ROOTS:
            return True
        if "hfdyaBAvA_usage" in t.tags:
            return True
    return False


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.44",
    sutra_type=SutraType.VIBHASHA,
    vibhasha_default=True,
    r1_form_identity_exempt=True,
    text_slp1="vibhASA smaratihfdyaBAvayoH",
    text_dev="विभाषा स्मरतिहृद्यभावयोः",
    padaccheda_dev="विभाषा (अव्यय) / स्मरति-हृद्यभावयोः (सप्तमी-द्विवचन)",
    why_dev=(
        "स्मृति-अर्थे हृद्यभाव-अर्थे च धातोः प्रयोगे विभाषा आत्मनेपदम् — "
        "smarate / smarati इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
