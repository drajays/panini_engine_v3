"""
1.3.92  वृद्भ्यः स्यसनोः  —  VIDHI

*Padaccheda:* *vṛd-bhyaḥ* (पञ्चमी-बहुवचन) / *sya-sanoḥ* (षष्ठी-द्विवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The roots of the vṛd group take ātmanepada endings before the
sya (future) and san (desiderative) pratyayas. For example: vṛtsyate —
he will grow; vivṛtsate — he desires to grow.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_92" is absent, (c) a dhātu Term carries "vṛd_group" tag
or upadesha is in _VRD_ROOTS, AND carries "sya_pratyaya" or "san_pratyaya".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_VRD_ROOTS: frozenset[str] = frozenset({
    "vftu~",  # vṛt — to be
    "vft",
    "vfDu~",  # vṛdh — to grow
    "vfD",
    "Sru",    # śru — heard in some lists
    "vfzu~",  # vṛṣ
    "vfz",
})

_CONDITION_TAGS: frozenset[str] = frozenset({"sya_pratyaya", "san_pratyaya"})

_REGISTRY_KEY = "1_3_92_vfD_sya_san_atmanepada"
_STAMP_KEY    = "Atmanepada_1_3_92"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        in_group = up in _VRD_ROOTS or "vfD_group" in t.tags or "vrd_group" in t.tags
        if in_group and _CONDITION_TAGS & t.tags:
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
    sutra_id="1.3.92",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="vfDByaH syasanoH",
    text_dev="वृद्भ्यः स्यसनोः",
    padaccheda_dev="वृद्भ्यः (पञ्चमी-बहुवचन) / स्य-सनोः (षष्ठी-द्विवचन)",
    why_dev=(
        "वृद्-गण-धातूनां स्य-प्रत्यये सन्-प्रत्यये च परे आत्मनेपदम् — "
        "vftsyate, vivftsate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
