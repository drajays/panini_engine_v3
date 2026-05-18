"""
1.3.72  स्वरितञितः कर्त्रभिप्राये क्रियाफले  —  VIDHI

*Padaccheda:* *svarita-ñitaḥ* (षष्ठी-एकवचन) / *kartṛ-abhiprāye* (सप्तमी-एकवचन)
/ *kriyā-phale* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* A root that is svarita-ñit (marked with ñ as anubandha, or has a
svarita accent) takes ātmanepada endings when the result/fruit (phala) of the
action is intended for the agent (kartṛ-abhiprāya — the agent's own intention/
benefit). This is the key kartrabhiprāya rule. For example: pacate (he cooks
for himself), from √pac which is ñit.

*Engine (VIBHASHA with vibhasha_default=True):* The rule is in principle
optional when the fruit may or may not benefit the agent. cond checks
(a) pada is not already "Atmanepada", (b) idempotency stamp
"Atmanepada_1_3_72" is absent, (c) a dhātu Term carries the tag
"svaritaYit" or "Yit_dhatu" AND "kartfBiprAya_usage". No arm flags.
r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_NIT_TAGS:  frozenset[str] = frozenset({"svaritaYit", "Yit_dhatu", "Yit"})

_REGISTRY_KEY = "1_3_72_svaritaYit_kartfBiprAya"
_STAMP_KEY    = "Atmanepada_1_3_72"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if bool(_NIT_TAGS & t.tags) and "kartfBiprAya_usage" in t.tags:
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
    sutra_id="1.3.72",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    vibhasha_default=True,
    text_slp1="svaritaYitaH kartfBiprAye kriyABale",
    text_dev="स्वरितञितः कर्त्रभिप्राये क्रियाफले",
    padaccheda_dev=(
        "स्वरित-ञितः (षष्ठी-एकवचन) / कर्तृ-अभिप्राये (सप्तमी-एकवचन) "
        "/ क्रिया-फले (सप्तमी-एकवचन)"
    ),
    why_dev=(
        "स्वरित-ञित्-धातूनां कर्तृ-अभिप्राय-क्रियाफल-विषये आत्मनेपदम् — "
        "pacate (स्वार्थे) इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
