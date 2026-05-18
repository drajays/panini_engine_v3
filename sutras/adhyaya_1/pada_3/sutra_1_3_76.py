"""
1.3.76  अनुपसर्गाज्ज्ञः  —  VIDHI

*Padaccheda:* *an-upasargāt* (पञ्चमी-एकवचन) / *jñaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root jñā (to know; √jñā class 9) when NOT preceded by any
upasarga (verbal prefix) takes ātmanepada endings. So simple jñā without any
prefix takes ātmanepada: jānīte — he knows (for himself). With an upasarga,
parasmaipada may apply depending on other rules.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_76" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _JNA_ROOTS does NOT carry any upasarga tag. No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_JNA_ROOTS:   frozenset[str] = frozenset({"jYA", "jYa"})
# All upasarga tags that would disqualify this rule
_UPASARGA_TAGS: frozenset[str] = frozenset({
    "pra_prefix", "prati_prefix", "A_prefix", "apa_prefix", "ava_prefix",
    "ud_prefix", "ut_prefix", "upa_prefix", "ni_prefix", "nis_prefix",
    "vi_prefix", "sam_prefix", "su_prefix", "dur_prefix", "anu_prefix",
    "abhi_prefix", "ati_prefix", "adhi_prefix", "api_prefix", "apa_prefix",
    "pari_prefix",
})

_REGISTRY_KEY = "1_3_76_anupasarga_jYA"
_STAMP_KEY    = "Atmanepada_1_3_76"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _JNA_ROOTS and not bool(_UPASARGA_TAGS & t.tags):
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
    sutra_id="1.3.76",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="anupasargAjjYaH",
    text_dev="अनुपसर्गाज्ज्ञः",
    padaccheda_dev="अन्-उपसर्गात् (पञ्चमी-एकवचन) / ज्ञः (षष्ठी-एकवचन)",
    why_dev=(
        "उपसर्गरहितस्य ज्ञा-धातोः आत्मनेपदम् — "
        "jAnIte इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
