"""
5.4.23  अनन्तावसथेतिहभेषजाञ्ञ्यः  —  VIDHI

Padaccheda: अनन्त-आवसथ-इतिह-भेषजात् ञ्यः

अनन्तावसथेतिहभेषजाञ्ञ्यः (5.4.23)
Pāṭha: ashtadhyayi.com data.txt row i=54023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_23_anantAvasa_23"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.23", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.23"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

# AMENDMENT 27: a svārthika sūtra — 5.4.23 svārthe ñyaḥ (Kāśikā; mahāvibhāṣā). No sense frame, no samartha-vibhakti (Kāśikā 5.3.1); the optional vā (4.1.82, Kāśikā 5.4.39 vikalpaḥ sarvatrānuvartate) is the "-" reading.


def _attach(state: State):
    if not vivaksita(state, "taddhitArtha", "svArTa"):
        return None
    return ('Yya', '-') if taddhita_site(state, None, ok=True, stems=frozenset({"ananta", "AvasaTa", "itiha", "Bezaja"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.23")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.23", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the plain stem stays
        state.meta["declined:5.4.23"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anantAvasaTetihaBezajAYYyaH",
    text_dev              = "अनन्तावसथेतिहभेषजाञ्ञ्यः",
    samagra_slp1          = "ananta-AvasaTa-itiha-BezajAt YyaH",
    samagra_dev           = "अनन्त-आवसथ-इतिह-भेषजात् ञ्यः",
    padaccheda_dev        = "अनन्त-आवसथ-इतिह-भेषजात् ञ्यः",
    why_dev               = "(सूत्रम् 5.4.23) अनन्तावसथेतिहभेषजाञ्ञ्यः।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
