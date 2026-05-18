"""
1.3.18  परिव्यवेभ्यः क्रियः  —  VIDHI

*Padaccheda:* *pari-vi-ava-ebhyaḥ* (पञ्चमी-बहुवचन) / *kriyaḥ* (षष्ठी-एकवचन,
referring to the dhātu kṛ).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for the dhātu kṛ (to do) when preceded by one of
the prefixes pari, vi, or ava (e.g. parikurute, vikurute, avakurute).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 in {"qukf~Y", "kf"} and carries at least
one of the prefix tags in _PARI_VI_AVA_PREFIXES, and (c) the idempotency
stamp "Atmanepada_1_3_18" is absent from state.meta.  No arm flags
(CONSTITUTION Art. 13).  r1_form_identity_exempt=True because no surface
phonological change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset of prefix tags that trigger this rule.
_PARI_VI_AVA_PREFIXES: frozenset[str] = frozenset({
    "pari_prefix",
    "vi_prefix",
    "ava_prefix",
})

# SLP1 upadeśa forms for dhātu kṛ (to do).
_KF_UPADESHA: frozenset[str] = frozenset({"qukf~Y", "kf"})

_REGISTRY_KEY = "1_3_18_pari_vi_ava_kf"
_STAMP_KEY    = "Atmanepada_1_3_18"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _KF_UPADESHA
        and not _PARI_VI_AVA_PREFIXES.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.18",
    sutra_type=SutraType.VIDHI,
    text_slp1="pari-vi-aveByaH kriyaH",
    text_dev="परिव्यवेभ्यः क्रियः",
    padaccheda_dev="परि-वि-अवेभ्यः (पञ्चमी-बहुवचन) / क्रियः (षष्ठी)",
    why_dev=(
        "परि-, वि-, अव-पूर्वस्य कृ-धातोः प्रयोगे आत्मनेपदम् — "
        "parikurute, vikurute, avakurute इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
