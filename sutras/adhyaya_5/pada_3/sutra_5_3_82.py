"""
5.3.82  अजिनान्तस्योत्तरपदलोपश्च  —  VIDHI

Padaccheda: अजिन-अन्तस्य उत्तरपद-लोपः च

अजिनान्तस्योत्तरपदलोपश्च (5.3.82)
Pāṭha: ashtadhyayi.com data.txt row i=53082 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_82_ajinAntasy_82"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.82", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.82"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    return "kan" if taddhita_site(state, None, ok=sense_in(state, "5.3.76", "5.3.77"), tag="manuzyanAman", final=lambda f: f.endswith(("ajina", "Ajina"))) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.82")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.82", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.82"] = True
        return state
    t = state.terms[-1]      # SHORTCUT S54: uttarapadalopa of ajina; the pada boundary of the compound is not a Term, so vyAGrAjina (savarṇadīrgha) gives back its a
    if t.varnas[-5].slp1 == "a":
        del t.varnas[-5:]
    else:
        del t.varnas[-4:]
        t.varnas[-1].slp1, t.varnas[-1].dev = "a", ""
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajinAntasyottarapadalopaSca",
    text_dev              = "अजिनान्तस्योत्तरपदलोपश्च",
    samagra_slp1          = "ajina-antasya manuzyanAmnaH anukampAyAmuttarapadalopaH kan ca",
    samagra_dev           = "अजिन-अन्तस्य मनुष्यनाम्नः अनुकम्पायामुत्तरपदलोपः, कन् च",
    padaccheda_dev        = "अजिन-अन्तस्य उत्तरपद-लोपः च",
    why_dev               = "(सूत्रम् 5.3.82) अजिनान्तस्योत्तरपदलोपश्च।",
    anuvritti_from        = ('5.3.70',),
    apavada_of     = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
