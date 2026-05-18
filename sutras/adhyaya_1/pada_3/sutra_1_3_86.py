"""
1.3.86  बुधयुधनशजनेङ्प्रुद्रुस्रुभ्यो णेः  —  VIDHI

*Padaccheda:* *budha-yudha-naśa-jana-iṅ-pru-dru-srubhyaḥ* (पञ्चमी-बहुवचन) / *ṇeḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The roots budh (to know), yudh (to fight), naś (to perish), jan
(to be born), iṅ (to study), pru (to fill), dru (to run), sru (to flow)
take ātmanepada endings when followed by the causative suffix ṇi (णि).
For example: bodhayate — he causes to know; yodhayate — he causes to fight.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_86" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _ROOTS carries the tag "NI_causative_context".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_ROOTS: frozenset[str] = frozenset({
    "buDa~", "buD",
    "yuDa~", "yuD",
    "naS", "naS~",
    "jana~", "jan",
    "i~N", "iN",
    "pru~N", "pru",
    "dru",
    "sru",
})

_REGISTRY_KEY = "1_3_86_buD_yuD_naS_jan_iN_pru_dru_sru_Ni_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_86"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _ROOTS and "NI_causative_context" in t.tags:
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
    sutra_id="1.3.86",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="buDayuDanaSajaneNprudrustByo NeH",
    text_dev="बुधयुधनशजनेङ्प्रुद्रुस्रुभ्यो णेः",
    padaccheda_dev="बुध-युध-नश-जन-इङ्-प्रु-द्रु-स्रुभ्यः (पञ्चमी-बहुवचन) / णेः (षष्ठी-एकवचन)",
    why_dev=(
        "बुध-युध-नश-जन-इङ्-प्रु-द्रु-स्रु-धातूनां णि-प्रत्यये परे आत्मनेपदम् — "
        "boDayate, yoDayate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
