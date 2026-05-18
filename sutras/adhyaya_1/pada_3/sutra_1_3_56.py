"""
1.3.56  उपाद्यमः स्वकरणे  —  VIDHI

*Padaccheda:* *upāt* (पञ्चमी-एकवचन) / *yamaḥ* (षष्ठी-एकवचन) / *svakaraṇe*
(सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root yam (√yam, to restrain/hold) preceded by the prefix upa
takes ātmanepada endings when the action is svakāraṇa — i.e., when the
restraint is for the agent's own sake or under the agent's own control.
For example: upayacchate — he restrains himself.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_56" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _YAM_ROOTS carries both the tag "upa_prefix" and the tag "svakAraNa_usage".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_YAM_ROOTS: frozenset[str] = frozenset({"yam", "yama"})

_REGISTRY_KEY = "1_3_56_upa_yam_svakAraNa"
_STAMP_KEY    = "Atmanepada_1_3_56"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _YAM_ROOTS and "upa_prefix" in t.tags and "svakAraNa_usage" in t.tags:
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
    sutra_id="1.3.56",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="upAdyamaH svakaraRe",
    text_dev="उपाद्यमः स्वकरणे",
    padaccheda_dev="उपात् (पञ्चमी-एकवचन) / यमः (षष्ठी-एकवचन) / स्वकरणे (सप्तमी-एकवचन)",
    why_dev=(
        "उप-पूर्वकस्य यम्-धातोः स्वकारण-अर्थे आत्मनेपदम् — "
        "upayacchate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
