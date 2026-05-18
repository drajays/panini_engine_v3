"""
1.3.37  कर्तृस्थे चाशरीरे कर्मणि  —  VIDHI

*Padaccheda:* *kartṛsthe* (सप्तमी-एकवचन) / *ca* (अव्यय) /
*aśarīre* (सप्तमी-एकवचन) / *karmaṇi* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* And [Ātmanepada] when the karma (object) resides in the kartṛ
(agent) itself — kartṛstha — and the karma is aśarīra (non-physical /
incorporeal). This covers reflexive actions where the result or object
stays within the doer rather than passing to an external entity.
For example: pacate odanam ātmane — he cooks rice for himself.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term carries both the tag "kartfstha_usage" (encoding the
kartṛstha semantic context) and the tag "aSarIra_karma" (encoding the
non-physical karma condition), and (c) the idempotency stamp
"Atmanepada_1_3_37" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_37_kartfstha_aSarIra"
_STAMP_KEY    = "Atmanepada_1_3_37"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and "kartfstha_usage" in t.tags
        and "aSarIra_karma" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.37",
    sutra_type=SutraType.VIDHI,
    text_slp1="kartfsTE cASarIre karmaRi",
    text_dev="कर्तृस्थे चाशरीरे कर्मणि",
    padaccheda_dev=(
        "कर्तृस्थे (सप्तमी-एकवचन) / च (अव्यय) / "
        "अशरीरे (सप्तमी-एकवचन) / कर्मणि (सप्तमी-एकवचन)"
    ),
    why_dev=(
        "कर्तृस्थे अशरीर-कर्मणि आत्मनेपदम् — "
        "कर्ता एव कर्मणो लाभं लभते इत्यर्थे; "
        "pacate odanam ātmane इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
