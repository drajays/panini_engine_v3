"""
5.2.127  अर्शआदिभ्योऽच्  —  VIDHI

Padaccheda: अर्श-आदिभ्यः अच्

अर्शआदिभ्योऽच् (5.2.127)
Pāṭha: ashtadhyayi.com data.txt row i=52127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_127_arSaAdiByo_127"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.127", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.127"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State, **kw):
    return taddhita_site(state, None, ok=sense_in(state, "5.2.94"), **kw)


# SHORTCUT S45: tunda, uras … stand in two gaṇas (117, 127): the loop attaches one pratyaya per stem and does not explore which sūtra fires
def _attach(state: State):
    if _site(state, gana_name="arSaAdiH") is not None:
        return 'ac'
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.127")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.127", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside; matup (5.2.94) stays and the generic 5.2.115 – 117 are barred
        state.meta["declined:5.2.127"] = True
        state.meta["special_aside"] = True
        return state
    if up.startswith("H:"):                        # handed on to the next sūtra of the chain (ca): matup waits for it
        state.meta["declined:5.2.127"] = True
        state.meta["hold:" + up[2:]] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'arSaAdiByoc',
    text_dev              = 'अर्शआदिभ्योऽच्',
    samagra_slp1          = "tat asya asmin astIti iti arSa-AdiByaH ac",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) अर्श-आदिभ्यः अच्",
    padaccheda_dev        = "अर्श-आदिभ्यः अच्",
    why_dev               = "(सूत्रम् 5.2.127) अर्शआदिभ्योऽच्।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.94', '5.2.115'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
