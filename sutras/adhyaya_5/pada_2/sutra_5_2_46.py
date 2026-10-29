"""
5.2.46  शदन्तविंशतेश्च  —  VIDHI

Padaccheda: शत्-अन्त-विंशतेः च

शदन्तविंशतेश्च (5.2.46)
Pāṭha: ashtadhyayi.com data.txt row i=52046 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_46_SadantaviM_46"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.46", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.46"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _ok(state: State) -> bool:
    return (vivaksita(state, "taddhitArtha", "tadasminnaDika"))


def _attach(state: State):
    ok = _ok(state)
    for kw, up in ((({"final": lambda f: f.endswith("Sat")}, "qa"), ({"stems": frozenset({'viMSati'})}, "qa"))):
        if taddhita_site(state, None, ok=ok, **kw) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.2.46")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.2.46", len(up))]
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SadantaviMSateSca",
    text_dev              = "शदन्तविंशतेश्च",
    samagra_slp1          = "tad asmin aDikam iti iti Sadanta-viMSateH qaH",
    samagra_dev           = "'तद् अस्मिन् अधिकम् इति' (इति) शदन्त-विंशतेः डः",
    padaccheda_dev        = "शत्-अन्त-विंशतेः च",
    why_dev               = "(सूत्रम् 5.2.46) शदन्तविंशतेश्च।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
