"""
5.2.117  तुन्दादिभ्य इलच् च  —  VIDHI

Padaccheda: तुन्द-आदिभ्यः इलच् च

तुन्दादिभ्य इलच् च (5.2.117)
Pāṭha: ashtadhyayi.com data.txt row i=52117 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_117_tundAdiBya_117"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.117", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.117"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State, **kw):
    return taddhita_site(state, None, ok=sense_in(state, "5.2.94"), **kw)


# SHORTCUT S45: tunda, uras … stand in two gaṇas (117, 127): the loop attaches one pratyaya per stem and does not explore which sūtra fires
def _attach(state: State):
    if state.meta.get("special_aside"):
        return None      # a special above stood aside for matup: the generic ini / ṭhan does not return
    if _site(state, gana_name="tundAdiH") is not None:
        return ('ilac', 'in', 'Wan', '-')
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.117")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.117", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside; matup (5.2.94) stays and the generic 5.2.115 – 117 are barred
        state.meta["declined:5.2.117"] = True
        state.meta["special_aside"] = True
        return state
    if up.startswith("H:"):                        # handed on to the next sūtra of the chain (ca): matup waits for it
        state.meta["declined:5.2.117"] = True
        state.meta["hold:" + up[2:]] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tundAdiBya ilac ca",
    text_dev              = "तुन्दादिभ्य इलच् च",
    samagra_slp1          = "tat asya asmin astIti iti tundAdiByaH ilac iniWanO matu~p anyatarasyAm",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) तुन्दादिभ्यः इलच्, इनिठनौ, मतुँप् अन्यतरस्याम्",
    padaccheda_dev        = "तुन्द-आदिभ्यः इलच् च",
    why_dev               = "(सूत्रम् 5.2.117) तुन्दादिभ्य इलच् च।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.94', '5.2.115'),
    also_vidhi     = True,          # a vā / ca reading that changes no letter (stands aside, hands on) must still reach act: effective_candidates keeps it
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
