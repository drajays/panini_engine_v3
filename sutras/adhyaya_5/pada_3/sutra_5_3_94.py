"""
5.3.94  एकाच्च प्राचाम्  —  VIDHI

Padaccheda: एकात् च प्राचाम्

एकाच्च प्राचाम् (5.3.94)
Pāṭha: ashtadhyayi.com data.txt row i=53094 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_94_ekAcca_94"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.94", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.94"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    if not vivaksita(state, "arthaViSeSa", "prAcAm"):      # prācām matam: the Eastern grammarians' option, said by the speaker
        return None
    if vivaksita(state, "taddhitArtha", "nirDAraRadvaya"):
        return "qatarac" if taddhita_site(state, None, ok=True, stems=frozenset({"eka"})) is not None else None
    return "qatamac" if vivaksita(state, "taddhitArtha", "nirDAraRabahu") and taddhita_site(state, None, ok=True, stems=frozenset({"eka"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.94")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.94", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.94"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAcca prAcAm",
    text_dev              = "एकाच्च प्राचाम्",
    samagra_slp1          = "dvayoH ekasya nirDAraRe ekAt qatarac bahUnAm ekasya nirDAraRe ekAt qatamac - iti prAcAm matam ",
    samagra_dev           = "द्वयोः एकस्य निर्धारणे एकात् डतरच्, बहूनाम् एकस्य निर्धारणे एकात् डतमच् - (इति) प्राचाम् (मतम्) ।",
    padaccheda_dev        = "एकात् च प्राचाम्",
    why_dev               = "(सूत्रम् 5.3.94) एकाच्च प्राचाम्।",
    anuvritti_from        = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
