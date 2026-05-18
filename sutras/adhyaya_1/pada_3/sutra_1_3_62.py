"""
1.3.62  पूर्ववत् सनः  —  VIDHI

*Padaccheda:* *pūrvavat* / *sanaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12; mriyateḥ from 1.3.61.

*Content:* In the desiderative (san), the root mṛ behaves "as before" —
i.e., it takes ātmanepada just as it did in the lākāras mentioned in 1.3.61.
"Pūrvavat" means "in the same way as stated before." So mumūrṣate (desiderative
of mṛ) takes ātmanepada. This extends the ātmanepada provision to the
san-pratyaya context.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_62" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _MR_ROOTS carries the tag "san_pratyaya". No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_MR_ROOTS: frozenset[str] = frozenset({"mf", "mfY", "mriya"})

_REGISTRY_KEY = "1_3_62_mf_san_pUrvavat"
_STAMP_KEY    = "Atmanepada_1_3_62"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _MR_ROOTS and "san_pratyaya" in t.tags:
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
    sutra_id="1.3.62",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="pUrvavat sanaH",
    text_dev="पूर्ववत् सनः",
    padaccheda_dev="पूर्ववत् / सनः (षष्ठी-एकवचन)",
    why_dev=(
        "मृ-धातोः सन्-प्रत्यये परे पूर्ववत् आत्मनेपदम् — "
        "mumUrzate इत्यादि; "
        "१.३.६१ अनुसारेण; १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.61"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
