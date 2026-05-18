"""
1.3.57  ज्ञाश्रुस्मृदृशां सनः  —  VIDHI

*Padaccheda:* *jñā-śru-smṛ-dṛśām* (षष्ठी-बहुवचन) / *sanaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The roots jñā (to know), śru (to hear), smṛ (to remember), and dṛś
(to see) take ātmanepada endings when followed by the san-pratyaya (the
desiderative suffix). For example: jijñāsate — he desires to know;
śuśrūṣate — he desires to hear/obey.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_57" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _ROOTS carries the tag "san_pratyaya". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_ROOTS: frozenset[str] = frozenset({"jYA", "jYa", "Sru", "smf", "dfS", "dfs"})

_REGISTRY_KEY = "1_3_57_jYA_Sru_smf_dfS_san"
_STAMP_KEY    = "Atmanepada_1_3_57"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _ROOTS and "san_pratyaya" in t.tags:
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
    sutra_id="1.3.57",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="jYASrusmfdftSAM sanaH",
    text_dev="ज्ञाश्रुस्मृदृशां सनः",
    padaccheda_dev="ज्ञा-श्रु-स्मृ-दृशाम् (षष्ठी-बहुवचन) / सनः (षष्ठी-एकवचन)",
    why_dev=(
        "ज्ञा-श्रु-स्मृ-दृश्-धातूनां सन्-प्रत्यये परे आत्मनेपदम् — "
        "jijYAsate, SuSrUzate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
