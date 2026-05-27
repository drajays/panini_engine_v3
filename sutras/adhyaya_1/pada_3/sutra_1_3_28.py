"""
1.3.28  आङो यमहनः  —  PARIBHASHA

*Padaccheda:* *āṅaḥ* (pañcamī) / *yam-hanaḥ* (ṣaṣṭhī).

*Śāstra:* when **āṅ** (*A~N*) immediately precedes *yam* / *han* *dhātu*, *ātmanepada*
is licensed in *kartari* (P010 *āyacchate*).

*Engine:* reads prefix ``upasarga`` tag + following *dhātu* stem ``yam``; sets
``kartari_atmanepada_licensed`` (Art. 2 safe).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import ATMANE_LICENSE_META_KEY

_YAM_STEMS = frozenset({"yam", "han"})


def _anga_base(up: str | None) -> str:
    s = (up or "").strip().replace("~", "")
    while s and s[-1] in {"N", "Y", "R"}:
        s = s[:-1]
    return s


def _witness(state: State) -> tuple[Term, Term] | None:
    for i in range(len(state.terms) - 1):
        t0, t1 = state.terms[i], state.terms[i + 1]
        if "upasarga" not in t0.tags:
            continue
        if _anga_base(t0.meta.get("upadesha_slp1")) != "A":
            continue
        if "dhatu" not in t1.tags:
            continue
        stem = "".join(v.slp1 for v in t1.varnas)
        if stem in _YAM_STEMS:
            return t0, t1
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("1.3.28_Anga_yamhan_atmanepada"):
        return False
    return _witness(state) is not None


def act(state: State) -> State:
    hit = _witness(state)
    if hit is None:
        return state
    _, dhatu = hit
    dhatu.meta[ATMANE_LICENSE_META_KEY] = True
    state.meta["pada"] = "Atmanepada"
    state.paribhasha_gates["1.3.28_Anga_yamhan_atmanepada"] = True
    state.samjna_registry["1.3.28_Anga_yam"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.28",
    sutra_type=SutraType.PARIBHASHA,
    r1_form_identity_exempt=True,
    text_slp1="ANgo yamhanos tu karmaRi",
    text_dev="आङो यमहनः",
    padaccheda_dev="आङः / यमहनः",
    why_dev="आङ्-पूर्वयोः यम्-हन्-धात्वोः कर्तरि आत्मनेपदम् (P010 आयच्छते)।",
    anuvritti_from=("1.3.27",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
