"""
1.3.30  निसमुपविभ्यो ह्वः  —  VIDHI

*Padaccheda:* *ni-sam-upa-vi-bhyaḥ* (पञ्चमी-बहुवचन) / *hvaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for the root hve / hvā (to call) when preceded by
any of the prefixes ni, sam, upa, or vi (e.g. nihvayate, samhvayate,
upahvayate, vihvayate).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 in _HVA_ROOTS and carries at least one
of the prefix tags in _NISAM_PREFIXES, and (c) the idempotency stamp
"Atmanepada_1_3_30" is absent from state.meta.  No arm flags (CONSTITUTION
Art. 13).  r1_form_identity_exempt=True because no surface phonological
change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_HVA_ROOTS: frozenset[str] = frozenset({"hve", "hvA", "hu"})
_NISAM_PREFIXES: frozenset[str] = frozenset({
    "ni_prefix",
    "sam_prefix",
    "upa_prefix",
    "vi_prefix",
})

_REGISTRY_KEY = "1_3_30_ni_sam_upa_vi_hve"
_STAMP_KEY    = "Atmanepada_1_3_30"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _HVA_ROOTS
        and not _NISAM_PREFIXES.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.30",
    sutra_type=SutraType.VIDHI,
    text_slp1="ni-sam-upa-vi-ByaH hvaH",
    text_dev="निसमुपविभ्यो ह्वः",
    padaccheda_dev="नि-सम्-उप-वि-भ्यः (पञ्चमी-बहुवचन) / ह्वः (षष्ठी-एकवचन)",
    why_dev=(
        "नि-, सम्-, उप-, वि-पूर्वस्य ह्वे-धातोः प्रयोगे आत्मनेपदम् — "
        "nihvayate, samhvayate, upahvayate, vihvayate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
