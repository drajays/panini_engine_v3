"""
1.4.42  साधकतमं करणम्  (sādhakatamam karaṇam)  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (baked anuvṛtti):** *kārake sādhakatamam karaṇam* — **1.4.23** *kārake*.

*Śāstra (laghu):* The most efficient means (sādhakatama) for accomplishing
an action receives the technical name *karaṇa-kāraka*. This is the foundational
definition of karaṇa. E.g. *dātreṇa lunāti* — the sickle is karaṇa.

*Engine:* This is a gate-style definitional rule. ``cond`` fires when the
``samjna_registry`` has no entry for ``"karaRa"`` yet. ``act`` installs
the gate entry and also tags any term bearing ``"sADakatama"``.
``r1_form_identity_exempt = True``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_DONE   = "1_4_42_karaka_done"
_TRIGGER    = frozenset({"sADakatama"})
_SAMJNA     = "karaRa"
_GATE_KEY   = "karaRa"


def cond(state: State) -> bool:
    if state.samjna_registry.get(_GATE_KEY) is None:
        return True
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            return True
    return False


def act(state: State) -> State:
    if state.samjna_registry.get(_GATE_KEY) is None:
        state.samjna_registry[_GATE_KEY] = "sADakatama"
    for t in state.terms:
        if META_DONE not in t.meta and _TRIGGER & t.tags:
            t.tags.add(_SAMJNA)
            t.meta[META_DONE] = True
    state.samjna_registry["1_4_42_karaRa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.42",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "sADakatamaM karaRam",
    text_dev             = "साधकतमं करणम्",
    padaccheda_dev       = "साधकतमम् / करणम्",
    why_dev              = (
        "क्रियासिद्धौ यत् साधकतमम् (अत्यन्तोपकारकम्) तत् करण-कारक-संज्ञकम्। "
        "करण-कारक-परिभाषाद्वारम्। चिह्नम्: sADakatama इति।"
    ),
    anuvritti_from       = ("1.4.23",),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
