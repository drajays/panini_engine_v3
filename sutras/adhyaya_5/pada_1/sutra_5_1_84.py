"""
5.1.84  अवयसि ठंश्च  —  VIDHI

Padaccheda: अवयसि ठन् च

अवयसि ठंश्च (5.1.84)
Pāṭha: ashtadhyayi.com data.txt row i=51084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_84_avayasi_84"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.84", state, "5.1.78"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.84"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "kAlaBUta") and vivaksita(state, "arthaViSeSa", "avayas")
    return ("Wan", "Ryat") if ok and arhiya_site(state, "5.1.80", tag="dvigu", final=lambda f: f.endswith("zaRmAsa")) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.84")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.84", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.84"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avayasi WaMSca",
    text_dev              = "अवयसि ठंश्च",
    samagra_slp1          = "tam BUtaH iti avayasi zaRmAsAt dvigoH Ryat Wan ca",
    samagra_dev           = "'तम् भूतः' (इति) अवयसि षण्मासात् द्विगोः ण्यत् ठन् च",
    padaccheda_dev        = "अवयसि ठन् च",
    why_dev               = "(सूत्रम् 5.1.84) अवयसि ठंश्च।",
    anuvritti_from        = ('5.1.78',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
