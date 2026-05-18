"""
1.3.67  णेरणौ यत्कर्म णौ चेत् स कर्ताऽनाध्याने  —  VIDHI

*Padaccheda:* *ṇeḥ* (षष्ठी-एकवचन) / *ṇau* (सप्तमी-एकवचन) / *yat-karma* /
*ṇau* / *cet* / *saḥ* / *kartā* / *anādhyāne* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* When the ṇi (causative) suffix is used, and the object of the
causative (the karma in the causative construction) is the same as the agent
(kartā) in the base verb — and this is NOT in the context of self-study/
recitation (anādhyāna) — then ātmanepada is used. This covers causatives where
the causer and the caused action's object coincide, outside of Vedic recitation
contexts.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_67" is absent, (c) a dhātu Term whose upadesha_slp1 is
in any dhātu set carries the tag "Ni_pratyaya" (causative) and
"karmakartf_usage" (karma=kartā overlap) and does NOT carry "anADyAna_usage".
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_67_Ni_karmakartf_anADyAna"
_STAMP_KEY    = "Atmanepada_1_3_67"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if ("Ni_pratyaya" in t.tags
                and "karmakartf_usage" in t.tags
                and "anADyAna_usage" not in t.tags):
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
    sutra_id="1.3.67",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="ReRaRau yatkarma Rau cet sa kartAnADyAne",
    text_dev="णेरणौ यत्कर्म णौ चेत् स कर्ताऽनाध्याने",
    padaccheda_dev=(
        "णेः (षष्ठी-एकवचन) / णौ (सप्तमी-एकवचन) / यत्-कर्म / णौ / चेत् "
        "/ सः / कर्ता / अनाध्याने (सप्तमी-एकवचन)"
    ),
    why_dev=(
        "णि-प्रत्यये परे णि-कर्म-कर्तृ-सम्पाते अनाध्यान-व्यतिरिक्ते आत्मनेपदम् — "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
