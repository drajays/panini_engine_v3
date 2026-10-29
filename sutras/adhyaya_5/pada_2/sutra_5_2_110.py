"""
5.2.110  गाण्ड्यजगात् संज्ञायाम्  —  VIDHI

Padaccheda: गाण्ड्य-जगात् संज्ञायाम्

गाण्ड्यजगात् संज्ञायाम् (5.2.110)
Pāṭha: ashtadhyayi.com data.txt row i=52110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_110_gARqyajagA_110"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.110", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.110"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State, **kw):
    return taddhita_site(state, None, ok=sense_in(state, "5.2.94"), **kw)


def _attach(state: State):
    if vivaksita(state, "arthaViSeSa", "saMjYA") and _site(state, stems=frozenset({'gARqI', 'ajaga'})) is not None:
        return 'va'
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.110")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.110", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside; matup (5.2.94) stays and the generic 5.2.115 – 117 are barred
        state.meta["declined:5.2.110"] = True
        state.meta["special_aside"] = True
        return state
    if up.startswith("H:"):                        # handed on to the next sūtra of the chain (ca): matup waits for it
        state.meta["declined:5.2.110"] = True
        state.meta["hold:" + up[2:]] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gARqyajagAt saMjYAyAm",
    text_dev              = "गाण्ड्यजगात् संज्ञायाम्",
    samagra_slp1          = "tat asya asmin astIti iti saMjYAyAm gARqI-ajagAt vaH",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) संज्ञायाम् गाण्डी-अजगात् वः",
    padaccheda_dev        = "गाण्ड्य-जगात् संज्ञायाम्",
    why_dev               = "(सूत्रम् 5.2.110) गाण्ड्यजगात् संज्ञायाम्।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.94', '5.2.115'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
