"""
5.2.82  तदस्मिन्नन्नं प्राये संज्ञायाम्  —  VIDHI

Padaccheda: तत् अस्मिन् अन्नम् प्राये संज्ञायाम्

तदस्मिन्नन्नं प्राये संज्ञायाम् (5.2.82)
Pāṭha: ashtadhyayi.com data.txt row i=52082 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_82_tadasminna_82"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.82", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.82"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _ok(state: State) -> bool:
    return (vivaksita(state, "taddhitArtha", "annaprAya")) and (vivaksita(state, "arthaViSeSa", "saMjYA"))


def _attach(state: State):
    ok = _ok(state)
    for kw, up in ((({}, "kan"),)):
        if taddhita_site(state, None, ok=ok, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.82")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.82", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasminnannaM prAye saMjYAyAm",
    text_dev              = "तदस्मिन्नन्नं प्राये संज्ञायाम्",
    samagra_slp1          = "tat annamasmin iti saMjYAyAm prAye kan",
    samagra_dev           = "'तत् अन्नमस्मिन्' (इति) संज्ञायाम् प्राये कन्",
    padaccheda_dev        = "तत् अस्मिन् अन्नम् प्राये संज्ञायाम्",
    why_dev               = "(सूत्रम् 5.2.82) तदस्मिन्नन्नं प्राये संज्ञायाम्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
