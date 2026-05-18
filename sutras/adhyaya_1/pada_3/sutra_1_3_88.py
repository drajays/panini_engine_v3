"""
1.3.88  अणावकर्मकाच्चित्तवत्कर्तृकात्  —  VIDHI

*Padaccheda:* *aṇau* (सप्तमी-एकवचन) / *akarmakāt* (पञ्चमी-एकवचन) / *cittavat-kartṛkāt* (पञ्चमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* When NOT followed by the causative ṇi suffix (aṇau), an intransitive
(akarmaka) root with a conscious/sentient agent (cittavat-kartṛ) takes
ātmanepada endings. For example: śete — he sleeps (conscious agent, intransitive).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_88" is absent, (c) a dhātu Term carries "akarmaka" and
"cittvat_kartf" tags, and does NOT carry "NI_causative_context".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_88_akarmaka_cittvat_kartf_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_88"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if (
            "akarmaka" in t.tags
            and "cittvat_kartf" in t.tags
            and "NI_causative_context" not in t.tags
        ):
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
    sutra_id="1.3.88",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="aNAvakarmakAccittvatkartrfkAt",
    text_dev="अणावकर्मकाच्चित्तवत्कर्तृकात्",
    padaccheda_dev="अणौ (सप्तमी-एकवचन) / अकर्मकात् (पञ्चमी-एकवचन) / चित्तवत्-कर्तृकात् (पञ्चमी-एकवचन)",
    why_dev=(
        "अणि-परे (न णि-प्रत्यये) अकर्मक-धातोः चित्तवत्-कर्तृके आत्मनेपदम् — "
        "Sete इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
