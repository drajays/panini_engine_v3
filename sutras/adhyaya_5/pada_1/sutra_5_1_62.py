"""
5.1.62  त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्  —  VIDHI

Padaccheda: त्रिंशत्-चत्वारिंशतोः ब्राह्मणे संज्ञायाम् डण्

त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण् (5.1.62)
Pāṭha: ashtadhyayi.com data.txt row i=51062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_62_triMSaccat_62"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.62", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.62"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    if not vivaksita(state, "arthaViSeSa", "brAhmaRasaMjYA"):
        return None
    return "qaR" if arhiya_site(state, "5.1.57", stems=frozenset({"triMSat", "catvAriMSat"})) is not None else None      # brāhmaṇe saṃjñāyām


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.62")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.62", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.62"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "triMSaccatvAriMSatorbrAhmaRe saMjYAyAM qaR",
    text_dev              = "त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्",
    samagra_slp1          = "tat asya parimARam iti triMSat-catvAriMSatoH saMjYAyAM brAhmaRe qaR",
    samagra_dev           = "'तत् अस्य परिमाणम्' (इति) त्रिंशत्-चत्वारिंशतोः संज्ञायां ब्राह्मणे डण्",
    padaccheda_dev        = "त्रिंशत्-चत्वारिंशतोः ब्राह्मणे संज्ञायाम् डण्",
    why_dev               = "(सूत्रम् 5.1.62) त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
