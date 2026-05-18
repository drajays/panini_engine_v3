"""
2.1.20  नदीभिश्च  (nadībhiś ca)  —  VIDHI

**Pāṭha:** River (*nadī*) names also combine (with *saṃkhyā* words —
anuvṛtti from 2.1.19, *ca* extends the scope) to form avyayībhāva
samāsas.

Example: *pañca gaṅgābhiḥ* → *pañcagaṅgam* ("at the confluence of five
Gaṅgās").

v3 narrow slice: gate-marks the compound with key
``2_1_20_nadi_samkhya``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_20_nadi_samkhya"

_NADI_TAGS: frozenset[str] = frozenset({"nadi", "nadI", "river"})

_SANKHYA_TAGS: frozenset[str] = frozenset({"sankhya", "samkhya"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    has_nadi    = any(_NADI_TAGS & t.tags for t in state.terms)
    has_sankhya = any(_SANKHYA_TAGS & t.tags for t in state.terms)
    return has_nadi and has_sankhya


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nadIBiS ca",
    text_dev              = "नदीभिश्च",
    padaccheda_dev        = "नदीभिः / च",
    why_dev               = "नदी-शब्दैः सह संख्यायाश्च अव्ययीभावः (२.१.२०)।",
    anuvritti_from        = ("2.1.5", "2.1.19"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
